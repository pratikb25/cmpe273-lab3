from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

port = 15432

class HandleUDPServer(DatagramProtocol):

    def startProtocol(self):
        """
        Called after protocol has started listening.
        """
        print("Set the TTL>1 so multicast will cross router hops...")
        self.transport.setTTL(5)
        print("Join a specific multicast group...")
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (repr(datagram), repr(address)))
        if datagram == b"Hello World" or datagram == "Hello World":
            print("Sending the unicast reply to the originating port...")
            self.transport.write(datagram, address)


def main():
    reactor.listenMulticast(port, HandleUDPServer(), listenMultiple=True)
    reactor.run()

if __name__ == '__main__':
    main()
