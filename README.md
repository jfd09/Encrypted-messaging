# Encrypted-messaging

Server and client program are able to send encrypted messages to each other

Messages are encrypted by randomizing each character in the message

Randomization is determined by the seed that is chosen. If both sides enter the same
seed, they will be able to correctly decode the sender’s messages

Code to receive messages is ran in a separate thread to avoid being blocked by the code
to send a message

Code for error checking of input and of networking still needs to be coded
