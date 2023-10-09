#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A simple Web server.
GET requests must name a specific file,
since it does not assume an index.html.
"""

import socket
import threading
from os.path import exists


def handler(conn_socket: socket.socket, address: tuple[str, int]) -> None:
    """
    Handles the part of the client work-flow that is client-dependent,
    and thus may be delayed (blocking program flow).
    """
    try:
        # Receives the request message from the client
        # Delete pass and write
        old_message = conn_socket.recv(1024)
        message = old_message.decode()

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        # Delete pass and write
        path = message.split(" ")[1]

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        # Read file off disk, to send
        # Store the content of the requested file in a temporary buffer
        # Delete pass and write
        path = path[1:]
        if not exists(path):
            raise IOError("File not found 404")
        else:
            file = open(path, "r")
            file_content = file.read()

        # Send the HTTP response header line to the connection socket
        # Delete pass and write
        http_response = "HTTP/1.1 200 OK\n\n"
        http_response += file_content

        # Send the content of the requested file to the connection socket
        # Delete pass and write
        conn_socket.send(http_response.encode())

    except IOError:
        # Send HTTP response message for file not found (404)
        # Delete pass and write
        http_response = "HTTP/1.1 404\n\n"
        conn_socket.send(http_response.encode())

        # Open file, store the content of the requested file in a temporary buffer
        # Delete pass and write
        file = open("web_files/not_found.html")
        message = file.read()

        # Send the content of the requested file to the connection socket
        # Delete pass and write
        conn_socket.send(message.encode())

    except:
        print("Bad request")
    finally:
        conn_socket.close()


def main() -> None:
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_port = 6789
    # Bind the socket to server address and server port
    # Delete pass and write
    # server_socket.bind(("192.168.0.21", server_port))
    server_socket.bind(("127.0.0.1", server_port))

    # Listen to at most 2 connection at a time
    # Server should be up and running and listening to the incoming connections
    # Delete pass and write
    server_socket.listen(2)
    # print("now listening")
    threads = []
    try:
        while True:
            # Set up a new connection from the client
            # Delete pass and write
            c, address = server_socket.accept()

            # call handler here, start any threads needed
            # Delete pass and write
            new_thread = threading.Thread(target=handler, args=(c, address))
            new_thread.start()

            # Just to keep track of threads
            threads.append(new_thread)
    except:
        print("Exception occured (maybe you killed the server)")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
