import socket


def is_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex(
        ("127.0.0.1", port)
    )

    sock.close()

    return result == 0