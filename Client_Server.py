import random
import socket
import os
import threading
import sys

class Client(threading.Thread):
    def __init__(self):
        super().__init__()
        self.port_number = 0

    def run(self):
        try:
            #port number of target
            self.port_number = int(input())
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.connect(('localhost', self.port_number))
            name = sys.argv[1]
            socket_connection.sendall(name.encode())
            server_name = socket_connection.recv(1024).decode()
            print(f"connected to {server_name}")
            while True:
                #entered message
                message_line = input()
                #executes when client enters transfer file message else send message directly to server
                if message_line.startswith("transfer"):
                    file_name_entered = message_line.split()[1]
                    path_of_file = os.path.join(os.getcwd(), file_name_entered)
                    #executes if file exists
                    if os.path.exists(path_of_file):
                        #Send transfer signal to server
                        socket_connection.sendall("transfer".encode())
                        # Send file name to server
                        socket_connection.sendall(file_name_entered.encode())
                        #sends file to server, 1000 bytes each time as file size may be large
                        with open(path_of_file, 'rb') as file_reader:
                            while True:
                                data_to_transfer = file_reader.read(1000)
                                if len(data_to_transfer)<1000:
                                    socket_connection.sendall(data_to_transfer)
                                    break
                                socket_connection.sendall(data_to_transfer)
                            print("File sent successfully")
                    else:
                        #if client entred wrong file name
                        print("Entered a wrong file, Please enter the correct file name")
                else:
                    #disconnects from server when client enters exit by closing connection
                    if message_line.startswith("exit"):
                        print(f"Disconnected from {server_name}")
                        socket_connection.sendall("1".encode()) 
                        socket_connection.close()
                        break
                    else:
                        socket_connection.sendall(message_line.encode())
        except Exception as e:
            print("There is an error try reconnecting or else restart the program")

class Server:
    def __init__(self):
        pass

    def main(self):
        name = sys.argv[1]
        print(f"{name} is running...")
        thread = Client()
        # strats client as thread
        thread.start()
        #assigns random port number to server
        port_number = random.randint(1000,5000)
        try:
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.bind(('localhost', port_number))
            socket_connection.listen()
            print(f"The server port of {name} is {port_number}")
            print("Input target port number to communicate: ")
            #server listens for clients to connect
            connection, addr = socket_connection.accept()
            client_name = connection.recv(1024).decode()
            connection.send(name.encode())
            print(f"{client_name} connected")
            while True:
                #message recieved from client
                message_line = connection.recv(1024).decode()
                #executes if server get transfer message from client
                if message_line == "transfer":
                    file_name_recieved = connection.recv(1024).decode()
                    connection.sendall("File received".encode())
                    # creates new file with by adding new keyword as prefix for existing file name
                    path_of_file_recieved = os.path.join(os.getcwd(), f"new{file_name_recieved}")    
                    with open(path_of_file_recieved, 'wb') as file_writer:
                        while True:
                            data_recieved = connection.recv(1000)
                            #recives data, 1000 bytes each time from client
                            if len(data_recieved)<1000:
                                file_writer.write(data_recieved)
                                break
                            file_writer.write(data_recieved)
                        print(f"File '{file_name_recieved}' received and saved as 'new{file_name_recieved}'")
                elif message_line == "1":
                    #executes when clients enter exit
                    print(f"{client_name} got Disconnected")
                    break
                else:
                    print(f"{client_name}: {message_line}")
            socket_connection.close()
        except Exception as e:
            print("Error occured and client got disconnected")

if __name__ == "__main__":
    server = Server()
    server.main()
