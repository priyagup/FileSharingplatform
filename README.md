# FileSharingPlatform

Author: Priya Gupta

**Client-Side/ Server-Side Programing: JavaScript - HTML - Flask - Python - WSGI - MongoDB**

Inspired by Google and Dropbox  - Grade Project
>Initial Design Phase - Version 1.0.1

>Description:
1. Supports real time editing and viewing files/folders/database by clients. 
2. It is a distributed system where multiple client can simultaneously edit and view. 
3. Every write done by any client will be reflected in all the locations the file is open.

Static Folder: Code of Javascript and CSS on bootstrap Framework
Templates: HTML pages to give UI to client
- Login.html
  - This is the entry page where you have to login and while login call going to the mongodb to check whether the user is register or not. another feature is you have to login first after login only you are able to access upload, welcome and show URL.  
- show.html
  - Display the three sections 
    - Text written in the file
    - Table which showes editing history like IP address of editor, Username of editor and Date-Time of editing.   
- upload.html
  - This page gives you box to upload a file, at present it is supporting .text format.
- welcome.html
  - Display the file which you can see and edit with personalized greeting.
