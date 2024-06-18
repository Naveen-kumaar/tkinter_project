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
headframe = Frame(window,width = 700,bd=1)
headframe.pack(side=TOP)
headlabel = Label(headframe,text='PCHYSIO THERAPY CLINIC - LOGIN',font=('arial',24),fg='white',bg='blue')

headlabel.grid(row=0,column=0)
#default ah center ku  than pokum



midframe =Frame(window,width = 600,bd=1)
midframe.pack(side=TOP)

username=StringVar()
pwd= StringVar()
username.set('')
pwd.set('')

usernamelabel = Label(midframe,text='Username',font=('arial',16),fg='white',bg='blue')
usernamelabel.grid(row=1,column=0,padx=10,pady=10)
usernametexbox= Entry(midframe,font=('arial',16),textvariable=username)
usernametexbox.grid(row=1,column=1,padx=10,pady=10)

pwdlabel = Label(midframe,text='Password',font=('arial',16),fg='white',bg='blue')
pwdlabel.grid(row=2,column=0,padx=10,pady=10)
pwdtexbox= Entry(midframe,font=('arial',16),textvariable=pwd)
pwdtexbox.grid(row=2,column=1,padx=10,pady=10)


def register():
    window.destroy()
    import reg

def login():
    con = sqlite3.connect('medical.db')
    cursor = con.cursor()
    cursor.execute("""select * from 'userdata' where username = ? and pwd = ? """,(username.get(),pwd.get()))
    if len(list(cursor.fetchall()))>0:
        msg.showinfo('login confirmation','login successfully',icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo('login error','user not defined',icon='warning')

submit_btn = Button(midframe,text='Register',command=register,font=('arial',16),fg='white',bg='green')
submit_btn.grid(row=4,column=1,padx=10,pady=10)

notuserlabel = Label(midframe,text='Not a User yet?..',font=('arial',16),fg='white',bg='blue')
notuserlabel.grid(row=4,column=0,padx=10,pady=10)

login_btn = Button(midframe,text='Login',command=login,font=('arial',16),fg='white',bg='Red')
login_btn.grid(row=3,column=1,padx=10,pady=10)


window.mainloop()