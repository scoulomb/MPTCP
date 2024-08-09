import socket
import time


def main_tcp():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_MPTCP) as s:
        s.connect(("test.multipath-tcp.org", 80))
        print("Connection open")
        while True:
            data = s.recv(1024)
            print("message: %s" % data)
            time.sleep(1)


if __name__ == "__main__":
    print("I am a client")
    main_tcp()
