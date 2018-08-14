#! /usr/bin/env python3

import os
import shutil
import sys
from socket import *

MY_PORT = 50000 + 42

def usage():
    """TODO: Docstring for usage.
    on host A server imagefile [port]
    """
    sys.stdout = sys.stderr
    print('(on host A) server imagefile [port]')
    sys.exit(2)

def server():
    """TODO: Docstring for server
    Creates server for recieving files

    """
    if len(sys.argv) > 2:
        port = eval(sys.argv[2])
    else:
        port = MY_PORT
    file = open(sys.argv[1], 'rb')
    BUFSIZE = len(file.read())
    print(BUFSIZE)
    file.close()
    del file
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print('Server ready ... ')
    while True:
        c = 0
        conn, (host, remoteport) = s.accept()
        while True:
            data = conn.recv(BUFSIZE)
            if data:
                c += 1
                conn.send(b'1')
                file = open('./temp/img' + str(c) + '.' + sys.argv[1][-3:], 'wb')
                file.write(data)
                file.close()
            if not data:
                break
            del data
            del file
        conn.send(b'OK\n')
        conn.close()
        print('Done with', host, 'port', remoteport, 'Recieved {} images'.format(c))
        shutil.rmtree('./temp')
        os.mkdir('./temp')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    server()


