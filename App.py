# coding: utf-8
from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import *
#from Speech import speechRest
import pyttsx3
#from tkinter import filedialog

def speechRest(tite):
    
    text_speech = pyttsx3.init()

    #answer = 'hello world'#input("que veut tu ecrire pour parler : ")
    answer = tite
    text_speech.say(answer)
    text_speech.runAndWait()

def ouvrire():
    global image
    filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])

    image = Image.open(filepath)
    image = image.resize((200, 200))
    image = ImageTk.PhotoImage(image)
    my_image = Label(frame2, image=image)
    my_image.grid(row=0, column=0, padx= 50, pady=50, sticky=W) 
    print(filepath)

#creation de la fenetre
window = Tk()

#personnaliser la fentre
window.title("BRAILLE TO SPEECH")
window.geometry("850x500")
window.minsize(850, 500)
window.maxsize(850, 500)
window.iconbitmap("ressource\logo.ico")
#window.config(background='#000')

#frame
frame1 = Frame(window)
frame1.pack()
#
frame2 = Frame(window)
frame2.pack()
#
frame3 = Frame(window, bd= 1, relief=SUNKEN)
frame3.pack(expand=1)

#Label
label_title = Label(frame1, text="PROJET DE FIN D’ANNEE D’ETUDE", font=("Courrier", 20))
label_title.pack()

#conteneur de baraille et text

width = 300
height = 300

filepath = "ressource/reading.png"
image = Image.open(filepath)
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)

my_image = Label(frame2, image=image)
my_image.grid(row=0, column=0, padx= 50, pady=50, sticky=W)

##

resultat = "B"
var_label = StringVar()
var_label.set(resultat)
label_resulta = Label(frame2, textvariable=var_label, font=("Courrier", 80))
label_resulta.grid(row=0, column=1, padx= 60, pady=1, sticky=E)

#boutton
#dir_img = PhotoImage(file='ressource/dir.png')
sel_button = Button(frame3, text="Selectioner une image", font=("Courrier", 14), bd= 1, command=ouvrire)#,command=le_de_la_f0nction_ou_la_librerie_importe
tra_button = Button(frame3, text="Traduire", font=("Courrier", 14), bd= 1)
son_button = Button(frame3, text="Speech", font=("Courrier", 14), bd= 1, command=speechRest(resultat))
#
sel_button.grid(row=0, column=0, padx= 50, pady=5, sticky=W)
tra_button.grid(row=0, column=1, padx= 50, pady=5, sticky=W)
son_button.grid(row=0, column=2, padx= 50, pady=5, sticky=W)

#Menu
menu_bar = Menu(window)
#premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau")#,command pour ajoute une nouvelle image
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)

#
#afficher
window.mainloop()

