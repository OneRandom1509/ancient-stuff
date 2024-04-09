from tkinter import *
from links import Linkopener as Link

win=Tk()
win.title("Notion Notes")

#happytext
label=Label(win,text="Welcome to your one stop notion notes!\nJust click any subject you want and it will take you right to your notes!",justify=CENTER,bd=2,relief="solid")

#buttons
chem=Button(win,text="Chemistry",height=2,width=12,command=Link.openchem)
phy=Button(win,text="Physics",height=2,width=12,command=Link.openphy)
maths=Button(win,text="Maths",height=2,width=12,command=Link.openmaths)

#grids
label.grid(column=0,row=0,columnspan=3)
chem.grid(row=2,column=0)
phy.grid(row=2,column=1)
maths.grid(row=2,column=2)

win.mainloop()