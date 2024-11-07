import json
from datetime import datetime

log_file = 'log_existentes.json'
frequentes_file = 'log_frequentes.json'
FREQUENCIA_LIMITE = 5

def carregar_logs(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def grava_logs(logs_data, filename):
    with open(filename, 'w') as file:
        json.dump(logs_data, file, indent=4)

def atualizar_logs(dispositivos):
    logs_data = carregar_logs(log_file)
    frequentes_data = carregar_logs(frequentes_file)

    for disp in dispositivos:
        mac = disp['mac']
        # Atualiza o log histórico
        if mac not in logs_data:
            logs_data[mac] = {'ip': disp['ip'], 'fabricante': disp['fabricante']}
        # Atualiza a contagem de frequentes
        if mac in frequentes_data:
            frequentes_data[mac]['contagem'] = min(frequentes_data[mac].get('contagem', 1) + 1, FREQUENCIA_LIMITE)
        else:
            frequentes_data[mac] = {'ip': disp['ip'], 'fabricante': disp['fabricante'], 'contagem': 1}

    grava_logs(logs_data, log_file)
    grava_logs(frequentes_data, frequentes_file)


