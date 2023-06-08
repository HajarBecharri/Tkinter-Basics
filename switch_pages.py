from tkinter import *

root=Tk()
root.geometry("{}x{}+{}+{}".format(300,400,0,0))
root.title('SWITCH PAGES')
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
    


def home_page():
    delete_pages()
    home_frame=Frame(main_frame)
    home_label=Label(home_frame,text='welcome to home')
    home_label.pack()
    home_frame.pack(pady=20)

def menu_page():
    delete_pages()
    menu_frame=Frame(main_frame)
    menu_label=Label(menu_frame,text='welcome to menu')
    menu_label.pack()
    menu_frame.pack(pady=20)

side_frame=Frame(root,bg='grey')

home_btn=Button(side_frame,text='Home',command=home_page)
home_btn.place(x=10,y=50)
menu_btn=Button(side_frame,text='Menu',command=menu_page)
menu_btn.place(x=10,y=100)
side_frame.pack(side=LEFT)
side_frame.pack_propagate(False)
side_frame.config(width=100,height=400)

main_frame=Frame(root,bg='#fff')
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.config(width=300,height=400)


root.mainloop()