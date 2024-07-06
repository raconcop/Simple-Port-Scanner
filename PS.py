
import socket
import sys
from datetime import datetime


target = input(str("Target IP: "))


def lines():
    print("_"*50)


# Banner
lines()
print("Scanner Target: "+ target)
print("Scanning started at: " + str(datetime.now()))
lines()



try:
    # Scan every port on the target IP
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        # Return open port
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
            
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting...")
    
except socket.error:
    print("\n Host not responding...")
    sys.exit()