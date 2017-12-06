from pybrain.structure import FeedForwardNetwork
n = FeedForwardNetwork()

from pybrain.structure import LinearLayer,SigmoidLayer
inLayer = LinearLayer(2, name="Foo The II of LinearLayer")
hiddenLayer = SigmoidLayer(3, name="Bob the Pesant")
outLayer = LinearLayer(1, name="Foo The II Royal Decree")
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

from pybrain.structure import FullConnection
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.sortModules()

print n
