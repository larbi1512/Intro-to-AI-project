from problem import Problem
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gui import *


class toolbox:
    def __init__(self, problem):
        self.__problem = Problem([])
        self.__problem = problem
        self.Menu()

    def Menu(self):
        main_menu(self.__problem)

    # path parameter here will be replaced when calling this function with
    # the functions of uninformed or infomed search
    def animate_solution(self, path):
        init_pos = nx.spring_layout(self.__problem.graph)

        def update(frame):
            # Clear the old graph
            plt.clf()

            # Run BFS for the current frame number
            nodes_to_color = list(path)[:frame+1]
            print(f"the nodes to color: {nodes_to_color}")
            node_colors = [
                'green' if node in nodes_to_color else 'gray' for node in self.__problem.graph.nodes()]

            edge_labels = nx.get_edge_attributes(
                self.__problem.graph, 'weight')
            print(edge_labels)
            # Draw the new graph with the updated colors and the initial positions of the nodes

            nx.draw(self.__problem.graph, init_pos, node_color=node_colors, with_labels=True)
            nx.draw_networkx_edge_labels(self.__problem.graph, init_pos, edge_labels=edge_labels)
            nx.draw_networkx_labels(self.__problem.graph, init_pos, labels=nx.get_node_attributes(self.__problem.graph, 'h'))


        # Create the animation
        ani = FuncAnimation(plt.gcf(), update, frames=len(
            list(path)), interval=1000)

        # Show the animation
        plt.show()
