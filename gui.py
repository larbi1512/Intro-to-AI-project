from csp import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
from problem import Problem
import tkinter as tk


def get_user_edge(entry_1, entry_2, entry_3, p):
    # Get the user input from the Entry widget
    node_1 = entry_1.get()
    node_2 = entry_2.get()
    # create a variable to put the edge format
    edge = []
    edge.append(node_1)
    edge.append(node_2)
    p.add_an_edge(edge)
    p.modify_edge_weight(edge, entry_3.get())
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)


def get_node_info(entry_1, entry_2, p):
    # Get the user input from the Entry widget
    label = entry_1.get()
    value = entry_2.get()
    if value == None:  # check if the node has a value or no
        value = 0
    p.add_a_node(label)  # add a node to the problem graph
    p.modify_heuristic_value(label, value)
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)


def add_initial_state(root, entry_1, p):
    # Get the user input from the Entry widget
    label = entry_1.get()
    p.initial_state = label  # addthe initial state of the program
    goal_states_interface(root, p)  # redirect tto the goal states menu


def delete_content(root):
    # delete_content all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()


# read the variable label and set its name
def get_variable_label(root, label, csp):
    var.name = label
    # call the menu of inserting the domain of this variable
    csp_domain_interface(root, csp)


# read a value for the variable domain
def get_variable_value(root, value, csp):
    # adding value for the domain of the variable
    var.add_value_domain(value.get())
    value.delete(0, tk.END)

# read the constraints in order to add them to the CSP


# get the format of constraints in order to inseret them
def get_constraints(different, equal, root, csp):
    diff = different.split(",")
    eq = equal.split(",")
    csp.add_constraint(AllDifferentConstraint(diff))
    csp.add_constraint(AllEqualConstraint(eq))
    CSP_solver(root, csp)

# get the format of constraints in order to inseret them


def csp_solutions(csp):  # function to print all the possible assignments of variables
    sol = csp.get_solutions()
    for s in sol:
        assignment = ""
        first = True
        for key in s.keys():
            assignment = assignment + key + " = " + s[key] + " ,"
        if assignment != "":
            label = tk.Label(root, text=assignment, font=('Arial', 20))
            label.pack(padx=20, pady=40)
        else:
            label = tk.Label(
                root, text="No assignment found for your CSP", font=('Arial', 20))
            label.pack(padx=20, pady=40)


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
        # nx.draw_networkx_labels(p.graph, init_pos,
        #                   labels=nx.get_node_attributes(p.graph, 'h'))

    # Create the animation
    ani = FuncAnimation(plt.gcf(), update, frames=len(
        list(path)), interval=1000)

    # Show the animation
    plt.show()


def main_menu(p, csp=0, sender=0):
    if sender != 0:  # check if it is called from onther menu
        delete_content(sender)
    else:
        global root
        root = tk.Tk()  # parent window
    p.__init__([])
    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(root, text=" Welcome! ", font=('Arial', 30))
    label.pack(padx=20, pady=100)

    button = tk.Button(root, text=" Define your problem ", font=(
        'Arial', 18), command=lambda: problem_interface(root, p))  # call new menu to enter the problem
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="    Define your CSP    ", font=(
        'Arial', 18), command=lambda: csp_variable_interface(root, csp))  # call new menu to enter the problem
    button.pack(padx=10, pady=10)

    button = tk.Button(
        root, text="         Play Game        ", font=('Arial', 18))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=100)

    root.mainloop()  # Keep the window open


