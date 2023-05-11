import socket
import struct
import sys
import time
import datetime


def requestTimefromNtp(addr='0.de.pool.ntp.org'):
# https://stackoverflow.com/questions/36500197/how-to-get-time-from-an-ntp-server
    REF_TIME_1970 = 2208988800  # Reference time
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (addr, 123))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= REF_TIME_1970
    return time.ctime(t), t

def isoDateTime (t):
# https://www.geeksforgeeks.org/isoformat-method-of-datetime-class-in-python/
    dt=datetime.datetime.fromtimestamp(t)
    return dt.isoformat()
    
