import tkinter as tk
from problem import Problem
import networkx as nx
from matplotlib.animation import FuncAnimation


def get_user_edge(entry_1, entry_2, entry_3, p):
    # Get the user input from the Entry widget
    node_1 = entry_1.get()
    node_2 = entry_2.get()
    # create a variable to put the edge format
    edge = []
    edge.append(node_1)
    edge.append(node_2)
    p.add_an_edge(edge)
    p.modify_edge_weight(edge, entry_3)


def get_node_info(entry_1, entry_2, p):
    # Get the user input from the Entry widget
    label = entry_1.get()
    value = entry_2.get()
    if value == None:  # check if the node has a value or no
        value = 0
    p.add_a_node(label)  # add a node to the problem graph
    p.modify_heuristic_value(label, value)


def add_initial_state(root, entry_1, p):
    # Get the user input from the Entry widget
    label = entry_1.get()
    p.initial_state = label  # addthe initial state of the program
    goal_states_interface(root, p)  # redirect tto the goal states menu


def delete_content(root):
    # delete_content all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()


# path parameter here will be replaced when calling this function with
    # the functions of uninformed or infomed search

def animate_solution(p, path):
    init_pos = nx.spring_layout(p.graph)

    def update(frame):
        # Clear the old graph
        plt.clf()

        # Run BFS for the current frame number
        nodes_to_color = list(path)[:frame+1]
        print(f"the nodes to color: {nodes_to_color}")
        node_colors = [
            'green' if node in nodes_to_color else 'gray' for node in p.graph.nodes()]

        edge_labels = nx.get_edge_attributes(
            p.graph, 'weight')
        print(edge_labels)
        # Draw the new graph with the updated colors and the initial positions of the nodes

        nx.draw(p.graph, init_pos,
                node_color=node_colors, with_labels=True)
        nx.draw_networkx_edge_labels(
            p.graph, init_pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(p.graph, init_pos,
                                labels=nx.get_node_attributes(p.graph, 'h'))

    # Create the animation
    ani = FuncAnimation(plt.gcf(), update, frames=len(
        list(path)), interval=1000)

    # Show the animation
    plt.show()


def main_menu(p, sender=0):
    if sender != 0:  # check if it is called from onther menu
        delete_content(sender)
    else:
        global root
        root = tk.Tk()  # parent window

    width, height = 600, 700
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(root, text="Welcome!", font=('Arial', 30))
    label.pack(padx=20, pady=30)

    button = tk.Button(root, text="Define your problem", font=(
        'Arial', 18), command=lambda: problem_interface(root, p))  # call new menu to enter the problem
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="    Play Game   ", font=('Arial', 18))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10)

    root.mainloop()  # Keep the window open


def problem_interface(sender, p):

    delete_content(sender)

    width, height = 600, 700
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your problem by entering nodes", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    label = tk.Label(
        root, text="Node label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry for lebel of that node
    node_label = tk.Entry(root)
    node_label.pack()

    label = tk.Label(
        root, text="Node's heuristic funtion's value", font=('Arial', 20))
    label.pack(padx=10, pady=13)

    # Create an Entry for heuristic value of that node
    node_value = tk.Entry(root)
    node_value.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add node", font=(
        'Arial', 18), command=lambda: get_node_info(node_label, node_value, p))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root, p))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Add the initial state   ", font=(
        'Arial', 18), command=lambda: initial_state_interface(root, p))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def initial_state_interface(sender, p):
    delete_content(sender)

    width, height = 600, 700
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your initial state", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    label = tk.Label(
        root, text="Initial state label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry widget
    entry = tk.Entry(root)
    entry.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add ", font=('Arial', 18),
                       command=lambda: add_initial_state(root, entry, p))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, root))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def goal_states_interface(sender, p):
    delete_content(sender)

    width, height = 600, 700
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your goal states", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    label = tk.Label(
        root, text="Node label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry widget
    entry = tk.Entry(root)
    entry.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add a goal", font=(
        'Arial', 18),  command=lambda: p.add_goal_state(entry.get()))  # call the fuction to add a goal state to the problem
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Add the edges   ", font=(
        'Arial', 18), command=lambda: edges_interface(root, p))
    button.pack(padx=10, pady=10, side="bottom")

    label = tk.Label(
        root, text="When you finish entring your goal states click below", font=('Arial', 15))
    label.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def edges_interface(sender, p):
    delete_content(sender)

    width, height = 600, 700
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your edges", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    label = tk.Label(
        root, text="Node 1", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry widget
    entry_1 = tk.Entry(root)
    entry_1.pack()

    label = tk.Label(
        root, text="Node 2", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry for the second node
    entry_2 = tk.Entry(root)
    entry_2.pack()

    label = tk.Label(
        root, text="Edge cost", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry for path cost
    entry_3 = tk.Entry(root)
    entry_3.pack()

    button = tk.Button(root, text="Add edge", font=(
        'Arial', 18), command=lambda: get_user_edge(entry_1, entry_2, entry_3, p))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Solve the problem   ", font=(
        'Arial', 18), command=lambda: algorithms_menu(p, root)  # ,  go to menu of algorithms
    )

    button.pack(padx=10, pady=10, side="bottom")
    label = tk.Label(
        root, text="PS: every node that is not predifined before will be added automatically", font=('Arial', 15))
    label.pack(padx=10, pady=10, side="bottom")

    label = tk.Label(
        root, text="When you finish your edges click below to choose an algorithm to solve your problem", font=('Arial', 15))
    label.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def algorithms_menu(p, sender=0):

    delete_content(sender)

    width, height = 600, 700
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Choose the algorithm you want to use", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    button = tk.Button(root, text="Breadth first search", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.breadth_first_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Depth first search", font=(
        'Arial', 18), command=lambda: print(p.goal_states)
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Depth limited first search", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Iterative deepening depth first search", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Hill climbing", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Simulated annealing", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Minimax", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root, p))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


p = Problem([])
main_menu(p)
