import tkinter as tk


def get_user_input(entry):
    # Get the user input from the Entry widget
    user_input = entry.get()
    # Print the user input
    print("User input:", user_input)


def delete_content(root):
    # delete_content all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()


def problem_interface():
    global root
    root = tk.Tk()
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
    node1 = tk.Entry(root)
    node1.pack()

    # need to know the structure to implement the function
    button = tk.Button(root, text="Add node", font=(
        'Arial', 18), command=lambda: get_user_input(node1))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, text="         Exit         ",
                       font=('Arial', 18), command=lambda: exit())
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Main menu   ", font=(
        'Arial', 18), command=lambda: main_menu(root))
    button.pack(padx=10, pady=10, side="bottom")

    button = tk.Button(root, text="    Add the initial state   ", font=(
        'Arial', 18), command=lambda: initial_state_interface(root))
    button.pack(padx=10, pady=10, side="bottom")

    root.mainloop()  # Keep the window open


problem_interface()
