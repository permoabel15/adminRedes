import os
import re
import subprocess

ips = []
output = os.popen("nmap -sP 192.168.0.0/24").read()

# Lista de direcciones IP
ips = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output)

# Nombre del script a ejecutar
script_name = "run_script.sh"

# Ejecuta el script en cada dirección IP
for ip in ips:
    subprocess.call(["ssh", "abelperez@" + ip, "permoabel", script_name])
