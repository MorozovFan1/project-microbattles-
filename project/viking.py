from tkinter import *
from PIL import ImageTk, Image
from classs import *



def abba():
    
    mainloop()
    root.mainloop()

def vikings():
  
    
    pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/viking_photos/main.jpeg")
    pone = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(600,300,image=pone)
    pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/viking_photos/first.png")
    pone = ImageTk.PhotoImage(pilImage)
    im = canvas.create_image(600,300,image=pone)
    canvas.bind('<Button-1>', abba)
    mainloop()
    root.mainloop()
    


vikings()
abba()

