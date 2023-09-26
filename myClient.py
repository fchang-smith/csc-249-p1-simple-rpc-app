import socket

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
    command = changeInput(msg)
    if (not command):
        return False
    print(f"sending message '{command}' to server")
    sock.sendall(command.encode('utf-8'))
    print("message sent, waiting for reply")
    reply = sock.recv(1024)
    if not reply:
        return False
    else:
        print(f"received reply '{reply}' from server")
        return reply

def changeInput(msg):
    length = len(msg)
    plus = []
    minus = []
    sign = 'plus'
    for i in range(0, length):
        if (msg[i].isnumeric()) and (sign == 'plus'):
            plus.append(msg[i])
        elif (msg[i].isnumeric()) and (sign == 'minus'):
            minus.append(msg[i])
        elif (msg[i] == '+'):
            sign = 'plus'
        elif (msg[i] == '-'):
            sign = 'minus'
        else:
            print(msg[i], 'is not recognized')
            return False
    plusStr = ','.join(plus)
    minuStr = ','.join(minus)
    result = '+' + plusStr + ';' + '-' + minuStr
    return result

if __name__ == "__main__":
    run_client()
    print("test client is done, exiting...")

