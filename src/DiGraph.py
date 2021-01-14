from GraphInterface import GraphInterface
from NodeData import NodeData
from typing import Dict

class DiGraph(GraphInterface):

    def __init__(self):
        self.__nodes:Dict[int,NodeData]=dict()
        self.__edges_out: Dict[int, Dict[int, float]] = dict()
        self.__edges_in:Dict[int,Dict[int,float]]=dict()
        self.__counterMC = 0
        self.__Edge_size=0

    def v_size(self) -> int:
        return len(self.__nodes)

    def e_size(self) -> int:

        return self.__Edge_size

    def get_mc(self) -> int:
        return self.__counterMC

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__edges_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__edges_out.get(id1)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 is not id2 and id1 in self.__nodes and id2 in self.__nodes and id2 not in self.__edges_out.get(id1):
            #add edge
            self.__edges_out.get(id1).update({id2:weight})
            self.__edges_in.get(id2).update({id1:weight})
            self.__counterMC+=1
            self.__Edge_size+=1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        node= NodeData(node_id,pos)
        if node_id not in self.__nodes:
            self.__nodes.update({node_id: node})
            self.__edges_out.update({node_id:dict()})
            self.__edges_in.update({node_id:dict()})
            self.__counterMC+=1
            return True
        else:
            return False


    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__nodes:
            for x in self.all_out_edges_of_node(node_id).keys():
                self.__edges_in.get(x).pop(node_id)
                # self.__counterMC += 1
                self.__Edge_size -=1

            for x in self.all_in_edges_of_node(node_id):
                self.__edges_out.get(x).pop(node_id)
                # self.__counterMC += 1
                self.__Edge_size -=1

            self.__edges_out.pop(node_id)
            self.__edges_in.pop(node_id)
            self.__nodes.pop(node_id)
            self.__counterMC+=1
            return True
        else:return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 is not node_id2 and node_id1 in self.__nodes and node_id2 in self.__nodes and node_id2 in self.__edges_out.get(node_id1):
            # remove edge
            self.__edges_out.get(node_id1).pop(node_id2)
            self.__edges_in.get(node_id2).pop(node_id1)
            self.__counterMC += 1
            self.__Edge_size -= 1
            return True
        else:
            return False


    def __repr__(self):
        return "Graph %s"%(self.__nodes)