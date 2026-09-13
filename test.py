"""from customtkinter import *
def on_enter(event):
    # put whatever you want to do 'on hover' into this function
    print('Button hovered!')


def on_leave(event):
    print(event)  # do something here

parent = CTk()
button = CTkButton(parent, text='Button!')
# use '+' to avoid overwriting the existing binding
button.bind('<Enter>', on_enter, add='+')
# you may also want to bind to '<Leave>' to complete the hover handler
button.bind("<Leave>", on_leave, add='+')
button.pack()
parent.mainloop()"""
import pickle
#with open("tickets.dat","wb") as f:
#    pass
with open("tickets.dat","rb") as f:
    while True:
        try:
            s = pickle.load(f)
            print(s)
        except:
            break
with open("remem.dat","rb") as f:
    while True:
        try:
            s = pickle.load(f)
            print(s)
        except:
            break
"""with open("remem.dat","wb") as f:
    pass"""