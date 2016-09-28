import os
import time
import json
import argparse
parser = argparse.ArgumentParser()

parse.add_argument("-s", "--start", dest="start", help="Starting block")
parse.add_argument("-e", "--end", dest="end", help="Ending block")

args = parser.parse_args()

print ("Scanning from block# {} to block# {}".format(args.start, args.end))

time.sleep ("1")
os.system ("clear")

for x in range (args.start, args.end, 1)
    bashCommand = "curl http://45.55.217.124:46657/get_block?height={}".format(a)
    os.system (bashCommand)
    time.sleep("1")
    os.system ("clear")
