import time
import os
os.system ("clear")
for a in range (236221, 236223, 1) :
    bashCommand = "curl http://45.55.217.124:46657/get_block?height=%d" % a
    os.system (bashCommand)
    time.sleep (1)
    #os.system ("clear")



