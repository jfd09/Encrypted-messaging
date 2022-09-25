import random


# Return encrypted form of a message
def encrypt(message):
    messageAsList = list(message)
    
    encryptedList = []
    
    for i in messageAsList:
        randomInt = random.randint(1, 1000000)
        randomInt = randomInt % 30
        encryptedList.append(chr(ord(i) - randomInt))

    encryptedMessage = ''.join(encryptedList)
    return encryptedMessage

# Return decrypted form of a message
def decrypt(message):
    messageAsList = list(message)

    decryptedList = []

    for i in messageAsList:
        randomInt = random.randint(1, 1000000)
        randomInt = randomInt % 30
        decryptedList.append(chr(ord(i) + randomInt))

    decryptedMessage = ''.join(decryptedList)
    return decryptedMessage