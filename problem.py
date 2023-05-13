import networkx as nx
import matplotlib.pyplot as plt

## an important thing to consider when using the class problem
# is the structure of variables and attributes.
#
# example of a node:
# "A"
# 
# example of an edge:
# ("A", "B")
# 
# two examples of nodes_list
# "ABCDEFG"
# ["A", 1, 3, "m"]
# 
# example of edges_list
# [("A", "B"), ("A", "C"), ("i am a node", "B")]
# 
# 
# example of heuristic_values_list:
# [(1,  {'h': 20}), (4,  {'h': 2}), ("A",  {'h': 3}), ("C",  {'h': 14})] (remark: the letter "h" here stands for the goal node)




class Problem:
    # in the constracture, every attribute is optional
    # to provide, except for th edges_list attribute
    def __init__(self, edges_list = None, nodes_list = None, heuristic_values_list = None, digraph = False):
        self.__digraph = digraph
        if(self.__digraph):
            self.__graph = nx.DiGraph()
        else:
            self.__graph = nx.Graph()

        if(nodes_list):
            self.nodes_list = nodes_list
        
        if(heuristic_values_list):
            self.heuristic_values_list = heuristic_values_list

        self.edges_list = edges_list

    @property
    def nodes_list(self):
        return self.__nodes_list
    

    # two examples of nodes_list
    # "ABCDEFG"
    # ["A", 1, 3, "m"]
    @nodes_list.setter
    def nodes_list(self, value):
        self.__graph.add_nodes_from(value)

    
    @property
    def edges_list(self):
        return self.__graph.edges
    
    # example of edges_list
    # [("A", "B"), ("A", "C"), ("i am a node", "B")]
    @edges_list.setter
    def edges_list(self, value):
        self.__graph.add_edges_from(value)
    
    @property
    def heuristic_values_list(self):
        h = []
        for n in self.__graph.nodes(data = True):
            h.append(n)

        return h
    
    # example of heuristic_values_list:
    # [(1,  {'h': 20}), (4,  {'h': 2}), ("A",  {'h': 3}), ("C",  {'h': 14})]
    @heuristic_values_list.setter
    def heuristic_values_list(self, heuristic_values_list):
        for node, heuristic_value in heuristic_values_list:
            self.modify_heuristic_value(node, heuristic_value)

    # digraph here is a boolean
    @property
    def digraph(self):
        return self.__digraph
    
    # example of a node:
    # "A"
    def add_a_node(self, node_name):
        self.__graph.add_node(node_name)

    # two example of an edge_couple:
    # ("A", 1)
    # "CG"
    def add_an_edge(self, edge_couple):
        self.__graph.add_edge(edge_couple)

    #this function sets or modify the weight value of the edge provided 
    # in edge_couple to new_weight
    #however if this edge_couple doesn't exist, it will be created
    #also, if one or both nodes in the edge_couple doesn't exist, it will be created
    def modify_edge_weight(self, edge_couple, new_weight):
        self.__graph.add_edge(edge_couple[0], edge_couple[1], weight = new_weight)

    #weight is an integer number
    def add_an_edge(self, edge_couple, weight=None):
        if weight is not None:
            self.__graph.add_edge(edge_couple[0], edge_couple[1], weight=weight)
        else:
            self.__graph.add_edge(edge_couple[0], edge_couple[1])

    #this function sets or modify the heuristic value of the node provided 
    # in node_name to new_heuristic_value
    #however if this node doesn't exist, it will be created
    def modify_heuristic_value(self, node_name, goal_node, new_heuristic_value):
        if node_name not in self.__graph.nodes:
            self.__graph.add_node(node_name)
        self.__graph.nodes[node_name][goal_node] = new_heuristic_value

    @property
    def graph(self):
        return self.__graph
    





