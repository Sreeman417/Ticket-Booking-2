from customtkinter import *
class eye1():
    def __init__(self,frame,hidden_eye_icon,eye_icon,var,x,y):
        self.button4 = CTkButton(frame,image=hidden_eye_icon,text="",fg_color="white",width=26,
                                 height=26,hover_color="white",command = lambda:eye1.checker2(self,hidden_eye_icon,eye_icon,var,x,y))
        self.button4.place(relx = x,rely = y)
    def checker2(self,hidden_eye_icon,eye_icon,var,x,y):
        self.button4.configure(image=eye_icon,command = lambda:eye1.checker3(self,hidden_eye_icon,eye_icon,var,x,y))
        eye1.checker4(self,"show",var)
        self.button4.place(relx = x,rely = y)
    def checker3(self,hidden_eye_icon,eye_icon,var,x,y):
        self.button4.configure(image=hidden_eye_icon,command =lambda: eye1.checker2(self,hidden_eye_icon,eye_icon,var,x,y))
        eye1.checker4(self,"hidden",var)
        self.button4.place(relx=x,rely= y)
    def checker4(self,s,var):
        if s == "show":
            var.configure(show="")
        if s == "hidden":
            var.configure(show="*")
    def payment(self,root):
            self.payf = CTkToplevel(root)
            self.payf.geometry("350x500")
            self.payf.wm_attributes("-topmost",True)
            self.payf.title("Payment")
            self.mlabel = CTkLabel(self.payf,text= "PAYMENT",font = ("bold",30),text_color="white")
            self.mlabel.place(relx = 0.35,rely = 0.1)
            self.cvv =CTkEntry(self.payf,text_color="black",placeholder_text="Cvv",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.card = CTkEntry(self.payf,text_color="black",placeholder_text="Card number",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.card.place(relx = 0.1,rely =0.3)
            self.cvv.place(relx = 0.1,rely = 0.6)
            self.payb = CTkButton(self.payf,text="Pay",height=10,width = 30)