def problem_interface(sender, p):

    delete_content(sender)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your problem by entering nodes", font=('Arial', 20))
    label.pack(padx=20, pady=70)

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
    button.pack(padx=10, pady=20)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, csp, root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="     Add the initial state    ", font=(
        'Arial', 18), command=lambda: initial_state_interface(root, p))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def csp_variable_interface(sender, csp):

    delete_content(sender)

    global var
    var = Variable()  # creat a variable in order to insert it to the csp

    if var != None:
        csp.add_variable(var)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your CSP by entering your variables and constraints", font=('Arial', 20))
    label.pack(padx=20, pady=70)

    label = tk.Label(
        root, text="Variable label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry for lebel of that node
    variable_label = tk.Entry(root)
    variable_label.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add a variable", font=(
        'Arial', 18), command=lambda: get_variable_label(root, variable_label.get(), csp))
    button.pack(padx=10, pady=20)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, csp, root))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def csp_domain_interface(sender, csp):

    delete_content(sender)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Enter the domain of the variable you entered", font=('Arial', 20))
    label.pack(padx=20, pady=70)

    label = tk.Label(
        root, text="Domain's value", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry for lebel of that node
    variable_value = tk.Entry(root)
    variable_value.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add value", font=(
        'Arial', 18), command=lambda: get_variable_value(root, variable_value, csp))
    button.pack(padx=10, pady=20)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, csp, root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text=" Define your constraints  ", font=(
        'Arial', 18), command=lambda: constraints_interface(root, csp))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="     Add more variables    ", font=(
        'Arial', 18), command=lambda: csp_variable_interface(root, csp))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def constraints_interface(sender, csp):

    delete_content(sender)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="PS: Follow the format: variable1, variable2, ...", font=('Arial', 20))
    label.pack(padx=10, pady=70)

    label = tk.Label(
        root, text="Enter the variables that must be equal", font=('Arial', 20))
    label.pack(padx=20, pady=20)

    # Create an Entry for lebel of that node
    equale_variables = tk.Entry(root)
    equale_variables.pack()

    label = tk.Label(
        root, text="Enter the variables that must be different", font=('Arial', 20))
    label.pack(padx=20, pady=20)

    # Create an Entry for lebel of that node
    different_variables = tk.Entry(root)
    different_variables.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Solve the CSP subject to this constrains", font=(
        'Arial', 18), command=lambda: get_constraints(different_variables.get(), equale_variables.get(), root, csp))
    button.pack(padx=10, pady=30)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, csp, root))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def CSP_solver(sender, csp):

    delete_content(sender)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="The possible assignment(s) for the variables is(are):", font=('Arial', 20))
    label.pack(padx=10, pady=40)

    csp_solutions(csp)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, csp, root))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def initial_state_interface(sender, p):
    delete_content(sender)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your initial state", font=('Arial', 20))
    label.pack(padx=20, pady=70)

    label = tk.Label(
        root, text="Initial state label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry widget
    entry = tk.Entry(root)
    entry.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add ", font=('Arial', 18),
                       command=lambda: add_initial_state(root, entry, p))
    button.pack(padx=10, pady=20)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(p, root))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


def goal_states_interface(sender, p):
    delete_content(sender)

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your goal states", font=('Arial', 20))
    label.pack(padx=20, pady=70)

    label = tk.Label(
        root, text="Node label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry widget
    entry = tk.Entry(root)
    entry.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add a goal", font=(
        'Arial', 18),  command=lambda: p.add_goal_state(entry.get()))  # call the fuction to add a goal state to the problem
    button.pack(padx=10, pady=20)

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

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your edges", font=('Arial', 20))
    label.pack(padx=20, pady=70)

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
    button.pack(padx=10, pady=20)

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

    width, height = 650, 800
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("Your AI Toolbox")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Choose the algorithm you want to use", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    button = tk.Button(root, text="                Breadth first search                ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.breadth_first_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="                Depth First Search                ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.depth_first_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="          Depth Limited First Search          ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.depth_limited_search(p.initial_state, "C", 3)
                                                       ))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Iterative Deepening Depth First Search", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.iterative_deepening_depth_first_search(p.initial_state, "C", 5))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="             Uniformed Cost Search            ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.uniform_cost_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="                       A* Search                       ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.a_star_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="           Greedy Best First Search           ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.greedy_best_first_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="               Bidirectional Search               ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.bidirectional_search(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="                     Hill Climbing                     ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.hill_climbing(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="               Simulated annealing              ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.simulated_annealing(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="                       Minimax                         ", font=(
        'Arial', 18), command=lambda: animate_solution(p, p.minimax(p.initial_state, "C"))
    )  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root, csp,  p))
    button.pack(padx=10, pady=15, side="bottom")

    root.mainloop()  # Keep the window open


p = Problem([])
csp = CSP()
main_menu(p, csp)
