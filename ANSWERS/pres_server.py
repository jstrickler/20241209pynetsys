import socket

from president import President


def handle_client(client):
    while True:
        raw_request = client.recv(1024)

        if not raw_request:
            break

        (num, field) = raw_request.split()

        p = President(num)

        if field == b'FNAME':
            response = p.first_name.encode()
        if field == b'LNAME':
            response = p.last_name.encode()
        if field == b'BDATE':
            response = p.birth_date.encode()
        if field == b'DDATE':
            response = p.death_date.encode()
        if field == b'TSDATE':
            response = p.term_start.encode()
        if field == b'TEDATE':
            response = p.term_end.encode()
        if field == b'PARTY':
            response = p.party.encode()
        if field == b'BSTATE':
            response = p.birth_state.encode()
        if field == b'BPLACE':
            response = p.birth_place.encode()

        client.send(response + b'\n')

    client.close()

    return


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))

server.listen(5)

while True:
    (c, addr) = server.accept()
    handle_client(c)

server.close()
