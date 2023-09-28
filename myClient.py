import socket
import re

HOST = "127.0.0.1"  # This is the loopback address
PORT = 65432        # The port used by the server

def run_client():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(s):
                break

def talk_to_server(sock):
    msg = input("What message would you like to send to the server? ")
    if msg == 'quit':
        print("client quitting at operator request")
        return False
    if (checkFormat(msg)):
        command = changeInput(msg)
    else:
        return False
    if not command:
        return False
    print(f"sending message '{command}' to server")
    sock.sendall(command.encode('utf-8'))
    print("message sent, waiting for reply")
    reply = sock.recv(1024)
    if not reply:
        return False
    else:
        print(f"received reply '{reply}' from server")
        reply = reply.decode()
        print(msg, '=', reply)
        return reply
    
def checkFormat(msg):
    if (len(msg)==0):
        print('The message is empty')
        return False
    firstSign = False
    if (msg[0]=='+') or (msg[0]=='-'):
        sign = msg[0]
        msg = msg[1:]
        firstSign = True
    number = re.split('\+|-', msg)
    for num in number:
        if (num == ''):
            print('no number between two signs')
            return False
        if not num.isnumeric():
            print(num, 'is not recognized')
            return False
    list = []
    if (firstSign):
        list.append(sign)
    for i in range(0, len(msg)):
        if (msg[i]=='+') or (msg[i]=='-'):
            list.append(msg[i])
    if (len(number)==len(list)):
        return True
    elif (len(number)-1==len(list)):
        return True
    else:
        return False
    

def changeInput(msg):
    length = len(msg)
    plus = []
    minus = []
    list = []
    firstSign = True
    if (msg[0].isnumeric()):
        list.append('+')
        firstSign = False
    for i in range(0, length):
        if (msg[i]=='+') or (msg[i]=='-'):
            list.append(msg[i])
    number = re.split('\+|-', msg)
    if (firstSign):
        number = number[1:]
    if not (len(number) == len(list)):
        return False
    for i in range (0, len(list)):
        if (list[i]=='+'):
            plus.append(number[i])
        else:
            minus.append(number[i])
    plusStr = ''
    if (len(plus)!=0):
        plusStr = ','.join(plus)
        plusStr = '+' + plusStr
    minuStr = ''
    if (len(minus)!=0):
        minuStr = ','.join(minus)
        minuStr = '-' + minuStr
    if (len(plus)!=0) and (len(minus)!=0):
        result = plusStr + ';' + minuStr
    if (len(plus)!=0) and (len(minus)==0):
        result = plusStr
    if (len(plus)==0) and (len(minus)!=0):
        result = minuStr
    print('The input message is changed into: ', result)
    return result


if __name__ == "__main__":
    run_client()
    print("test client is done, exiting...")
 
 
        

