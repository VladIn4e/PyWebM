import socket
import os


def ExecuteCommand(command):
    output = os.popen(command).read()
    return output


def main():
    host = '192.168.1.68'
    port = 9090
    while True:
        while True:
            try:
                s = socket.socket()
                s.connect((host, port))
            except:
                break

            while True:
                try:
                    data = s.recv(1024).decode()
                    print(data)
                    toSend = input("-> ")
                    if toSend == '':
                        a = '.'
                        s.send(a.encode())
                    else:
                        s.send(toSend.encode())
                except:
                    break
    s.close()


if __name__ == "__main__":
    main()