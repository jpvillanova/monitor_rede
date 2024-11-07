def display_devices(devices):
    # Exibe o cabeçalho da tabela
    print("Dispositivos conectados:") # Título
    print("IP" + " "*18 + "MAC") # Cabeçalho da tabela
    # Itera sobre a lista de dispositivos e exibe suas informações
    for device in devices:
        print(f"{device['ip']:16}    {device['mac']}") # IP e MAC address


