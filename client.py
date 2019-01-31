import socket                
#from operator import itemgetter
import operator 

s = socket.socket() 
host = socket.gethostname()         
port = 12345            
s.connect((host, port)) 
msg_encrypt = s.recv(1024) 

#Standard frequency values 
genFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

#number of letters
letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

msg = msg_encrypt.decode('utf-8')
length = len(msg)
msg = msg.upper()
print(length)
for s in msg:
 if s in letterCount:
   letterCount[s]=letterCount[s]+1

#calculate frequency
for let in letterCount:
  letterCount[let] = letterCount[let]/length

print(letterCount)

#sort by descending order of frequencies of letters
sortedf = sorted(letterCount.items(), key=operator.itemgetter(1),reverse=True)
sorted_dictf = dict(sortedf)   

#set frequency dictionary values with general frequency values
compare_dict={}
gfq = list(genFreq.keys())
sdf = list(sorted_dictf.keys())

for i,x in enumerate(sdf):
   compare_dict[x] = gfq[i]


#decrypt using respective key words
decrypt = []
print(msg)
for a in msg:
  if a in compare_dict:
    decrypt.append(compare_dict[a])

final_msg = "".join(str(s) for s in decrypt)
print(final_msg.lower())




      





