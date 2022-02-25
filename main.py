import sipfullproxy
import socketserver
import socket
import sys

def vypisy():
    hostname = socket.gethostname()
    print(hostname)
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1": ipaddress = sys.argv[1]
    print(ipaddress)
    return ipaddress

def spustenie(ipaddress):
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

def main():    
    spustenie(vypisy())

main()