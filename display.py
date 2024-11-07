def display_devices(devices):
    print("Dispositivos conectados:")
    print("IP" + " "*18 + "MAC")
    for device in devices:
        print(f"{device['ip']:16}    {device['mac']}")

