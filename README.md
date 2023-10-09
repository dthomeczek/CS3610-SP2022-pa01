# Assignment pa01

Within the provided assignment, the task was to create a socket, bind it to a specific address and port, and send/receive HTTP packet(s). We also developed a simple web server that handles client requests. The breakdown of functionality was as follows:
* accept and parse the HTTP request, 
* get the requested file from the server's file system, 
* create an HTTP response message consisting of the requested file preceded by header lines, and then 
* send the response directly to the client.
* If the requested file is not present in the server, the server should send an HTTP "404 Not Found" message back to the client.

Initially, there was a skeleton of the code with several places marked with 'pass' that required implementation and testing of our own developed code. We were to further multi-thread the server, as well as code a simple HTTP client to test the server and query from websites.

Within this repository are my two (2) files that demonstrate my work for this simple server. Due to the nature of this assignment, I have not included the supplementary files.
