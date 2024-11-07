from network_scan import scan_network
from logs import atualizar_logs

def main():
    dispositivos = scan_network()
    atualizar_logs(dispositivos)
    print("Escaneamento completo. Logs atualizados.")

if __name__ == "__main__":
    main()
