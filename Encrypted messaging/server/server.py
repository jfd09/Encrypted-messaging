import socket
import random
import threading
import sys
import encryptDecrypt


# Receive messages
def recieveMessage():
    while True:
      try:
         messageReceived = c.recv(1024)
      except:
         print("Unable to receive messages from client")
         c.close()
         print("Connection closed")
         return
      messageReceived = messageReceived.decode('utf-8')
      print("Message received: ", messageReceived)
      messageReceived = encryptDecrypt.decrypt(messageReceived)
      print("Message received decrypted: ", messageReceived, '\n')


s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
   # Set seed for random numbers
   seed = input("Input seed: ")
   random.seed(seed)
   
   c, addr = s.accept()
   print ('Got connection from', addr)

   # Start thread to receive messages
   t = threading.Thread(target=recieveMessage)
   t.start()

   # Send messages
   while True:
      messageToSend = input("")
      messageToSend = encryptDecrypt.encrypt(messageToSend)
      messageToSend = messageToSend.encode('utf-8')
      # If thread to receive messages is_alive
      if t.is_alive():
         try:
            c.sendall(messageToSend)
         except:
            print("Unable to send messages to client")
            break
      else:
         break
      print("Encrypted message sent: ", messageToSend, '\n')

   # Close connection if not already closed
   if not c._closed:
      c.close()
      print("Connection closed")