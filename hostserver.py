from socket import *

# reserve a port for the server to use
SERVER_PORT = 8000
# ip address to listen on to, Left blank to wait for a connection
HOST = ''
# variable to save string encoding type as UTF-8
ENCODING = 'utf-8'
# variable to save Carriage Return Line Feed
CLRF = '\r\n'
# create socket and start a tcp connection 
serverSocket = socket(AF_INET, SOCK_STREAM)
# set socket option to reuse socket address
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# create socket address
socketAddress = (HOST, SERVER_PORT)
# bind socket to a local address
serverSocket.bind(socketAddress)
# listen and wait for a connection
serverSocket.listen()

# once connection is established
print("Connection Established")
#accept a connection from client
connection, address = serverSocket.accept()
print("connection from: "+ str(address))

with connection:
    #try to get a valid input from connection
    try:
        #save message
        clientMessage = connection.recv(1024)
        print(clientMessage)
        #grab file name from http request 
        filename = clientMessage.split()[1]
       
        print(filename)
        # open the file ignoring character at position 0 '/'
        serverFile = open(filename[1:])
        #create http header with OK response
        header ='HTTP/1.1 200 OK' + CLRF*2
        #send response back to client with utf8 encoding
        connection.send(header.encode(ENCODING))  
        # parse and send each line of the files content
        # for every line in the file requested
        for line in serverFile.readlines():
            #send line with utf 8 encoding
            connection.sendall(line.encode(ENCODING))
        # close file
        serverFile.close()
        # close connection
        connection.close()
    except IOError: #if file is not found return a error to the browser
        header = 'HTTP/1.1 404 Not Found' + CLRF*2
        connection.send(header.encode(ENCODING))
        print('File not found')
        connection.close()

