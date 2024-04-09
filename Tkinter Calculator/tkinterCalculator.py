from tkinter import *
root=Tk()
root.title("Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)



def buttonclick(number):
    currentnum=e.get()
    e.delete(0,END)
    e.insert(0,str(currentnum)+str(number))

def buttonclear():
    e.delete(0,END)

def buttonadd():
    first=e.get()
    global fnum
    fnum=float(first)
    global operator
    operator = '+'
    e.delete(0,END)

def buttonsub():
    first=e.get()
    global fnum
    fnum=float(first)
    global operator
    operator = '-'
    e.delete(0,END)

def buttonmul():
    first=e.get()
    global fnum
    fnum=float(first)
    global operator
    operator = '*'
    e.delete(0,END)

def buttondiv():
    first=e.get()
    global fnum
    fnum=float(first)
    global operator
    operator = '/'
    e.delete(0,END)

def add(first, second):
    s = float(first)+float(second)
    return s

def subtract(first, second):
    s = float(first)-float(second)
    return s

def multiply(first, second):
    s = float(first)*float(second)
    return s

def divide(first, second):
    s = float(first)/float(second)
    return s

def buttonequalf():
    second=e.get()
    match operator:
        case '+':
            s = add(fnum, second)
        case '-':
            s = subtract(fnum, second)
        case '*':
            s = multiply(fnum, second)
        case '/':
            s = divide(fnum, second)
    e.delete(0,END)
    e.insert(0,f"{s}")


button1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonclick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonclick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonclick(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonclick(0))
buttondot=Button(root,text=".",padx=40,pady=20,command=lambda:buttonclick('.'))
buttonplus=Button(root,text="+",padx=20,pady=20,command=buttonadd)
buttonminus=Button(root,text="-",padx=20,pady=20,command=buttonsub)
buttondivide=Button(root,text="/",padx=20,pady=20,command=buttondiv)
buttonmultiply=Button(root,text="x",padx=20,pady=20,command=buttonmul)
buttonequal=Button(root,text="=",padx=40,pady=20,command=buttonequalf)
buttonclq=Button(root,text="Clear",padx=140,pady=20,command=buttonclear)






button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
buttonplus.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonminus.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonmultiply.grid(row=3,column=3)

buttondot.grid(row=4,column=0)
button0.grid(row=4,column=1)
buttonequal.grid(row=4,column=2)
buttondivide.grid(row=4,column=3)

buttonclq.grid(row=5,column=0,columnspan=4)

root.mainloop()