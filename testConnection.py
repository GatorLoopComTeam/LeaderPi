from twisted.internet import reactor, protocol

PORT = 9000

class MyServer(protocol.Protocol):
    def connectionMade(self):
        print "connected from ", self.transport.client 
        self.transport.write("hi client")
    def dataReceived(self, data):
        print data

class MyServerFactory(protocol.Factory):
    protocol = MyServer

factory = MyServerFactory()
reactor.listenTCP(PORT, factory)
reactor.run()
