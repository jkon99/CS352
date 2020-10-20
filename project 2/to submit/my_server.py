#Abraham gale 2020
#Jonathan Konopka, netid: jk1549
#Michael Mlot, netid: mfm184
#feel free to add functions to this part of the project, just make sure that the get_dns_response function works
from resolver_backround import DnsResolver   #if there's issues here change "resolver_backround" to "resolver_background" depending on .py naming 
import threading
import socket
import struct
import argparse
from sys import argv
from time import sleep
from helper_funcs import DNSQuery

parser = argparse.ArgumentParser(description="""This is a DNS resolver""")
parser.add_argument('port', type=int, help='This is the port to connect to the resolver on',action='store')
args = parser.parse_args(argv[1:])

class MyResolver(DnsResolver):
	def __init__(self, port):
		self.port = port
		#define variables and locks you will need here
		self.nameserver = ["91.239.100.100","198.101.242.72"]
		self.cache_lock = threading.Lock()
	def get_dns_response(self, query):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#input: A query and any state in self
		#returns: the correct response to the query obtained by asking DNS name servers
		#Your code goes here, when you change any 'self' variables make sure to use a lock
		
		
		question = DNSQuery(query)
                #see if answer is in local information, if so return to client (1)
                #find best servers to ask (2)
		question.header['RD'] = 0
		#Nameserver's ip = ip
		ip = self.nameserver[0]
		while(1): #send queries until one returns a response (3)
			sock.sendto(question.to_bytes(), (ip , 53) )
			returnedVal = sock.recv(1024)		
			#query that we are given from dig, converted to_bytes
			tuples = DNSQuery(returnedVal)
			print(tuples.answers)
			x = 1
			if(tuples.answers[0]['TYPE'] == 2):
				while(tuples.answers[x]['TYPE'] != 1):
					x = x + 1
			ip = (tuples.answers[x]['RDATA'][0])
			#IP in hex
			#print(ip)
			sock.sendto(question.to_bytes(), (ip , 53) )
			returnedVal = sock.recv(1024)
			tuples = DNSQuery(returnedVal)
			#print(tuples.answers)
			break
		
		#assigns necessary values to the multiple parts of our header
		answer = DNSQuery()
		
		answer.header['QR'] = 1
		answer.header ['RA'] = 0
		answer.header['RCODE'] = 2
		answer.header['AA'] = 1
		answer.header['TC'] = 0   
		answer.header ['NSCOUNT'] = 0
		answer.header ['ARCOUNT'] = 0
		answer.header['ID'] = question.header['ID']
		answer.header['OPCODE'] = question.header['OPCODE']
		answer.header['RD'] = question.header['RD']
		answer.header ['QDCOUNT'] = question.header['QDCOUNT']
		answer.header ['ANCOUNT'] = len(tuples.answers)
		answer.question = question.question
		answer.answers = tuples.answers

		answer.question = question.question
		print(answer)
		return answer.to_bytes()
		
#most code above is where self code goes
resolver = MyResolver(args.port)
print("Waiting for requests...")
resolver.wait_for_requests()
