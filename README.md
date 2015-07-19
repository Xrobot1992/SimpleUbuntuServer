# SimpleUbuntuServer
SimpleUbuntuServer: a simple python application to tweak HTTP connections
This roughly has the same code as its Windows and Android counterparts. 
To run this you must first make the SimpleServer.py executable

	$chmod +x SimpleServer.py

then 

	$./SimpleServer.py
Edit the configuration file in the same folder to whatever server you
intend to use.

change your network proxy to 127.0.0.1:8080 as you do windows and Android.
To make it work with apt, you must create a file with your favourite 
editor in /etc/apt/. Assuming you're using 'leafpad' then

	$sudo leafpad /etc/apt/apt.conf 
then copy the follwing to it, save and quit.

Acquire::http::proxy "http://localhost:8080/";
Acquire::https::proxy "https://localhost:8080/";
Acquire::ftp::proxy "ftp://localhost:8080/";
Acquire::socks::proxy "socks://localhost:8080/";

** You must remove this file when not using a proxy server otherwise 
apt cannot reach the internet.
It is best to keep it anywhere in your home directory and copy it to /etc/apt/
each time you use SimpleServer.

Happy tweaking :-0
