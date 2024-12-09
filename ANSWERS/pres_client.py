import socket

for n in range(1, 45):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('localhost', 7777))  # connect to server
    client.send(f'{n} LNAME\n'.encode())
    lname = client.recv(1024).strip().decode()
    client.send(f'{n} FNAME\n'.encode())
    fname = client.recv(1024).strip().decode()
    client.close()

    print(f"{fname} {lname}")
