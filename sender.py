import socket                

cipher={
   'a': 'm',
   'b': 'n',
   'c': 'b',
   'd': 'v',
   'e': 'c',
   'f': 'x',
   'g': 'z',
   'h': 'a',
   'i': 's',
   'j': 'd',
   'k': 'f',
   'l': 'g',
   'm': 'h',
   'n': 'j',
   'o': 'k',
   'p': 'l',
   'q': 'p',
   'r': 'o',
   's': 'i',
   't': 'u',
   'u': 'y',
   'v': 't',
   'w': 'r',
   'x': 'e',
   'y': 'w',
   'z': 'q',
	' ': ' ',
}

#accept and encrypt message using cipher
msg_en_list=[]
ip = input("Enter message to encrypt\n")
ip=list(ip.lower())

for x in ip:
  if x in cipher:
    msg_en_list.append(cipher[x])

msg_en="".join(str(x) for x in msg_en_list)
print(msg_en)
print("\n")
byte_msg = bytearray(msg_en,'utf-8')

#socket init and setup  
s = socket.socket()          
host = socket.gethostname() 
port = 12345   
s.bind((host,port))         
s.listen(5)
print("socket listening...") 

#send the encrypted message
while True: 
   c, addr = s.accept() 
   c.send(byte_msg)    
   c.close() 







