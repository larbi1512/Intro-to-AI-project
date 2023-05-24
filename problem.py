import networkx as nx
import matplotlib.pyplot as plt
import random
import math
from queue import PriorityQueue
from collections import deque


# an important thing to consider when using the class problem
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
    def __init__(self, edges_list, initial_state=None, goal_states=[], nodes_list=None, heuristic_values_list=None, digraph=False):
        self.__digraph = digraph
        if (self.__digraph):
            self.__graph = nx.DiGraph()
        else:
            self.__graph = nx.Graph()

        if (nodes_list):
            self.nodes_list = nodes_list

        if (heuristic_values_list):
            self.heuristic_values_list = heuristic_values_list

        self.edges_list = edges_list

        if initial_state:
            self.initial_state = initial_state

        self.goal_states = goal_states

    # example of an initial_state:
    # "A"
    @property
    def initial_state(self):
        return self.__initial_state

    @initial_state.setter
    def initial_state(self, value):
        self.__initial_state = value
        self.add_a_node(self.__initial_state)

    @property
    def goal_states(self):
        return self.__goal_states

    @goal_states.setter
    def goal_states(self, value):
        self.__goal_states = value
        for goal_node in self.__goal_states:
            self.add_a_node(goal_node)

    def add_goal_state(self, state):
        self.__goal_states.append(state)
        self.add_a_node(state)

    @property
    def nodes_list(self):
        return self.__nodes_list

    # two examples of nodes_list
    # "ABCDEFG"
    # ["A", 1, 3, "m"]

    @nodes_list.setter
    def nodes_list(self, value):
        self.__nodes_list = value
        self.__graph.add_nodes_from(self.__nodes_list)

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
        for n in self.__graph.nodes(data=True):
            h.append((n[0], n[1]['h']))

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

    # this function sets or modify the weight value of the edge provided
    # in edge_couple to new_weight
    # however if this edge_couple doesn't exist, it will be created
    # also, if one or both nodes in the edge_couple doesn't exist, it will be created
    def modify_edge_weight(self, edge_couple, new_weight):
        self.__graph.add_edge(edge_couple[0], edge_couple[1], weight = new_weight)
        
        
    # get the weight of the edge
    def get_edge_weight(self, edge_couple):
        edge_data = self.__graph.get_edge_data(edge_couple[0], edge_couple[1])
        if edge_data is not None and 'weight' in edge_data:
            return int(edge_data['weight'])
        else:
            return 0
    
    #weight is an integer number
    def add_an_edge(self, edge_couple, weight=None):
        if weight is not None:
            self.__graph.add_edge(
                edge_couple[0], edge_couple[1], weight=weight)
        else:
            self.__graph.add_edge(edge_couple[0], edge_couple[1])

    # this function sets or modify the heuristic value of the node provided
    # in node_name to new_heuristic_value
    # however if this node doesn't exist, it will be created
    def modify_heuristic_value(self, node_name, new_heuristic_value):
        if node_name not in self.__graph.nodes:
            self.__graph.add_node(node_name)
        self.__graph.nodes[node_name]['h'] = new_heuristic_value
  
      
