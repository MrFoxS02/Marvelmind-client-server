import socket
HOST = "192.168.88.22"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"Give me marvelmind data")
        data = s.recv(1024)
        list_data = format(data.decode())
        list_data = list_data.split()
        print('x = ', list_data[1], ' y = ', list_data[2], ' angle = ', int(list_data[4]) / 10, sep='')

print(f"Received {data!r}")