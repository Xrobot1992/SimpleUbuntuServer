If you intend to use this program as only a server-adblock, then all strings must be blank but if you have a working tweak or maybe another hide-my-butt ip's then go ahead and fill.

To use adblock feature, You must have the adblockparser module and a 'host3.txt' file, for host-like blocking pattern.
see https://pypi.python.org/pypi/adblockparser/0.5 for more

To use in Windows, ensure there is a working python2.7.x installation.

Configuration Details:
LHOST => Localhost Address to listen default is 127.0.0.1
LPORT => Proxy Port to listen, default is 8080
PHOST => Proxy Host address/ip
PPORT => Proxy port 

FQUERY => Front Query url
MQUERY => Middle Query Url
BQUERY => Back query url
RQUERY => Reverse Query url

IQUERY => Url/Host to inject
IMETHOD => Injection Methods 1 --> get, 2 --> post, see SimpleServer.py source for more.
ILINE => Injection Line
ISPLIT => Injection Splitline
RPORT => Remove Port from urls: 1 --> enable, 0 --> disable
RPATH => Remove paths: 1 --> enable, 0 --> disable
ADMODE => Advanced mode, 1 --> enable, 0 --> disable, Default:1
LOGS => Logging to console/terminal 1 --> enable, 0 --> disable, 2 --> log to file, use for debugging.
ADBLOCKER => Host-like blocking of url requests received, 1 --> enable, 0 --> disable.

CUSHDRx => Custom Headers, use if you know what is.
VALHDRx => Header Values, use if you know what is.
KEEP => Keep Server
RHTTP => HTTP Request Version. 0 --> default, 1 --> HTTP/1.0, 2 --> HTTP/1.1
PTYPE => Tunnel Proxy or not, 1 --> enable, 0 --> disable
SBUFF => Server Buffer size, use 2^(10+x)
RHTTPS => Use HTTPS Connections
TIMEOUT => Server Timeout in secs.
