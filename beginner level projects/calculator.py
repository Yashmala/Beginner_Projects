from tkinter import *
root=Tk()
#root.frame()
root.title("calculator")
root.geometry("600x200")
e = Entry(root,font=(" Times new Roman",34))
e.grid(row=4,column=5)
#widgets
mylabel=Label(root,text=" hello world")


def myclick():
    mylabel2=Label(root,text=" clicked on button")
    mylabel2.grid(row=1,column=2,padx=50,pady=20)


mylabel1=Label(root,text=" GRID ")
mylabel.grid(row=1,column=2,padx=50,pady=50)

myButton=Button(root,text=" click",command=myclick) 
myButton.grid(row=1,column=2,padx=50,pady=20)
mylabel1.grid(row=5,column=2)
#mylabel.pack()
#mylabel1.pack() # we can use only one between place,grid and pack 
#mylabel2.pack()

root.mainloop()# main loop is used so that screenn will continously seems to appear otherwise it will vainsh i.e it will come and go