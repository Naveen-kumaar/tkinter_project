import sqlite3
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')

#for width and height
#png , gif file mattum than tkinter la work agum
#first image view panrathuku first image ah load pannanum

reg_img = PhotoImage(file= 'namebg.png')

#photoimage indrathu inbuild function in tkinter
#image view pannanum na athuku first nama oru label create pannanum

bg_label = Label(window, image=reg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 1 na true 0 na false relwidth& relheight ethu vanthu image oda
#image oda real height and width oda display pannum

window.title('pchysio therapy clinic')
window.iconbitmap('icon.ico') #for icon
headframe = Frame(window,width = 700,bd=1)
headframe.pack(side=TOP)
headlabel = Label(headframe,text='PCHYSIO THERAPY CLINIC - HOME',font=('arial',24),fg='white',bg='blue')

headlabel.grid(row=0,column=0)
#default ah center ku  than pokum

midframe =Frame(window,width = 600,bd=1)
midframe.pack(side=TOP)

def add():
    window.destroy()
    import add_medicine


add_btn = Button(midframe,text='ADD MEDICINE',command=add,font=('arial',16),fg='white',bg='green')
add_btn.grid(row=0,column=1,padx=10,pady=10)

def view():
    window.destroy()
    import view_med

view_btn = Button(midframe,text='VIEW MEDICINE',command=view,font=('arial',16),fg='white',bg='green')
view_btn.grid(row=1,column=1,padx=10,pady=10)

def search():
    window.destroy()
    import search_med

search_btn = Button(midframe,text='SEARCH MEDICINE',command=search,font=('arial',16),fg='white',bg='green')
search_btn.grid(row=2,column=1,padx=10,pady=10)

def delete():
    window.destroy()
    import delete

delete_btn = Button(midframe,text='DELETE MEDICINE',command=delete,font=('arial',16),fg='white',bg='green')
delete_btn.grid(row=3,column=1,padx=10,pady=10)

def logout():
    window.destroy()
    import login

login_btn = Button(midframe,text='LOGOUT',command=logout,font=('arial',16),fg='white',bg='Red')
login_btn.grid(row=4,column=1,padx=10,pady=10)

window.mainloop()