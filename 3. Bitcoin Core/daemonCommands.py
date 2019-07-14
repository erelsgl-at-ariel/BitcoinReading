import os
import subprocess
import time
import re

os.system(r"bitcoind -daemon")
time.sleep(9)

cmd = ['bitcoin-cli', 'getblockchaininfo']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output = proc.communicate()[0].decode('ascii') # all blockchaininfo as a string

os.system(r"bitcoin-cli stop")


try:
    blocks = re.search('"blocks": (.+?),\n', output).group(1)
except AttributeError:
    # not found in the output
    blocks = 'not found any blocks' # apply your error handling

try:
    diff = re.search('"difficulty": (.+?),\n', output).group(1)
except AttributeError:
    # not found in the output
    diff = 'not found any difficulty' # apply your error handling



print("blobks:",blocks)
print("difficulty:",diff)
