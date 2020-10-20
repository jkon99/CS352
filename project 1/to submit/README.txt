Project 1
Name: Jonathan Konopka
Netid: jk1549
Group status: SOLO
Python version: 2.7

The general idea of the project was to send a UDP message to the indicated DNS servers and get the received IP address to the Client

There were some things to note about my code. Even though most of my results work, they don't match the expected results file. For example, google.com is supposed to give me 172.217.10.228, but instead it gave me 142.250.64.110 which still sends me to the same site no problems. The BBC IP also brings me to an unknown domain error. The BBC IP's from the intended results also give me this same error anyways. 

What was the REAL issue was determing the type of the answer so that I could display "not found". This is the ONE function that does not work in my code. My results for multiple answers and how many there are are correct, but for facebook.com I get "31.13.71.36,48.114.192.16" when it should "31.13.71.36,not found". Not using packets or bit manipulation might have hindered me from doing this successfully. I assure that I am aware of these problems but I could not fix them without reworking my code. The idea should be to check if the type is 01 (A record) or not, or, I could check if the RDLength is greater than 4 on that ip, but getting the right index to check is not defined. It is difficult to currently satisfy this condition. Hopefully this does not significantly impact my score.

Some of the problems faced when developing the code was converting the byte data to different formats. I remember two errors that drove me crazy during the assignment. The first was when I was on python 3.6 and the Server was not breaking the loop I set for when the source_strings is empty. Switching to python 2.7 seems to have fixed this issue without presenting any others. The other issue was that the websites would send only 0.0.0.0 as their IP address. I noticed that the length of the string tokens I made was displayed as say "7" instead of "07" after converting to hex. I used the format() function instead of hex() for these lines and it fixed the issue. This project took me around 7 hours to complete, which is much longer than the first. Much of the time was going over the material related to the project in order to debug my problems. I made a citation to one of the resources commented in Server.py