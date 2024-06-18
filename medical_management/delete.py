import sqlite3
from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

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
headlabel = Label(headframe,text='PCHYSIO THERAPY CLINIC -DELETE MEDICINE',font=('arial',24),fg='white',bg='blue')

headlabel.grid(row=0,column=0)
#default ah center ku  than pokum

midframe = Frame(window, width=700, bd=1)
midframe.pack(side=TOP)

medicinename =StringVar()
medicinename.set('')

medicinenamelabel = Label(midframe, text='MEDICINE NAME', font=('arial', 16), fg='white', bg='blue')
medicinenamelabel.grid(row=1, column=0, padx=10, pady=10)
medicinenametextbox = Entry(midframe, font=('arial', 16), textvariable=medicinename)
medicinenametextbox.grid(row=1, column=1, padx=10, pady=10)

view_frame = Frame(window,bd=1)
view_frame.pack(side=TOP,fill=X)
tv = ttk.Treeview(view_frame,
                  columns=('medicinename','medicineid','brandname','chemicalcomponent','mfgdate','expdate','price'))
tv.heading('#1',text='MedicineName')
tv.heading('#2',text='MedicineId')
tv.heading('#3',text='BrandName')
tv.heading('#4',text='ChemicalCom')
tv.heading('#5',text='MfgDate')
tv.heading('#6',text='ExpDate')
tv.heading('#7',text='Price')

tv.column('#0',width=0,stretch=NO)
tv.column('#1',width=0)
tv.column('#2',width=0)
tv.column('#3',width=0)
tv.column('#4',width=0)
tv.column('#5',width=0)
tv.column('#6',width=0)
tv.column('#7',width=0)



tv.pack(fill=X)
def view():
    con = sqlite3.connect('medical.db')
    cursor = con.cursor()
    cursor.execute("select * from 'medicine'")
    data = cursor.fetchall()
    for i in data:
        tv.insert("",END,values=i)
        break

    con.commit()

def back():
    window.destroy()
    import home

def delete():

    con = sqlite3.connect('medical.db')
    cursor = con.cursor()
    medname = str(medicinename.get())
    cursor.execute("delete from 'medicine' Where medicinename = ?",(medname,))
    print(cursor.rowcount)
    if cursor.rowcount > 0:
        msg.showinfo('DELETED', 'Medicine deleted successfully', icon='info')
    else:
        msg.showinfo('NOT DELETED', 'Medicine not Deleted', icon='warning')
    cursor.close()
    con.commit()

back_btn = Button(midframe,text='BACK',command=back, font=('arial', 16), fg='white', bg='blue')
back_btn.grid(row=2, column=1, padx=10, pady=10)


delete_btn = Button(midframe,text='DELETE',command=delete, font=('arial', 16), fg='white', bg='blue')
delete_btn.grid(row=1, column=2, padx=10, pady=10)

view_btn = Button(midframe,text='VIEW',command=view, font=('arial', 16), fg='white', bg='blue')
view_btn.grid(row=1, column=3, padx=10, pady=10)



window.mainloop()