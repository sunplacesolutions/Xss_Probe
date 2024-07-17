![XSS_Probe Logo](Xss_Probe/xssprobe.webp)
## Descripción
## XSS_Probe V1.0: 
Es una herramienta para detectar vulnerabilidades de Cross-Site Scripting (XSS) en aplicaciones web. Permite probar múltiples payloads de XSS contra una URL base y reportar las URLs vulnerables.

## Instalación:

1. Clona este repositorio:
git clone https://github.com/tu_usuario/XSS_Probe.git
2. cd Xss_Probe
3. pip install -r requirements.txt
4. python xssprobe.py

Ingresa la URL base cuando se te solicite (ejemplo: https://www.ejemplo.com/prueba.php?param=).

vulnerables.txt: Contiene las URLs vulnerables a XSS.
no_vulnerables.txt: Contiene las URLs que no son vulnerables a XSS.
