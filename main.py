from mininet.cli import CLI
from src.mininet_core import mininet_core, topo_core
from mininet.node import RemoteController

# if __name__ == '__main__':
    # net = mininet_core.create_mininet(topo_core.Topology())
    # net.addController("c0", controller= RemoteController, ip= "127.0.0.1", port= 6653)
    # print(net.controllers)
    # net.start()
    # print(net.controllers)
    # CLI(net)
    # net.stop()

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # add host
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # add connection
        self.addLink(s1, s2)
        self.addLink(s3, s2)
        self.addLink(s3, s1)

        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)


    # sudo mn --controller=remote,ip=127.0.0.1,port=6653 --custom code2.py --topo tp

topos = { 'tp': ( lambda: MyTopo() ) }