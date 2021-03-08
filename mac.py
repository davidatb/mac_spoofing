# herramienta de mac spoofing, simple tool mac changer
# www.davidatb.com

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help="interface a la que se le cambiara la mac ")
    parser.add_option("-m", "--mac", dest = "new_mac", help="nueva direccion mac ")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor indica una Interfaz de red, usa --help para obtener ayuda ")
    elif not options.new_mac:
        parser.error("[-] Por favor indica una Mac address, usa --help para obtener ayuda ")
    return options
    
def change_mac(interface, new_mac):
    print("[+] Cambiando direccion mac de la interface " + interface + " a " + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No se pudo leer la direccion Mac")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Mac actual = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac cambio correctamente a " + current_mac)
else:
    print("[-] Mac no se pudo cambiar")

