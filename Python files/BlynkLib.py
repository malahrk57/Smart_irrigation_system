import socket

class Blynk:

    
    def __init__(self, auth, server="blynk.cloud", port=80):
        self.auth = auth
        self.server = server
        self.port = port

    def virtual_write(self, pin, value):

        sock = socket.socket()
        sock.connect((self.server, self.port))

        request = "GET /external/api/update?token={}&V{}={} HTTP/1.1\r\nHost: {}\r\n\r\n".format(
            self.auth, pin, value, self.server
            )

        sock.send(request.encode())
        sock.close()

    def run(self):
        pass
    

