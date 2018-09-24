from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

port = 15432

# Class to handle UDP Client
class HandleUDPClient(DatagramProtocol):

    def startProtocol(self):
        print("Join the multicast address, so we can receive replies...")
        self.transport.joinGroup("228.0.0.5")
        print("Send to 228.0.0.5:%d - all listeners on the multicast address (including us) will receive this message..." % port)
        self.transport.write(b'Hello World', ("228.0.0.5", port))

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (repr(datagram), repr(address)))

def main():
    reactor.listenMulticast(port, HandleUDPClient(), listenMultiple=True)
    reactor.run()

if __name__ == '__main__':
    main()
