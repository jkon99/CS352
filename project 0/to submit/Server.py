import socket
import argparse

#this is the server file to reverse a string from the client
#Jonathan Konopka, Netid: jk1549

#first step is to parse arguments from user
parser = argparse.ArgumentParser(description='get host/port number')
#default type= is string, might need to change
#maybe use metavar? or use optional arguments
#parser.add_argument('ip', help = 'get the ip address from user')
parser.add_argument('port', type=int, help = 'get port number from user')
args = parser.parse_args()

#ip = args.ip
port = args.port

#print("ip")
#print("port")

#next step is to listen to client
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('',port))
ss.listen(0) #see how many clients can connect at once
sock,addr = ss.accept()

print("Client connected to server!")
#keep looping until no more lines
while True: #loop forever? otherwise modify or comment this out if problems
    client = sock.recv(256)
    if client=="":  #check when received string is empty, then break
        break
    client = client[::-1]  #reverse the string sent
    sock.sendall(client)
    #close gracefully when done sending strings
print("Sent back to server!")
ss.close()
sock.close()
