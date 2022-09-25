import socket
import random
import threading
import sys
import encryptDecrypt


# Receive messages
def recieveMessage():
    while True:
        messageReceived = s.recv(1024).decode('utf-8')
        if not messageReceived:
            sys.exit(0)
        print ('Message received: ', messageReceived)
        messageReceived = encryptDecrypt.decrypt(messageReceived)
        print ('Message received decrypted: ', messageReceived, '\n')


# Set seed for random numbers
seed = input("Input seed: ")
random.seed(seed)

s = socket.socket()
host = socket.gethostname()
port = 12345
try:
    s.connect((host, port))
except:
    print("Couldn't connect to server")
    quit()
t = threading.Thread(target=recieveMessage)
t.start()

# Send messages
while True:
    messageToSend = input("Message to send: ")
    messageToSend = encryptDecrypt.encrypt(messageToSend)
    messageToSend = messageToSend.encode('utf-8')
    s.sendall(messageToSend)
    print("Encrypted message sent: ", messageToSend, '\n')

s.close()
print("Connection closed\n")