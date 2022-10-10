from tkinter import *
t =Tk()
def add():
    e1.insert(END, "+")
def sub():
    e1.insert(END, "-")
def mul():
    e1.insert(END, "*")
def div():
    e1.insert(END, "/")



def calculate():

    l.config(text =f"ANSWER IS: {eval(e1.get())}", fg="green")









t.geometry("200x340")
f =Frame(t, borderwidth=2, bg="black")
f.pack()
b1 =Button(f, text="+", padx=12,pady=10, bg="black", command =add, fg="white", font=("Times", "40", "bold italic"))
b1.grid()
b2 =Button(f, text="-", padx=12,pady=10, bg="black",command=sub, fg="white", font=("Times", "40", "bold italic"))
b2.grid(row =0, column=1)
b3 =Button(f, text="x", padx=14,pady=10, bg="black",command=mul, fg="white", font=("Times", "40", "bold italic"))
b3.grid(row =1, column=0)
b4 =Button(f, text="/", padx=12,pady=10, bg="black",command=div, fg="white", font=("Times", "40", "bold italic"))
b4.grid(row =1, column=1)
f2 =Frame(t, borderwidth=2, bg="green")
f2.pack(padx=2)

e1 =Entry(f2,width=30)
e1.pack()
s =Button(t, text="SUBMIT", activeforeground="green", activebackground="black", command=calculate)
s.pack(pady=10)










l =Label(t, text="ENTER NUMBERS", fg="green")
l.pack()
t.mainloop()