from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel

class Topology(Topo):
    def build(self):
        self._switches = []
        numSwitch = 10
        for i in range(0, numSwitch):
            switch = self.addSwitch('sw{}'.format(i+1))
            self._switches.append(switch)
            
        self._input = [
            [1, 2],
            [1, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [2, 7],
            [1, 8],
            [7, 9],
            [3, 10],
            [2, 4],
            [10, 1],
            [8, 3],
            [9, 3]
        ]
        
        for _input in self._input:
            first_switch = self._switches[_input[0]-1]
            second_switch = self._switches[_input[1]-1]
            self.addLink(first_switch, second_switch)


# topos = { 'tp': ( lambda: Topology() ) }