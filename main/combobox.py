
from tkinter import *
from tkinter.ttk import Combobox

def myCombobox(root,frame):

    options = [
        "año",
        "director",
        "genero",
        "idioma original"
    ]
    año = [2000,2001,2002,2003,2004] #Se hace una lista de años que haya en el JSON
    director = ["jhon","pedro","juan"] #Se hace una lista de directores que haya en el JSON
    genero = ["Acción", "Drama","Terror","Suspenso","Romance","Fantasía"] #Se hace una lista de generos que haya en el JSON
    idioma_original = ["Francés","Alemán","Inglés"]

    frame = Frame(root,bg="brown1")
    frame.place(relx=0.005,rely=0.1,relwidth=0.99,relheight=0.85)
    list= []

    def maincombo():
        global combo1, combo2
        combo1 = Combobox(frame,values=options)
        combo1.place(relx=0.01,rely=0.1,relwidth=0.49,relheight=0.8)
        combo1.bind('<<ComboboxSelected>>', combofill)
        combo2 = Combobox(frame,values=options)
        combo2.place(relx = 0.5, rely= 0.1,relwidth=0.49,relheight=0.8)
    def combofill(event):
        if combo1.get() == "año":
            list = año
        elif combo1.get()=="director":
            list = director
        elif combo1.get()=="genero":
            list = genero
        elif combo1.get()=="idioma original":
            list = idioma_original  
        combo2.config(values=list)
        return combo2.get()


    maincombo()


