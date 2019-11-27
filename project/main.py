from tkinter import *
from PIL import ImageTk, Image
from random import randrange as rnd, choice
from viking import *
from kovboy import *
from samuray import *
from ads import *


i = 0

'''
генерация вызова вещи
'''
something = rnd(1, 10)



'''
функции мигания всех иконок с замедлением
'''

def update11():
    global im1, updateTime, something, i
    updateTime += 1
    im1 = canvas.create_image(384,226,image=vik)
    root.after(updateTime, update12)
    
def update12():
    canvas.delete(im1)
    if (something>=1)*(something<=30)*(updateTime>=50) == 1:
        global i
        if i>=5:
            canvas.delete(ALL)
            start_button.pack_forget()
            start_button.pack()
            vikings()
        else:
            i+=1
            root.after(300, update11)
            
    else:
        root.after(updateTime, update21)

def update21():
    global im2, updateTime, something, i
    updateTime += 1
    im2 = canvas.create_image(529,226,image=kov)
    root.after(updateTime, update22)
    
def update22():
    canvas.delete(im2)
    if (something>=31)*(something<=60)*(updateTime>=50) == 1:
        global i
        if i>=5:
            canvas.delete(ALL)
            start_button.pack_forget()
            start_button.pack()
            kovboys()
        else:
            i+=1
            root.after(300, update21)
            
    else:
        root.after(updateTime, update31)

def update31():
    global im3, updateTime, something, i
    updateTime += 1
    im3 = canvas.create_image(672,226,image=sam)
    root.after(updateTime, update32)
    
def update32():
    canvas.delete(im3)
    if (something>=61)*(something<=90)*(updateTime>=50) == 1:
        global i
        if i>=5:
            canvas.delete(ALL)
            start_button.pack_forget()
            start_button.pack()
            samurays()
        else:
            i+=1
            root.after(300, update31)
            
    else:
        root.after(updateTime, update41)
    
def update41():
    global im4, updateTime, something, i
    updateTime += 1
    im4 = canvas.create_image(815,226,image=ass)
    root.after(updateTime, update42)
    
def update42():
    canvas.delete(im4)
    if (something>=91)*(something<=100)*(updateTime>=50) == 1:
        global i
        if i>=5:
            canvas.delete(ALL)
            start_button.pack_forget()
            start_button.pack()
            ads()
        else:
            i+=1
            root.after(300, update41)
            
    else:
        root.after(updateTime, update11)

    
'''
импорт фото
'''

root.geometry('1200x750')


pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/main_photos/main_menu.png")
im = ImageTk.PhotoImage(pilImage)

pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/main_photos/vikings.jpeg")
vik = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/main_photos/kovboys.jpeg")
kov = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/main_photos/samurays.jpeg")
sam = ImageTk.PhotoImage(pilImage)
pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/main_photos/ass.jpeg")
ass = ImageTk.PhotoImage(pilImage)

pilImage = Image.open("/Users/daniilstrizak/Desktop/python/project/main_photos/lala.jpeg")
lala = ImageTk.PhotoImage(pilImage)





'''
кнопка
'''
def start():
    root.after(updateTime, update11)

ima9 = ImageTk.PhotoImage(file="/Users/daniilstrizak/Desktop/python/project/main_photos/start.jpeg")
start_button = Button(root, image=ima9, command=start)

    
'''
создание графического фона
'''

def menu():

    imagesprite = canvas.create_image(600,300,image=im)
    im5 = canvas.create_image(815,226,image=lala)
    start_button.place(x=470, y=382)



if __name__ == "__main__":
    menu()

mainloop()
root.mainloop()
