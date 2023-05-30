import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()

rec = c.create_rectangle(25,55,50,80,fill="#aa0000")

f = open('map1.txt')
data = f.read()
lines = data.split('\n')

walls = []

x = 25
y = 25


for i in range(len(lines)):
    for a in range(len(lines[i])):
        if lines[i][a] == "*":
            walls.append( c.create_rectangle(x,y,x+25,y+25,fill="Black"))
        x += 30
    x = 25
    y += 30


def keyPress(e):
    key = e.keysym
    if key == "Up":
        x=0
        y=-30
        c.move(rec,x,y)
    if key == "Down":
        x=0
        y=30
        c.move(rec,x,y)
    if key == "Left":
        x=-30
        y=0
        c.move(rec,x,y)
    if key == "Right":
        x=30
        y=0
        c.move(rec,x,y)
    
    cordsrec = (c.coords(rec))
    for i in range(len(walls)):
        cordswalls = c.coords(walls[i])
        if cordsrec == cordswalls:
            if key == "Up":
                x=0
                y=30
                c.move(rec,x,y)
            if key == "Down":
                x=0
                y=-30
                c.move(rec,x,y)
            if key == "Left":
                x=30
                y=0
                c.move(rec,x,y)
            if key == "Right":
                x=-30
                y=0
                c.move(rec,x,y)
            
            

w.bind("<Key>",keyPress)

w.mainloop()