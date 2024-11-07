import json
from datetime import datetime

log_file = 'logs.json'

def carregar_logs(filename):
    # Carrega os logs a partir de um arquivo JSON
    try:
        with open(filename, 'r') as file:
            return json.load(file) # Retorna os dados do arquivo
    except FileNotFoundError:
        return {}

def grava_logs(logs_data, filename):
    # Grava os logs em um arquivo JSON
    with open(filename, 'w') as file: # Abre o arquivo para escrita
        json.dump(logs_data, file, indent=4) # Grava os dados no arquivo

def atualizar_logs(dispositivos):
    # Carrega os logs existentes e frequentes
    logs_data = carregar_logs(log_file) # Carrega os logs existentes

    for disp in dispositivos:
        mac = disp['mac']
        data_atual = datetime.now().strftime('%d-%m-%Y | %H:%M:%S')
        # Atualiza o log histórico
        if mac not in logs_data: # Se o dispositivo não está nos logs
            logs_data[mac] = {'ip': disp['ip'], 'fabricante': disp['fabricante'], 'data_entrada': data_atual, 'tempo_na_rede': 0}
        else: # Se o dispositivo já está nos logs
            # Calcula o tempo na rede
            data_entrada = datetime.strptime(logs_data[mac]['data_entrada'], '%d-%m-%Y | %H:%M:%S') 
            tempo_na_rede = (datetime.now() - data_entrada).total_seconds() / 60  # Tempo na rede em minutos
            logs_data[mac]['tempo_na_rede'] = tempo_na_rede # Atualiza o tempo na rede

    # Grava os logs atualizados
    grava_logs(logs_data, log_file)
