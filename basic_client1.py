import socket
import sys

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = "localhost"
port = 7000
server_address = (host , port)

print >>sys.stderr, "connecting to %s port %s" % server_address
s.connect(server_address)

try:
    message = raw_input("Input message: ")
    print >>sys.stderr, "sending '%s'" % message
    s.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = s.recv(len(message))
        amount_received += len(data)
        print >>sys.stderr, "received '%s'" % data

finally:
    print >>sys.stderr, "closing socket"
    s.close()