# heuristic getter 
    def get_heuristic(self, node):
        try:
            return self.__graph.nodes[node]['h']
        except KeyError:
            return 0
        


    @property
    def graph(self):
        return self.__graph
    
    def hill_climbing(self, start_node, goal_node):
        # Initialize the current node to the start node
        current_node = start_node
        # Loop until we reach the goal node or can't find a better successor
        while current_node != goal_node:
            # Initialize variables to keep track of the best successor and its score
            best_successor = None
            best_score = float("inf")
            # Loop over all the neighbors (successors) of the current node
            for successor in self.graph.neighbors(current_node):
                # Compute the score of the current successor
                score = self.get_edge_weight((current_node, successor)) + self.heuristic(successor, goal_node)
                # Update the best successor and its score if the current successor has a better score
                if score < best_score:
                    best_successor = successor
                    best_score = score
            # If there's no better successor, return the current node (we're stuck)
            if best_successor is None or self.heuristic(best_successor, goal_node) >= self.heuristic(current_node, goal_node):
                return current_node
            # Otherwise, setcurrent node to the best successor and continue the loop
            current_node = best_successor
        # If we reach this point, we've found the goal node
        return current_node
    
    # uniform-cost search
    def uniform_cost_search(self, start_node, goal_node):
        # Search the node that has the lowest cumulative cost first.
        # Returns the path to the goal node if it is found, otherwise returns None.
        queue = PriorityQueue()
        queue.put((0, start_node, [start_node]))
        explored = set()
        while not queue.empty():
            cost, node, path = queue.get()
            if node == goal_node:
                return path
            if node not in explored:
                explored.add(node)
                for child_node in self.__graph.neighbors(node):
                    if child_node not in path:
                        child_cost = cost + self.get_edge_weight((node, child_node))
                        if child_cost is None:
                            child_cost = 0
                        queue.put((child_cost, child_node, path + [child_node]))
        return None
    
    
    def breadth_first_search(self, start_node, goal_node):
        # Search the shallowest nodes in the search tree first using BFS.
        # Returns the path to the goal node if it is found, otherwise returns None.
        visited = set()
        queue = deque([(start_node, [start_node])])
        while queue:
            node, path = queue.popleft()
            if node == goal_node:
                return path
            visited.add(node)
            for child in self.graph.neighbors(node):
                if child not in visited and child not in path:
                    queue.append((child, path + [child]))
        return None
    
    

    # A* search
    def a_star_search(self, start_node, goal_node):
        # Search the node that has the lowest combined cost and heuristic first.
        # Returns the path to the goal node if it is found, otherwise returns None.
        queue = PriorityQueue()
        queue.put((0, start_node, [start_node]))
        visited = {start_node: 0}
        while queue:
            cost, node, path = queue.get()
            print(node, " : " , cost)
            if node == goal_node:
                return path
            for child in self.graph.neighbors(node):
                child_cost = self.get_edge_weight((node, child)) + self.get_heuristic(child)
                if child not in visited or child_cost < visited[child]:
                    visited[child] = child_cost
                    print("Child node is:", child, "with cost:",child_cost)
                    queue.put((child_cost, child, path + [child]))
        return None
    
    #greedy best first search
    def greedy_best_first_search(self, start_node, goal_node):
        # Search the node that has the lowest heuristic first.
        # Returns the path to the goal node if it is found, otherwise returns None.
        queue = PriorityQueue()
        queue.put((0, start_node, [start_node]))
        while queue:
            cost, node, path = queue.get()
            if node == goal_node:
                return path
            for child in self.graph.neighbors(node):
                if child not in path:
                    child_cost = self.get_heuristic(child)
                    queue.put((child_cost, child, path + [child]))
        return None
     
    # depth-first search    
    def depth_first_search(self, start_node, goal_node):
        # Search the deepest nodes in the search tree first using DFS.
        # Returns the path to the goal node if it is found, otherwise returns None.
        stack = [(start_node, [start_node])]
        while stack:
            node, path = stack.pop()
            if node == goal_node:
                return path
            for child in self.graph.neighbors(node):
                if child not in path:
                    stack.append((child, path + [child]))
        return None

      
    # depth-limited-search
    def depth_limited_search(self, start_node, goal_node, depth_limit):
        # Search the deepest nodes in the search tree first using depth-limited search.
        # Returns the path to the goal node if it is found within the depth limit, otherwise returns None.
        def recursive_dls(node, depth):
            if depth == 0 and node == goal_node:
                return [node]
            elif depth > 0:
                for child in self.graph.neighbors(node):
                    result = recursive_dls(child, depth-1)
                    if result is not None:
                        return [node] + result
            return None

        for depth in range(depth_limit):
            result = recursive_dls(start_node, depth)
            if result is not None:
                return result
        return None

    # Iterative deepening depth-first-search:
    def iterative_deepening_depth_first_search(self, start_node, goal_node, max_depth):
        for depth in range(1, max_depth + 1):
            result = self.depth_limited_search(start_node, goal_node, depth)
            if result is not None:
                print(result)
                return result
        print("Goal not found within the depth limit.")
        return None

    # Bidirectional search


    def bidirectional_search(self, start_node, goal_nodes):
        # Perform bidirectional search from the start node to any of the goal nodes
        forward_queue = deque([(start_node, [start_node])])
        backward_queue = deque([(goal_node, [goal_node])
                               for goal_node in goal_nodes])
        forward_visited = set()
        backward_visited = set(goal_nodes)

        while forward_queue and backward_queue:
            # Expand nodes in the forward direction
            forward_node, forward_path = forward_queue.popleft()
            forward_visited.add(forward_node)

            if forward_node in backward_visited:
                # Path from start to goal found
                return forward_path + backward_queue[forward_node][1]

            for forward_child in self.graph.neighbors(forward_node):
                if forward_child not in forward_visited and forward_child not in [node for node, _ in forward_queue]:
                    forward_queue.append(
                        (forward_child, forward_path + [forward_child]))

            # Expand nodes in the backward direction
            backward_node, backward_path = backward_queue.popleft()
            backward_visited.remove(backward_node)

            if backward_node in forward_visited:
                # Path from start to goal found
                return forward_queue[backward_node][1] + backward_path

            for backward_child in self.graph.neighbors(backward_node):
                if backward_child not in backward_visited and backward_child not in [node for node, _ in backward_queue]:
                    backward_queue.append(
                        (backward_child, backward_path + [backward_child]))
                    backward_visited.add(backward_child)

        # No path found
        return None




    def simulated_annealing(self, start_node, max_iterations=1000, temperature=1.0, cooling_rate=0.003):
            # Initialize the current state as the start node
            current_node = start_node
            current_value = self.get_heuristic(current_node)
            
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
                neighbor_value = self.heuristic(random_neighbor, goal_node)
                
                # Calculate the energy difference between the current and neighbor states
                energy_diff = current_value - neighbor_value
                
                # If the neighbor is better, move to that state
                if energy_diff > 0:
                    current_node = random_neighbor
                # Increment the iteration count
                iteration += 1
                
            # Return the best state found
            return best_node

    def minimax(self, node, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.graph.out_degree(node) == 0:
            return self.get_heuristic(node)

        min_or_max = max if maximizing_player else min
        result = float("-inf") if maximizing_player else float("inf")
        for child in self.graph.neighbors(node):
            value = self.minimax(child, depth - 1, alpha, beta, not maximizing_player)
            result = min_or_max(result, value)
            if maximizing_player:
                alpha = max(alpha, result)
            else:
                beta = min(beta, result)
            if beta <= alpha:
                break

        return result

            

