from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch

def create_mininet(topo):
    return Mininet(topo= topo, controller= RemoteController, switch=OVSSwitch)

