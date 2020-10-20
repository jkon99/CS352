import socket
import binascii
import argparse
import struct

#Project 1, this is to send UDP message to server and return the IP address 
#Jonathan Konopka, Netid: jk1549

#first step is to parse arguments from user
parser = argparse.ArgumentParser(description='get port number')
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
#above is basically my project 0

#make a loop and then put that information into a new socket for DNS
#convert from client into hexadecimal DNS query, convert to binary then send to DNS

#message ="AA AA 01 00 00 01 00 00 00 00 00 00 07 65 78 61 6d 70 6c 65 03 63 6f 6d 00 00 01 00 01"



#Cited below from  https://routley.io/posts/hand-writing-dns-messages/
def send_udp_message(message,address,port):
    #message is hexadecimal encoded string
    message = message.replace(" ", "").replace("\n","")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        data, _ = sock.recvfrom(4096)
    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")

def format_hex(hex):
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)

#END OF CITATION

def message_helper(message):
    #to help the message and response process
    response = send_udp_message(message, "8.8.8.8", 53)
    #print("response:" + response)
    splitresponse = format_hex(response).split()
    """
    typeA1 = str(int(splitresponse[1],16))
    typeA2 = str(int(splitresponse[2],16))
    print("Type: " + typeA1)
    print("Type: " + typeA2)
    if typeA2 !=1:
        return "not found"
    """
    answers = int(splitresponse[7],16)
    #print("response:" + response)
    j = 0
    k = 0
    DNSip = ""
    while j != answers:
        #IF NOT AN A RECORD OR RDLENGTH >4 THEN PRINT "NOT FOUND"
        ip1 = str(int(splitresponse[-4+k],16))
        ip2 = str(int(splitresponse[-3+k],16))
        ip3 = str(int(splitresponse[-2+k],16))
        ip4 = str(int(splitresponse[-1+k],16))
        DNSip = DNSip + ip1 + "." + ip2 +  "." + ip3 + "." + ip4
        j = j + 1
        k = k - 16
        if j!=answers:
            DNSip = DNSip + ","
    return DNSip

#above is taking the received message and turning into ip format, will go into loop from client

#print(format_hex(response))

print("Client connected to server!")
#i = 0
while True:
    client = sock.recv(256)
    if client=="":
        break
    #convert client bytes into format to send to DNS message

    #try packing and unpacking? 
    message ="AA AA 01 00 00 01 00 00 00 00 00 00 " #header of message, then add the URL

    #google.com or whatever
    clientstring  = str(client)
    clientsplit = clientstring.split(".")
    #length = len(client[1])
    #print(clientsplit[0])
    #print(clientsplit[1])
    #print(clientsplit[2])
    #i = i+1
    #print(i)
    splits = len(clientsplit)
    for i in range(0,splits):
        tempstr = clientsplit[i]
        length = len(tempstr)
        message = message + format(length, '02x') + " "
        for x in range(0,length):
            #tempint = int(tempstr[x])
            message = message + hex(ord(tempstr[x])).lstrip("0x").rstrip("L") + " "
    """
    tempstr = clientsplit[2]
    #print("temp:" + tempstr)
    length = len(tempstr)
    #print("increment:" + str(i))
    message = message + format(length, '02x') + " "
    for y in range(0,length):
        #tempint = int(tempstr[x])
    message = message + hex(ord(tempstr[y])).lstrip("0x").rstrip("L") + " "
    """
    #rest of message 
    message = message + "00 00 01 00 01"
    #print(message)
    client = message_helper(message)
    #print(client)
    client = client.encode()
    sock.sendall(client) #byte object not string

print("sent back to server")

ss.close()
sock.close()

