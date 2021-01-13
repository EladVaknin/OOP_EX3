#  Weighted Directed Graph :
Welcome to the fourth assignment in the OOP course and the first exercise in Python! 
In this task we built a weighted and directed graph and implemented a number of algorithms.

**DiGraph** - A class that implements the GraphInterface interface to build a graph.

**GraphAlgo** - A class that implements the GraphAlgoInterface interface to execute algorithms on the graph.

# Classes and Methods
**NodeData** -   A regular init function.


### DiGraph
In this class i implements the interfaces - GraphInterface

| Name |  Description|
|--|--|
| __init__(self)|  A regular init function.|
| v_size(self)| Returns the number of nodes in the graph|
|e_size(self)  |Returns the number of edges in the graph |
| get_mc(self) |  Returns the number of actions performed on the graph|
| get_all_v(self) |  Returns a Dictionary representing all the nodes in the graph |
|all_in_edges_of_node(self, id1: int) | Returns a Dictionary representing all the edges that go in to the node |
|all_out_edges_of_node(self, id1: int) | Returns a Dictionary representing all the edges that go out from the node|
| add_edge(self, id1: int, id2: int, weight: float)| Check if we sucsess to  add a edge |
| add_node(self, node_id: int, pos: tuple = None)| Check if we sucsess to  add a node |
|remove_node(self, node_id: int)| Check if we sucsess to remove a node  |
| remove_edge(self, node_id1: int, node_id2: int)| Check if we sucsess to remove a edge |


### GraphAlgo

- In this class i implements the interfaces - GraphAlgo.
- In this class we implement the Dijkstra and Tarjan algorithms.

| Name |  Description|
|--|--|
|__init__(self,g:DiGraph=DiGraph()) |  A regular init function.|
|get_graph(self) | Returns a pointer to the initialized graph
| copy()| Copy constructor - deep copy |
| shortest_path(self, id1: int, id2: int)| Returns the sort distance between src to dest whit Dijkstra's algorithm and returns the way whit a list |
| save_to_json(self, file_name: str)  | Saves a graph to a file whit Json|
| load_from_json(self, file_name: str) | Load a graph from a file whit Jason |
| connected_component(self, id1: int) | Returns a list of strong binding component  |
| connected_components(self) |Returns a list of binding component  |
| plot_graph(self) | This function builds the graphic design. |
| Dijkstra (self, id1: int, id2: int) | This function implements the Dijkstra algorithm. |


***Example graph*** : 
![WhatsApp Image 2021-01-12 at 17 13 44](https://user-images.githubusercontent.com/74238558/104333463-ec1f5b80-54f9-11eb-9ea9-91d3e3b1c730.jpeg)



* In this project we compared our work at Java (assigment two in this course) and the standard library in python- networkx.
*  To the results table visit in our **Wiki** page.

## Sources and links

https://en.wikipedia.org/wiki/Connectivity_(graph_theory)

https://www.w3schools.com/python/

https://math-wiki.com/images/a/ae/Algo_tirgul8-9.pdf

https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

https://www.youtube.com/watch?v=1d2bqlI5PR4

https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

https://iq.opengenus.org/tarjans-algorithm/

https://www.youtube.com/watch?v=wUgWX0nc4NY
