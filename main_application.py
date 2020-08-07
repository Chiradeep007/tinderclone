from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from DBhelper import DBHelper
from tkinter import filedialog
import shutil,os

class Tinder:
    def __init__(self):
        self._db=DBHelper()
        self.load_login_window()

    def load_login_window(self):
        self._root = Tk()
        self._root.title("TINDER")
        self._root.minsize(600,800)
        self._root.maxsize(600,800)
        self._root.config(background="#07B95A")

        self._welcome=Label(self._root,text="WELCOME TO TINDER",fg="#FF0000",bg="#07B95A")
        self._welcome.config(font=("Algerian",40))
        self._welcome.pack(pady=(40,10))

        self._label1=Label(self._root,text="LOGIN HERE",fg="#070FB9",bg="#07B95A")
        self._label1.config(font=("Algerian",30))
        self._label1.pack(pady=(20,30))

        self._email=Label(self._root,text="ENTER YOUR EMAIL",fg="#000",bg="#07B95A")
        self._email.config(font=("Times",18))
        self._email.pack(pady=(10,10))

        self._emailInput=Entry(self._root)
        self._emailInput.pack(pady=(5,25),ipady=10,ipadx=70)

        self._password=Label(self._root,text="ENTER YOUR PASSWORD",fg="#000",bg="#07B95A")
        self._password.config(font=("Times",18))
        self._password.pack(pady=(10,10))

        self._passwordInput=Entry(self._root)
        self._passwordInput.pack(pady=(5,25),ipady=10,ipadx=70)

        self._login= Button(self._root,text="LOGIN",bg="#FFF300",fg="#FF0000",width=25,height=2,command= lambda: self.check_login())
        self._login.config(font=("Times",10,'bold'))
        self._login.pack()

        self._register = Button(self._root,text = "NEW USER, SIGN UP HERE",bg="#FFF300",fg="#FF0000",width = 25,height=2,command= lambda :self.reg_window())
        self._register.config(font=("Algerian",18,'bold'))
        self._register.pack(pady=(40,10))

        self._root.mainloop()


    def check_login(self):
        email = self._emailInput.get()
        password = self._passwordInput.get()

        data = self._db.check_login(email,password)

        if len(data)==0:
            messagebox.showerror("ERROR","INVALID CREDENTIALS")
        else:
            self.user_id=data[0][0]
            self.is_logged_in=1
            #self.login_handler()
            self.logo()

    def logo(self):
        #image = PhotoImage(file = "images\logo.jpg")
        #labelimage = Label(self._root,image = image)
        #labelimage.pack()
        self.clear()
        self.headermenu()
        imageurl = "images\logo.jpg"
        load = Image.open(imageurl)
        load = load.resize((150,150), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(image=render,)
        img.image = render
        img.pack(pady= (50,50))

        aboutus= Label(self._root,text= "WELCOME TO TINDER",fg="#FFF300",bg="#07B95A")
        aboutus.config(font=("Algerian",40,'bold'))
        aboutus.pack(pady=(10,30))

        desclabel= Label(self._root,text= "This is the Official App\n of the TINDER GROUP. Here we\n will help you all to find \nyour correct dating partners.\n Its not a matrimonial app but\n it helps you to find your\n best matches. So go ahead\n and ENJOY your TIME",fg="#FF0000",bg="#07B95A")
        desclabel.config(font = ("Algerian",20,'bold'))
        desclabel.pack(pady=(20,10))

        created_by= Label(self._root,text="Created By       CHIRADEEP GHOSH",fg="#FFF300",bg="#07B95A")
        created_by.config(font=("Algerian",15,'bold'))
        created_by.pack(pady=(3,30))




    def reg_window(self):
        self.clear()
        self._reg_now= Label(self._root,text="REGISTER HERE",fg="#FF0000",bg="#07B95A")
        self._reg_now.config(font=("Algerian",18,'bold','underline'))
        self._reg_now.pack(pady=(10,15))

        self._name_label= Label(self._root,text="ENTER YOUR FULL NAME",fg="#070FB9",bg="#07B95A")
        self._name_label.config(font=("Arial",18))
        self._name_label.pack(pady=(0,8))

        self._reg_nameInput= Entry(self._root)
        self._reg_nameInput.pack(pady=(0,8),ipady= 10,ipadx= 70)

        self._email_label= Label(self._root,text="ENTER A VALID EMAIL ID",fg="#070FB9",bg="#07B95A")
        self._email_label.config(font=("Arial",18))
        self._email_label.pack(pady=(0,8))

        self._reg_emailInput= Entry(self._root)
        self._reg_emailInput.pack(pady=(0,8),ipady=10,ipadx=70)

        self._password_label= Label(self._root,text="ENTER A STRONG PASSWORD",fg="#070FB9",bg="#07B95A")
        self._password_label.config(font=("Arial",18))
        self._password_label.pack(pady=(0,8))

        self._reg_passwordInput= Entry(self._root)
        self._reg_passwordInput.pack(pady=(0,8),ipady=10,ipadx=70)

        self._age_label= Label(self._root,text="ENTER YOUR AGE CORRECTLY TO FIND BEST MATCHES",fg="#070FB9",bg="#07B95A")
        self._age_label.config(font=("Arial",14))
        self._age_label.pack(pady=(0,8))

        self._reg_ageInput= Entry(self._root)
        self._reg_ageInput.pack(pady=(0,8),ipady=10,ipadx=70)

        self._gender_label= Label(self._root,text="ENTER YOUR GENDER",fg="#070FB9",bg="#07B95A")
        self._gender_label.config(font=("Arial",18))
        self._gender_label.pack(pady=(0,8))

        self._reg_genderInput= Entry(self._root)
        self._reg_genderInput.pack(pady=(0,8),ipady= 10,ipadx= 70)

        self._city_label= Label(self._root,text="WHERE DO YOU BELONGS TO",fg="#070FB9",bg="#07B95A")
        self._city_label.config(font=("Arial",18))
        self._city_label.pack(pady=(0,8))

        self._reg_cityInput= Entry(self._root)
        self._reg_cityInput.pack(pady=(0,8),ipady=10,ipadx=70)

        self._dpButton= Button(self._root,text= "UPLOAD A NICE PROFILE PICTURE",fg="#070FB9",bg="#07B95A",command= lambda :self.select_dp())
        self._dpButton.config(font=("Times",10))
        self._dpButton.pack(pady=(0,10))

        self._dp_filename= Label(self._root)
        self._dp_filename.pack()

        self._signupButton= Button(self._root,text="SIGN UP NOW",fg="#070FB9",bg="#07B95A",command= lambda :self.reg_handler())
        self._signupButton.config(font=("Algerian",16))
        self._signupButton.pack(pady=(10,40))


    def reg_handler(self):

        actual_filename = self._filename.split("/")[-1]

        flag= self._db.register(self._reg_nameInput.get(),self._reg_emailInput.get(),self._reg_passwordInput.get(),self._reg_ageInput.get(),self._reg_genderInput.get(),self._reg_cityInput.get(),actual_filename)
        print(flag)
        if flag == 1:
            destination = "C:\\Users\\CHIRADEEP GHOSH\\PycharmProjects\\TINDER\\images\\" + actual_filename
            shutil.copyfile(self._filename,destination)
            messagebox.showinfo("CONGRATS","SUCCESSFULL RESGISTERED. ENJOY YOUR TIME")
            self._root.destroy()
            self.load_login_window()
        else:
            messagebox.showerror("ERROR","SOMETHING WRONG HAPPENED. PLEASE TRY AGAIN")


    def select_dp(self):
        self._filename = filedialog.askopenfilename(initialdir= "/images",title= "UPLOAD YOUR PROFILE PICTURE")
        self._dp_filename.config(text = self._filename)








    def main_window(self,data,flag=0,index=0):

        name= "Name:  " + str(data[index][1])
        email= "Email:  " + str(data[index][2])
        age= "Age:  " + str(data[index][4])
        gender= "Gender:  " + str(data[index][5])
        city= "City:  " + str(data[index][6])
        dp= data[0][7]

        imageurl= "images\{}".format(data[index][7])
        load = Image.open(imageurl)
        load= load.resize((200,200),Image.ANTIALIAS)
        render= ImageTk.PhotoImage(load)
        img= Label(image=render)
        img.image= render
        img.pack()


        name_label=Label(self._root,text= name,fg="#FF00D8",bg="#07B95A")
        name_label.config(font=("Algerian",20))
        name_label.pack(pady=(20,10))

        email_label=Label(self._root,text=email,fg="#FF00D8",bg="#07B95A")
        email_label.config(font=("Arial",16))
        email_label.pack(pady=(5,10))

        age_label=Label(self._root,text=age,fg="#FF00D8",bg="#07B95A")
        age_label.config(font=("Algerian",16))
        age_label.pack(pady=(5,10))

        gender_label=Label(self._root,text=gender,fg="#FF00D8",bg="#07B95A")
        gender_label.config(font=("Arial",16))
        gender_label.pack(pady=(5,10))

        city_label=Label(self._root,text=city,fg="#FF00D8",bg="#07B95A")
        city_label.config(font=("Algerian",16))
        city_label.pack(pady=(5,10))

        if flag == 1:
            frame = Frame(self._root)
            frame.pack(pady=(60,30))
            frame.config(background = "#07B95A")

            previous = Button(frame,text="PREVIOUS USER",fg = "#FFF300",bg = "#FF0000",command = lambda: self.view_others(index-1))
            previous.pack(padx=(50,50), side = LEFT)

            propose = Button(frame,text="PROPOSE THIS USER",fg = "#FFF300",bg = "#FF0000",command = lambda : self.propose(self.user_id,data[index][0]))
            propose.pack(padx=(40,60),side = LEFT)

            next = Button(frame,text="NEXT USER",fg = "#FFF300",bg = "#FF0000",command = lambda :self.view_others(index+1))
            next.pack(padx=(50,50),side = LEFT)

        if flag == 2:
            frame = Frame(self._root)
            frame.pack(pady=(60, 30))
            frame.config(background="#07B95A")

            previous = Button(frame, text="PREVIOUS USER", fg="#FFF300", bg="#FF0000",
                              command=lambda: self.view_proposals(index - 1))
            previous.pack(padx=(50, 50), side=LEFT)

            propose = Button(frame, text="PROPOSE THIS USER", fg="#FFF300", bg="#FF0000",
                             command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(padx=(40, 60), side=LEFT)

            next = Button(frame, text="NEXT USER", fg="#FFF300", bg="#FF0000",
                          command=lambda: self.view_proposals(index + 1))
            next.pack(padx=(50, 50), side=LEFT)

        if flag == 3:
            frame = Frame(self._root)
            frame.pack(pady=(60, 30))
            frame.config(background="#07B95A")

            previous = Button(frame, text="PREVIOUS USER", fg="#FFF300", bg="#FF0000",
                              command=lambda: self.view_requests(index - 1))
            previous.pack(padx=(50, 50), side=LEFT)

            next = Button(frame, text="NEXT USER", fg="#FFF300", bg="#FF0000",
                          command=lambda: self.view_requests(index + 1))
            next.pack(padx=(50, 50), side=LEFT)

        if flag == 4:
            frame = Frame(self._root)
            frame.pack(pady=(60, 30))
            frame.config(background="#07B95A")

            previous = Button(frame, text="PREVIOUS USER", fg="#FFF300", bg="#FF0000",
                              command=lambda: self.view_matches(index - 1))
            previous.pack(padx=(50, 50), side=LEFT)

            next = Button(frame, text="NEXT USER", fg="#FFF300", bg="#FF0000",
                          command=lambda: self.view_matches(index + 1))
            next.pack(padx=(50, 50), side=LEFT)



    def propose(self, proposer_id,proposed_id):
        flag = self._db.insert_proposal(proposer_id,proposed_id)
        if flag == 1:
            messagebox.showinfo("CONGRATULATIONS DEAR","PROPOSAL SENT. FINGERS CROSSED")
        elif flag == 2:
            messagebox.showerror("SORRY","YOU HAVE ALREADY PROPOSED THIS USER")
        else:
            messagebox.showerror("SORRY", "CAN'T SEND THE PROPOSAL" )


    def view_proposals(self,index=0):
        data = self._db.fetch_proposals(self.user_id)

        if len(data) == 0:
            self.login_handler()
            messagebox.showerror("SORRY","YOU HAVE GOT NO PROPOSALS")
        else:
            new_data= []
            for i in data:
                new_data.append(i[3:])

            if index == 0:
                    self.clear()
                    self.main_window(new_data,flag = 2,index=0)
            else:
                if index<0:
                        messagebox.showerror("ERROR","NO USERS LEFT")
                elif index == len(new_data):
                        messagebox.showerror("ERROR","NO USERS LEFT")
                else:
                        self.clear()
                        self.main_window(new_data,flag=2,index=index)


    def view_requests(self,index = 0):
        data = self._db.fetch_requests(self.user_id)
        if len(data) == 0:
            self.login_handler()
            messagebox.showerror("SORRY","YOU HAVE SEND NO PROPOSAL REQUESTS")
        else:

            new_data = []
            for i in data:
                new_data.append(i[3:])
            if index == 0:
                self.clear()
                self.main_window(new_data,flag = 3,index = 0)
            else:
                if index<0:
                    messagebox.showerror("ERROR","NO USERS LEFT")
                elif index == len(new_data):
                    messagebox.showerror("ERROR","NO USERS LEFT")
                else:
                    self.clear()
                    self.main_window(new_data,flag = 3,index=index)


    def view_matches(self,index = 0):
        data = self._db.fetch_matches(self.user_id)
        if len(data) == 0:
            self.login_handler()
            messagebox.showerror("SORRY","YOU HAVE GOT NO MATCHES")
        else:
            new_data = []
            for i in data:
                new_data.append(i[3:])

            if index == 0:
                self.clear()
                self.main_window(new_data,flag= 4,index = 0)
            else:
                if index<0:
                    messagebox.showerror("ERROR","NO MORE MATCHES FOUND. CLICK NEXT")
                elif index == len(new_data):
                    messagebox.showerror("ERROR","NO MORE MATCHES FOUND. CLICK PREVIOUS")
                else:
                    self.clear()
                    self.main_window(new_data,flag=4,index=index)

    def login_handler(self):

        self.clear()
        self.headermenu()
        data = self._db.fetch_userdata(self.user_id)
        self.main_window(data)


    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()


    def edit_profile(self):
        data= self._db.fetch_userdata(self.user_id)
        self.clear()
        self._edit_name = Label(self._root, text="UPDATE YOUR FULL NAME", fg="#070FB9", bg="#07B95A")
        self._edit_name.config(font=("Arial", 18))
        self._edit_name.pack(pady=(0, 8))

        self._update_nameInput = Entry(self._root)
        self._update_nameInput.pack(pady=(0, 8), ipady=10, ipadx=70)
        self._update_nameInput.insert(0,data[0][1])


        self._edit_age = Label(self._root, text="HAVE A DOUBT WITH YOUR AGE?", fg="#070FB9",bg="#07B95A")
        self._edit_age.config(font=("Arial", 14))
        self._edit_age.pack(pady=(0, 8))

        self._update_ageInput = Entry(self._root)
        self._update_ageInput.pack(pady=(0, 8), ipady=10, ipadx=70)
        self._update_ageInput.insert(0,data[0][4])

        self._edit_city = Label(self._root, text="HAVE YOU CHANGED YOUR CITY", fg="#070FB9", bg="#07B95A")
        self._edit_city.config(font=("Arial", 18))
        self._edit_city.pack(pady=(0, 8))

        self._update_cityInput = Entry(self._root)
        self._update_cityInput.pack(pady=(0, 8), ipady=10, ipadx=70)
        self._update_cityInput.insert(0,data[0][6])

        self._dpButton = Button(self._root, text="UPLOAD A NICE PROFILE PICTURE", fg="#070FB9", bg="#07B95A",command=lambda: self.select_dp())
        self._dpButton.config(font=("Times", 10))
        self._dpButton.pack(pady=(0, 10))

        self._dp_filename = Label(self._root)
        self._dp_filename.pack()



        self._update_btn = Button(self._root, text="UPDATE YOUR DETAILS", fg="#070FB9", bg="#07B95A",command=lambda: self.edit_info())
        self._update_btn.config(font=("Times", 10))
        self._update_btn.pack(pady=(0, 10))


    def edit_info(self):
        original_dp_name = self._filename.split("/")[-1]

        flag= self._db.update_info(self._update_nameInput.get(),self._update_ageInput.get(),self._update_cityInput.get(),original_dp_name,self.user_id)
        if flag == 1:
            destination = "C:\\Users\\CHIRADEEP GHOSH\\PycharmProjects\\TINDER\\images\\" + original_dp_name
            shutil.copyfile(self._filename, destination)
            messagebox.showinfo("SUCCESS","YOUR PROFILE HAS BEEN SUCCESSFULLY UPDATED")
        else:
            messagebox.showerror("ERROR","SOMETHING WENT WRONG. PLEASE TRY AGAIN")


    def view_others(self,index=0):

        data = self._db.fetch_otheruserdata(self.user_id)

        if index == 0:
            self.clear()
            self.main_window(data,flag=1,index=0)
        else:
            if index<0:
                messagebox.showerror("NO USERS LEFT","CLICK ON NEXT")
            elif index == len(data):
                messagebox.showerror("NO USERS LEFT","CLICK ON PREVIOUS")
            else:
                self.clear()
                self.main_window(data,flag=1,index=index)


    def logout(self):
        self.is_logged_in=0
        self._root.destroy()
        self.load_login_window()


    def headermenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home",menu = filemenu)
        filemenu.add_command(label="My Profile",command = lambda: self.login_handler())
        filemenu.add_command(label= "Edit My Profile",command= lambda : self.edit_profile())
        filemenu.add_command(label="View Others Profile",command= lambda: self.view_others())
        filemenu.add_command(label="About US", command=lambda: self.logo())
        filemenu.add_command(label="Log Out",command= lambda:self.logout())
        filemenu.config(background = "#FFF300")

        helpmenu= Menu(menu)
        menu.add_cascade(label= "Proposals", menu= helpmenu)
        helpmenu.add_command(label="My Proposals",command = lambda: self.view_proposals())
        helpmenu.add_command(label="My Requests",command = lambda :self.view_requests())
        helpmenu.add_command(label= "My Matches",command = lambda :self.view_matches())
        helpmenu.config(background = "#FFF300")












obj= Tinder()






