import socket
 
UDP_IP1 = "192.168.0.18"
UDP_IP2 = "192.168.0.7"
UDP_PORT = 5005
MESSAGE = "2"
     
print "UDP target IP1:", UDP_IP1
print "UDP target IP2:", UDP_IP2
print "message:", MESSAGE
   
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP1, UDP_PORT))
sock.sendto(MESSAGE, (UDP_IP2, UDP_PORT))