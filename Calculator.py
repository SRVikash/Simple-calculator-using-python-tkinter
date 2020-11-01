from tkinter import *
root=Tk()
root.title('Simple Calculator')
root.configure(bg='#F0E68C')

e=Entry(root,width=35,borderwidth=10,bg='black',fg='white')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

label1=Label(root,text="Vikash's",bg='black',fg='white')
label2=Label(root,text="Calculator",bg='black',fg='white')

#function for calculating
def click(number):
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c)+str(number))
def clear():
    e.delete(0,END)
def add():
    num1=e.get()
    global n1
    global cal
    cal='sum'
    n1=int(num1)
    e.delete(0,END)
def subtract():
    num1=e.get()
    global n1
    global cal
    cal='difference'
    n1=int(num1)
    e.delete(0,END)
def multiply():
    num1=e.get()
    global n1
    global cal
    cal='product'
    n1=int(num1)
    e.delete(0,END)
def division():
    num1=e.get()
    global n1
    global cal
    cal='divide'
    n1=int(num1)
    e.delete(0,END)
def b_equal():
    num2=e.get()
    n2=int(num2)
    e.delete(0,END)
    if cal=='sum':
        e.insert(0,int(n1) + int(n2))
    if cal=='difference':
        e.insert(0,int(n1) - int(n2))
    if cal=='divide':
        e.insert(0,int(n1) / int(n2))
    if cal=='product':
        e.insert(0,int(n1) * int(n2))
#defining buttons
b1=Button(root,text='1',padx=40,pady=20,bg='black',fg='white',command=lambda:click(1))
b2=Button(root,text='2',padx=40,pady=20,bg='black',fg='white',command=lambda:click(2))
b3=Button(root,text='3',padx=49,pady=20,bg='black',fg='white',command=lambda:click(3))
b4=Button(root,text='4',padx=40,pady=20,bg='black',fg='white',command=lambda:click(4))
b5=Button(root,text='5',padx=40,pady=20,bg='black',fg='white',command=lambda:click(5))
b6=Button(root,text='6',padx=49,pady=20,bg='black',fg='white',command=lambda:click(6))
b7=Button(root,text='7',padx=40,pady=20,bg='black',fg='white',command=lambda:click(7))
b8=Button(root,text='8',padx=40,pady=20,bg='black',fg='white',command=lambda:click(8))
b9=Button(root,text='9',padx=49,pady=20,bg='black',fg='white',command=lambda:click(9))
b0=Button(root,text='0',padx=40,pady=22,bg='black',fg='white',command=lambda:click(0))
clear=Button(root,text='clear',padx=38,pady=20,bg='black',fg='red',command=clear)
add=Button(root,text='+',padx=39,pady=22,bg='black',fg='white',command=add)
sub=Button(root,text='-',padx=40,pady=25,bg='black',fg='white',command=subtract)
mul=Button(root,text='x',padx=40,pady=26,bg='black',fg='white',command=multiply)
div=Button(root,text='/',padx=40,pady=20,bg='black',fg='white',command=division)
equal=Button(root,text='=',padx=44,pady=29,bg='black',fg='blue',command=b_equal)

#placing buttons
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b0.grid(row=4,column=1)
add.grid(row=4,column=0)
clear.grid(row=4,column=2)

sub.grid(row=5,column=0)
mul.grid(row=5,column=1)
div.grid(row=6,column=0)

equal.grid(row=5,column=2)

label1.grid(row=6,column=1)
label2.grid(row=6,column=2)


root.mainloop()