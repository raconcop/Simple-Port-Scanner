import socket
import subprocess
import sys
from datetime import datetime


#Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)