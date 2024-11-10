from tkinter import *
win=Tk()
win.geometry('600x500')

# Widget====================
lbl_fname = Label(win,text='Fname',font=' 15 ').place(x=80,y=50)


lbl_Lname = Label(win,text='Lname',font=' 15 ').place(x=80,y=125)


lbl_Email = Label(win,text='Email',font=' 15 ').place(x=80,y=200)


lbl_password = Label(win,text='password',font=' 15 ').place(x=80,y=275)

ent_f = Entry(win,font=' 15 ',width=25)
ent_f.place(x=220,y=53)


ent_l = Entry(win,font=' 15 ',width=25)
ent_l.place(x=220,y=128)


ent_e = Entry(win,font=' 15 ',width=25)
ent_e.place(x=220,y=203)


ent_p = Entry(win,font=' 15 ',width=25)
ent_p.place(x=220,y=278)


btn_sing_up = Button(win,text='sing up',font=' 15')
btn_sing_up.place(x=250,y=350)

btn_sing_in = Button(win,text='sing in',font=' 15')
btn_sing_in.place(x=400,y=350)
win.mainloop()
