 #!/usr/bin/env python
import socket


    
TCP_IP = '192.168.28.6'
TCP_PORT = 6669
BUFFER_SIZE = 1024
MESSAGE = "02323030323032303031303031323530202020203130312020313034464630313132303138393133303031323031383931360317"
MESSAGE2 = "200202"
"""
print MESSAGE.decode("hex")

toHex = MESSAGE.encode("hex")
print MESSAGE 
print toHex
"""
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
toASCII = data.encode("ascii")
print "received data:", data
print "ascii:", toASCII

