import tkinter as tk

# --- functions ---

def move_a(event):
    canvas.coords(a, event.x-50, event.y-50, event.x+50, event.y+50)

def move_b():
    canvas.move(b, 1, 0)
    # move again after 25ms (0.025s)
    root.after(25, move_b)

# --- main ---

# init
root = tk.Tk()

# create canvas
canvas = tk.Canvas(root)
canvas.pack()

# create objects
a = canvas.create_rectangle(0, 0, 100, 100, fill='red')
b = canvas.create_rectangle(0, 0, 100, 100, fill='blue')

# start moving `a` with mouse
canvas.bind("<Motion>", move_a)

# start moving `b` automatically
move_b()

# start program
root.mainloop()
