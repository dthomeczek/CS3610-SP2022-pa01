#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Run with the following command line parameters:
python3 client_browser.py hostname port file

Examples:
$ python3 client_browser.py info.cern.ch 80 ""
$ python3 client_browser.py localhost 6789 "hello_world.html"
"""

import sys
import socket
import requests  # type: ignore

# check for args
if len(sys.argv) != 4:
    server_hostname = "localhost"
    server_ip = "127.0.0.1"
    server_port = 6789
    file_name = "hello_world.html"
else:
    # Dele the pass and do your arg parsing here
    # Hint, you may need to get an IP from a hostame.
    server_hostname = sys.argv[1]
    server_ip = socket.gethostbyname(server_hostname)
    server_port = int(sys.argv[2])
    file_name = sys.argv[3]

try:
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # Delete the pass and make your GET request here
    client_socket.connect((server_ip, server_port))
    if server_hostname != "localhost":
        get_response = requests.get("http://" + server_hostname)
        status_val = get_response.status_code
        print("HTTP/1.1 " + str(status_val) + " OK")
        headers = get_response.headers
        for i in headers:
            print(str(i) + ": " + str(headers[i]))
        print("")
        print(get_response.text)
    else:
        request = "GET /" + file_name + " HTTP/1.1  "
        client_socket.send(request.encode())
        get_response = ""
        get_response = client_socket.recv(10024)
        response_code = get_response.decode()

        # Delete the pass and parse the return data here
        # Hint: a loop helps to make sure you got all the data
        # Just print what's returned from the server
        print(response_code)
except Exception as e:
    print("Exception was: ", e)

finally:
    client_socket.close()
