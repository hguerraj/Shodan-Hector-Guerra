#Seguridad de sistemas
import shodan
import json

# Clave de API de Shodan
API_KEY = 't2CBQHoxqK8j5MOLE1e4tZFaNtmS56Fb'

# Inicializar el cliente de Shodan utilizando la clave API proporcionada
api = shodan.Shodan(API_KEY)

# Comando de filtrado: búsqueda de dispositivos en Guatemala, específicamente en la ciudad de Guatemala
query = 'country:"Guatemala" city:"Guatemala"'

def main():
    try:
        # Realizar la búsqueda en Shodan con el comando de consulta especificado
        results = api.search(query)
        
        # Variables para almacenar el resumen de la búsqueda
        total_ips = 0  # Contador de direcciones IP encontradas
        ip_por_puerto = {}  # Diccionario para contar las IPs por puerto abierto
        
        # Mostrar los resultados obtenidos en la búsqueda
        print(f"Resultados de la búsqueda para: {query}")
        print("-----------------------------------------------------")
        
        # Iterar sobre los resultados de la búsqueda para mostrar información relevante
        for result in results['matches']:
            ip = result['ip_str']  # Obtener la IP del resultado
            ports = result['port']  # Obtener el puerto abierto del dispositivo
            print(f"IP: {ip}, Puerto: {ports}")
            
            total_ips += 1  # Incrementar el contador de IPs encontradas
            
            # Contabilizar las IPs por puerto
            if ports not in ip_por_puerto:
                ip_por_puerto[ports] = 1  # Si el puerto no existe en el diccionario, inicializarlo
            else:
                ip_por_puerto[ports] += 1  # Incrementar el contador de IPs para el puerto dado

        # Mostrar un resumen de los resultados obtenidos
        print("\nResumen:")
        print(f"Total de direcciones IP identificadas: {total_ips}")
        
        # Mostrar la cantidad de IPs por cada puerto encontrado
        print("Total de IPs por puerto abierto:")
        for puerto, cantidad in ip_por_puerto.items():
            print(f"Puerto {puerto}: {cantidad} IPs")
        
        # Información adicional para identificar al autor del script
        print("\nNúmero de carnet: 1990-18-10585")
        print("Nombre completo: Héctor Alfredo Guerra Jimenez")
        print("Curso: Auditoría y Seguridad de Sistemas")
        print("Sección: B")

    except shodan.APIError as e:
        # Manejo de errores en caso de que la consulta falle
        print(f"Error al realizar la consulta: {e}")

# Verificar si este script es ejecutado directamente, en cuyo caso se llama a la función principal
if __name__ == "__main__":
    main()

#fin