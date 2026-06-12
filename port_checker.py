import socket
import time


def is_port_open(port):
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    result = sock.connect_ex(
        ("127.0.0.1", port)
    )

    sock.close()

    return result == 0


def wait_for_port(
    port,
    timeout=120,
    interval=2
):
    start_time = time.time()

    while time.time() - start_time < timeout:

        if is_port_open(port):
            return True

        time.sleep(interval)

    return False