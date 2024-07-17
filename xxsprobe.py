import requests
import re
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Color:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    RESET = "\033[0m"

art = '''\

██╗  ██╗███████╗███████╗        ██████╗ ██████╗  ██████╗ ██████╗ ███████╗
╚██╗██╔╝██╔════╝██╔════╝        ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝
 ╚███╔╝ ███████╗███████╗        ██████╔╝██████╔╝██║   ██║██████╔╝█████╗  
 ██╔██╗ ╚════██║╚════██║        ██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔══╝  
██╔╝ ██╗███████║███████║███████╗██║     ██║  ██║╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ '''

print(Color.GREEN + art + Color.BLUE + "SunplaceSolutions\n" + Color.RESET)

# Entrada del usuario para la URL base
url_base = input('Ingrese la URL base (Ejemplo: https://www.ejemplo.com/prueba.php?param=): ')

# Leer payloads de XSS desde un archivo
try:
    with open("payloadxss.txt", "r") as file:
        payloads = file.readlines()
except FileNotFoundError:
    print(Color.RED + "El archivo 'payloadxss.txt' no se encontró. Asegúrese de que el archivo esté en el mismo directorio que el script." + Color.RESET)
    exit()

# Probar cada payload
try:
    for payload in payloads:
        payload = payload.strip()
        test_url = url_base + payload
        
        response = requests.get(test_url, verify=False)

        if response.status_code == 200:
            content = response.text

            # Buscar palabras clave 'alert' o '31337'
            if re.search(r'alert|31337', content, re.IGNORECASE):
                print(Color.GREEN + f"{test_url} es vulnerable a XSS!" + Color.RESET)
                with open("vulnerables.txt", "a") as archivo_vulnerables:
                    archivo_vulnerables.write(test_url + "\n")
            else:
                with open("no_vulnerables.txt", "a") as archivo_no_vulnerables:
                    archivo_no_vulnerables.write(test_url + "\n")
        else:
            print(Color.RED + f"No se pudo acceder a la URL: {test_url}" + Color.RESET)
        
        # Esperar 5 segundos antes de probar el siguiente payload
        time.sleep(5)
except KeyboardInterrupt:
    print(Color.RED + "\nEjecución interrumpida por el usuario. Saliendo..." + Color.RESET)
