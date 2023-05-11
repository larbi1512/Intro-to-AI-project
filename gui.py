import tkinter as tk
from problem import Problem

def get_user_input(entry):
    # Get the user input from the Entry widget
    user_input = entry.get()
    # Print the user input
    print("User input:", user_input)

def delete_content(root):
    # delete_content all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()

def main_menu(sender=0):
    if sender != 0:  # check if it is called from the main
        delete_content(sender)
    else:
        global root
        root = tk.Tk()  # parent window

    width, height = 500, 500
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(root, text="Welcome!", font=('Arial', 30))
    label.pack(padx=20, pady=30)

    button = tk.Button(root, text="Define problem", font=(
        'Arial', 18), command=lambda: problem_interface(root))  # call new menu to enter the problem
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="    Play Game   ", font=('Arial', 18))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10)

    root.mainloop()  # Keep the window open

def problem_interface(sender):
    p = Problem([])
    delete_content(sender)

    width, height = 500, 500
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Define your problem using nodes", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    label = tk.Label(
        root, text="Node label", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry widget
    entry = tk.Entry(root)
    entry.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add node", font=('Arial', 18))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Add the edges   ", font=(
        'Arial', 18), command=lambda: edges_interface(root))
    button.pack(padx=10, pady=10, side="bottom")

    label = tk.Label(
        root, text="When you finish your nodes enter the edges", font=('Arial', 15))
    label.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open

def edges_interface(sender):
    delete_content(sender)

    width, height = 500, 500
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

    # Create an Entry for the first node
    entry = tk.Entry(root)
    entry.pack()

    label = tk.Label(
        root, text="Node 2", font=('Arial', 20))
    label.pack(padx=10, pady=10)

    # Create an Entry for the second node
    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Add edge", font=('Arial', 18))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Solve the problem   ", font=(
        'Arial', 18), command=lambda: algorithms_menu(root)  # ,  go to menu of algorithms
    )
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open

def algorithms_menu(sender=0):

    delete_content(sender)

    width, height = 500, 500
    v_dim = str(width)+'x'+str(height)
    root.geometry(v_dim)  # Size of the window
    root.title("AI Project")  # Adding a title

    # Creating the Frame for the GUI
    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(
        root, text="Choose the algorithm you want to use", font=('Arial', 20))
    label.pack(padx=20, pady=30)

    button = tk.Button(root, text="Algo 1", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Algo 2", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Algo 3", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Algo 4", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="Algo 5", font=(
        'Arial', 18))  # call the function of this algorithm
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10)

    root.mainloop()  # Keep the window open


