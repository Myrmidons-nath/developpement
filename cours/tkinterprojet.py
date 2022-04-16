from tkinter import *
from turtle import onclick #importation du module

fenetre = Tk() #creation fenetre 

fenetre.title('application') # ajout du titre
fenetre.config(bg="#82C8A8")
fenetre.iconbitmap(r'C:\Users\Nathan\Documents\github\git\cours\image.ico')
frame = Frame(fenetre)
titre1 = Label(frame, text="conference 1", bg="#82C8A8", fg="red")
titre1.pack()
titre2= Label(frame, text="conference 2", bg="#82C8A8", fg="red")

titre2.pack()

frame.pack(expand=YES)

fenetre.mainloop() #affichage