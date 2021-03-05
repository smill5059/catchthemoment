import socket
from raspshot import happy
from picamera import PiCamera


UDP_IP = "192.168.0.7"
UDP_PORT = 5005
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
camera=PiCamera()
camera.resolution = (640,480)
camera.framerate = 90
camera.start_preview()
while True:
    
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    if data== "1":
        camera.start_recording('/home/pi/video.h264')
    elif data=="2":
        camera.stop_recording()
        camera.stop_preview()
        break