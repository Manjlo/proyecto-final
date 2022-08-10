from tkinter import filedialog as FileDialog
from work_logic.handleJson import create_new_register

def opfile():
    file = FileDialog.askopenfilename(
    initialdir="C:", 
    filetypes=(
        ("Ficheros de texto", "*.txt"),
        ("Todos los ficheros","*.*")
    ), 
    title = "Abrir un fichero."
    )

    return file
    

    

