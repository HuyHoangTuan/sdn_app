from mininet.cli import CLI
from src.mininet_core import mininet_core, topo_core
from mininet.node import RemoteController

if __name__ == '__main__':
    net = mininet_core.create_mininet(topo_core.Topology())
    net.start()
    CLI(net)
    net.stop()
    
