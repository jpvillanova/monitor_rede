import time
from network_scan import scan_network
from logs import atualizar_logs

def main():
    while True:
        # Escaneia a rede para obter dispositivos conectados
        dispositivos = scan_network()
        # Atualiza os logs com os dispositivos escaneados
        atualizar_logs(dispositivos)
        # Imprime uma mensagem de conclusão
        print("Escaneamento completo. Logs atualizados.")
        # Aguarda 10 minutos antes de escanear novamente
        time.sleep(600)

if __name__ == "__main__":
    main()
