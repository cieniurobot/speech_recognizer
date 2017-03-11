import os
import time
import subprocess

print 'recording'
p1 = subprocess.call('rec record.wav rate 16k silence 1 0.1 3% 1 3.0 3%',shell=True)
time.sleep(1)
print 'recognizing'
p2 = subprocess.check_output('pocketsphinx_continuous -infile record.wav -logfn /dev/null',shell=True, stderr=subprocess.STDOUT)
print 80*'*'
print p2 
print 80*'*'
