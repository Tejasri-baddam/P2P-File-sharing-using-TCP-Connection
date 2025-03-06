## Project Description

- **Chat Program with Peer-to-Peer Network**  
  This project involves creating a chat program where two users can communicate over a network. The program uses two threads: a main thread responsible for handling connections and message exchange, and a writing thread for sending messages. Each user obtains a unique port number for their connection, and they establish connections to each other using these port numbers, allowing bidirectional communication.

- **Real-time Message Exchange & File Transfer**  
  Messages typed by one user appear on the other user's console in real-time. Additionally, the program supports file transfer functionality, enabling users to send files between each other during the chat session.

- **Peer-to-Peer Architecture**  
  Each user acts as both a client and a server, establishing a peer-to-peer network. This architecture allows direct communication between users without relying on a centralized server.

- **How to Run**  
   1. **Check Python Installation**  
      Ensure Python is installed on your system. You can check the version with the command:  
      ```bash
      python --version
      ```
      If Python isn't installed, download the latest version from the official website.

   2. **Run the Program**  
      Open two terminals and run the program by entering a unique identifier for each peer:  
      ```bash
      python Client_Server.py User1
      python Client_Server.py User2
      ```

   3. **Connect and Start Chatting**  
      After launching the program, each user should enter the server port number of the other peer to establish a connection. Once connected, both peers can send messages and transfer files.

   4. **End the Connection**  
      To end the session, type the "exit" command in the terminal.
