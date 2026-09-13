from customtkinter import *
import csv
from PIL import Image,ImageTk
from Classes import eye1
import pickle as p
import smtplib
import random
class app(CTk):
    def __init__(self,nam = False):
        with open("remem.dat","ab") as f:
            pass
        with open("accounts.csv","a") as f:
            pass
        super().__init__()
        global l
        global email_l
        global phone_l
        self.some = False
        self.profile_out = False
        self.tickets = []
        self.lmo = []
        temp = []
        email_l = []
        phone_l = []
        with open("tickets.dat","a") as f:
            pass
        file = open("accounts.csv","r")
        myreader = csv.reader(file)
        for i in myreader:
            temp.append(i)
        file.close()
        l = {}
        for i in temp:
            if i == []:
                continue
            l[i[0]]= [i[1],i[2],i[3]]
            email_l.append(i[2])
            phone_l.append(i[3])
        self.time = 0
        self.i = 0.5
        self.j=1
        self.k = 0.5
        self.n=0
        self.b = 0.15
        self.t = 0.35
        self.o = 1
        self.boat = CTkImage(Image.open("boatpost.jpg"),size=(220,400))
        self.saripodha = CTkImage(Image.open("saripodhpost.png"),size=(220,400))
        self.mai = CTkImage(Image.open("maipost.jpg"),size=(220,400))
        self.devara = CTkImage(Image.open("devarapost.png"),size=(220,400))
        self.indian2 = CTkImage(Image.open("indian2post.jpg"),size=(220,400))
        self.pechi = CTkImage(Image.open("pechipost.jpg"),size=(220,400))
        self.goat = CTkImage(Image.open("goatpost.jpg"),size=(220,400))
        self.raayan = CTkImage(Image.open("raayanpost.png"),size=(220,400))
        self.out_img = CTkImage(Image.open("play.png"),size=(25,25))
        self.credit = CTkImage(Image.open("credit.png"),size=(25,25))
        self.cvv = CTkImage(Image.open("cvv.png"),size=(25,25))
        self.in_img = CTkImage(Image.open("play1.png"),size=(25,25))
        self.phone_img = CTkImage(Image.open("phone-call.png"),size=(25,25))
        self.email_img = CTkImage(Image.open("email.png"),size=(25,25))
        self.leftarrow_img = CTkImage(Image.open("leftarrow.png"),size=(20,20))
        self.account_icon_img = CTkImage(Image.open("account icon.png"),size=(25,25))
        self.padlock_img = CTkImage(Image.open("padlock.png"),size = (25,25))
        self.account_profile_img = CTkImage(Image.open("account profile.png"),size=(50,50))
        self.eye_icon = CTkImage(Image.open("eye.png"),size=(25,25))
        self.hidden_eye_icon = CTkImage(Image.open("hidden.png"),size=(25,25))
        self.img1 = CTkImage(Image.open("theatre.jpg"),size=(900,650))
        self.cinema = CTkImage(Image.open("cinema.png"),size=(20,20))
        self.imagelabel_1 = CTkLabel(self,image=self.img1,text="")
        self.title("Login")
        set_appearance_mode("system")
        set_default_color_theme("dark-blue")
        self.geometry("900x650")
        self.resizable(False,False)
        self.frame = CTkFrame(self,width = 340,height = 380,fg_color="white")
        self.frame2 = CTkFrame(self,width = 100,height = 60,fg_color="white")
        self.frame3 = CTkFrame(self,width = 100,height = 60,fg_color="white",corner_radius=5)
        self.l2 = CTkLabel(self.frame,text= "𝖫𝗈𝗀𝗂𝗇",font = ("Century Gothic",30),text_color="black")
        self.poplabel = CTkLabel(self.frame2,text = "Created",height=20,width = 80,text_color="black",bg_color="white",fg_color="white",font = ("bold",20))
        self.poplabel2 = CTkLabel(self.frame3,text = "Created",height=20,width = 80,text_color="black",bg_color="white",fg_color="white",font = ("bold",20))
        self.closeb = CTkButton(self.frame2,text="Close",height=10,width = 30,command = lambda:app.checkofclose(self))
        self.closeb2 = CTkButton(self.frame3,text="Close",height=10,width = 30,command = lambda:app.checkofclose2(self,0.88))
        self.phonecall = CTkLabel(self.frame,image = self.phone_img,text="")
        self.email1 = CTkLabel(self.frame,image = self.email_img,text="")
        self.e1 = CTkEntry(self.frame,text_color="black",placeholder_text="Username",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
        self.e2 = CTkEntry(self.frame,text_color="black",show = "*",placeholder_text="Password",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
        self.account_icon = CTkLabel(self.frame,image = self.account_icon_img,text="")
        self.left_label = CTkButton(self.frame,image = self.leftarrow_img,text_color="black",text="Back",font = ("bold",20),width= 13,height= 13,hover_color="white",fg_color="white",command=lambda:app.loginpage(self))
        self.account_profile = CTkLabel(self.frame,image= self.account_profile_img,text = "")
        self.padlock_icon = CTkLabel(self.frame,image = self.padlock_img,text ="")
        self.back_label = CTkLabel(self.frame,text = "Back",text_color="black",bg_color="white",fg_color="white",font = ("bold",20))
        self.button1 = CTkButton(self.frame,text="Forgot Password",cursor = "hand2",text_color="blue",fg_color="transparent",height = 5,hover_color="white",command=lambda:app.forgotpassword(self))
        self.button2 = CTkButton(self.frame,text="𝖫𝗈𝗀𝗂𝗇",width = 220,corner_radius=5,command=lambda: app.checker1(self))
        self.label_noaccount = CTkLabel(self.frame,text = "No account?",text_color="black",bg_color="white",fg_color="white")
        self.button3 = CTkButton(self.frame,text="Create an account",text_color="blue",fg_color="white",hover_color="white",width=20,cursor = "hand2",command= lambda:app.createanacc(self))
        self.label_nomovie = CTkLabel(self.frame,text = "No movie entered",corner_radius=5,text_color="red",font=("century gothic",12))
        self.button4 = CTkButton(self.frame,image=self.hidden_eye_icon,text="",fg_color="white",width=26,height=26,hover_color="white")
        self.terms = CTkCheckBox(self.frame,text = "Terms and condition",corner_radius=5,text_color="blue",font=("century gothic",12),checkbox_height=20,checkbox_width=20,hover=False,offvalue=False,onvalue=True,fg_color="black")
        self.sign = CTkCheckBox(self.frame,text = "Remember me",corner_radius=5,text_color="blue",font=("century gothic",12),checkbox_height=20,checkbox_width=20,hover=False,offvalue=False,onvalue=True,fg_color="black")
        if nam:
            app.mainpage(self,nam)
            self.mainloop()
        else:
            self.imagelabel_1.pack()            
            self.frame.place(relx = self.i , rely= 0.5,anchor = "center")
            self.l2.place(relx = 0.15,rely = 0.1)
            self.poplabel.place(relx = 0.1,rely = 0.05)
            self.poplabel2.place(relx = 0.1,rely = 0.05)
            self.closeb.place(relx = 0.3,rely = 0.6)
            self.closeb2.place(relx = 0.3,rely = 0.6)
            self.e1.place(relx = 0.15,rely = 0.3)
            self.e2.place(relx = 0.15,rely=0.4)
            self.account_icon.place(relx=0.05,rely=0.3)
            self.account_profile.place(relx=0.35,rely=0.075)
            self.padlock_icon.place(relx = 0.05,rely = 0.4)
            self.button2.place(relx = 0.15,rely = 0.6)
            self.label_noaccount.place(relx = 0.27,rely=0.68)
            self.button3.place(relx=0.48,rely=0.68)
            eye1(self.frame,self.hidden_eye_icon,self.eye_icon,var = self.e2,x=0.8,y=0.393)
            self.sign.place(relx =0.1,rely = 0.9)
            self.frame3.place(relx = 1,rely = 0.88)
            self.mainloop()
    def loginpage(self):
        for i in self.winfo_children():
            i.place_forget()
        for i in self.frame.winfo_children():
            i.place_forget()
        global l
        temp = []
        file = open("accounts.csv","r")
        myreader = csv.reader(file)
        for i in myreader:
            temp.append(i)
        file.close()
        l = {}
        for i in temp:
            if i == []:
                continue
            l[i[0]]= [i[1],i[2],[3]]
        self.out_img = CTkImage(Image.open("play.png"),size=(25,25))
        self.in_img = CTkImage(Image.open("play1.png"),size=(25,25))
        self.phone_img = CTkImage(Image.open("phone-call.png"),size=(25,25))
        self.email_img = CTkImage(Image.open("email.png"),size=(25,25))
        self.leftarrow_img = CTkImage(Image.open("leftarrow.png"),size=(20,20))
        self.account_icon_img = CTkImage(Image.open("account icon.png"),size=(25,25))
        self.padlock_img = CTkImage(Image.open("padlock.png"),size = (25,25))
        self.account_profile_img = CTkImage(Image.open("account profile.png"),size=(50,50))
        self.eye_icon = CTkImage(Image.open("eye.png"),size=(25,25))
        self.hidden_eye_icon = CTkImage(Image.open("hidden.png"),size=(25,25))
        self.img1 = ImageTk.PhotoImage(Image.open("theatre.jpg"))
        self.imagelabel_1 = CTkLabel(self,image=self.img1,text="")
        self.imagelabel_1.pack()
        self.title("Login")
        set_appearance_mode("system")
        set_default_color_theme("dark-blue")
        self.geometry("900x650")
        self.frame = CTkFrame(self,width = 340,height = 380,fg_color="white")
        self.frame2 = CTkFrame(self,width = 100,height = 60,fg_color="white")
        self.frame3 = CTkFrame(self,width = 100,height = 60,fg_color="white")
        self.frame.place(relx = self.i , rely= 0.5,anchor = "center")
        self.l2 = CTkLabel(self.frame,text= "𝖫𝗈𝗀𝗂𝗇",font = ("Century Gothic",30),text_color="black")
        self.l2.place(relx = 0.15,rely = 0.1)
        self.poplabel = CTkLabel(self.frame2,text = "Created",height=20,width = 80,text_color="black",bg_color="white",fg_color="white",font = ("bold",20))
        self.poplabel.place(relx = 0.1,rely = 0.05)
        self.closeb = CTkButton(self.frame2,text="Close",height=10,width = 30,command = lambda:app.checkofclose(self))
        self.closeb.place(relx = 0.3,rely = 0.6)
        self.closeb2 = CTkButton(self.frame3,text="Close",height=10,width = 30,command = lambda:app.checkofclose2(self,0.88))
        self.closeb2.place(relx = 0.3,rely = 0.6)
        self.phonecall = CTkLabel(self.frame,image = self.phone_img,text="")
        self.email1 = CTkLabel(self.frame,image = self.email_img,text="")
        self.e1 = CTkEntry(self.frame,text_color="black",placeholder_text="Username",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
        self.e1.place(relx = 0.15,rely = 0.3)
        self.e2 = CTkEntry(self.frame,text_color="black",show = "*",placeholder_text="Password",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
        self.e2.place(relx = 0.15,rely=0.4)
        self.poplabel2 = CTkLabel(self.frame3,text = "Created",height=20,width = 80,text_color="black",bg_color="white",fg_color="white",font = ("bold",20))
        self.poplabel2.place(relx = 0.1,rely = 0.05)
        self.account_icon = CTkLabel(self.frame,image = self.account_icon_img,text="")
        self.left_label = CTkButton(self.frame,image = self.leftarrow_img,text_color="black",text="Back",font = ("bold",20),width= 13,height= 13,hover_color="white",fg_color="white",command=lambda:app.loginpage(self))
        self.account_icon.place(relx=0.05,rely=0.3)
        self.account_profile = CTkLabel(self.frame,image= self.account_profile_img,text = "")
        self.account_profile.place(relx=0.35,rely=0.075)
        self.padlock_icon = CTkLabel(self.frame,image = self.padlock_img,text ="")
        self.padlock_icon.place(relx = 0.05,rely = 0.4)
        self.back_label = CTkLabel(self.frame,text = "Back",text_color="black",bg_color="white",fg_color="white",font = ("bold",20))
        self.button1 = CTkButton(self.frame,text="Forgot Password",cursor = "hand2",text_color="blue",fg_color="transparent",height = 5,hover_color="white",command=lambda:app.forgotpassword(self))
        self.button2 = CTkButton(self.frame,text="𝖫𝗈𝗀𝗂𝗇",width = 220,corner_radius=5,command=lambda: app.checker1(self))
        self.button2.place(relx = 0.15,rely = 0.6)
        self.label_noaccount = CTkLabel(self.frame,text = "No account?",text_color="black",bg_color="white",fg_color="white")
        self.label_noaccount.place(relx = 0.27,rely=0.68)
        self.button3 = CTkButton(self.frame,text="Create an account",text_color="blue",fg_color="white",hover_color="white",width=20,cursor = "hand2",command= lambda:app.createanacc(self))
        self.button3.place(relx=0.48,rely=0.68)
        self.label_nomovie = CTkLabel(self.frame,text = "No movie entered",corner_radius=5,text_color="red",font=("century gothic",12))
        self.button4 = CTkButton(self.frame,image=self.hidden_eye_icon,text="",fg_color="white",width=26,height=26,hover_color="white")
        self.terms = CTkCheckBox(self.frame,text = "Terms and condition",corner_radius=5,text_color="blue",font=("century gothic",12),checkbox_height=20,checkbox_width=20,hover=False,offvalue=False,onvalue=True,fg_color="black")
        self.sign = CTkCheckBox(self.frame,text = "Remember me",corner_radius=5,text_color="blue",font=("century gothic",12),checkbox_height=20,checkbox_width=20,hover=False,offvalue=False,onvalue=True,fg_color="black")
        eye1(self.frame,self.hidden_eye_icon,self.eye_icon,var = self.e2,x=0.8,y=0.393)
        self.sign.place(relx =0.1,rely = 0.9)
        self.frame3.place(relx = 1,rely = 0.88)
    def popup(self,msg,y=0.05):
        if self.o>0.85:
            self.poplabel.configure(text = msg)
            self.frame2.place(relx = self.o,rely = 0.05)
            self.o-=0.001
            self.after(1,lambda:app.popup(self,msg,0.05))
        self.some = True
    def popup2(self,msg,y=0.88):
        if self.o>0.85:
            self.poplabel2.configure(text = msg)
            self.frame3.place(relx = self.o,rely = 0.88)
            self.o-=0.001
            self.after(1,lambda:app.popup2(self,msg,0.88))
    def vibrating(self,widget,x,y):
        self.n+=1
        if self.n < 31:
            if self.i >0.499:
                widget.place(relx=self.i,rely=y)
                self.i-=0.005
                self.after(10,lambda:app.vibrating(self,widget,x,y))
            elif self.i < 0.501:
                widget.place(relx=self.i,rely = 0.5)
                self.i+=0.005
                self.after(10,lambda:app.vibrating(self,widget,x,y))
        else:
            widget.place_configure(relx = x)
            self.n=1
    """def vibrating(self):
        self.n+=1
        if self.n < 31:
            if self.i >0.499:
                self.frame.place(relx=self.i,rely=0.5)
                self.i-=0.005
                self.after(10,lambda:app.vibrating(self,self.frame,0.5,0.5))
            elif self.i < 0.501:
                self.frame.place(relx=self.i,rely = 0.5)
                self.i+=0.005
                self.after(10,lambda:app.vibrating(self,self.frame,0.5,0.5))
        else:
            self.frame.place_configure(relx = 0.5)
            self.n=1"""
    def checkofclose(self,y=0.05):
        if self.o<1.05:
            self.frame2.place(relx = self.o,rely = 0.05)
            self.o+=0.001
            self.after(1,lambda:app.checkofclose(self,0.05))
        self.some = False
    def checkofclose2(self,y=0.88):
        if self.o<1.05:
            self.frame3.place(relx = self.o,rely = 0.88)
            self.o+=0.001
            self.after(1,lambda:app.checkofclose2(self,0.88))
    def checker1(self):
        global l
        temp = []
        file = open("accounts.csv","r")
        myreader = csv.reader(file)
        for i in myreader:
            temp.append(i)
        file.close()
        l = {}
        for i in temp:
            if i == []:
                continue
            l[i[0]]= [i[1],i[2],i[3]]
            email_l.append(i[2])
            phone_l.append(i[3])
        if self.e1.get().isspace() or self.e1.get() == "":
            self.button2.place(relx = 0.15,rely = 0.65)
            self.label_nomovie.configure(text = "Enter any username")
            self.label_nomovie.place(relx=0.32,rely=0.5)
            self.button1.place_forget()
            self.label_noaccount.place(relx = 0.273,rely=0.78)
            self.button3.place(relx=0.48,rely=0.78)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.e1.get().isspace()or self.e1.get()=="") and self.e1.get() not in l.keys():
            self.button2.place(relx = 0.15,rely = 0.65)
            self.label_nomovie.configure(text = "No username found")
            self.label_nomovie.place(relx=0.32,rely=0.5)
            self.button1.place_forget()
            self.label_noaccount.place(relx = 0.273,rely=0.78)
            self.button3.place(relx=0.48,rely=0.78)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.e1.get() in l.keys() and (self.e2.get().isspace() or self.e2.get()==""):
            self.button2.place(relx = 0.15,rely = 0.7)
            self.label_nomovie.configure(text = "Invalid password")
            self.label_nomovie.place(relx=0.32,rely=0.5)
            self.button1.place(relx=0.45,rely = 0.6)
            self.label_noaccount.place(relx = 0.273,rely=0.78)
            self.button3.place(relx=0.48,rely=0.78)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.e1.get() not in l.keys():
            self.button2.place(relx = 0.15,rely = 0.65)
            self.label_nomovie.configure(text = "Username not found")
            self.label_nomovie.place(relx=0.32,rely=0.5)
            self.button1.place_forget()
            self.label_noaccount.place(relx = 0.273,rely=0.78)
            self.button3.place(relx=0.48,rely=0.78)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.e1.get() in l.keys() and str(self.e2.get()) != str(l[self.e1.get()][0]):
            self.button2.place(relx = 0.15,rely = 0.7)
            self.label_nomovie.configure(text = "Invalid password")
            self.label_nomovie.place(relx=0.32,rely=0.5)
            self.button1.place(relx=0.45,rely = 0.6)
            self.label_noaccount.place(relx = 0.273,rely=0.78)
            self.button3.place(relx=0.48,rely=0.78)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.e1.get() in l.keys() and str(self.e2.get()) == str(l[self.e1.get()][0]):  
            """self.button2.place(relx = 0.15,rely = 0.6)
            self.label_nomovie.configure(text="")
            self.label_nomovie.place(relx = 0.32,rely =0.5 )
            self.button1.place_forget()
            self.label_noaccount.place(relx = 0.273,rely=0.68)
            self.button3.place(relx=0.48,rely=0.68)"""
            self.frame.place_forget()
            jj=[]
            if self.sign.get():
                with open("remem.dat","ab") as f:
                    p.dump([self.e1.get()],f)
            ###########################################
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("<your mail id which will send otp>", "<add your mail key for the mail id that sends otp>")
            message = "Your account got logged in"
            s.sendmail("<your mail id which will send otp>", str(l[self.e1.get()][1]), message)
            s.quit()
            app.mainpage(self,self.e1.get())
    def framemover(self):
        if self.k>-1:
            self.frame.place_configure(relx = self.k)
            self.k-=0.001
            self.after(1,lambda:app.framemover(self))

    def forgotpassword(self):
        if self.e1.get()=="":
            self.button2.place(relx = 0.15,rely = 0.75)
            self.label_nomovie.configure(text = "Enter username")
            self.label_nomovie.place(relx=0.32,rely=0.5)
            self.button1.place(relx=0.45,rely = 0.6)
            self.label_noaccount.place(relx = 0.273,rely=0.9)
            self.button3.place(relx=0.48,rely=0.9)
            app.vibrating(self,self.frame,0.5,0.5)
        else:
            for i in self.frame.winfo_children():
                i.place_forget()
            self.reset_password_title = CTkLabel(self.frame,text= "𝖱𝖾𝗌𝖾𝗍 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽",font = ("Century Gothic",30),text_color="black")
            self.username = CTkEntry(self.frame,text_color="black",placeholder_text="OTP",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.newpassword = CTkEntry(self.frame,text_color="black",show = "*",placeholder_text="New password",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.newpassword.place(relx = 0.15,rely = 0.4)
            self.phonecall.place(relx = 0.05,rely = 0.3)
            self.padlock_icon.place(relx = 0.05,rely = 0.4)
            self.reset_password_title.place(relx = 0.15,rely = 0.1)
            self.username.place(relx = 0.15,rely = 0.3)
            self.left_label.place(relx =0.02,rely = 0.9)
            self.invalid = CTkLabel(self.frame,text = "Enter vaild mail",corner_radius=5,text_color="red",font=("century gothic",12))
            self.reset = CTkButton(self.frame,text="Reset",width = 220,corner_radius=5,command=lambda:app.checker5(self))
            self.reset.place(relx = 0.15,rely=0.6)
            eye1(self.frame,self.hidden_eye_icon,self.eye_icon,var = self.newpassword,x = 0.8,y = 0.393)
            global jam
            jam =self.e1.get()
            global number
            number = random.randrange(1000,10000)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("<your mail id which will send otp>", "<add your mail key for the mail id that sends otp>")
            message = "Your account got logged in"
            s.sendmail("<your mail id which will send otp>", str(l[self.e1.get()][1]), message)
            s.quit()
    def checker5(self):
        global username
        global newpassword
        newpassword = self.newpassword.get()
        username = self.username.get()
        self.u = True
        for i in self.newpassword.get():
            if i.isalnum() == True:
                self.u = False
            elif i.isalnum() == False:
                self.u = True
                break
        """"if len(self.username.get())!=10:
            self.invalid.destroy()
            self.invalid = CTkLabel(self.frame,text = "Enter valid number",corner_radius=5,text_color="red",font=("century gothic",12))
            self.invalid.place(relx = 0.32,rely = 0.5)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.username.get() != str(l[self.e1.get()][2]):
            self.invalid.destroy()
            self.invalid = CTkLabel(self.frame,text = "Phone doesnt match",corner_radius=5,text_color="red",font=("century gothic",12))
            self.invalid.place(relx = 0.28,rely = 0.5)
            app.vibrating(self,self.frame,0.5,0.5)"""
        if str(number) != str(self.username.get()):
            self.invalid.destroy()
            self.invalid = CTkLabel(self.frame,text = "Wrong OTP",corner_radius=5,text_color="red",font=("century gothic",12))
            self.invalid.place(relx = 0.35,rely = 0.5)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.newpassword.get().isspace() or self.newpassword.get() == "":
            self.invalid.destroy()
            self.invalid = CTkLabel(self.frame,text = "Enter vaild password",corner_radius=5,text_color="red",font=("century gothic",12))
            self.invalid.place(relx = 0.3,rely = 0.5)
            app.vibrating(self,self.frame,0.5,0.5)
        elif len(str(self.newpassword.get()))<4:
            self.invalid.destroy()
            self.invalid = CTkLabel(self.frame,text = "Enter more atleast 4 characters",corner_radius=5,text_color="red",font=("century gothic",12))
            self.invalid.place(relx = 0.2,rely = 0.5)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.u == False:
            self.invalid.destroy()
            self.invalid = CTkLabel(self.frame,text = "Password must contain atleast 1 special character",corner_radius=5,text_color="red",font=("century gothic",12))
            self.invalid.place(relx = 0.08,rely = 0.5)
            app.vibrating(self,self.frame,0.5,0.5)
            """"number = random.randrange(1000,10000)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("ticketbooking757@gmail.com", "fqmv xakm fxpy qayn")
            message = str(number)
            s.sendmail("ticketbooking757@gmail.com", str(l[self.e1.get()][1]), message)
            s.quit()"""
        else:
            self.invalid.place_forget()
            for i in self.frame.winfo_children():
                i.destroy()
            file = open("accounts.csv","r",newline="")
            myreader = csv.reader(file)
            g=[]
            for i in myreader:
                if i != []:
                    if str(i[0]) == str(jam):
                        g.append([i[0],str(newpassword),i[2],i[3]])
                    else:
                        g.append(i)
            file.close()
            file = open("accounts.csv","w",newline="")
            file = open("accounts.csv","a",newline="")
            mywriter = csv.writer(file)
            mywriter.writerows(g)
            file.seek(0)
            file.close()
            app.loginpage(self)
    def createanacc(self):
        for i in self.frame.winfo_children():
            i.place_forget() 
        self.account_profile.place(relx = 0.4,rely = 0.05)
        self.left_label.place(relx = 0.02,rely= 0.9)
        self.email = CTkEntry(self.frame,text_color="black",placeholder_text="Email",placeholder_text_color="black",
                              height = 30,width = 220,fg_color="transparent",font=("Bold",12))
        self.username = CTkEntry(self.frame,text_color="black",placeholder_text="Username",
                                 placeholder_text_color="black",height = 30,width = 220,
                                 fg_color="transparent",font=("Bold",12))
        self.phone = CTkEntry(self.frame,text_color="black",placeholder_text="Phone",placeholder_text_color="black",
                              height = 30,width = 220,fg_color="transparent",font=("Bold",12))
        self.createb = CTkButton(self.frame,text="Create account",width = 220,corner_radius=5,
                                command=lambda:app.create(self))
        self.createb.place(relx = 0.15,rely = 0.7)
        self.wellcome = CTkLabel(self.frame,text = "Wellcome",text_color="black",bg_color="white",fg_color="white",
                                 font= ("bold",20))
        self.terms.place(relx = 0.5,rely = 0.9)
        self.wellcome.place(relx = 0.34,rely = 0.2)
        self.account_icon.place(relx = 0.05,rely = 0.4)
        self.padlock_icon.place(relx =0.05,rely = 0.6 )
        self.email1.place(relx = 0.05,rely = 0.3)
        self.phonecall.place(relx = 0.05,rely = 0.5)
        self.email.place(relx = 0.15,rely = 0.3)
        self.username.place(relx = 0.15,rely = 0.4)
        self.phone.place(relx = 0.15,rely= 0.5)
        self.e2.place(relx = 0.15,rely = 0.6)
        eye1(self.frame,self.hidden_eye_icon,self.eye_icon,var = self.e2,x = 0.8,y = 0.6)
    """def slideoutof1(self):
        if self.b>-2 and self.t>-2:
            self.l2.place(relx = self.b,rely = 0.1)
            self.account_profile.place(relx=self.t,rely=0.075)
            self.b-=0.001
            self.t -=0.001
            self.frame.after(1,lambda:app.slideoutof1(self))
    def slideoutof2(self):
        if self.b > -2 and self.o>-2:
            self.e1.place(relx = self.b,rely = 0.3)
            self.account_icon.place(relx=self.o,rely=0.3)
            self.b-=0.001
            self.o-=0.001
            self.frame.after(1,lambda:app.slideoutof2(self))
    def slideoutof3(self):
        if self.b > -2 and self.o>-2:
            self.e2.place(relx = self.b,rely = 0.3)
            self.padlock_icon.place(relx=self.o,rely=0.3)
            self.b-=0.001
            self.o-=0.001
            self.frame.after(1,lambda:app.slideoutof3(self))
    def slideoutof4(self):
        self.p=self.o + 0.4
        if self.p>-2:
            self.button1.place_configure(relx = self.p)
            self.p -= 0.001
            self.frame.after(1,lambda:app.slideoutof4(self))
    def slideoutof5(self):
        if self.i>-2:
            self.label_nomovie.place_configure(relx = self.i)
            self.i -= 0.001
            self.frame.after(1,lambda:app.slideoutof5(self))
    def slideoutof6(self):
        if self.b > -2:
            self.button2.place_configure(relx = self.b)
            self.b -= 0.001
            self.frame.after(1,lambda:app.slideoutof6(self))
    def slideoutof7(self):
        self.o +=0.43
        if self.o>-2:
            self.label_noaccount.place_configure(relx = self.o)
            self.button3.place_configure(relx = self.o)
            self.o -= 0.001
            self.frame.after(1,lambda:app.slideoutof7(self))"""
    def create(self):
        self.u = True
        self.g = True
        self.df = True
        for i in self.username.get():
            if i.isdigit():
                self.df = True
                break
            else:
                self.df = False
        for i in self.phone.get():
            if i.isdigit():
                self.g = False
            else:
                self.g = True
                break
        for i in self.e2.get():
            if i.isalnum() == True:
                self.u = False
            elif i.isalnum() == False:
                self.u = True
                break
        if (self.email.get().isspace()) or (self.email.get() == "") or (self.username.get().isspace()) or (self.username.get()=="") or (self.e2.get() == "") or (self.e2.get().isspace()) or (self.phone.get().isspace()) or (self.phone.get() == ""):
            self.label_nomovie.configure(text = "Fill all the fields")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.35,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.email.get().isspace())or("@" not in self.email.get()) or(".com" not in self.email.get()):
            self.label_nomovie.configure(text = "Enter a proper mail id")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.28,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.phone.get() in phone_l):
            self.label_nomovie.configure(text = "Number already registered")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.25,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.email.get() in email_l):
            self.label_nomovie.configure(text = "Email already exists")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.28,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.username.get() in l.keys()):
            self.label_nomovie.configure(text = "Username already exists")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.25,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (len(self.username.get())<5)or(self.df):
            self.label_nomovie.configure(text = "Enter proper username")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.25,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.username.get().isspace()):
            self.label_nomovie.configure(text = "Enter valid username")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.28,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (len(self.phone.get()) != 10) or self.g:
            self.label_nomovie.configure(text = "Enter valid phone number")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.25,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif (self.e2.get().isspace())or(self.e2.get() == ""):
            self.label_nomovie.configure(text = "Enter valid password")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.28,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif len(self.e2.get())<4:
            self.label_nomovie.configure(text = "Password must contain atleast 4 characters")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.12,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif self.u == False:
            self.label_nomovie.configure(text = "Password must contain 1 speacial character")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.12,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        elif not(self.terms.get()):
            self.label_nomovie.configure(text = "Accept Terms and Condition")
            self.createb.place(relx = 0.15,rely= 0.8)
            self.label_nomovie.place(relx = 0.23,rely = 0.7)
            app.vibrating(self,self.frame,0.5,0.5)
        else:
            global fff
            fff = self.username.get()
            global number
            number = random.randrange(1000,10000)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("<yourmail@gmail.com>", "<password key>")
            message = str(number)
            s.sendmail("<yourmail@gmail.com>", str(self.email.get()), message)
            s.quit()
            for i in self.frame.winfo_children():
                i.place_forget()
            self.createb = CTkButton(self.frame,text="Create account",width = 220,corner_radius=5,
                                command=lambda:app.checker7(self))
            self.reset_password_title = CTkLabel(self.frame,text= "Verify its you",font = ("Century Gothic",30),text_color="black")
            self.username = CTkEntry(self.frame,text_color="black",placeholder_text="OTP",placeholder_text_color="black",height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.username.place(relx = 0.15,rely = 0.3)
            self.left_label.configure(command = lambda:app.createanacc(self))
            self.left_label.place(relx = 0.02,rely= 0.9)
            self.reset_password_title.place(relx = 0.15,rely = 0.1)
            self.createb.place(relx = 0.15,rely = 0.7)
    def checker7(self):
        if self.username.get()==str(number):
            app.popup(self,msg = "Created")
            self.label_nomovie.configure(text = "")
            self.createb.place(relx = 0.15,rely= 0.7)
            self.label_nomovie.place(relx = 0.28,rely = 0.7)
            file = open("accounts.csv","a",newline="\n")
            mywriter = csv.writer(file)
            mywriter.writerow([fff,self.e2.get(),self.email.get(),self.phone.get()])
            file.close()
            app.loginpage(self)
        else:
            self.label_nomovie.configure(text = "Wrong otp")
            self.label_nomovie.place(relx = 0.35,rely = 0.4)
            app.vibrating(self,self.frame,0.5,0.5)

    ###################
    ###################
    ###################
    ###################
    ###################
    def mainpage(self,u):
        self.imagelabel_1 = CTkLabel(self,image=self.img1,text="")
        for i in self.winfo_children():
            i.place_forget()
        self.imagelabel_1.pack()
        self.variable = -0.12
        self.account_profile = CTkButton(self,image= self.account_profile_img,corner_radius = 0,text = "",height = 20,width =20,fg_color="black",hover = False,command=lambda:app.profilebt(self,u,False))
        self.scroll = CTkScrollableFrame(self,width = 730,height =400,orientation="horizontal",fg_color="black")
        self.scroll.place(relx = 0.08,rely = 0.15)
        self.boat_l = CTkButton(self.scroll,image=self.boat,text="",height=400,width = 220,
                                  fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"Boat"))
        self.devara_l = CTkButton(self.scroll,image=self.devara,text="",height=400,width = 220,
                                  fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"Devara"))
        self.mai_l = CTkButton(self.scroll,image=self.mai,text="",height=400,
                               width = 220,fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"Meiyazhagan"))
        self.saripodha_l = CTkButton(self.scroll,image=self.saripodha,text="",height=400,
                                     width = 220,fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"Saripodhaa Sanivaaram"))
        self.indian2_l = CTkButton(self.scroll,image=self.indian2,text="",height=400,
                                   width = 220,fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"INDIAN 2"))
        self.pechi_l = CTkButton(self.scroll,image=self.pechi,text="",height=400,
                                 width = 220,border_width=0,fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"Pechi"))
        self.goat_l = CTkButton(self.scroll,image=self.goat,text="",height=400,
                                width = 220,border_width=0,fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,name ="Goat"))
        self.raayan_l = CTkButton(self.scroll,image=self.raayan,text="",height=400,
                                  width = 220,border_width=0,fg_color="transparent",cursor = "hand2",hover = False,command=lambda:app.movie(self,u,"Raayan"))
        self.frame3 = CTkFrame(self,height = 650,width = 150,fg_color="white",corner_radius=0)
        #self.account_b = CTkButton(self,width = 50,height = 50,text = "")
        #self.account_profile = CTkLabel(self,image= self.account_profile_img,text = "",bg_color="red")
        #pywinstyles.set_opacity(self.account_b,0)
        self.out = CTkButton(self.frame3,image=self.out_img,text="",fg_color="white",width=26,height=26,hover_color="white",command=lambda:app.outter(self,u))
        #self.account_b.place(relx = 0,rely = 0)
        #self.account_profile.place(relx = 0.1,rely=0.1)
        self.inn = CTkButton(self.frame3,image=self.in_img,text="",fg_color="white",width=26,height=26,hover_color="white",command=lambda:app.inner(self,u))
        self.indian2_l.grid(row = 0,column=0,padx = 10,pady = 10)
        self.pechi_l.grid(row = 0,column = 1,padx= 10,pady = 10)
        self.raayan_l.grid(row = 0,column = 2,padx= 10,pady = 10)
        self.goat_l.grid(row = 0,column = 3,padx =10,pady = 10)
        self.saripodha_l.grid(row = 0,column = 4,padx =10,pady = 10)
        self.mai_l.grid(row = 0,column = 5,padx =10,pady = 10)
        self.devara_l.grid(row = 0,column = 6,padx =10,pady = 10)
        self.boat_l.grid(row = 0,column = 7,padx =10,pady = 10)
        #self.frame3.place(relx = self.variable,rely = 0)
        self.out.place(relx = 0.7,rely = 0.5)
        self.n =False
        self.account_profile.place(relx = 0,rely = 0)
    def checker3(self,u,name,j = False):
        global movie_n
        movie_n = ""
        n=0.1
        if name == "Goat":
            self.goat_l.place_forget()
            movie_n = "Goat"
        elif name == "Boat":
            self.boat_l.place_forget()
            movie_n = "Boat"
        elif name == "Devara":
            self.devara_l.place_forget()
            movie_n = "Devara"
        elif name == "Meiyazhagan":
            self.mai_l.place_forget()
            movie_n = "Meiyazhagan"
        elif name == "Raayan":
            self.raayan_l.place_forget()
            movie_n = "Raayan"
        elif name == "Saripodhaa Sanivaaram":
            self.saripodha_l.place_forget()
            movie_n = "Saripodhaa Sanivaaram"
        elif name == "Pechi":
            self.pechi_l.place_forget()
            movie_n = "Pechi"
        elif name == "INDIAN 2":
            self.indian2_l.place_forget()
            movie_n = "INDIAN 2"
        self.mol.place_forget()
        self.update()
        if self.some:
            app.checkofclose(self)
        self.book.configure(text = "Pay",command = lambda:app.checker4(self,u))
        self.mol.place_forget()
        self.screen = CTkFrame(self,width = 829,height = 380,fg_color="white")
        self.screen.place(relx = 0.04,rely = 0.1)
        self.H1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H1,1,"self.H1",0.5,1.0))
        self.H1.place(relx = 0.05,rely = 0.1)
        self.H2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H2,2,"self.H2",1.22,1.0))
        self.H2.place(relx = 0.122,rely = 0.1)
        self.H3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H3,3,"self.H3",1.94,1.0))
        self.H3.place(relx = 0.194,rely = 0.1)
        self.H4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H4,4,"self.H4",2.66,1.0))
        self.H4.place(relx = 0.266,rely = 0.1)
        self.H5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H5,5,"self.H5",3.38,1.0))
        self.H5.place(relx = 0.338,rely = 0.1)
        self.H6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H6,6,"self.H6",4.1,1.0))
        self.H6.place(relx = 0.41,rely = 0.1)
        self.G1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G1,1,"self.G1",0.5,2.0))
        self.G1.place(relx = 0.05,rely = 0.2)
        self.G2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G2,2,"self.G2",1.22,2.0))
        self.G2.place(relx = 0.122,rely = 0.2)
        self.G3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G3,3,"self.G3",1.94,2.0))
        self.G3.place(relx = 0.194,rely = 0.2)
        self.G4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G4,4,"self.G4",2.66,2.0))
        self.G4.place(relx = 0.266,rely = 0.2)
        self.G5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G5,5,"self.G5",3.38,2.0))
        self.G5.place(relx = 0.338,rely = 0.2)
        self.G6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G6,6,"self.G6",4.1,2.0))
        self.G6.place(relx = 0.41,rely = 0.2)
        self.F1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F1,1,"self.F1",0.5,3.0))
        self.F1.place(relx = 0.05,rely = 0.3)
        self.F2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F2,2,"self.F2",1.22,3.0))
        self.F2.place(relx = 0.122,rely = 0.3)
        self.F3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F3,3,"self.F3",1.94,3.0))
        self.F3.place(relx = 0.194,rely = 0.3)
        self.F4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F4,4,"self.F4",2.66,3.0))
        self.F4.place(relx = 0.266,rely = 0.3)
        self.F5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F5,5,"self.F5",3.38,3.0))
        self.F5.place(relx = 0.338,rely = 0.3)
        self.F6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F6,6,"self.F6",4.1,3.0))
        self.F6.place(relx = 0.41,rely = 0.3)
        self.E1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E1,1,"self.E1",0.5,4.0))
        self.E1.place(relx = 0.05,rely = 0.4)
        self.E2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E2,2,"self.E2",1.22,4.0))
        self.E2.place(relx = 0.122,rely = 0.4)
        self.E3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E3,3,"self.E3",1.94,4.0))
        self.E3.place(relx = 0.194,rely = 0.4)
        self.E4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E4,4,"self.E4",2.66,4.0))
        self.E4.place(relx = 0.266,rely = 0.4)
        self.E5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E5,5,"self.E5",3.38,4.0))
        self.E5.place(relx = 0.338,rely = 0.4)
        self.E6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E6,6,"self.E6",4.1,4.0))
        self.E6.place(relx = 0.41,rely = 0.4)
        self.D1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D1,1,"self.D1",0.5,5.0))
        self.D1.place(relx = 0.05,rely = 0.5)
        self.D2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D2,2,"self.D2",1.22,5.0))
        self.D2.place(relx = 0.122,rely = 0.5)
        self.D3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D3,3,"self.D3",1.94,5.0))
        self.D3.place(relx = 0.194,rely = 0.5)
        self.D4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D4,4,"self.D4",2.66,5.0))
        self.D4.place(relx = 0.266,rely = 0.5)
        self.D5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D5,5,"self.D5",3.38,5.0))
        self.D5.place(relx = 0.338,rely = 0.5)
        self.D6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D6,6,"self.D6",4.1,5.0))
        self.D6.place(relx = 0.41,rely = 0.5)
        self.C1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C1,1,"self.C1",0.5,6.0))
        self.C1.place(relx = 0.05,rely = 0.6)
        self.C2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C2,2,"self.C2",1.22,6.0))
        self.C2.place(relx = 0.122,rely = 0.6)
        self.C3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C3,3,"self.C3",1.94,6.0))
        self.C3.place(relx = 0.194,rely = 0.6)
        self.C4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C4,4,"self.C4",2.66,6.0))
        self.C4.place(relx = 0.266,rely = 0.6)
        self.C5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C5,5,"self.C5",3.38,6.0))
        self.C5.place(relx = 0.338,rely = 0.6)
        self.C6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C6,6,"self.C6",4.1,6.0))
        self.C6.place(relx = 0.41,rely = 0.6)
        self.B1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B1,1,"self.B1",0.5,7.0))
        self.B1.place(relx = 0.05,rely = 0.7)
        self.B2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B2,2,"self.B2",1.22,7.0))
        self.B2.place(relx = 0.122,rely = 0.7)
        self.B3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B3,3,"self.B3",1.94,7.0))
        self.B3.place(relx = 0.194,rely = 0.7)
        self.B4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B4,4,"self.B4",2.66,7.0))
        self.B4.place(relx = 0.266,rely = 0.7)
        self.B5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B5,5,"self.B5",3.38,7.0))
        self.B5.place(relx = 0.338,rely = 0.7)
        self.B6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B6,6,"self.B6",4.1,7.0))
        self.B6.place(relx = 0.41,rely = 0.7)
        self.A1 = CTkButton(self.screen,image=self.cinema,text="1",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A1,1,"self.A1",0.5,8.0))
        self.A1.place(relx = 0.05,rely = 0.8)
        self.A2 = CTkButton(self.screen,image=self.cinema,text="2",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A2,2,"self.A2",1.22,8.0))
        self.A2.place(relx = 0.122,rely = 0.8)
        self.A3 = CTkButton(self.screen,image=self.cinema,text="3",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A3,3,"self.A3",1.94,8.0))
        self.A3.place(relx = 0.194,rely = 0.8)
        self.A4 = CTkButton(self.screen,image=self.cinema,text="4",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A4,4,"self.A4",2.66,8.0))
        self.A4.place(relx = 0.266,rely = 0.8)
        self.A5 = CTkButton(self.screen,image=self.cinema,text="5",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A5,5,"self.A5",3.38,8.0))
        self.A5.place(relx = 0.338,rely = 0.8)
        self.A6 = CTkButton(self.screen,image=self.cinema,text="6",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A6,6,"self.A6",4.1,8.0))
        self.A6.place(relx = 0.41,rely = 0.8)
        self.H7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H7,7,"self.H7",5.4,1.0))
        self.H7.place(relx = 0.54,rely = 0.1)
        self.H8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H8,8,"self.H8",6.12,1.0))
        self.H8.place(relx = 0.612,rely = 0.1)
        self.H9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H9,9,"self.H9",6.84,1.0))
        self.H9.place(relx = 0.684,rely = 0.1)
        self.H10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H10,10,"self.H10",7.56,1.0))
        self.H10.place(relx = 0.756,rely = 0.1)
        self.H11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H11,11,"self.H11",8.28,1.0))
        self.H11.place(relx = 0.828,rely = 0.1)
        self.H12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.H12,12,"self.H12",9.0,1.0))
        self.H12.place(relx = 0.9,rely = 0.1)
        self.G7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G7,7,"self.G7",5.4,2.0))
        self.G7.place(relx = 0.54,rely = 0.2)
        self.G8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G8,8,"self.G8",6.12,2.0))
        self.G8.place(relx = 0.612,rely = 0.2)
        self.G9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G9,9,"self.G9",6.84,2.0))
        self.G9.place(relx = 0.684,rely = 0.2)
        self.G10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G10,10,"self.G10",7.56,2.0))
        self.G10.place(relx = 0.756,rely = 0.2)
        self.G11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G11,11,"self.G11",8.28,2.0))
        self.G11.place(relx = 0.828,rely = 0.2)
        self.G12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.G12,12,"self.G12",9.0,2.0))
        self.G12.place(relx = 0.9,rely = 0.2)
        self.F7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F7,7,"self.F7",5.4,3.0))
        self.F7.place(relx = 0.54,rely = 0.3)
        self.F8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F8,8,"self.F8",6.12,3.0))
        self.F8.place(relx = 0.612,rely = 0.3)
        self.F9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F9,9,"self.F9",6.84,3.0))
        self.F9.place(relx = 0.684,rely = 0.3)
        self.F10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F10,10,"self.F10",7.56,3.0))
        self.F10.place(relx = 0.756,rely = 0.3)
        self.F11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F11,11,"self.F11",8.28,3.0))
        self.F11.place(relx = 0.828,rely = 0.3)
        self.F12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.F12,12,"self.F12",9.0,3.0))
        self.F12.place(relx = 0.9,rely = 0.3)
        self.E7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E7,7,"self.E7",5.4,4.0))
        self.E7.place(relx = 0.54,rely = 0.4)
        self.E8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E8,8,"self.E8",6.12,4.0))
        self.E8.place(relx = 0.612,rely = 0.4)
        self.E9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E9,9,"self.E9",6.84,4.0))
        self.E9.place(relx = 0.684,rely = 0.4)
        self.E10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E10,10,"self.E10",7.56,4.0))
        self.E10.place(relx = 0.756,rely = 0.4)
        self.E11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E11,11,"self.E11",8.28,4.0))
        self.E11.place(relx = 0.828,rely = 0.4)
        self.E12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.E12,12,"self.E12",9.0,4.0))
        self.E12.place(relx = 0.9,rely = 0.4)
        self.D7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D7,7,"self.D7",5.4,5.0))
        self.D7.place(relx = 0.54,rely = 0.5)
        self.D8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D8,8,"self.D8",6.12,5.0))
        self.D8.place(relx = 0.612,rely = 0.5)
        self.D9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D9,9,"self.D9",6.84,5.0))
        self.D9.place(relx = 0.684,rely = 0.5)
        self.D10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D10,10,"self.D10",7.56,5.0))
        self.D10.place(relx = 0.756,rely = 0.5)
        self.D11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D11,11,"self.D11",8.28,5.0))
        self.D11.place(relx = 0.828,rely = 0.5)
        self.D12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.D12,12,"self.D12",9.0,5.0))
        self.D12.place(relx = 0.9,rely = 0.5)
        self.C7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C7,7,"self.C7",5.4,6.0))
        self.C7.place(relx = 0.54,rely = 0.6)
        self.C8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C8,8,"self.C8",6.12,6.0))
        self.C8.place(relx = 0.612,rely = 0.6)
        self.C9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C9,9,"self.C9",6.84,6.0))
        self.C9.place(relx = 0.684,rely = 0.6)
        self.C10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C10,10,"self.C10",7.56,6.0))
        self.C10.place(relx = 0.756,rely = 0.6)
        self.C11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C11,11,"self.C11",8.28,6.0))
        self.C11.place(relx = 0.828,rely = 0.6)
        self.C12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.C12,12,"self.C12",9.0,6.0))
        self.C12.place(relx = 0.9,rely = 0.6)
        self.B7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B7,7,"self.B7",5.4,7.0))
        self.B7.place(relx = 0.54,rely = 0.7)
        self.B8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B8,8,"self.B8",6.12,7.0))
        self.B8.place(relx = 0.612,rely = 0.7)
        self.B9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B9,9,"self.B9",6.84,7.0))
        self.B9.place(relx = 0.684,rely = 0.7)
        self.B10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B10,10,"self.B10",7.56,7.0))
        self.B10.place(relx = 0.756,rely = 0.7)
        self.B11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B11,11,"self.B11",8.28,7.0))
        self.B11.place(relx = 0.828,rely = 0.7)
        self.B12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.B12,12,"self.B12",9.0,7.0))
        self.B12.place(relx = 0.9,rely = 0.7)
        self.A7 = CTkButton(self.screen,image=self.cinema,text="7",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A7,7,"self.A7",5.4,8.0))
        self.A7.place(relx = 0.54,rely = 0.8)
        self.A8 = CTkButton(self.screen,image=self.cinema,text="8",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A8,8,"self.A8",6.12,8.0))
        self.A8.place(relx = 0.612,rely = 0.8)
        self.A9 = CTkButton(self.screen,image=self.cinema,text="9",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A9,9,"self.A9",6.84,8.0))
        self.A9.place(relx = 0.684,rely = 0.8)
        self.A10 = CTkButton(self.screen,image=self.cinema,text="10",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A10,10,"self.A10",7.56,8.0))
        self.A10.place(relx = 0.756,rely = 0.8)
        self.A11 = CTkButton(self.screen,image=self.cinema,text="11",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A11,11,"self.A11",8.28,8.0))
        self.A11.place(relx = 0.828,rely = 0.8)
        self.A12 = CTkButton(self.screen,image=self.cinema,text="12",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.A12,12,"self.A12",9.0,8.0))
        self.A12.place(relx = 0.9,rely = 0.8)

        for i in range(72,64,-1):
            self.alpha = CTkLabel(self.screen,text = chr(i),text_color="black",bg_color="white",fg_color="white",font = ("bold",15))
            self.alpha.place(relx = 0.02,rely = n)
            n+=0.1
        l = []
        f = open("tickets.dat","rb")
        while True:
            try:
                s = p.load(f)
                l.append(s)
            except EOFError:
                break
        f.close()
        for i in l:
            if str(i[1]) == movie_n:
                for j in i[2]:
                    if j == "self.H1":
                        self.H1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H2":
                        self.H2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H3":
                        self.H3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H4":
                        self.H4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H5":
                        self.H5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H6":
                        self.H6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H7":
                        self.H7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H8":
                        self.H8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H9":
                        self.H9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H10":
                        self.H10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H11":
                        self.H11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.H12":
                        self.H12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G1":
                        self.G1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G2":
                        self.G2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G3":
                        self.G3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G4":
                        self.G4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G5":
                        self.G5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G6":
                        self.G6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G7":
                        self.G7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G8":
                        self.G8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G9":
                        self.G9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G10":
                        self.G10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G11":
                        self.G11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.G12":
                        self.G12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F1":
                        self.F1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F2":
                        self.F2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F3":
                        self.F3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F4":
                        self.F4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F5":
                        self.F5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F6":
                        self.F6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F7":
                        self.F7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F8":
                        self.F8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F9":
                        self.F9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F10":
                        self.F10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F11":
                        self.F11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.F12":
                        self.F12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E1":
                        self.E1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E2":
                        self.E2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E3":
                        self.E3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E4":
                        self.E4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E5":
                        self.E5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E6":
                        self.E6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E7":
                        self.E7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E8":
                        self.E8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E9":
                        self.E9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E10":
                        self.E10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E11":
                        self.E11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.E12":
                        self.E12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D1":
                        self.D1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D2":
                        self.D2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D3":
                        self.D3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D4":
                        self.D4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D5":
                        self.D5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D6":
                        self.D6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D7":
                        self.D7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D8":
                        self.D8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D9":
                        self.D9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D10":
                        self.D10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D11":
                        self.D11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.D12":
                        self.D12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C1":
                        self.C1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C2":
                        self.C2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C3":
                        self.C3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C4":
                        self.C4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C5":
                        self.C5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C6":
                        self.C6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C7":
                        self.C7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C8":
                        self.C8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C9":
                        self.C9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C10":
                        self.C10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C11":
                        self.C11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.C12":
                        self.C12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B1":
                        self.B1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B2":
                        self.B2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B3":
                        self.B3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B4":
                        self.B4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B5":
                        self.B5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B6":
                        self.B6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B7":
                        self.B7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B8":
                        self.B8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B9":
                        self.B9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B10":
                        self.B10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B11":
                        self.B11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.B12":
                        self.B12.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A1":
                        self.A1.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A2":
                        self.A2.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A3":
                        self.A3.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A4":
                        self.A4.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A5":
                        self.A5.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A6":
                        self.A6.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A7":
                        self.A7.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A8":
                        self.A8.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A9":
                        self.A9.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A10":
                        self.A10.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A11":
                        self.A11.configure(state = "disabled",fg_color = "yellow")
                    if j == "self.A12":
                        self.A12.configure(state = "disabled",fg_color = "yellow")
        self.left_label.configure(command = lambda:app.movie(self,u,movie_n,h = True))
        self.left_label.place(relx = 0.05,rely = 0.9)
        self.theatre = CTkLabel(self.screen,text = "All eyes this way please",text_color="black",bg_color="white",fg_color="white",font =("bold",20))
        self.theatre.place(relx = 0.38,rely=0.9)
    def payment(self,u,root):
        if self.some:
            app.checkofclose(self)
        self.book.place_forget()
        self.screen.place_forget()
        self.payf = CTkFrame(root,width = 340,height = 380,fg_color="white")
        self.payf.place(relx = self.i , rely= 0.5,anchor = "center")
        self.mlabel = CTkLabel(self.payf,text= "PAYMENT",font = ("bold",30),text_color="black")
        self.mlabel.place(relx = 0.28,rely = 0.1)
        self.credit_1 = CTkLabel(self.payf,image=self.credit,text="")
        self.cvv_1 = CTkLabel(self.payf,image=self.cvv,text="")
        self.cvve =CTkEntry(self.payf,text_color="black",fg_color = "white",placeholder_text="Cvv",placeholder_text_color="black",height = 30,width = 220,font=("Bold",12))
        self.carde = CTkEntry(self.payf,text_color="black",fg_color = "white",placeholder_text="Card number",placeholder_text_color="black",height = 30,width = 220,font=("Bold",12))
        self.carde.place(relx = 0.17,rely =0.3)
        self.cvve.place(relx = 0.17,rely = 0.5)
        self.payb = CTkButton(self.payf,text=f"Pay {190*len(self.tickets)}",height=30,width = 220,command=lambda:app.checker6(self,u))
        self.payb.place(relx = 0.17,rely = 0.7)
        self.left_label.configure(command = lambda:app.movie(self,u,movie_n,t=True))
        self.credit_1.place(relx = 0.08,rely =0.3)
        self.cvv_1.place(relx = 0.08,rely =0.5)
        self.label_nomovie = CTkLabel(self.payf,text = "",corner_radius=5,text_color="red",font=("century gothic",12))
    def checker6(self,u):
        if self.some:
            app.checkofclose(self)
        e = False
        t = False
        for i in self.carde.get():
            if i.isalpha():
                e = True
                break
        for i in self.cvve.get():
            if i.isalpha():
                t = True
                break
        if self.carde.get().isspace() or self.carde.get() == "":
            self.label_nomovie.configure(text = "Enter cardno.")
            self.label_nomovie.place(relx = 0.35,rely = 0.6)
            app.vibrating(self,self.payf,0.5,0.5)
        elif e or len(self.carde.get()) != 16:
            self.label_nomovie.configure(text = "Enter valid cardno.")
            self.label_nomovie.place(relx = 0.33,rely = 0.6)
            app.vibrating(self,self.payf,0.5,0.5)
        elif self.cvve.get().isspace() or self.cvve.get() == "":
            self.label_nomovie.configure(text = "Enter cvv")
            self.label_nomovie.place(relx = 0.37,rely = 0.6)
            app.vibrating(self,self.payf,0.5,0.5)
        elif t or len(self.cvve.get()) != 3:
            self.label_nomovie.configure(text = "Enter valid cvv")
            self.label_nomovie.place(relx = 0.35,rely = 0.6)
            app.vibrating(self,self.payf,0.5,0.5)
        else:
            temp = []
            file = open("accounts.csv","r")
            myreader = csv.reader(file)
            for i in myreader:
                temp.append(i)
            file.close()
            l = {}
            for i in temp:
                if i == []:
                    continue
                l[i[0]]= [i[1],i[2],i[3]]
            message =""
            for i in self.tickets:
                message+=i[-2:].lower()+","
            message = movie_n + " : " + message[0:-1]
            message = "Thank you for booking ticket in our interface\nDetails\n" + message
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("<your mail id to send otp>", "<your mail id's password key>")
            s.sendmail("<your mail id to send otp>", str(l[u][1]),message)
            s.quit()
            self.lmo.extend(self.tickets)
            v =[]
            with open("tickets.dat","ab") as f:
                l =[]
                file = open("tickets.dat","rb")
                while True:
                    try:
                        s = p.load(file)
                        l.append(s)
                    except EOFError:
                        break
                file.close()
                for i in l:
                    if i[0] == u and i[1] == movie_n:
                        self.lmo.extend(i[2])
                        l.remove(i)
                print(u)
                v = [u,movie_n]
                v.append(self.lmo)
                l.append(v)
                for i in l:
                    with open("tickets.dat","wb") as fi:
                        pass
                    p.dump(i,f)
            v =[]
            self.tickets = []
            self.lmo = []
            app.mainpage(self,u)
            #time.sleep(2)
            self.update()
            app.popup(self,"Booked")
    def checker4(self,u):
        if self.some:
            app.checkofclose(self)
        if self.tickets != []:
            """self.lmo.extend([u,movie_n,self.tickets])
            with open("tickets.dat","ab") as f:
                p.dump(self.lmo,f)"""
            #self.screen.place_forget()
            self.book.configure(state = "disabled")
            app.payment(self,u,self)
            #app.movie(self,movie_n,t=True)
            #app.popup(self,"Booked")
        else:
            self.screen.place_forget()
            app.movie(self,u,movie_n)
    def seat(self,u,id,txt,t,x,y):
        id.configure(fg_color = "green",command = lambda:app.seatoff(self,u,id,txt,t,x,y))
        self.tickets.append(t)
    def seatoff(self,u,id,txt,t,x,y):
        self.tickets.remove(t)
        id.configure(fg_color = "white",command = lambda:app.seat(self,u,id,txt,t,x,y))


    def movie(self,u,name,h = False,t = False):
        self.tickets =[]
        if self.some:
            app.checkofclose(self)
        if t:
            self.payf.place_forget()
        if h:
            self.screen.place_forget()
        self.frame3.place_forget()
        #self.scroll2 = CTkScrollableFrame(self,width = 540,height =400,orientation="horizontal",fg_color="black")
        #self.scroll2.place(relx = 0.37,rely = 0.05)
        self.boat_l = CTkLabel(self,image=self.boat,text="",height=400,width = 220,
                                  fg_color="transparent")
        self.devara_l = CTkLabel(self,image=self.devara,text="",height=400,width = 220,
                                  fg_color="transparent")
        self.mai_l = CTkLabel(self,image=self.mai,text="",height=400,
                               width = 220,fg_color="transparent")
        self.saripodha_l = CTkLabel(self,image=self.saripodha,text="",height=400,
                                     width = 220,fg_color="transparent")
        self.indian2_l = CTkLabel(self,image=self.indian2,text="",height=400,
                                   width = 220,fg_color="transparent")
        self.pechi_l = CTkLabel(self,image=self.pechi,text="",height=400,
                                 width = 220,fg_color="transparent")
        self.goat_l = CTkLabel(self,image=self.goat,text="",height=400,
                                width = 220,fg_color="transparent")
        self.raayan_l = CTkLabel(self,image=self.raayan,text="",height=400,
                                  width = 220,fg_color="transparent")
        self.scroll.place_forget()
        self.left_label = CTkButton(self,image = self.leftarrow_img,text_color="black",text="Back",font = ("bold",20),width= 13,height= 13,hover_color="white",fg_color="white",command=lambda:app.mainpage(self,u))
        self.left_label.place(relx = 0.05,rely = 0.9)
        if name == "Goat":
            self.mol = CTkLabel(self,fg_color="black",text= """Gandhi is a hostage negotiator, field agent, and spy working\nfor the Special Anti-Terrorist Squad (SATS). After years \nof service, he is called back for a critical mission that sets him\n on a dangerous collision course with his own past.\n\nDirector:Venkat Prabhu\nWriters: M Prasad Babu,K.Chandru,Ezhilarasu Gunasekaran\nStars:Joseph Vijay,Prashanth,Prabhu Deva""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Goat",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.goat_l.place(relx = 0.07,rely = 0.05)
        elif name == "Boat":
            self.mol = CTkLabel(self,fg_color="black",text= """10 people escape bombing on small boat, which unexpectedly\nstops and sinks mid-journey. Passengers struggle to survive as\nboat goes down.\n\nDirector:Chimbudeven\nWriter:Chimbudeven\nStars:Jesse Fox Allen,Yogi Babu,M.S. Bhaskar """,font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Boat",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.boat_l.place(relx = 0.07,rely = 0.05)
        elif name == "Devara":
            self.mol = CTkLabel(self,fg_color="black",text= """An epic action saga set against coastal lands, which briefs\nabout rip-roaring ,emotionally charged incidents in the periodic\ntimeline, also comprises the titular protagonist being the\nrescuer to deprived and fear to evildoers.\n\nDirector:Koratala Siva\nWriter:Koratala Siva\nStars:N.T. Rama Rao Jr.,Saif Ali Khan,Janhvi Kapoor""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Devara",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.devara_l.place(relx = 0.07,rely = 0.05)
        elif name == "Pechi":
            self.mol = CTkLabel(self,fg_color="black",text= """Revolves around age-old practices such as black magic and\nwitchcraft.\n\nDirector:B. Ramachandran\nWriter:B. Ramachandran\nStars:Gayathri Shanker,Bala Saravanan,Dev Ramnath""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Pechi",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.pechi_l.place(relx = 0.07,rely = 0.05)
        elif name == "INDIAN 2":
            self.mol = CTkLabel(self,fg_color="black",text= """Senapathy, an ex-freedom fighter turned vigilante who\nfights against corruption. Senapathy returns to the country to\naid a young man who has been exposing corrupt politicians\nin the country through videos on the internet.\n\nDirector:S. Shankar\nWriters:G. Chandrasekhar,Jayamohan,Vamsy Krishna\nStars:Kamal Haasann,Siddharth,Rakul Preet Singh""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"INDIAN 2",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.indian2_l.place(relx = 0.07,rely = 0.05)
        elif name == "Saripodhaa Sanivaaram":
            self.mol = CTkLabel(self,fg_color="black",text= """In order to defend the innocent from a corrupt and brutal\ncop,a vigilante hero must work around his own self-imposed\ncode of honor.\n\nDirector:Vivek Athreya\nWriter:Vivek Athreya\nStars:Nani,S.J. Suryah,Priyanka Arulmohan""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Saripodhaa Sanivaaram",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.saripodha_l.place(relx = 0.07,rely = 0.05)
        elif name == "Raayan":
            self.mol = CTkLabel(self,fg_color="black",text= """A series of unfortunate events lead Raayan, a simpleton to be\ndragged into the dreaded world of crime and manipulation.\n\nDirector:Dhanush\nWriters:Manish Bhavan,Dhanush,Bhawan Manish\nStars:Dhanush,Aparna Balamurali,Devadarshini Chetan""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Raayan",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.raayan_l.place(relx = 0.07,rely = 0.05)
        elif name == "Meiyazhagan":
            self.mol = CTkLabel(self,fg_color="black",text= """A man's life is changed when he bumps into\nsomeone from his hometown in this moving Tamil-language\ndrama; gentle scenes are occasionally\npunctuated by sporting threat and recollections of\nviolence.\n\nDirector:C. Prem Kumar\nWriter:C. Prem Kumar\nStars:Karthi,Arvind Swamy,Sri Divya""",font = ("bold",20),text_color="white")
            self.mol.place(relx = 0.32,rely = 0.2)
            self.book = CTkButton(self,text="Book Tickets",width = 220,fg_color="black",corner_radius=0,text_color="white",hover = False,font= ("bold",20),command=lambda: app.checker3(self,u,"Meiyazhagan",j=True))
            self.book.place(relx = 0.36,rely =0.85)
            self.mai_l.place(relx = 0.07,rely = 0.05)
        #self.frame3.place(relx = self.variable,rely = 0)

    def inner(self,u):
        for i in self.frame3.winfo_children():
            i.place_forget()
        if self.variable>=-0.12:
            self.frame3.place(relx = self.variable,rely = 0)
            self.variable-=0.001
            self.after(100,app.inner(self))
            self.update()
        self.inn.place_forget()
        self.out.place(relx = 0.7,rely = 0.5)
        if self.profile_out:
            self.profileframe.place_forget()
            self.profile_out = False
    def outter(self,u):
        for i in self.frame3.winfo_children():
            i.place_forget()
        if self.variable<=0:
            self.frame3.place(relx = self.variable,rely = 0)
            self.variable+=0.001
            self.after(100,app.outter(self))
            self.update()
        self.out.place_forget()
        self.inn.place(relx = 0.7,rely = 0.5)
        self.account_profile_img = CTkImage(Image.open("account profile.png"),size=(100,100))
        self.account_profile = CTkLabel(self.frame3,image= self.account_profile_img,text = "")
        self.account_profile.place(relx = 0.16,rely = 0.05)
        self.profileb = CTkButton(self.frame3,text="Profile",width = 140,fg_color="white",text_color="black",corner_radius=5,hover=False,font = ("bold",18),command=lambda: app.profilebt(self,u))
        self.user = CTkLabel(self.frame3,text= u,font = ("Century Gothic",25),text_color="black")
        self.user.place(relx = 0.18,rely = 0.21)
        self.profileb.place(relx = 0,rely = 0.3)
    def placeforget(self,u,id):
        id.place_forget()
        self.account_profile.configure(command = lambda:app.profilebt(self,u,False))
    def profilebt(self,u,n,k = False):
        if n == False:
            self.account_profile.configure(command = lambda:app.profilebt(self,u,True))
            self.n = True
            var_for_details = "Username: {} \n\nPassword: {} \n\nEmail: {}\n\nMobile: {}".format(u,l[u][0],l[u][1],l[u][2])
            self.profileframe = CTkFrame(self,height = 650,width = 890,fg_color="white",corner_radius=0)
                #self.show_password = CTkEntry(self.profileframe,text_color="black",placeholder_text="Password",placeholder_text_color="black",
                #                      height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.detail =CTkLabel(self.profileframe,text= var_for_details,font = ("bold",20),text_color="black")
                #self.done = CTkButton(self.profileframe,text="Click here",width = 220,corner_radius=5,command=lambda: app.checker2(self))
                #self.done.place(relx = 0.45,rely = 0.52) 
                #self.show_password.place(relx = 0.45,rely = 0.45)
            self.left_label2 = CTkButton(self.profileframe,image = self.leftarrow_img,text_color="black",text="Back",font = ("bold",20),width= 13,height= 13,hover_color="white",fg_color="white",command = lambda:app.placeforget(self,u,self.profileframe))
            self.left_label2.place(relx = 0,rely = 0.9)
            self.logout = CTkButton(self.profileframe,text="Logout",width = 140,fg_color="white",text_color="black",corner_radius=5,hover=False,font = ("bold",18),command=lambda: app.loginpage(self))
            self.booked = CTkButton(self.profileframe,text="Booked tickets",width = 140,fg_color="white",text_color="black",corner_radius=5,hover=False,font = ("bold",18),command = lambda:app.ticbooked(self,u))
            self.left_label2.configure(command = lambda:app.placeforget(self,u,self.profileframe))
            self.booked.place(relx = 0,rely =0.05)
            self.logout.place(relx = -0.02,rely = 0.8)
            self.profileframe.place(relx = 0.06,rely = 0)
            self.detail.place(relx =0.32 ,rely = 0.35)
        else:
            self.account_profile.configure(command = lambda:app.profilebt(self,u,False))
            self.n = False
            self.profileframe.place_forget()
    """def profilebt(self):
        if self.profile_out == False:
            self.profile_out = True
            var_for_details = "Username: {} \n\nPassword: {} \n\nEmail: {}\n\nMobile: {}".format(u,l[u][0],l[u][1],l[u][2])
            self.profileframe = CTkFrame(self,height = 650,width = 770,fg_color="white",corner_radius=0)
            #self.show_password = CTkEntry(self.profileframe,text_color="black",placeholder_text="Password",placeholder_text_color="black",
            #                      height = 30,width = 220,fg_color="transparent",font=("Bold",12))
            self.detail =CTkLabel(self.profileframe,text= var_for_details,font = ("bold",20),text_color="black")
            #self.done = CTkButton(self.profileframe,text="Click here",width = 220,corner_radius=5,command=lambda: app.checker2(self))
            #self.done.place(relx = 0.45,rely = 0.52)
            #self.show_password.place(relx = 0.45,rely = 0.45)
            self.profileframe.place(relx = 0.163,rely = 0)
            self.detail.place(relx =0.32 ,rely = 0.35)
        else:
            self.profile_out=False
            self.profileframe.place_forget()"""
    """def checker2(self):
        if self.show_password.get() != l[u][0]:
            self.show_password.configure(border_color="red")
            app.vibrating(self,self.show_password,0.5,0.5)
        else:
            self.show_password.configure(border_color = "white")
            self.detail.place(relx =0.35 ,rely = 0.35)"""
    def bb(self,u):
        for i in self.profileframe.winfo_children():
            i.place_forget()
        self.left_label2.place(relx = 0,rely = 0.9)
        self.booked.place(relx = 0,rely =0.05)
        self.logout.place(relx = -0.02,rely = 0.8)
        self.profileframe.place(relx = 0.06,rely = 0)
        self.detail.place(relx =0.32 ,rely = 0.35)
        self.left_label2.configure(command=lambda:app.placeforget(self,u,self.profileframe))
        self.account_profile.configure(command =lambda:app.profilebt(self,u,True))
    def ticbooked(self,u):
        self.account_profile.configure(command = lambda:app.profilebt(self,u,n = True))
        for i in self.profileframe.winfo_children():
            i.place_forget()
        self.left_label2.configure(command=lambda:app.bb(self,u))
        self.left_label2.place(relx = 0,rely = 0.9)
        l =[]
        with open("tickets.dat","rb") as f:
            while True:
                try:
                    s = p.load(f)
                    l.append(s)
                except EOFError:
                    break
        var ={}
        for i in l:
            if str(i[0]) == u:
                var[i[1]]=i[2]
        var2 ={}
        for k,v in var.items():
            l =""
            for i in v:
                i = i[-2:].lower()
                l += i+","
                var2[k] = l
        f =""
        for i in var2:
            f+=f"{i} : {var2[i][0:-1]}\n"
        self.detail2 =CTkLabel(self.profileframe,text= f,font = ("bold",25),text_color="black")
        self.detail2.place(relx = 0.4,rely =0.4)
    
 
k = []
with open("remem.dat","rb") as f:
    while True:
        try:
            s = p.load(f)
            k.append(s)
        except EOFError:
            break
print(k)
try:
    app(s[0])
except NameError:
    app()
