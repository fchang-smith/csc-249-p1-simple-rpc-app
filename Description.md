# Overview of Application
This simple client-server program do simple mathematic integer addition and substraction. The user is able to enter a mathematic formula that contains only integers, '+', and/or '-'. 

# Client->Server Message Format
There are three rules for the format:
1. There should be a '+' or '-' in front of any integer, except the first number. If there is no sign in front of the first number, it will be regarded as a '+' operation. Example: '+1-2+3' is the same as '1-2+3', and they are both valid inputs.
2. No other symbol besides '+' or '-' is allowed. Example: '3 - 2 + 5' and '3-2+5=' are not allowed, because space and '=' are not recognized by the program.
3. There should be one integer between every two signs, that means '++', '+-', '--', '-+' are not allowed.

If the input obeys all rules above, then the client will automatically convert the input into a format that the server can understand.

# Server->Client Message Format
The server only process messages in a specific format:
1. The message should begins with '+' or '-' that indicates which operation to do, and follows by a chain of integers that are separated by ','. For example: '+1,3,5' means add 1, 3, 5 together; '-5,6,1' means substract 5, 6, 1.
2. The server can do addition and substration at the same time, if the message use ';' to separate two different operations. Example: '+1,2,3;-4,5,6' means adding 1, 2, 3 together and then substract 4, 5, 6.
 
# Example Output
valid input:
1. input = 1-2+3    output: 2
2. input = +1-2+3    output: 2
3. input = -2+3+5    output: 6
4. input = +1+2+3    output: 6
5. input = -1-2-3    output: -6
invalid input:
input = 3++5    The client will print a warning message 'No number between two signs' and exits.

# Acknowledgments

# Command line traces

Client trace:

client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
What message would you like to send to the server? 1+2+3-5
The input message is changed into:  +1,2,3;-5
sending message '+1,2,3;-5' to server
message sent, waiting for reply
received reply 'b'1'' from server
1+2+3-5 = 1

Server trace:

server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 59063)
Received client message: 'b'+1,2,3;-5'' [9 bytes]
returning 'b'1'' back to clien

