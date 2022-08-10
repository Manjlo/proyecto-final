
#ventanas en HD
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#crear interfaz del crud
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tokenize import Name
from turtle import bgcolor, up
from combobox import myCombobox
from messagebox import test
from archivoJSON import opfile
from work_logic.handleJson import create_new_register
from models.movie import Movie

#--- Interfaz ----------------------------------------------

#--- Raiz ---
root = tk.Tk()
root.geometry('650x250')
root.title("Péliculas Icónicas")
color = 'old lace'
root.configure(bg= color)
root.resizable(False, False)

#---Frames principales--------------------------------------
page = Frame(root,bg=color)
page.place(relx=0,rely= 0,relheight=1,relwidth=1)
#---funciones de interfaz --------------------------------


def get_Json():
    file = opfile()
    root.setvar('file', file)





def view():
    for p in page.winfo_children():
        p.destroy()
    selectorPage("/view")

def addRegister():
    file = root.getvar('file')
    pelicula = Movie('hola', 'si', 2020, "español", "joselo", "comedia", ["joselo"])
    create_new_register(file, pelicula)
    # for p in page.winfo_children():
    #     p.destroy()
    # selectorPage("/addRegister")

def updateRegister():
    for p in page.winfo_children():
        p.destroy()
    selectorPage("/updateRegister")

def deleteRegister():
    for p in page.winfo_children():
        p.destroy()
    selectorPage("/deleteRegister")

def backButton():
    for p in page.winfo_children():
        p.destroy()
    selectorPage('/home')

