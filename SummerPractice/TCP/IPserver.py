import socket


class IPserver:
    host = "localhost"
    port = 4000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Server listening on port: ", port)

    c, addr = s.accept()
    print("connection from: ", str(addr))
    c.send(b"Connection successfully established")
    c.send(b"SPaceX launched rocket yesterday")
    c.send(b"Scientists reached ISS today")
    c.close()
