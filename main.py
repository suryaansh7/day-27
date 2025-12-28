from tkinter import*

window=Tk()
window.title("miles to km converter")
window.minsize(width=500, height=300)



input1=Entry()
input1.grid(column=2,row=0)

label1=Label(text="miles",font=("arial",20,"bold"))
label1.grid(column=3, row=0)

label2=Label(text="is equal to",font=("arial",20,"bold"))
label2.grid(column=1, row=1)

text = Label()


text.grid(column=2,row=1)

label3=Label(text="km",font=("arial",20,"bold"))
label3.grid(column=3, row=1)

def calc():
    s=input1.get()
    print(type(s))
    k=float(s)
    print(type(k))
    k*= 1.609
    st=f"{k}"
    text.config(text=st)








but=Button(text="calculate", command=calc)
but.grid(column=2, row=2)




















window.mainloop()