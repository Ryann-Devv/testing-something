import socket
import sys
import time

print("This is a UDP Pinger")
print("Created by FuyuWinter")
print("")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    ip = raw_input("IP Address: ")
except:
    print("Error: There must be an IP Address.")

try:
    size = raw_input("Data Size: ")
    data = size
except:
    print("Error: You must set how much data to send.")

def is_connected():
    try:
        host = socket.gethostbyname(ip)
        s = socket.create_connection((host, 80))
        print("Sending %s %s Bytes of data" % (host, size))
    except:
        print("Request Failed")

host = socket.gethostbyname(ip)

while True:
    sock.sendto(data, (host, 80))
    is_connected()
    time.sleep(1)
