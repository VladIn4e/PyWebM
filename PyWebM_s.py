import socket

def main():
    host = '192.168.1.68'
    port = 9090

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    print("Waiting for connection...")
    connection, address = s.accept()
    print("Connection from " + str(address))
    while True:
        try:
            toSend = input("-> ")
            if toSend == '':
                a = '.'
                connection.send(a.encode())
            else:
                connection.send(toSend.encode())
            data = connection.recv(1024).decode('utf-8')
            print(data)
        except:
            break
    print("Connection refused")
    connection.close()

if __name__ == '__main__':
    main()