import socket
import math

ClientSocket = socket.socket()
host = '192.168.56.110'
port = 8888

print('\nWaiting for connection\n')
print("Please select operation :-\n" \
          "1. Logarithmic(log)\n" \
          "2. Square root(sqrt)\n" \
          "3. Exponential(ex)\n")

select = int(input("Select operations form 1, 2, 3 : "))

while True:
     num = input("Enter number: ")
     break
     s_sock.close()


if select == 1:
   print("log()", "=", math.log(int(num)))
   print(str(math.log))

elif select == 2:
   print("sqrt()", "=", math.sqrt(int(num)))
   print(str(math.sqrt))

elif select == 3:
   print("exp()", "=", math.exp(int(num)))
   print(str(math.exp))

else:
   print("Invalid Input")

try:

       ClientSocket.connect((host, port))
except socket.error as e:
       print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
	num = input('Calculated')
	ClientSocket.send(str.encode(num))
	Response = ClientSocket.recv(1024)
	print(Response.decode('utf-8'))

ClientSocket.close()
