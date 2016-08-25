#!/usr/bin/env python

import socket


TCP_IP = '192.168.28.6'
TCP_PORT = 6668
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
MESSAGE = "02323030323032303031303031323530202020203130312020313034464630313132303138393133303031323031383931360317"
s.send(MESSAGE)
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()