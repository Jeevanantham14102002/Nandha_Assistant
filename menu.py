from tkinter import *
from tkinter import messagebox
w=Tk()
class men:
    w.title("Menu 1")
    w.geometry('500x300')
    l1=Label(w,text="Password:",fg='blue',font=('Arial',14))
    l1.grid(row=0,column=0,padx=5,pady=10)
    global data1
    data1=StringVar() 
    t1=Entry(w,textvariable=data1,fg='black',font=('Arial',14))
    t1.grid(row=0,column=1)
    l2=Label(w,text="Breakfast:",fg='blue',font=('Arial',14))
    l2.grid(row=1,column=0,padx=5,pady=10)
    global data2
    data2=StringVar() 
    global data3
    data3=StringVar() 
    global data4
    data4=StringVar() 
    t2=Entry(w,textvariable=data2,fg='black',font=('Arial',14))
    t2.grid(row=1,column=1)
    l3=Label(w,text="Lunch:",fg='blue',font=('Arial',14))
    l3.grid(row=2,column=0,padx=5,pady=10)
    t3=Entry(w,textvariable=data3,fg='black',font=('Arial',14))
    t3.grid(row=2,column=1)
    l3=Label(w,text="Snack Items:",fg='blue',font=('Arial',14))
    l3.grid(row=3,column=0,padx=5,pady=10)
    t3=Entry(w,textvariable=data4,fg='black',font=('Arial',14))
    t3.grid(row=3,column=1)

    def menu1():   
        if(data1.get()=="159"):
            global s1
            global r1
            global j1
            s=data2.get()
            f=open("breakfast.txt",'w')
            f.write(s)
            f.close()
            
            r=data3.get()
            f1=open("lunch.txt",'w')
            f1.write(r)
            f1.close()
            j=data4.get()
            f2=open("snack.txt",'w')
            f2.write(j)
            f2.close()
            w.destroy()
        
        else:
            messagebox.showinfo("warning","Please enter a correct password")
    def hide1():
          w.destroy()

    b1=Button(w,command=menu1,text="OK",fg='violet',font=('Arial',14))
    b1.grid(row=4,column=1)
    b2=Button(w,command=hide1,text="Cancel",fg='red',font=('Arial',14))
    b2.grid(row=4,column=2)
    def start():
        w.mainloop()
    


