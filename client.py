#! /usr/bin/env python3

import os
from socket import *
import sys
import time

MY_PORT = 50000 + 42
def usage():
    sys.stdout = sys.stderr
    print('on host b: client.py count host_A imagefile [time] [port]')
    sys.exit(2)

def client():
    f_time = False
    port = MY_PORT
    if len(sys.argv) < 3:
        usage()
    elif len(sys.argv) > 4:
        f_time = True
        count_time = int(eval(sys.argv[4]))
    elif len(sys.argv) > 5:
        port = eval(sys.argv[5])
    count = int(eval(sys.argv[1]))
    host = sys.argv[2]
    file = open(sys.argv[3], 'rb')
    testdata = bytearray(file.read())
    file.seek(0)
    BUFSIZE = len(file.read())
    print(BUFSIZE)
    file.close()
    del file
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((host, port))
    t3 = time.time()
    i = 0
    if not f_time:
        while i < count:
            i += 1
            s.send(testdata)
            reply = s.recv(1)
            if reply:
                continue
    else:
        t_end = time.time() + count_time
        while time.time() < t_end:
            s.send(testdata)
            reply = s.recv(1)
            if reply:
                continue

    s.shutdown(1)
    t4 = time.time()
    data = s.recv(BUFSIZE)
    t5 = time.time()
    print('Raw Timers: ' , t1, t2, t3, t4, t5)
    print('Intervals: ' , t2 - t1, t3 - t2, t4 - t3, t5- t4)
    print('Total:', t5 - t1)
    print('Throughout:' ,round((BUFSIZE * count * 0.001) / (t5 -t1) , 3), 'K/sec')


if __name__ == "__main__" :
	client()

