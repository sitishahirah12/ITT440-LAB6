import socket
import sys
import errno
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server\n'))

    while True:
        data = s_sock.recv(2048)
        print(data)
        break
        s_sock.close()

if __name__ == '__main__':

  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind(("", 8888))
  print("The server is connected")
  s.listen(3)

try:
    while True:
      try:
        s_sock, s_addr = s.accept()
        p = Process(target=process_start,args=(s_sock,))
        p.start()
      except socket.error:
        print('got a socket error')

except Exception as e:
    print('an exception occurred!')
    print(e)
    sys.exit(1)
finally:
    print(" Closing socket")
    s.close()
