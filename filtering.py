import SimpleHTTPServer, SocketServer
import ServerConfig
sets = ServerConfig.Sets()
PORT = sets.LPORT + 1

def log_message(format, *args):
    pass

def filtering():
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    Handler.log_message = log_message
    httpd = SocketServer.TCPServer((sets.LHOST, PORT), Handler)
    print "Listening on %s:%s" %(sets.LHOST, PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        
if __name__ == "__main__":
    filtering()