def selectorPage(link):
    if (link == '/home'):
        #----Frames -----------------------------------------------
        RH = 0.3
        frame1 = tk.Frame(page, bg= color, bd= 1.5)
        frame1.place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.15)
        frame2 = tk.Frame(page, bg= color, bd=1.5)
        frame2.place(relx=0.03, rely=0.25, relwidth=0.47, relheight=0.15)
        frame3 = tk.Frame(page, bg= color, bd=1.5)
        frame3.place(relx=0.42, rely=0.25, relwidth=0.55, relheight=0.15)
        frame4 = tk.Frame(page, bg = color)
        frame4.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.5)
        SE_frame = tk.Frame(page, bg = color)
        SE_frame.place(relx=0.8, rely=0.75, relwidth=0.15, relheight=0.2)
        SW_frame = tk.Frame(page, bg = color)
        SW_frame.place(relx=0.032, rely=0.75, relwidth=0.28, relheight=0.22)
        mostrar = tk.Frame(page, bg = color)
        mostrar.place(relx=0.8, rely=0.46, relwidth=0.15, relheight=0.15)
        #-- Labels y Entradas Texto ---
        SW_label = tk.Label(SW_frame, text="Universidad del Valle",font=('Times New Roman',10,'italic'),bg="brown1",fg="white")
        SW_label.place(relx = 0, rely= RH + 0.2 , relheight=RH, relwidth=1)
        label2 = tk.Label(frame2, text="Listar por: ",font=('Times New Roman',10,'italic'),bg="linen")
        label2.place(relx = 0.4, rely= RH  , relheight=2*RH, relwidth=0.5)
        #--- Botones ---
            #--- Style buttons ---
        style = ttk.Style()
        style.configure('Custom.TButton',font = ('Times New Roman',9,'italic'),borderwidth ='4')
        style.map('Custom.TButton', foreground = [('pressed', 'green'),('active', 'black')], background=[('active', 'skyblue')])


        myCombobox(frame3,root)

        #-----
        B1 = ttk.Button(frame1, text="Seleccionar Archivo JSON",style = 'Custom.TButton', command= get_Json)
        B1.place(relx = 0.2, rely = 0.2 ,relheight=0.9, relwidth=0.6)
        B2 = ttk.Button(frame4, text="Adicionar registro",style = 'Custom.TButton', command=addRegister)
        B2.place(relx = 0.25, rely= 0.03, relheight= RH, relwidth=0.5)
        B3 = ttk.Button(frame4, text="Actualizar registro",style = 'Custom.TButton', command=updateRegister)
        B3.place(relx = 0.25, rely= 0.34, relheight= RH , relwidth=0.5)
        B4 = ttk.Button(frame4, text="Borrar registro",style = 'Custom.TButton', command= deleteRegister)
        B4.place(relx = 0.25, rely= 0.65, relheight= RH , relwidth=0.5)
        B5 = ttk.Button(SE_frame, text="Autores",style = 'Custom.TButton',command=test)
        B5.place(relx = 0.15, rely= 0.3, relheight= RH+0.3 , relwidth=0.8)
        most = ttk.Button(mostrar,text="ver",style='Custom.TButton', command=view)
        most.place(relx=0.15, rely= 0.15, relheight=0.8, relwidth=0.6)
        
    if (link == "/addRegister"):
        #frames
        left_frame = tk.Frame(page,bg = color)
        left_frame.place(relx=0,rely=0,relwidth=0.5,relheight=1)
        rigth_frame = tk.Frame(page,bg = color)
        rigth_frame.place(relx=0.4,rely=0,relwidth=0.6,relheight=1)
        SE2_frame = tk.Frame(page,bg = color)
        SE2_frame.place(relx=0.9,rely=0.5,relwidth=0.09,relheight=0.5)
        #-- Labels y Entradas Texto ---
        colorLabel = 'linen'
        l1 = tk.Label(left_frame, text="nombre",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l1.place(relx = 0.1, rely= 0.05 , relheight=0.1, relwidth=0.5)
        l2 = tk.Label(left_frame, text="image",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l2.place(relx = 0.1, rely= 0.18 , relheight=0.1, relwidth=0.5)
        l3 = tk.Label(left_frame, text="año",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l3.place(relx = 0.1, rely= 0.31 , relheight=0.1, relwidth=0.5)
        l4 = tk.Label(left_frame, text="idioma original",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l4.place(relx = 0.1, rely= 0.44 , relheight=0.1, relwidth=0.5)
        l5 = tk.Label(left_frame, text="director",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l5.place(relx = 0.1, rely= 0.57 , relheight=0.1, relwidth=0.5)
        l6 = tk.Label(left_frame, text="genero",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l6.place(relx = 0.1, rely= 0.7 , relheight=0.1, relwidth=0.5)
        l7 = tk.Label(left_frame, text="actores principales",font=('Times New Roman',10,'italic'),bg=colorLabel)
        l7.place(relx = 0.1, rely= 0.83 , relheight=0.1, relwidth=0.5)
        #entrys
        name = ttk.Entry(rigth_frame)
        name.place(relx = 0, rely= 0.05 , relheight=0.1, relwidth=0.83)
        image = ttk.Entry(rigth_frame)
        image.place(relx = 0, rely= 0.18 , relheight=0.1, relwidth=0.83)
        año = ttk.Entry(rigth_frame)
        año.place(relx = 0, rely= 0.31 , relheight=0.1, relwidth=0.83)
        idioma_original = ttk.Entry(rigth_frame)
        idioma_original.place(relx = 0, rely= 0.44 , relheight=0.1, relwidth=0.83)
        director = ttk.Entry(rigth_frame)
        director.place(relx = 0, rely= 0.57 , relheight=0.1, relwidth=0.83)
        genero = ttk.Entry(rigth_frame)
        genero.place(relx = 0, rely= 0.7 , relheight=0.1, relwidth=0.83)
        actores_principales = ttk.Entry(rigth_frame)
        actores_principales.place(relx = 0, rely= 0.83 , relheight=0.1, relwidth=0.83)
        #button
        Back = ttk.Button(SE2_frame,text="Back",style='Custom.TButton', command=backButton)
        Back.place(relx = 0.1, rely= 0.1, relheight= 0.3 , relwidth=0.8)
        ok = ttk.Button(SE2_frame,text="agregar",style='Custom.TButton', command=addRegister)
        ok.place(relx = 0.1, rely= 0.55, relheight= 0.3 , relwidth=0.8)

    if (link == "/updateRegister"):

        colorLabel = 'linen'
        #frames
        up_frame = tk.Frame(page, bg = color)
        up_frame.place(relx = 0.04, rely= 0.09, relheight= 0.18, relwidth= 0.92)
        middle_frame = tk.Frame(page, bg = color)
        middle_frame.place(relx = 0.04, rely= 0.31, relheight= 0.18, relwidth= 0.92)
        middle2_frame = tk.Frame(page, bg = color)
        middle2_frame.place(relx = 0.04, rely= 0.53, relheight= 0.18, relwidth= 0.92)
        down_frame = tk.Frame(page, bg = color)
        down_frame.place(relx = 0.2, rely= 0.75, relheight= 0.18, relwidth= 0.53)
        #labels
        L_nPelicula = tk.Label(up_frame, text="nombre",font=('Times New Roman',10,'italic'),bg=colorLabel)
        L_nPelicula.place(relx = 0.1, rely= 0.3 , relheight=0.35, relwidth=0.2)
        L_elemento = tk.Label(middle_frame, text="elemento a cambiar",font=('Times New Roman',10,'italic'),bg=colorLabel)
        L_elemento.place(relx = 0.05, rely= 0.3, relheight=0.4, relwidth=0.3)
        #Entrys
        e_nPelicula = ttk.Entry(up_frame)
        e_nPelicula.place(relx = 0.4, rely= 0.27, relheight= 0.55, relwidth=0.5)
        e_elemento = ttk.Entry(middle_frame)
        e_elemento.place(relx = 0.4, rely= 0.27, relheight= 0.55, relwidth=0.5)
        entry = ttk.Entry(middle2_frame)
        entry.place(relx = 0.2, rely= 0.27, relheight= 0.55, relwidth=0.6)
        #Botones
        back1 = ttk.Button(down_frame,text="Back",style='Custom.TButton', command=backButton)
        back1.place(relx = 0.25, rely= 0.27, relheight= 0.6, relwidth=0.2)
        oK1 = ttk.Button(down_frame,text="oK",style='Custom.TButton')
        oK1.place(relx = 0.6, rely= 0.27, relheight= 0.6, relwidth=0.2)
    
    if (link == "/deleteRegister"):

        colorLabel = 'linen'
        #frames
        frame = tk.Frame(page,bg=color) 
        frame.place(relx=0.1, rely= 0.1, relheight= 0.5, relwidth= 0.8)
        botones = tk.Frame(page,bg=color)
        botones.place(relx=0.25, rely= 0.7, relheight= 0.2, relwidth= 0.5)
        #labels
        n_label = tk.Label(frame, text="nombre",font=('Times New Roman',10,'italic'),bg=colorLabel)
        n_label.place(relx=0.3, rely= 0.2, relheight= 0.2, relwidth= 0.4)
        #entrys
        en_try = ttk.Entry(frame)
        en_try.place(relx=0.1, rely= 0.6, relheight= 0.2, relwidth= 0.8)
        #botones
        back2 = ttk.Button(botones,text="Back",style='Custom.TButton', command=backButton)
        back2.place(relx=0.2, rely= 0.2, relheight= 0.55, relwidth= 0.2)
        delete = ttk.Button(botones,text="Delete",style='Custom.TButton')
        delete.place(relx=0.6, rely= 0.2, relheight= 0.55, relwidth= 0.2)

    if (link == "/view"):
        print("")
        


selectorPage('/home')
root.mainloop()
