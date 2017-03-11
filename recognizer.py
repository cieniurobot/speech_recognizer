import os
import time
import subprocess

class Recognizer():

    def recognize():
        print 'recording'
        p1 = subprocess.call('rec record.wav rate 16k silence 1 0.1 3% 1 3.0 3%',shell=True)
        time.sleep(1)
        print 'recognizing'
        recognized_text = subprocess.check_output('pocketsphinx_continuous -infile record.wav -logfn /dev/null',shell=True, stderr=subprocess.STDOUT)
        return recognized_text


if __name__ == "__main__":
    r = Recognizer()
    recognized_text = r.recognize()
    print recognized_text