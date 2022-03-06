import sys
import socket

#default ports : https://docs.oracle.com/en/storage/tape-storage/sl4000/slklg/default-port-numbers.html#GUID-8B442CCE-F94D-4DFB-9F44-996DE72B2558
#mapping of protocols to their default ports
defaultPorts = {
    22: "SSH", 
    25: "SMTP", 
    53: "DNS",
    80: "HTTP",
    123: "NTP",
    443: "HTTPS",
    7104: "HTTP",
    7102: "HTTPS",
    7105: "HTTPS",
}

#get input from command line
input = sys.argv

#get starting and ending port numbers, test if all input arguments are there
if len(input) == 4:
    hostname = input[1]
    targetHost = socket.gethostbyname(input[1])
    portRange = input[3][:-1].split(":")
    startPort = int(portRange[0])
    endPort = int(portRange[1]) + 1
else:
    sys.exit("Incorrect input. Please use the format: python tcpPortScanner.py hostname [-p start:end]")

# scan for open ports and list out default ports
openPorts = 0
print("Here are the open ports and protocols of default ports within the range given: ")
for x in range(startPort, endPort): 
    #recieved help from https://www.geeksforgeeks.org/python-simple-port-scanner-with-sockets/
    #also https://docs.python.org/3/library/socket.html 
    newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    connect = newSocket.connect_ex((targetHost, x))
    #if protocol has current port as default port
    if x in defaultPorts:
        print("Port " + str(x) + " has default protocol: " + defaultPorts[x])
    #0 if operation suceeded
    if connect == 0:
        print("Port " + str(x) + " is open")
        openPorts += 1

    newSocket.close()

if openPorts == 0:
	print("No ports open within port range")

#END