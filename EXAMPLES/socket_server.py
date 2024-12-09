
import socket


def main():
    serv = setup()
    while True:
        (csock, addr) = serv.accept()  # blocks until client connects
        handle_client(csock)


def setup():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create server socket
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse a port even if it is busy (usually no consequences from this)

    serv.bind((socket.gethostname(), 7777))  # listen on port 7777

    serv.listen(5)  # mark socket as accepting connections; limit listen queue to 5 connections

    return serv


def handle_client(cli_sock):
    request = cli_sock.recv(1024)  # read data (in bytes) from client

    reply = request.upper()[::-1]  # reverse client data and make it upper case

    cli_sock.sendall(reply)  # send reply to client
    cli_sock.close()  # close client connection


if __name__ == '__main__':
    main()
