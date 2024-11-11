import socket 

ip= input("Enter IP address: ")
port= int(input("Enter the port: "))

try:
    #Creating a ipv4 connection
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #Socket connects to client and prompts for command
    s.connect((ip,port))

    #Accepting 1 connection
    """s.listen(1)
    client_socket, client_address =s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected Successfully!")"""

    cmdlet = input("$>")
    while cmdlet!='end':
        #Sending to client
        s.send(cmdlet.encode('utf-8'))
        #Receiveing 2048 bytes
        result = s.recv(2048).decode()
        cmdlet = input("$")
    s.close()
     
except:
    print("An error has occured.")