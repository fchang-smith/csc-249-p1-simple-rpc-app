import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def addition(msg):
    length = len(msg)
    print('length of the message: ', length)
    for i in range (1, length):
        if (not msg[i].isnumeric()) and (not msg[i]==','):
            print('The receiving message is not in correct format')
            return False
    num = msg[1:].split(',')
    print('get single number: ', num)
    sum = 0
    for i in range(0, len(num)):
        print('num[i]: ',num[i])
        sum += int(num[i])
    return sum 

def substraction(msg):
    length = len(msg)
    diff = 0
    for i in range (1, length):
        if (not msg[i].isnumeric()) and (not msg[i]==','):
            print('The receiving message is not in correct format')
            return False
    num = msg[1:].split(',')
    diff = 0
    for i in range(0, len(num)):
        diff -= int(num[i])
    return diff 

def recvCommand(data):
    data = data.decode('utf-8')
    print('Decoding data: ', data)
    opList = data.split(';')
    print('after split: ', opList)
    sum = 0
    diff = 0
    result = 0
    add = True
    minus = True
    for operation in opList:
        if (len(operation)!=0):
            if (operation[0] == '+'):
                add = addition(operation)
                if (not add):
                    return False
                sum += add
            elif (operation[0] == '-'):
                minus = substraction(operation)
                if (not minus):
                    return False
                diff += minus
            else:
                print('The command format is incorrect (should be + or -)')
                return False
    
    result = sum + diff
    result = str(result).encode('utf-8')
    return result

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            result = recvCommand(data)
            if not result:
                break
            print(f"returning '{result!r}' back to client")
            conn.sendall(result)

print("server is done!")



