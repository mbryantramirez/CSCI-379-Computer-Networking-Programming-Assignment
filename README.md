# CSCI-379-Computer-Networking-Programming-Assignment

In this assignment, you will develop a simple Web server in Python that is capable
of processing only one request. Specifically, your Web server will
(i) Create a connection socket when contacted by a client (browser)
(ii) Receive the HTTP request from this connection
(iii) Parse the request to determine the specific file being requested
(iv) Get the requested file from the server’s file system
(v) Create an HTTP response message consisting of the requested file
preceded by header lines
(vi) Send the response over the TCP connection to the requesting browser.
If a browser requests a file that is not present in your server, your server should
return a “404 Not Found” error message.
Your job is to code the steps above, run your server, and then test your server by
sending requests from browsers running on different hosts. If you run your server
on a host that already has a Web server running on it, then you should use a different
port than port 80 for your Web server.
