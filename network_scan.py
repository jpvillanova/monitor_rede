import requests
from scapy.all import ARP, Ether, srp

def get_fabricante(mac):
    url = f"https://api.macvendors.co/{mac}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('result', {}).get('company', 'Desconhecido')
    else:
        return "Erro na consulta"

def scan_network():
    dispositivos = []
    # Lógica de escaneamento usando ARP e Scapy
    # Exemplo simplificado
    result = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.1/24"), timeout=2, verbose=False)[0]
    for _, dispositivo in result:
        mac = dispositivo.hwsrc
        ip = dispositivo.psrc
        fabricante = get_fabricante(mac)
        dispositivos.append({'ip': ip, 'mac': mac, 'fabricante': fabricante})
    return dispositivos
