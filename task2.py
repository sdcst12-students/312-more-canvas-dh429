import tkinter as tk
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map2.txt')
data = f.read()
lines = data.split('\n')

walls = []

x = 25
y = 25

wimg = tk.PhotoImage(file="assets/map.water.png")
plains = tk.PhotoImage(file="assets/map.plains.png")
forest = tk.PhotoImage(file="assets/map.forest.png")
hills = tk.PhotoImage(file="assets/map.hills.png")
mountians = tk.PhotoImage(file="assets/map.mountain.png")
swamp = tk.PhotoImage(file="assets/map.swamp.png")
city = tk.PhotoImage(file="assets/map.city.png")
for i in range(len(lines)):
    for a in range(len(lines[i])):
        print( lines[i][a] )
        if lines[i][a] == "0":       
            walls.append(c.create_image(x,y,image=wimg))
        if lines[i][a] == "1":
            walls.append(c.create_image(x,y,image=plains))
        if lines[i][a] == "2":
            walls.append(c.create_image(x,y,image=forest))
        if lines[i][a] == "3":
            walls.append(c.create_image(x,y,image=hills))
        if lines[i][a] == "4":
            walls.append(c.create_image(x,y,image=mountians))
        if lines[i][a] == "5":
            walls.append(c.create_image(x,y,image=swamp))
        if lines[i][a] == "6":
            walls.append(c.create_image(x,y,image=city))
        x += 30
    x = 25
    y += 30


w.mainloop()