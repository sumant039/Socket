import socket # for socket 
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")    
# default port for socket 
port = 80
host_ip = socket.gethostbyname('www.google.com')
print(host_ip)
s.connect((host_ip, port)) 
print ("the socket has successfully connected to google \ on port == %s" %(host_ip))
