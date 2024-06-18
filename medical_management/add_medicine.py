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
headlabel = Label(headframe,text='PCHYSIO THERAPY CLINIC -ADD MEDICINE',font=('arial',24),fg='white',bg='blue')

headlabel.grid(row=0,column=0)
#default ah center ku  than pokum

midframe = Frame(window, width=600, bd=1)
midframe.pack(side=TOP)

con = sqlite3.connect('medical.db')
cursor = con.cursor()  # cursor vechu than execute panna mudiyum
cursor.execute(""" create table if not exists 'medicine'
 (medicinename text,medicineid int,brandname text,chemicalcomponent text,mfgdate text,expdate text,price int)""")
con.commit()

medicinename = StringVar()
medicineid = IntVar()
brandname = StringVar()
chemicalcomponent = StringVar()
mfgdate = StringVar()
expdate = StringVar()
price = IntVar()
medicinename.set('')
medicineid.set('')
brandname.set('')
chemicalcomponent.set('')
mfgdate.set('')
expdate.set('')
price.set('')
medicinenamelabel = Label(midframe, text='MEDICINE NAME', font=('arial', 16), fg='white', bg='blue')
medicinenamelabel.grid(row=0, column=0, padx=10, pady=10)
medicinenametextbox = Entry(midframe, font=('arial', 16), textvariable=medicinename)
medicinenametextbox.grid(row=0, column=1, padx=10, pady=10)

medicineidlabel = Label(midframe, text='MEDICINE ID', font=('arial', 16), fg='white', bg='blue')
medicineidlabel.grid(row=2, column=0, padx=10, pady=10)
medicineidtextbox = Entry(midframe, font=('arial', 16), textvariable=medicineid)
medicineidtextbox.grid(row=2, column=1, padx=10, pady=10)

brandnamelabel = Label(midframe, text='BRAND NAME', font=('arial', 16), fg='white', bg='blue')
brandnamelabel.grid(row=3, column=0, padx=10, pady=10)
brandnametextbox = Entry(midframe, font=('arial', 16), textvariable=brandname)
brandnametextbox.grid(row=3, column=1, padx=10, pady=10)

chemicalcomponentlabel = Label(midframe, text='CHEMICAL COMPONENT', font=('arial', 16), fg='white', bg='blue')
chemicalcomponentlabel.grid(row=4, column=0, padx=10, pady=10)
chemicalcomponenttextbox = Entry(midframe, font=('arial', 16), textvariable=chemicalcomponent)
chemicalcomponenttextbox.grid(row=4, column=1, padx=10, pady=10)

mfgdatelabel = Label(midframe, text='MFG DATE', font=('arial', 16), fg='white', bg='blue')
mfgdatelabel.grid(row=5, column=0, padx=10, pady=10)
mfgdatetextbox = Entry(midframe, font=('arial', 16), textvariable=mfgdate)
mfgdatetextbox.grid(row=5, column=1, padx=10, pady=10)

expdatelabel = Label(midframe, text='EXP DATE', font=('arial', 16), fg='white', bg='blue')
expdatelabel.grid(row=6, column=0, padx=10, pady=10)
expdatetextbox = Entry(midframe, font=('arial', 16), textvariable=expdate)
expdatetextbox.grid(row=6, column=1, padx=10, pady=10)

pricelabel = Label(midframe, text='PRICE', font=('arial', 16), fg='white', bg='blue')
pricelabel.grid(row=7, column=0, padx=10, pady=10)
pricetextbox = Entry(midframe, font=('arial', 16), textvariable=price)
pricetextbox.grid(row=7, column=1, padx=10, pady=10)

def add():
    con = sqlite3.connect('medical.db')
    cursor = con.cursor()  # cursor vechu than execute panna mudiyum
    cursor.execute(""" insert into 'medicine'
    (medicinename ,medicineid ,brandname,chemicalcomponent ,mfgdate ,expdate,price)values(?,?,?,?,?,?,?)""", (
    str(medicinename.get()), str(medicineid.get()), str(brandname.get()), str(chemicalcomponent.get()), str(mfgdate.get()), str(expdate.get()), str(price.get())))
    con.commit()
    if cursor.rowcount > 0:
        msg.showinfo('ADD MEDICINE', 'New Medicine added', icon='info')
    else:
        msg.showinfo('Error', 'New Medicine not added', icon='waring')


def back():
    window.destroy()
    import home


add_btn = Button(midframe, text='ADD', command=add, font=('arial', 16), fg='white', bg='green')
add_btn.grid(row=8, column=1, padx=10, pady=10)

back_btn = Button(midframe, text='BACK', command=back, font=('arial', 16), fg='white', bg='Red')
back_btn.grid(row=9, column=1, padx=10, pady=10)

window.mainloop()
