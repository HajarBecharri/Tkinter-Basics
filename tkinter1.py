

from tkinter import * 
#**creation of a window**

fenetre = Tk() 
fenetre.geometry("{}x{}+{}+{}".format(400,500,400,400))
fenetre.title('my first fenetre')
fenetre['bg']='red'
#you will not have the ability of resizing the window when it will be showed
fenetre.resizable(height=False,width=False) 

#**creation of a label inside the window**
label_bouton=Label(fenetre,text="EVENT DONE !",
            font=("Verdana",20),fg="black",bg="red")
label=Label(fenetre,text="my first label",
            font=("Verdana",20,"italic bold"),fg="white",bg="red")
#pack and place pour placer label
#pour placer label au milieu de la fenetre
label.pack()
#pour placer label dans un endroit precis de la fenetre,mettre à 50px de la cote gauche
#label.pack(side=RIGHT,padx=50)

#placer à 50px de la cote gauche et à 30px a partir du haut
#label.place(x='50',y='30')
#modifier text du label

label['text']="my first label modifie"

#**creation of buttons**
def hello_word():
    label_bouton.place(x='100',y='150')

bouton=Button(fenetre,text="click here",width='8',height='2',bg='black',fg='white',command=hello_word)
bouton.pack()


#**recuperer user data**

def method_user():
    label_user['text']=ma_variable.get()
    label.pack()

ma_variable=StringVar()
label_user=Label(fenetre,text='Veuiller entrer la valeur')
label_user.pack()
entree=Entry(fenetre,textvariable=ma_variable)
entree.pack()
button_user=Button(fenetre,text='click',command=method_user)
button_user.pack()

#**creation of a menu**

my_menu=Menu(fenetre)

#sous onglet files
files=Menu(my_menu,tearoff=0) #pour retirer ----------
files.add_cascade(label="save at")
#sous onglet options
options =Menu(my_menu)
options.add_command(label="Modifier",command=hello_word)
options.add_command(label="ajouter",command=hello_word)



#les 2 principaux onglets
my_menu.add_cascade(label="files",menu=files)
my_menu.add_cascade(label="options",menu=options)

#for showing
fenetre.config(menu=my_menu)

#**frame** pour regrouper les choses

frame=Frame(fenetre,bg='green')
label_frame1=Label(frame,text='frame label 1')
label_frame1.pack()
label_frame2=Label(frame,text='frame label 2')
label_frame2.pack()
frame.pack(expand=YES) #pour le mettre au milieu

#**showing images**

picture=PhotoImage(file='Mario.png')
label_picture=Label(fenetre,image=picture)

def method_image():
    label_picture.pack()

button_image=Button(fenetre,text='show image',command=method_image)

button_image.place(x='200',y='200')
fenetre.mainloop()



 


