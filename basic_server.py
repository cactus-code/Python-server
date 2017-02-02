import socket
import sys

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = "localhost"
port = 7000
server_address = (host , port)
print >>sys.stderr, "starting up server on %s port %s" % server_address
s.bind(server_address)

s.listen(1)
while True:
    print >>sys.stderr, "waiting for a connection"
    connection , client_address = s.accept()

    try:
        print >>sys.stderr, "connection from" , client_address

        while True:
            data = connection.recv(100)
            if data:
                print >>sys.stderr, "received '%s'" % data
                print >>sys.stderr, "sending data back to the client"
                connection.sendall(data)
            else:
                print >>sys.stderr, "no more data from" , client_address
                break

    finally:
        connection.close()
