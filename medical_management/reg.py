from tkinter import *
import sqlite3
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
headlabel = Label(headframe,text='PCHYSIO THERAPY CLINIC',font=('arial',24),fg='white',bg='blue')

headlabel.grid(row=0,column=0)
#default ah center ku  than pokum

midframe =Frame(window,width = 600,bd=1)
midframe.pack(side=TOP)

con = sqlite3.connect('medical.db')
cursor = con.cursor()#cursor vechu than execute panna mudiyum
cursor.execute(""" create table if not exists 'userdata'
 (name text,id int,username text,pwd text,email text,mobile text)""")
con.commit()

name = StringVar()
id = IntVar()
username=StringVar()
pwd= StringVar()
email=StringVar()
mobile=StringVar()
name.set('')
id.set('')
username.set('')
pwd.set('')
email.set('')
Namelabel = Label(midframe,text='Name',font=('arial',16),fg='white',bg='blue')
Namelabel.grid(row=0,column=0,padx=10,pady=10)
Nametexbox= Entry(midframe,font=('arial',16),textvariable=name)
Nametexbox.grid(row=0,column=1,padx=10,pady=10)

idlabel = Label(midframe,text='Id',font=('arial',16),fg='white',bg='blue')
idlabel.grid(row=2,column=0,padx=10,pady=10)
idtexbox= Entry(midframe,font=('arial',16),textvariable=id)
idtexbox.grid(row=2,column=1,padx=10,pady=10)

usernamelabel = Label(midframe,text='Username',font=('arial',16),fg='white',bg='blue')
usernamelabel.grid(row=3,column=0,padx=10,pady=10)
usernametexbox= Entry(midframe,font=('arial',16),textvariable=username)
usernametexbox.grid(row=3,column=1,padx=10,pady=10)

pwdlabel = Label(midframe,text='Password',font=('arial',16),fg='white',bg='blue')
pwdlabel.grid(row=4,column=0,padx=10,pady=10)
pwdtexbox= Entry(midframe,font=('arial',16),textvariable=pwd)
pwdtexbox.grid(row=4,column=1,padx=10,pady=10)

maillabel = Label(midframe,text='E-mail',font=('arial',16),fg='white',bg='blue')
maillabel.grid(row=5,column=0,padx=10,pady=10)
mailtexbox= Entry(midframe,font=('arial',16),textvariable=email)
mailtexbox.grid(row=5,column=1,padx=10,pady=10)

mobilelabel = Label(midframe,text='Mobile',font=('arial',16),fg='white',bg='blue')
mobilelabel.grid(row=6,column=0,padx=10,pady=10)
mobiletexbox= Entry(midframe,font=('arial',16),textvariable=mobile)
mobiletexbox.grid(row=6,column=1,padx=10,pady=10)

def register():
    con = sqlite3.connect('medical.db')
    cursor = con.cursor()  # cursor vechu than execute panna mudiyum
    cursor.execute(""" insert into 'userdata'
    (name,id,username,pwd,email,mobile)values(?,?,?,?,?,?)""",(str(name.get()),str(id.get()),str(username.get()),str(pwd.get()),str(email.get()),str(mobile.get())))
    con.commit()
    if cursor.rowcount>0:
        msg.showinfo('confirmation','New user added',icon='info')
    else:
        msg.showinfo('Error','New user not added',icon='waring')

def login():
    window.destroy()
    import login
    



submit_btn = Button(midframe,text='SUMIT',command=register,font=('arial',16),fg='white',bg='green')
submit_btn.grid(row=7,column=1,padx=10,pady=10)

alreadyuserlabel = Label(midframe,text='Already a User?..',font=('arial',16),fg='white',bg='blue')
alreadyuserlabel.grid(row=8,column=0,padx=10,pady=10)

login_btn = Button(midframe,text='Login',command=login,font=('arial',16),fg='white',bg='Red')
login_btn.grid(row=8,column=1,padx=10,pady=10)

window.mainloop()