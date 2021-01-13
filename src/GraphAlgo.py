from typing import List
import json
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph, NodeData
from src import GraphInterface
import matplotlib.pyplot as plot_avi
import random
import math
from queue import PriorityQueue
from typing import Dict

class GraphAlgo(GraphAlgoInterface):

    def __init__(self,g:DiGraph=DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name,'r') as f:
                json_file = json.load(f)

            self.graph = DiGraph()
            #{"id": 0}
            #{"pos": "35.20319591121872,32.10318254621849,0.0","id": 1}
            for x in json_file.get('Nodes'):
               if x.get('pos') is None:
                   self.graph.add_node(x.get('id'))
               else:
                   li=x.get('pos').split(",")
                   pos = tuple(map(float,li))
                   self.graph.add_node(x.get('id') , pos)


            # {"src":0,"w":1.4620268165085584,"dest":10}
            for x in json_file.get('Edges'):
                self.graph.add_edge(x.get('src'),x.get('dest'),x.get('w'))

            return True
        except FileNotFoundError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        # {"id": 0}
        # {"pos": "35.20319591121872,32.10318254621849,0.0","id": 1}
        for x in self.graph.get_all_v().values():
            node:NodeData= x
            if node.pos is None:
                nodes.append({"id": node.getKey()})
            else:
                str_pos = str(node.pos[0])+","+str(node.pos[1])+","+str(node.pos[2])
                nodes.append({"pos": str_pos,"id": node.getKey()})

        edges=[]
        for s in self.graph.get_all_v().keys():
            for d,value in self.graph.all_out_edges_of_node(s).items():
                edges.append({"src":s,"w":value,"dest":d})


        lists= {'Edges':edges,'Nodes':nodes}
        try:
            with open(file_name, 'w') as f:
                json.dump(lists,f)
            return True
        except FileNotFoundError:
            return False


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return math.inf,[]               # in case that we dont have the nodes in the list
        if id1 is id2 :                      # in case that id1 = id2
            return 0,[id1]

        return self.Dijkstra(id1, id2)

    def connected_component(self, id1: int) -> list:
        # in this two function we will use in DFS algorithm and we will sava the results from the end to the beginning,
        # we will make transpose to the graph and we make DFS again and all the sons that we got in the
        # algorithm (whit the recursion ) will be scc.
        # Complications -  O( v + |E|)

        scc=[]
        on_Scc:Dict[int,bool]=dict()
        low: Dict[int, int] = dict()
        ids: Dict[int, int] = dict()
        id = 0

        for node in self.graph.get_all_v().keys():
            low.update({node:0})
            ids.update({node: 0})
            on_Scc.update({node: False})

        recursion =[(id1,0)]
        while recursion:
            v,i=recursion[-1]
            del recursion[-1]
            if i==0:
                id+=1
                low.update({v:id})
                ids.update({v: id})
                scc.append(v)
                on_Scc.update({v:True})
            flag=False
            k=0
            for w in self.graph.all_out_edges_of_node(v).keys():
                if ids.get(w) == 0:
                    recursion.append((v,k+1))
                    recursion.append((w, 0))
                    flag=True
                    k+=1
                    break
                elif on_Scc.get(w):
                    k+=1
                    low.update({v:min(low.get(v),low.get(w))})
            if flag: continue
            if ids.get(v) == low.get(v):
                way=[]
                while scc:
                    node = scc.pop()
                    low.update({node:ids.get(v)})
                    on_Scc.update({node:False})
                    way.insert(0,node)
                    if node == v : break
            if recursion:
                w=v
                v,_=recursion[-1]
                low.update({v:min(low.get(v),low.get(w))})
        return way


    def connected_components(self) -> List[list]:
        scc = []
        on_Scc: Dict[int, bool] = dict()
        low: Dict[int, int] = dict()
        ids: Dict[int, int] = dict()
        id = 0

        way =[]
        for node in self.graph.get_all_v().keys():
            low.update({node: 0})
            ids.update({node: 0})
            on_Scc.update({node: False})
        for x in self.graph.get_all_v():
            if ids.get(x) == 0:
                id1=x
                recursion = [(id1, 0)]
                while recursion:
                    v, i = recursion[-1]
                    del recursion[-1]
                    if i == 0:
                        id += 1
                        low.update({v: id})
                        ids.update({v: id})
                        scc.append(v)
                        on_Scc.update({v: True})
                    flag = False
                    k = 0
                    for w in self.graph.all_out_edges_of_node(v).keys():
                        if ids.get(w) == 0:
                            recursion.append((v, k + 1))
                            recursion.append((w, 0))
                            flag = True
                            k += 1
                            break
                        elif on_Scc.get(w):
                            k += 1
                            low.update({v: min(low.get(v), low.get(w))})
                    if flag: continue
                    if ids.get(v) == low.get(v):
                        path = []
                        while scc:
                            node = scc.pop()
                            low.update({node: ids.get(v)})
                            on_Scc.update({node: False})
                            path.insert(0, node)
                            if node == v: break
                        way.insert(0,path)
                    if recursion:
                        w = v
                        v, _ = recursion[-1]
                        low.update({v: min(low.get(v), low.get(w))})

        return way

    def plot_graph(self) -> None:

        x_=[]
        y_=[]
        n_=[]
        for key,value in self.graph.get_all_v().items():
            node:NodeData = value
            if node.pos is None:
                node.pos= (random.uniform(35.18, 35.2),random.uniform(2.1, 32.2))
            x_.append(node.pos[0])
            y_.append(node.pos[1])
            n_.append(key)

        fig, ax = plot_avi.subplots()
        for p, txt in enumerate(n_):
            ax.annotate(n_[p], (x_[p], y_[p]))

        plot_avi.plot(x_,y_,"*",color = "black")

        for s in self.graph.get_all_v().keys():
            for d,value in self.graph.all_out_edges_of_node(s).items():
                node_s:NodeData=self.graph.get_all_v().get(s)
                node_d:NodeData = self.graph.get_all_v().get(d)

                plot_avi.arrow(node_s.pos[0], node_s.pos[1], (node_d.pos[0] - node_s.pos[0]),
                          (node_d.pos[1] - node_s.pos[1]), length_includes_head=True, width=0.0000003,
                          head_width=0.0002, color='blue')

        plot_avi.show()




    def Dijkstra (self, id1: int, id2: int) -> (float, list):
        # init all nodes
        for node in self.graph.get_all_v().values():
            node.tag=-1       # dont visit
            node.weight=math.inf     # default whight

        queue = PriorityQueue()
        src:NodeData = self.graph.get_all_v().get(id1)
        src.weight=0    # init the weight
        queue.put(src)

        while not queue.empty():
            node1:NodeData = queue.get()    # the first node in the queue
            #Dict[int,float]
            for key,weight_of_node in self.graph.all_out_edges_of_node(node1.getKey()).items():    # all the neighborhoods of node1
                node2:NodeData = self.graph.get_all_v().get(key)
                dest = node1.weight+weight_of_node
                if dest <node2.weight:
                    node2.weight=dest

                    node2.tag=node1.getKey()
                    queue.put(node2)

        dest: NodeData = self.graph.get_all_v().get(id2)
        if dest.weight is math.inf:     # for the case that id2 is not exist
            return math.inf,[]
        way=[]
        way.insert(0,dest.getKey())

        current = dest.tag
        while current != -1:
            way.insert(0, current)
            current = self.graph.get_all_v().get(current).tag

        return dest.weight,way




