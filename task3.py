#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()

fimg = tk.PhotoImage(file="assets/charmanderflip.png")
wimg = tk.PhotoImage(file="assets/charmander.png")
charmg = c.create_image(300,200,image=wimg)
swap = True

def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)

def update():
    global swap
    if swap == True:
        c.itemconfig(charmg,image=fimg)
        swap = False
    elif swap == False:
        c.itemconfig(charmg,image=wimg)
        swap = True
    w.after(200,update)


w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)

w.after(200,update)

w.mainloop()