from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

port = 15432

# Class to handle UDP
class HandleUDPDatagram(DatagramProtocol):
	def datagramReceived(self, datagram, address):
		print("Received %s from client %s!!" % (repr(datagram), repr(address)))
		self.transport.write(datagram, address)

def main():
	reactor.listenUDP(port, HandleUDPDatagram())
	reactor.run()

if __name__ == '__main__':
	main()
