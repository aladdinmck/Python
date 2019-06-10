import tkinter as tk
import os
import math


class FlowerBotSim:

    c = tk.Tk()
    WIDTH = 500
    HEIGHT = 200
    canvas = tk.Canvas(c, width=WIDTH, height=HEIGHT)
    canvas.pack()
    
    # Track
    # Left Vertical Line
    canvas.create_line(25, 170, 25, 75)
    
# Top Line
    canvas.create_line(0, 75, 375, 75)
    
# Bottom Line
    canvas.create_line(25, 125, 375, 125)
    
# Right end vertical Line
    canvas.create_line(375, 75, 375, 125)
    
    '''    
# Plants
    canvas.create_oval(50,130,60,140)
    canvas.create_oval(85,130,95,140)
    canvas.create_oval(120,130,130,140)
    canvas.create_oval(155,130,165,140)
    canvas.create_oval(195,130,205,140)
    canvas.create_oval(230,130,240,140)
    canvas.create_oval(265,130,275,140)
    canvas.create_oval(300,130,310,140)
    canvas.create_oval(335,130,345,140)
    canvas.create_oval(370,130,380,140)
    ''' 
# Plant Line
    canvas.create_line(75,170,399,170)
# Plants 
    canvas.create_line(75,165,75,175)
    canvas.create_line(111,165,111,175)
    canvas.create_line(147,165,147,175)
    canvas.create_line(183,165,183,175)
    canvas.create_line(219,165,219,175)
    canvas.create_line(255,165,255,175)
    canvas.create_line(291,165,291,175)
    canvas.create_line(327,165,327,175)
    canvas.create_line(363,165,363,175)
    canvas.create_line(399,165,399,175)
    
    
# Drop Zones
    canvas.create_rectangle(1,1,200,40, fill = 'green', outline = 'green')
    canvas.create_rectangle(200,1,400,40, fill = 'red', outline = 'red')
    
# Robot
    canvas.create_rectangle(5, 150, 55, 200, fill = 'gold')

    
    
    
    def getxy(event):    
        print("Position = ({0},{1})".format(event.x, event.y))
        
        
    canvas.bind('<Button-1>', getxy)
    canvas.pack()
     


    c.mainloop()
    
    
