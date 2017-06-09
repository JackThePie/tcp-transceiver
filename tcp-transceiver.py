'''Simple TCP receiver used in trasceiving data from cash register to MOBOTIX camera using Raspberry Pi
by Jacek Bera'''

import socket
import sys
import time

TCP_IP = '10.0.0.100'
TCP_PORT = 8601
BUFFER_SIZE = 32

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.0.0.36', 8100)
print >>sys.stderr, 'connecting to %s port %s' % server_address

sock.connect(server_address)
s.connect((TCP_IP, TCP_PORT))

# Main loop
while True:
    try:
		# Receiving and sending
        data = sock.recv(32)
        print >>sys.stderr, 'received "%s"' % data
        
        s.send('Pinstall;a;13:%s;' %data)

	# Except error
    except socket.error as e:
        print e
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        pass
		
# Closing connection
print >>sys.stderr, 'closing socket'
sock.close()
s.close()
