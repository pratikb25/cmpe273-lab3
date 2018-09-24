from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

port = 15432

# Class to handle UDP Datagram
class EchoClientDatagramProtocol(DatagramProtocol):
    data = "Hello World!"
    
    def startProtocol(self):
        self.transport.connect('127.0.0.1', port)
        self.sendDatagram()
    
    def sendDatagram(self):
        self.transport.write(bytes(self.data, 'utf-8'))

    def datagramReceived(self, datagram, host):
        print('Datagram received from the server: ', repr(datagram))
        reactor.stop()

    def connectionRefused(self):
        print("No one is listening :(")

def main():
    protocol = EchoClientDatagramProtocol()
    t = reactor.listenUDP(0, protocol)
    reactor.run()

if __name__ == '__main__':
    main()
