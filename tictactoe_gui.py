"""tictactoe.py: GUI tictactoe game"""


import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Tic Tac Toe")

# global varialbles
canvas_size = 500
count = 0
clicked = True  # starts with cross as True
padding = 21
won = False
game = 0

# creates canvas
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

# creates frame
frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

# creates photoimages
cross = tk.PhotoImage(file="./img/cross.png")
circle = tk.PhotoImage(file="./img/circle.png")
blank = tk.PhotoImage(file="./img/blank.png")

# resize images
cross = cross.subsample(5, 5)
circle = circle.subsample(5, 5)
blank = blank.subsample(5, 5)

# players
player1 = tk.Label(
    canvas,
    text="Player 1's turn",
    font=("Helvetica", 12),
    bg="white",
    relief=tk.SOLID,
    border=0,
)
player2 = tk.Label(
    canvas,
    text="Player 2's turn",
    font=("Helvetica", 12),
    bg="white",
    relief=tk.SOLID,
    border=0,
)

player1.place(relx=0.15, rely=0.93)
player2.place(relx=0.65, rely=0.93)


"""-------------- Functions ----------------"""


# creates all buttons
def start():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count, clicked, won, player1, player2, win_label
    count = 0
    clicked = True
    won = False

    if game > 0:
        win_label.destroy()

    player1.config(border=4)

    b1 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b1),
    )
    b2 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b2),
    )
    b3 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b3),
    )

    b4 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b4),
    )
    b5 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b5),
    )
    b6 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b6),
    )

    b7 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b7),
    )
    b8 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b8),
    )
    b9 = tk.Button(
        frame,
        image=blank,
        bg="white",
        activebackground="white",
        relief=tk.GROOVE,
        command=lambda: b_click(b9),
    )

    # grid our buttons to the screen
    """ 
        b1 | b2 | b3
        ------------
        b4 | b5 | b6
        ------------
        b7 | b8 | b9
    """
    b1.grid(row=0, column=0, padx=padding, pady=padding)
    b2.grid(row=0, column=1, padx=padding, pady=padding)
    b3.grid(row=0, column=2, padx=padding, pady=padding)

    b4.grid(row=1, column=0, padx=padding, pady=padding)
    b5.grid(row=1, column=1, padx=padding, pady=padding)
    b6.grid(row=1, column=2, padx=padding, pady=padding)

    b7.grid(row=2, column=0, padx=padding, pady=padding)
    b8.grid(row=2, column=1, padx=padding, pady=padding)
    b9.grid(row=2, column=2, padx=padding, pady=padding)


def b_click(b):
    global clicked, count
    global player1, player2

    if b["image"] != "pyimage6":
        messagebox.showerror(
            "Tic Tac Toe - Error",
            "That box has already been selected\nPick another box",
        )
    else:
        if clicked == True:
            b.config(image=cross)
        else:
            b.config(image=circle)

        if (count) % 2 == 1:
            player1.config(border=4)
            player2.config(border=0)
        else:
            player1.config(border=0)
            player2.config(border=4)

        count += 1
        clicked = not clicked
        checkifwon()


def checkifwon():
    global won, winner, game
    winner = "pyimage6"

    # check rows
    if (
        b1["image"] != "pyimage6"
        and b1["image"] == b2["image"]
        and b1["image"] == b3["image"]
    ):
        won = True
        winner = b1["image"]
    elif (
        b4["image"] != "pyimage6"
        and b4["image"] == b5["image"]
        and b4["image"] == b6["image"]
    ):
        won = True
        winner = b4["image"]
    elif (
        b7["image"] != "pyimage6"
        and b7["image"] == b8["image"]
        and b7["image"] == b9["image"]
    ):
        won = True
        winner = b7["image"]

    # check columns
    elif (
        b1["image"] != "pyimage6"
        and b1["image"] == b4["image"]
        and b1["image"] == b7["image"]
    ):
        won = True
        winner = b1["image"]
    elif (
        b2["image"] != "pyimage6"
        and b2["image"] == b5["image"]
        and b2["image"] == b8["image"]
    ):
        won = True
        winner = b2["image"]
    elif (
        b3["image"] != "pyimage6"
        and b3["image"] == b6["image"]
        and b3["image"] == b9["image"]
    ):
        won = True
        winner = b3["image"]

    # check diagonals
    elif (
        b1["image"] != "pyimage6"
        and b1["image"] == b5["image"]
        and b1["image"] == b9["image"]
    ):
        won = True
        winner = b1["image"]
    elif (
        b3["image"] != "pyimage6"
        and b3["image"] == b5["image"]
        and b3["image"] == b7["image"]
    ):
        won = True
        winner = b3["image"]

    # if its a tie
    elif count == 9 and won == False:
        show_winner("pyimage6")
        disable_all_buttons()
        game += 1

    if won == True:
        show_winner(winner)
        disable_all_buttons()
        game += 1


def show_winner(winner):
    global win_label
    if winner == "pyimage4":
        win_label = tk.Label(
            canvas,
            width=15,
            text="X's  won",
            font=("Helvetica", 12),
            anchor=tk.CENTER,
        )

    elif winner == "pyimage5":
        win_label = tk.Label(
            canvas,
            width=15,
            text="O's  won",
            font=("Helvetica", 12),
            anchor=tk.CENTER,
        )
    else:
        win_label = tk.Label(
            canvas,
            width=15,
            text="It's a tie",
            font=("Helvetica", 12),
            anchor=tk.CENTER,
        )
    win_label.place(relx=0.363, rely=0.03)


def disable_all_buttons():
    # global b1, b2, b3, b4, b5, b6, b7, b8, b9

    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)
    b7.config(state=tk.DISABLED)
    b8.config(state=tk.DISABLED)
    b9.config(state=tk.DISABLED)


# stars the game
start()


# menu
menu = tk.Menu(root)
root.config(menu=menu)

options_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=start)

root.mainloop()
