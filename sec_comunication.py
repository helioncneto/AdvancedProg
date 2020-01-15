import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile="server.pem")

bindsocket = socket.socket()
bindsocket.bind(('0.0.0.0', 4443))
bindsocket.listen(5)

def deal_with_client(connstream):
    data = connstream.read()
    # null data means the client is finished with us
    print (data.decode())
    #connstream.write("HTTP/1.0\r\n\r\nCHAMA".encode())
    # finished with client

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()

