Google docs is the most popular online shared file editor nowadays. It is very helpful when 
multiple people staying over different places globally want to edit one file simultaneously at the 
same time. Moreover, it keeps all the changing records to avoid malicious overrides. However, 
such a useful function is rarely too been seen in Dropbox or a database server due to various 
reasons. This project functioning is similar to Google Docs. It supports real time editing and viewing files/folders/database by clients. It is a distributed system where multiple client can 
simultaneously edit and view. Every write done by any client will be reflected in all the locations the file is open. To maintain the fault/crash tolerance, the project implements the conept of replication of servers with specific design.
We use python in this project to create a HTTP Server using Flask web framework. Ubuntu Operating System is used, and the Terminal is used to host the HTTP server created from Python.
The HTTP web server is nothing but a process that is running on your machine and does exactly two things:
1-	Listens for incoming http requests on a specific TCP socket address (IP address and a port number)
2-	Handles this request and sends a response back to the user.
Let us understand the basic of HTTP Server with a simple example.

Imagine you pull up your Chrome browser and type www.yahoo.com in the address bar. Of course, you are going to get the Yahoo home page rendered on your browser window.
But what really just happened under the hood?
At a high level, when you type www.yahoo.com on the browser, the browser will create a network message called an HTTP request.
This Request will travel all the way to a Yahoo computer that has a web server running on it. This web server will intercept your request and handle it by responding back with the html of the Yahoo home page.
Finally, your browser renders this html on the screen and that’s what you see on your screen.
Every interaction with the Yahoo home page after that (for example, when you click on a link) initiates a new request and response exactly like the first one.
To reiterate, the machine that receives the http request has a software process called a web server running on it. This web server is responsible for intercepting these requests and handling them appropriately.
We create this Web Server using Python programming language and host this on terminal and then wait for a client(browser) to connect to it and then provide the browser with whatever the requests it asks.

