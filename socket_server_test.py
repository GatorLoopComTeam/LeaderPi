import socket
from time import sleep
s = socket.socket()
address = ''
port = 9000
for x in range(0,10):
	try:
		s.bind((address, port))
		s.listen(1)
		conn, addr = s.accept()
		while True:
			data= conn.recv(1).decode("ascii")
			if data:
				print(data)
			else:
				sleep(1)
		s.close()
	except Exception as e: 
		print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
	finally:
		s.close()
