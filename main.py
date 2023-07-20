from tkinter import *
import time

clk = Tk()
clk.title("Saat")
clk.geometry("250x120+0+0")  # Pencere boyutunu 250x100 piksel olarak ayarlıyoruz
clk.config(bg="#0C1E28")

def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))

    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    lb_hr.after(200, clock)

lb_hr = Label(clk, text="12", font=("Times 20 bold", 40, 'bold'), bg="#087587", fg="white")
lb_hr.place(x=30, y=25, width=60, height=60)

lb_hr_text = Label(clk, text="SAAT", font=("Times 12 bold", 12, 'bold'), bg="#087587", fg="white")
lb_hr_text.place(x=30, y=90, width=60, height=15)

lb_mn = Label(clk, text="12", font=("Times 20 bold", 40, 'bold'), bg="#008EA4", fg="white")
lb_mn.place(x=100, y=25, width=60, height=60)

lb_mn_text = Label(clk, text="DAKİKA", font=("Times 12 bold", 12, 'bold'), bg="#008EA4", fg="white")
lb_mn_text.place(x=100, y=90, width=60, height=15)

lb_sc = Label(clk, text="12", font=("Times 20 bold", 40, 'bold'), bg="#06B4BB", fg="white")
lb_sc.place(x=170, y=25, width=60, height=60)

lb_sc_text = Label(clk, text="SANİYE", font=("Times 12 bold", 12, 'bold'), bg="#06B4BB", fg="white")
lb_sc_text.place(x=170, y=90, width=60, height=15)

clock()
clk.mainloop()
