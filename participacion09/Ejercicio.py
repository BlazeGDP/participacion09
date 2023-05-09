from typing import Dict, Any


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        total_solicitudes = 0
        solicitudes_por_metodo = {}
        solicitudes_por_codigo = {}
        tamano_total_respuesta = 0
        urls_solicitadas = {}

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                campos = linea.split()
                direccion_ip = campos[0]
                fecha_hora = campos[1] + ' ' + campos[2]
                metodo_http = campos[3]
                url = campos[4]
                codigo_respuesta = campos[5]
                tamano_respuesta = int(campos[6])

                total_solicitudes += 1
                if metodo_http in solicitudes_por_metodo:
                    solicitudes_por_metodo[metodo_http] += 1
                else:
                    solicitudes_por_metodo[metodo_http] = 1

                if codigo_respuesta in solicitudes_por_codigo:
                    solicitudes_por_codigo[codigo_respuesta] += 1
                else:
                    solicitudes_por_codigo[codigo_respuesta] = 1

                tamano_total_respuesta += tamano_respuesta

                if url in urls_solicitadas:
                    urls_solicitadas[url] += 1
                else:
                    urls_solicitadas[url] = 1

        tamano_promedio_respuesta = tamano_total_respuesta / total_solicitudes
        urls_mas_solicitadas = sorted(urls_solicitadas.items(), key=lambda x: x[1], reverse=True)[:10]

        estadisticas = {
            'total_solicitudes': total_solicitudes,
            'solicitudes_por_metodo': solicitudes_por_metodo,
            'solicitudes_por_codigo': solicitudes_por_codigo,
            'tamano_total_respuesta': tamano_total_respuesta,
            'tamano_promedio_respuesta': tamano_promedio_respuesta,
            'urls_mas_solicitadas': urls_mas_solicitadas}

        return estadisticas


analizador = AnalizadorLogs('ejemplo.log')
informe = analizador.procesar_logs()
print(informe)
