from tkinter import *

from cv2 import exp #importation de la biblioteque

fenetre = Tk() #creation de la fenetre contenus dans la variable fenetre
fenetre.title("racourcis") #je definis le titre de la fenetre

frame = Frame(fenetre)
label1 = Label(frame, text="mon premier texte")
label1.pack()
label2 = Label(frame, text="mon deuxiemme text")
label2.pack()

frame.pack(expand=YES)
fenetre.geometry("800x500")
fenetre.iconbitmap(r'C:\Users\Nathan\Documents\github\git\python\image.ico')
fenetre.resizable(False, False)
fenetre.config(bg="#4BA7C2")
fenetre.mainloop() #affichage de la fenetre 