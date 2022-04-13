from tkinter import *
import tkinter #importation de la biblioteque

fenetre = Tk() #creation de la fenetre contenus dans la variable fenetre
fenetre.title("racourcis") #je definis le titre de la fenetre


label1 = Label(fenetre, text="mon premier texte", )
label1.pack()



fenetre.geometry("500x500")
fenetre.iconbitmap('image.ico')
fenetre.resizable(False, False)
fenetre.config(bg="#4BA7C2")
print(dir(tkinter.Label))
fenetre.mainloop() #affichage de la fenetre 