0.)
Partner 1 name and netid: Jonathan Konopka, jk1549
Partner 2 name and netid: Michael Mlot, mfm184

Final Project (DNS protocol for full resolver)

Goal of this project was to implement the DNS protocol for a full resolver. No gethostbyname function or recursive queries to find addresses. Specifics outlined in these two links: https://tools.ietf.org/html/rfc1034, https://tools.ietf.org/html/rfc1035

1.)
Example input:
python3 my_server.py 5444
dig www.facebook.com @localhost -p 5444 +noedns (as per Piazza)

Based on Piazza posts, our output is not similar to what has been described as to what the output should look like. Upon submission, what we have returned as output from my_server.py replicates the Answer section that is returned from the answer of a DNS server. For most queries that we tested, there were ~12 tuples all in the format of...

{['NAME': bytearray(b'com.'), 'TYPE;: #, 'CLASS': #, 'TTL': ######, 'RDLENGTH': #, 'RDATA':[bytearray(''), 'b'']} x 12

...Followed by 12 more tuples, where 'NAME' is replaced with the 'RDATA' found previously. Within the RDATA of these tuples is the information that gives us our IP Addresses that we need. Sadly we were not able to neatly display this information. However the tuples are clearly separated by '{'s and '}'s.

This was all that we managed to complete. However, we believe we are on the right track as we are communicating with the Nameservers properly, and receiving RDATA that we believe to be accurate. We also face a "Temporary failure in name resolution" error after the code runs properly. However our server stays active until force-quit.

2.)
Problems facing development was time and direction given. The two week time limit was understandable especially considering grading deadlines, but it took at least a week to not only organize a group, but even comprehend the documentation dumped. More concise, specific instructions would have been more realistic for completing a project. Given the previous two assignments, the difficulty growth of projects in this class appears to be exponential. Also with the power outage, accommodation for students seems to have been messy. In Spring 2020 for CS214, the final project got an extra day extension just because ilabs were down. Grades were still in by the deadline with corrections available. The large scope of the project alone was honestly a reason for difficulty in completion, even with ~20 hours put into the actual programming, not reading documentation.