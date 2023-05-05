import networkx as nx
import matplotlib.pyplot as plt
import random
import math

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
# [(1,  {'h': 20}), (4,  {'h': 2}), ("A",  {'h': 3}), ("C",  {'h': 14})] (remark: the letter "h" here stands for heuristic value)




class Problem:
    # in the constracture, every attribute is optional
    # to provide, except for th edges_list attribute
    def __init__(self, edges_list, nodes_list = None, heuristic_values_list = None, digraph = False):
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
    def modify_heuristic_value(self, node_name, new_heuristic_value):
        if node_name not in self.__graph.nodes:
            self.__graph.add_node(node_name)
        self.__graph.nodes[node_name]['h'] = new_heuristic_value

    @property
    def graph(self):
        return self.__graph
    
    # depth-limited-search
    def depth_limited_search(self, start_node, goal_node, depth_limit):
    
        # Search the deepest nodes in the search tree first using depth-limited search.
        # Returns the path to the goal node if it is found within the depth limit, otherwise returns None.
    
        def recursive_dls(node, depth):
            if depth == 0 and node == goal_node:
                return [node]
            elif depth > 0:
                for child in problem.graph.neighbors(node):
                    result = recursive_dls(child, depth-1)
                    if result is not None:
                        return [node] + result
            return None

        for depth in range(depth_limit):
            result = recursive_dls(start_node, depth)
            if result is not None:
                return result
        return None
    
    #Iterative deepening depth-first-search:
    def iterative_deepening_depth_first_search(self, start_node, goal_node, max_depth):
        for depth in range(1, max_depth + 1):
            result = depth_limited_search(problem, start_node, goal_node, depth)
            if result is not None:
                return result
        return None
    # Bidirectional search

    def bidirectional_search(self, start, goal):
        # Initialize the forward and backward search graphs
        forward_graph = problem.graph.subgraph([start])
        backward_graph = problem.graph.subgraph([goal])

    # Initialize the sets of explored nodes for each direction
        forward_explored = set([start])
        backward_explored = set([goal])

    # Initialize the queue of nodes to explore for each direction
        forward_queue = [start]
        backward_queue = [goal]

    # Loop until the two search frontiers meet
        while forward_queue and backward_queue:
        # Check if there is an intersection of the forward and backward explored sets
            intersection = forward_explored.intersection(backward_explored)
            if intersection:
            # We have found a path from start to goal
                path = []
                node = intersection.pop()
                # Follow the path from start to the intersection node
                while node != start:
                    path.append(node)
                    node = next(n for n in forward_graph.predecessors(node))
                path.append(start)
                path.reverse()
            # Follow the path from the intersection node to the goal
                node = next(n for n in backward_graph.predecessors(node))
                while node != goal:
                    path.append(node)
                    node = next(n for n in backward_graph.predecessors(node))
                path.append(goal)
                return path

        # Explore one step in each direction
            forward_node = forward_queue.pop(0)
            for neighbor in problem.graph.neighbors(forward_node):
                if neighbor not in forward_explored:
                    forward_graph.add_edge(forward_node, neighbor)
                    forward_explored.add(neighbor)
                    forward_queue.append(neighbor)

            backward_node = backward_queue.pop(0)
            for neighbor in problem.graph.neighbors(backward_node):
                if neighbor not in backward_explored:
                    backward_graph.add_edge(backward_node, neighbor)
                    backward_explored.add(neighbor)
                    backward_queue.append(neighbor)

    # No path was found
        return None

    def hill_climbing(self, start_node, goal_node):
        # Define a nested function to get the best successor node
        def get_best_successor():
            # Get all the neighbors (successors) of the current node
            successors = self.graph.neighbors(current_node)
            # Initialize variables to keep track of the best successor and its score
            best_successor = None
            best_score = float("inf")
            # Loop over all the successors to find the one with the best score
            for successor in successors:
                # Compute the score of the current successor
                score = self.graph.get_edge_weight(current_node, successor) + self.heuristic(successor, goal_node)
                # Update the best successor and its score if the current successor has a better score
                if score < best_score:
                    best_successor = successor
                    best_score = score
            # Return the best successor
            return best_successor

        # Initialize the current node to the start node
        current_node = start_node
        # Loop until we reach the goal node or can't find a better successor
        while current_node != goal_node:
            # Get the best successor of the current node
            successor = get_best_successor()
            # If there's no better successor, return the current node (we're stuck)
            if successor is None or self.heuristic(successor, goal_node) >= self.heuristic(current_node, goal_node):
                return current_node
            # Otherwise, set the current node to the best successor and continue the loop
            current_node = successor
        # If we reach this point, we've found the goal node
        return current_node

    def simulated_annealing(self, start_node, max_iterations=1000, temperature=1.0, cooling_rate=0.003):
            # Initialize the current state as the start node
            current_node = start_node
            current_value = self.get_heuristic_value(current_node)
            
            # Initialize the best state as the current node
            best_node = current_node
            best_value = current_value
            
            # Initialize the iteration count
            iteration = 1
            
            # Loop until max_iterations is reached
            while iteration <= max_iterations:
                # Calculate the current temperature based on cooling rate and iteration count
                current_temperature = temperature / (1 + cooling_rate * iteration)
                
                # Get a random neighbor of the current node
                neighbor_nodes = list(self.graph.neighbors(current_node))
                if not neighbor_nodes:
                    break
                random_neighbor = random.choice(neighbor_nodes)
                neighbor_value = self.get_heuristic_value(random_neighbor)
                
                # Calculate the energy difference between the current and neighbor states
                energy_diff = current_value - neighbor_value
                
                # If the neighbor is better, move to that state
                if energy_diff > 0:
                    current_node = random_neighbor
                    current_value = neighbor_value
                    # If the neighbor is also better than the best state, update the best state
                    if current_value < best_value:
                        best_node = current_node
                        best_value = current_value
                # If the neighbor is worse, randomly move to that state with a probability dependent on temperature
                else:
                    probability = math.exp(energy_diff / current_temperature)
                    if random.random() < probability:
                        current_node = random_neighbor
                
                # Increment the iteration count
                iteration += 1
            
            # Return the best state found
            return best_node
        
    def get_heuristic_value(self, node):
            try:
                return self.graph.nodes[node]['h']
            except KeyError:
                return float('inf')
            
