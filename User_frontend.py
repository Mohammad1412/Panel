# You have to run with images else you give an error

import User_Backend as Backend
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from random import randint
from time import strftime
from hashlib import sha512
from os import path
from sys import modules

def TopLevel(Title, Geometry, Resize_Width= False, Resize_Height= False):
    Win_Name = Toplevel(win)
    Win_Name.title(Title)
    Win_Name.geometry(Geometry)
    Win_Name.resizable(Resize_Width, Resize_Height)
    return Win_Name

def Registry():
    global User_Name, User_Family, User_Year, User_Month, User_Day, User_Username, User_Password, User_Confirm_Password\
        , User_National, User_Phone, User_Email, User_Answer, result, Registry_win
    Registry_win = TopLevel('Registry', '210x370')

    Label(Registry_win, text= 'Name :').place(x= 0, y= 5)
    User_Name = Entry(Registry_win, width= 24)
    User_Name.place(x= 45, y= 7)

    Label(Registry_win, text= 'Family :').place(x= 0, y= 35)
    User_Family = Entry(Registry_win, width= 17)
    User_Family.place(x= 45, y= 37)

    Label(Registry_win, text= 'Berth :').place(x= 0, y= 65)
    User_Year = Spinbox(Registry_win, from_= int(strftime('%Y'))-120, to= int(strftime('%Y')), width= 5)
    User_Year.place(x= 45, y= 67)
    Label(Registry_win, text= '/              /').place(x= 90, y= 67)
    User_Month = Spinbox(Registry_win, from_= 1, to= 12, width= 3)
    User_Month.place(x= 102, y= 67)
    User_Day = Spinbox(Registry_win, from_= 1, to= 31, width= 3)
    User_Day.place(x= 150, y= 67)

    Label(Registry_win, text= 'Username :').place(x= 0, y= 95)
    User_Username = Entry(Registry_win, width= 20)
    User_Username.place(x= 65, y= 97)

    Label(Registry_win, text= 'Password :').place(x= 0, y= 125)
    User_Password = Entry(Registry_win, width= 20, show= '*')
    User_Password.place(x= 65, y= 127)

    Label(Registry_win, text= 'Confirm\npassword :').place(x= 0, y= 147)
    User_Confirm_Password = Entry(Registry_win, width= 20, show= '*')
    User_Confirm_Password.place(x= 65, y= 157)

    Label(Registry_win, text= 'Country :').place(x= 0, y= 185)
    User_National = Spinbox(Registry_win, values= countries.split('-'), width= 23, state= 'readonly')
    User_National.place(x= 53, y= 187)

    Label(Registry_win,text= 'Phone :').place(x= 5, y= 215)
    User_Phone = Entry(Registry_win, width= 12)
    User_Phone.place(x= 50, y= 217)

    Label(Registry_win, text= 'Email :').place(x= 0, y= 245)
    User_Email = Entry(Registry_win, width= 27)
    User_Email.place(x= 39, y= 247)

    Label(Registry_win, text= '-----------I`m not a robot !!-----------').place(x= 4, y= 275)
    num1 = randint(0, 9)
    num2 = randint(0, 9)
    num3 = randint(0, 9)
    result = str(num1 + num2 - num3)
    Label(Registry_win, text= f'Write the result of {num1} + {num2} - {num3} :').place(x= 10, y= 305)
    User_Answer = Entry(Registry_win, width= 5)
    User_Answer.place(x= 165, y= 307)

    Register_Button = Button(Registry_win, text= 'Register', command= Register)
    Register_Button.place(x= 75, y= 335)

def Register():
    User_Berth = f'{User_Year.get()}/{User_Month.get()}/{User_Day.get()}'
    R1 = Backend.check.property(Check, User_Name.get(), User_Family.get(), User_Berth)
    R2 = Backend.check.username(Check, User_Username.get())
    R3 = User_Password.get() == User_Confirm_Password.get() and len(User_Password.get()) >= 6
    R4 = len(User_Phone.get()) == 11
    R5 = '@' in User_Email.get() and '.com' in User_Email.get()
    R6 = User_Answer.get() == result
    if not R1:
        if not R2:
            if R3:
                if R4:
                    if R5:
                        if R6:
                            x1 = int(User_Password.get()[0])
                            x2 = int(User_Password.get()[1])
                            x3 = int(User_Password.get()[2])
                            x4 = int(User_Password.get()[3])
                            x5 = int(User_Password.get()[4])
                            x6 = int(User_Password.get()[5])
                            IsAdmin = False
                            if x2 != 0 and x4 != 0:
                                if ((x1 + x6 - x3) * x5) % (x2 * x4) == 0 and (x1 + x2 + x3 + x4 + x5 + x6
                                )% 5 == 0 and (x1 + x2 + x3 + x4 + x5 + x6) % 7 == 0:
                                    if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and (
                                            x1 + 1) != x2 and (x1 - 1) != x2:
                                        if x2 != x3 and x2 != x4 and x2 != x5 and x2 != x6 and (x2 + 1) != x3 and (
                                                x2 - 1) != x3:
                                            if x3 != x4 and x3 != x5 and x3 != x6 and (x3 + 1) != x4 and (
                                                    x3 - 1) != x4:
                                                if x4 != x5 and x4 != x6 and (x4 + 1) != x5 and (x4 - 1) != x5:
                                                    if x5 != x6 and (x5 + 1) != x6 and (x5 - 1) != x6:
                                                        IsAdmin = True

                            if (User_Username.get()[0] == 'A' and User_Username.get()[-1] == 'M') and IsAdmin:
                                messagebox.showinfo('Congratulation', 'Now you add to Admins')
                                Backend.Admin.admin_register(Admin, User_Name.get(), User_Family.get(), User_Berth, User_Username.get()[1:-1], sha512(User_Password.get().encode).hexdigest(), User_Phone.get(), User_Email.get(), User_National.get())
                                Registry_win.destroy()
                                win.mainloop()
                            else:
                                messagebox.showinfo('Congratulation', 'Now you add to Users')
                                Backend.User.user_register(User, User_Name.get(), User_Family.get(), User_Berth, User_Username.get(), sha512(User_Password.get().encode).hexdigest(), User_Phone.get(), User_Email.get(), User_National.get())
                                Registry_win.quit()
                                win.mainloop()

                        else:
                            messagebox.showerror('Error', 'Your security code is incorrect')
                    else:
                        messagebox.showerror('Error', 'your email is unnatural')
                else:
                    messagebox.showerror('Error', 'your phone is unnatural')
            else:
                messagebox.showerror('Error', 'Password and Confirm password has different or The password should be more than 8 characters')
        else:
            messagebox.showerror('Error', 'this username used')
    else:
        messagebox.showerror('Error', 'someone has been registered with this property')

def Enter():
    global Enter_win, User_username, User_password, Result, User_answer, Is_Admin

    def is_Admin():
        global Is_Admin
        if var.get():
            Is_Admin = True
        else:
            Is_Admin = False

    Enter_win = TopLevel('Log in', '200x250')

    Label(Enter_win, text= 'Username :').place(x= 5, y= 10)
    User_username = Entry(Enter_win, width= 20)
    User_username.place(x= 70, y= 12)

    Label(Enter_win, text= 'Password :').place(x= 5, y= 40)
    User_password = Entry(Enter_win, width= 20, show= '*')
    User_password.place(x= 70, y= 42)

    var = IntVar()
    Is_Admin = False
    If_Admin = Checkbutton(Enter_win, text= 'Admin', variable= var, onvalue= 1, offvalue= 0, command= is_Admin).place(x= 10, y= 70)

    Label(Enter_win, text= '----------I`m not robot !!----------').place(x= 5, y= 100)
    num1 = randint(0, 9)
    num2 = randint(0, 9)
    num3 = randint(0, 9)
    Result = str(num1 + num2 - num3)
    Label(Enter_win, text= f'Write the result of {num1} + {num2} - {num3} :').place(x= 5, y= 130)
    User_answer = Entry(Enter_win, width= 5)
    User_answer.place(x= 160, y= 132)

    Enter_button = Button(Enter_win, text= 'Login', command= Input)
    Enter_button.place(x= 75, y= 160)

def Input():
    global Username, Admin_Name, R1
    Username = User_username.get()
    if User_answer.get() == Result:
        if Is_Admin:
            Admin_Name = Backend.Admin.admin_input(Admin, User_username.get(), sha512(User_password.get().encode()).hexdigest())
            if Admin_Name != []:
                messagebox.showinfo('Congratulations', 'You logged in to admin`s panel')
                Admin_Name = Admin_Name[0][2:4]
                Admin_Panel()
            else:
                messagebox.showerror('Error', 'Your username or password is incorrect')
        else:
            R1 = Backend.User.user_input(User, User_username.get(), sha512(User_Password.get().encode).hexdigest())
            if R1 != []:
                messagebox.showinfo('Congratulations', 'You logged in to User`s panel')
                R1 = R1[0]
                User_Panel()
            else:
                messagebox.showerror('Error', 'Your username or password is incorrect')
    else:
        messagebox.showerror('Error', 'Your security code is incorrect')

def Admin_Panel():
    def main():
        global View_User, View_Messages, Username
        Enter_win.quit()
        for widget in Frame.winfo_children(win):
            widget.destroy()
        Username = 'Mohammad'
        win.title('Admin Panel')
        win.geometry('890x550')
        Label(win, text= f'{Admin_Name[0]} {Admin_Name[1]}').place(x= 100, y= 7)
        Back_Image = ImageTk.PhotoImage(Image.open(f'{path}Back.png'))
        Delete_Image = ImageTk.PhotoImage(Image.open(f'{path}Delete.png'))
        Edit_Image = ImageTk.PhotoImage(Image.open(f'{path}Edit.png'))
        Refresh_Image = ImageTk.PhotoImage(Image.open(f'{path}Refresh.png'))
        Add_User_Image = ImageTk.PhotoImage(Image.open(f'{path}Add.png'))
        Search_Image = ImageTk.PhotoImage(Image.open(f'{path}Search.png'))
        Message_Image = ImageTk.PhotoImage(Image.open(f'{path}Send Message.png'))
        Reset_Password_Image = ImageTk.PhotoImage(Image.open(f'{path}Reset password.png'))
        Star_Image = ImageTk.PhotoImage(Image.open(f'{path}Star.png'))
        Back_Button = Button(win, image=Back_Image, borderwidth=0, command=Back)
        Back_Button.place(x=5, y=5)
        Remove_Button = Button(win, image=Delete_Image, borderwidth=0, command=Remove)
        Remove_Button.place(x=35, y=5)
        Edit_Button = Button(win, image=Edit_Image, borderwidth=0, command=Edit)
        Edit_Button.place(x=65, y=5)

        View_User = Treeview(win, columns=('1', '2', '3', '4', '5', '6', '7', '8', '9'), show='headings', height=10)
        View_User.heading('1', text='Id')
        View_User.column('1', width=10)
        View_User.heading('2', text='Time registry')
        View_User.column('2', width=115)
        View_User.heading('3', text='Name')
        View_User.column('3', width=120)
        View_User.heading('4', text='Family')
        View_User.column('4', width=90)
        View_User.heading('5', text='Berth')
        View_User.column('5', width=65)
        View_User.heading('6', text='Username')
        View_User.column('6', width=80)
        View_User.heading('7', text='Phone')
        View_User.column('7', width=75)
        View_User.heading('8', text='Email')
        View_User.column('8', width=200)
        View_User.heading('9', text='Country')
        View_User.column('9', width=65)
        View_User.place(x=40, y=40)
        View_User.bind('<<TreeviewSelect>>', Admin_Column_Select)
        View_User.bind('<Double-1>', Admin_Column_Double_Click)
        View_User_Scrollbar = Scrollbar(win, orient=VERTICAL)
        View_User_Scrollbar.place(x=865, y=40)
        View_User.configure(yscrollcommand=View_User_Scrollbar.set)
        View_User_Scrollbar.configure(command=View_User.yview)
        User_Refresh()
        User_Refresh_Button = Button(win, image=Refresh_Image, borderwidth=0, command=User_Refresh)
        User_Refresh_Button.place(x=5, y=40)
        Add_User_Button = Button(win, image=Add_User_Image, borderwidth=0, command=Add_User)
        Add_User_Button.place(x=5, y=70)
        User_Search_Button = Button(win, image=Search_Image, borderwidth=0, command=User_Search)
        User_Search_Button.place(x=5, y=100)
        Message_Button = Button(win, image=Message_Image, borderwidth=0, command=Send_Message)
        Message_Button.place(x=5, y=130)
        User_Reset_Password_Button = Button(win, image=Reset_Password_Image, borderwidth=0, command=User_Reset_Password)
        User_Reset_Password_Button.place(x=5, y=160)
        User_Kick_Button = Button(win, image=Delete_Image, borderwidth=0, command=User_Kick)
        User_Kick_Button.place(x=5, y=190)
        View_Messages = Treeview(win, columns=('1', '2', '3', '4', '5', '6'), show='headings', height=10)
        View_Messages.heading('1', text='Id')
        View_Messages.column('1', width=10)
        View_Messages.heading('2', text='Time send')
        View_Messages.column('2', width= 120)
        View_Messages.heading('3', text= 'Transmitter')
        View_Messages.column('3', width= 130)
        View_Messages.heading('4', text= 'Title')
        View_Messages.column('4', width= 130)
        View_Messages.heading('5', text= 'Message')
        View_Messages.column('5', width= 310)
        View_Messages.heading('6', text= 'status')
        View_Messages.column('6', width= 120)
        View_Messages.place(x= 40, y= 280)
        View_Messages.bind('<Double-1>', Message_Column_Double_Click)
        View_Messages.bind('<<TreeviewSelect>>', Message_Column_Select)
        View_Message_Scrollbar = Scrollbar(win, orient= VERTICAL)
        View_Message_Scrollbar.place(x=865, y=280)
        View_Messages.configure(yscrollcommand= View_Message_Scrollbar.set)
        View_Message_Scrollbar.configure(command= View_Messages.yview)

        Message_Refresh()
        Message_Refresh_Button = Button(win, image= Refresh_Image, borderwidth=0, command=Message_Refresh)
        Message_Refresh_Button.place(x= 5, y= 280)
        Star_Button = Button(win, image= Star_Image, borderwidth= 0, command= Star_Message)
        Star_Button.place(x= 5, y= 310)
        Message_Delete_Button = Button(win, image=Delete_Image, borderwidth=0, command= Delete_Message)
        Message_Delete_Button.place(x=5, y=340)
        win.mainloop()

    def Admin_Column_Select(Users):
        try:
            global User_Properties
            Id = View_User.item(View_User.selection())['values'][0]
            User_Properties = Backend.check.get_user(Check, Id)
            User_Properties = [User_Properties[0], f'{User_Properties[2]} {User_Properties[3]}', User_Properties[5]]
        except:
            messagebox.showerror('Admin Panel', 'you should select one item')
            User_Refresh()

    def Admin_Column_Double_Click(Msg):
        try:
            User_Properties = View_User.item(View_User.selection())['values']
            Show_UP = TopLevel('User Properties', '247x300')
            Message(Show_UP, text= f'{User_Properties[0]}.').place(x= 2, y= 2)
            Message(Show_UP, text= User_Properties[2]+User_Properties[3], width= 200).place(x= 20, y= 2)
            Message(Show_UP, text= f'Berth : {User_Properties[4]}', width= 100).place(x= 2, y= 25)
            Message(Show_UP, text= f'Country : {User_Properties[8]}', width= 100).place(x= 120, y= 25)
            Message(Show_UP, text= f'Username : {User_Properties[5]}', width= 250).place(x= 2, y= 50)
            Message(Show_UP, text= f'Phone : {User_Properties[6]}', width= 200).place(x= 2, y= 75)
            Message(Show_UP, text= f'Email : {User_Properties[7]}', width= 300).place(x= 2, y= 100)
            Message(Show_UP, text= f'Time Registry : {User_Properties[1]}', width= 200).place(x= 2, y= 125)
            Show_UP.mainloop()
        except:
            messagebox.showerror('Admin Panel', 'You should click one User')

    def Message_Column_Select(Msg):
        try:
            global Message_Properties
            Message_Properties = [*View_Messages.item(View_Messages.selection())['values'], View_Messages.selection()[0]]
        except:
            messagebox.showerror('Admin Panel', 'You should select one message')
            Message_Refresh()

    def Message_Column_Double_Click(Msg):
        try:
            Message_Properties = View_Messages.item(View_Messages.selection())['values']
            Show_MP = TopLevel('Message Properties', '270x350')
            Message(Show_MP, text= f'{Message_Properties[0]}.').place(x= 2, y= 2)
            Message(Show_MP, text= f'Transmitter : {Message_Properties[2]}', width= 200).place(x= 100, y= 2)
            Message(Show_MP, text= f'Title : {Message_Properties[3]}', width= 100).place(x= 2, y= 30)
            Message(Show_MP, text= Message_Properties[4], width= 250).place(x= 12, y= 60)
            Message(Show_MP, text= f'Time Send : {Message_Properties[1]}', width= 200).place(x= 80, y= 320)
        except:
            messagebox.showerror('Admin Panel', 'You should click one message')

    def Back():
        for widget2 in Frame.winfo_children(win):
            widget2.destroy()
        win.title('Registry/Enter')
        win.geometry('400x200')
        RB = Button(win, text='Registry', height=1, command=Registry)
        RB.place(x=150, y=80)
        Label(win, text='/', font=('mitraa', 20)).place(x=200, y=76)
        EB = Button(win, text='Enter', height=1, command=Enter)
        EB.place(x=220, y=80)

    def Remove():
        R1 = messagebox.askyesno('Delete account', 'Are you sure you want to delete your account ?')
        if R1:
            Backend.Admin.admin_exit(Admin, Username)
            Back()

    def Edit():
        def edit():
            R1 = Admin_Password.get() == Admin_Confirm_Password.get() and len(Admin_Password.get()) >= 6
            R2 = len(Admin_Phone.get()) == 11
            R3 = '@' in Admin_Email.get() and '.com' in Admin_Email.get()
            R4 = Admin_Answer.get() == Admin_result
            if R1 and R2 and R3 and R4:
                answer = messagebox.askyesno('Edit', 'Are you sure you want to change your profile')
                if answer:
                    Id = Backend.Admin.get_id(Admin, Username)
                    Backend.Admin.admin_edit(Admin, Id, sha512(Admin_Password.get().encode()).hexdigest(), Admin_Phone.get(), Admin_Email.get(), Admin_National.get())
            else:
                messagebox.showerror('Edit', 'Anyone has problem')

        global Admin_Password, Admin_Confirm_Password, Admin_National, Admin_Phone, Admin_Email, Admin_result, Admin_Answer
        Edit_win = TopLevel('Edit me', '210x250')

        Label(Edit_win, text= 'Password :').place(x= 0, y= 5)
        Admin_Password = Entry(Edit_win, width= 20, show='*')
        Admin_Password.place(x= 65, y= 7)

        Label(Edit_win, text= 'Confirm\npassword :').place(x= 0, y= 27)
        Admin_Confirm_Password = Entry(Edit_win, width= 20, show='*')
        Admin_Confirm_Password.place(x= 65, y= 37)

        Label(Edit_win, text= 'Country :').place(x= 0, y= 65)
        Admin_National = Spinbox(Edit_win, values= countries.split('-'), width= 23, state='readonly')
        Admin_National.place(x= 53, y= 67)

        Label(Edit_win,text= 'Phone :').place(x= 5, y= 95)
        Admin_Phone = Entry(Edit_win, width= 12)
        Admin_Phone.place(x= 50, y= 97)

        Label(Edit_win, text= 'Email :').place(x= 0, y= 125)
        User_Email = Entry(Edit_win, width= 27)
        User_Email.place(x= 39, y= 127)

        Label(Edit_win, text= '-----------I`m not a robot !!-----------').place(x= 4, y= 155)
        num1 = randint(0, 9)
        num2 = randint(0, 9)
        num3 = randint(0, 9)
        Admin_result = str(num1 + num2 - num3)
        Label(Edit_win, text= f'Write the result of {num1} + {num2} - {num3} :').place(x= 10, y= 185)
        Admin_Answer = Entry(Edit_win, width= 5)
        Admin_Answer.place(x= 165, y= 187)

        AE_Button = Button(Edit_win, text= 'Edit', command= edit)
        AE_Button.place(x= 75, y= 215)

    def User_Refresh():
        Users = Backend.Admin.user_view(Admin)
        View_User.delete(*View_User.get_children())
        for user in Users:
            View_User.insert('', END,values= user)

    def Add_User():
        Registry()

    def User_Search():
        def search():
            Users = Backend.check.search(Check, Name_Search.get(), Family_Search.get(), Username_Search.get(), Phone_Search.get(), Email_Search.get(), National_Search.get())
            View_User.delete(*View_User.get_children())
            for user in Users:
                View_User.insert('', END,values= user)
        Search_win = TopLevel('Search', '203x300')
        Label(Search_win, text= 'Name :').place(x= 0, y= 5)
        Name_Search = Entry(Search_win, width= 25)
        Name_Search.place(x= 45, y= 7)
        Label(Search_win, text= 'Family :').place(x= 0, y= 35)
        Family_Search = Entry(Search_win, width= 25)
        Family_Search.place(x= 45, y= 37)
        Label(Search_win, text= 'Username :').place(x= 0, y= 65)
        Username_Search = Entry(Search_win, width= 21)
        Username_Search.place(x= 65, y= 67)
        Label(Search_win, text= 'Phone :').place(x= 0, y= 95)
        Phone_Search = Entry(Search_win, width= 25)
        Phone_Search.place(x= 45, y= 97)
        Label(Search_win, text= 'Email :').place(x= 0, y= 125)
        Email_Search = Entry(Search_win, width= 25)
        Email_Search.place(x= 45, y= 127)
        Label(Search_win, text= 'Country :').place(x= 0, y= 155)
        National_Search = Spinbox(Search_win, values=countries.split('-'), width=22, state='readonly')
        National_Search.place(x=55, y=157)
        search_Button = Button(Search_win, text= 'Search', command= search)
        search_Button.place(x= 80, y= 185)
        Search_win.mainloop()

    def Send_Message():
        def Send():
            R = messagebox.askyesno('Send Message', 'Are you want to send a message ??')
            if R:
                if Title_Enter.get():
                    Backend.Admin.send_message(Admin, User_Properties[2], Title_Enter.get(), Text_Enter.get('1.0', END))
                    SM_Win.destroy()
                else:
                    messagebox.showinfo('Send Message', 'You don`t fill title')
        SM_Win = TopLevel('Send Message', '243x300', False, False)
        Label(SM_Win, text= f'To {User_Properties[2]}').place(x= 5, y= 5)
        Label(SM_Win, text= 'Title :').place(x= 5, y= 30)
        Title_Enter = Entry(SM_Win, width= 20)
        Title_Enter.place(x= 40, y= 32)
        Text_Enter = Text(SM_Win, width= 28, height= 14)
        Text_Enter.place(x= 5, y= 55)
        Send_Button = Button(SM_Win, text= 'Send', height= 1, command= Send)
        Send_Button.place(x= 190, y= 29)

    def User_Reset_Password():
        New_Password = str(randint(100000, 1000000))
        Backend.Admin.user_reset_password(Admin, User_Properties[0], sha512(New_Password.encode()).hexdigest())
        messagebox.showinfo('Change password', f'You changed the password of user {User_Properties[1]} to {New_Password}')

    def User_Kick():
        Backend.Admin.user_remove(Admin, User_Properties[2])

    def Message_Refresh():
        Messages = Backend.Admin.message_view(Admin, Username).split('-')
        View_Messages.delete(*View_Messages.get_children())
        for message in Messages:
            View_Messages.insert('', END,values= message.split(','))

    def Star_Message():
        View_Messages.delete(Message_Properties[6])
        PMessage = Backend.Admin.message_view(Admin, Username).split('-')[Message_Properties[0]-1].split(',')
        if Message_Properties[-2] == 'Star':
            View_Messages.insert('', Message_Properties[0]-1, values= [*PMessage[:-1], 'UnStar'])
            Backend.check.starring(Check, 'Admin', Backend.Admin.get_id(Admin, Username), Message_Properties[0], 'UnStar')
        else:
            View_Messages.insert('', Message_Properties[0]-1, values= [*PMessage[:-1], 'Star'])
            Backend.check.starring(Check, 'Admin', Backend.Admin.get_id(Admin, Username), Message_Properties[0], 'Star')

    def Delete_Message():
        R = messagebox.askokcancel('Delete Message', 'Are you sure you want delete this message')
        if R:
            Backend.check.deleting(Check, 'Admin', Backend.Admin.get_id(Admin, Username),Message_Properties[0])
            Message_Refresh()

    main()

def User_Panel():
    def main():
        global UserP, View_Messages
        Enter_win.quit()
        UserP = R1
        for widget in Frame.winfo_children(win):
            widget.destroy()
        win.title('User Panel')
        win.geometry('700x432')
        Label(win, text=f'{UserP[2]} {UserP[3]}').place(x=500, y=5)
        Back_Image = ImageTk.PhotoImage(Image.open(f'{path}Back.png'))
        Delete_Image = ImageTk.PhotoImage(Image.open(f'{path}Delete.png'))
        Edit_Image = ImageTk.PhotoImage(Image.open(f'{path}Edit.png'))
        Refresh_Image = ImageTk.PhotoImage(Image.open(f'{path}Refresh.png'))
        Star_Image = ImageTk.PhotoImage(Image.open(f'{path}Star.png'))
        Back_Button = Button(win, image= Back_Image, borderwidth= 0, command= Back)
        Back_Button.place(x= 5, y= 5)
        Remove_Button = Button(win, image= Delete_Image, borderwidth= 0, command= Remove)
        Remove_Button.place(x= 35, y= 5)
        Edit_Button = Button(win, image= Edit_Image, borderwidth= 0, command= Edit)
        Edit_Button.place(x= 65, y= 5)
        # Select_Image = Button(win, text='Select', command=Image_Select)
        # Select_Image.place(x=95, y=5)
        View_Messages = Treeview(win, columns= ('1', '2', '3', '4', '5', '6'), show= 'headings', height= 15)
        View_Messages.heading('1', text= 'Id')
        View_Messages.column('1', width= 10)
        View_Messages.heading('2', text= 'Time send')
        View_Messages.column('2', width= 110)
        View_Messages.heading('3', text= 'Transmitter')
        View_Messages.column('3', width= 90)
        View_Messages.heading('4', text= 'Title')
        View_Messages.column('4', width= 90)
        View_Messages.heading('5', text= 'Message')
        View_Messages.column('5', width= 265)
        View_Messages.heading('6', text= 'status')
        View_Messages.column('6', width= 60)
        View_Messages.place(x= 40, y= 35)
        View_Messages.bind('<<TreeviewSelect>>', Message_Column_Select)
        # View_Messages.bind('<Double-1>', Message_Column_Double_Click)
        View_Message_Scrollbar = Scrollbar(win, orient=VERTICAL)
        View_Message_Scrollbar.place(x= 670, y= 35)
        View_Messages.configure(yscrollcommand=View_Message_Scrollbar.set)
        View_Message_Scrollbar.configure(command=View_Messages.yview)
        Message_Refresh()
        Refresh_Button = Button(win, image= Refresh_Image, borderwidth= 0, command= Message_Refresh)
        Refresh_Button.place(x= 5, y= 35)
        Star_Button = Button(win, image= Star_Image, borderwidth= 0, command= Star_Message)
        Star_Button.place(x= 5, y= 65)
        Delete_Button = Button(win, image= Delete_Image, borderwidth= 0, command= Delete_Message)
        Delete_Button.place(x= 5, y= 95)
        win.mainloop()

    def Message_Column_Select(Msg):
        try:
            global Message_Properties
            Message_Properties = [*View_Messages.item(View_Messages.selection())['values'], View_Messages.selection()[0]]
        except:
            messagebox.showerror('User Panel', 'You should select one Message')
            Message_Refresh()

    def Message_Column_Double_Click(Msg):
        try:
            Message_Properties = View_Messages.item(View_Messages.selection())['values']
            Show_MP = TopLevel('Message Properties', '270x350')
            Message(Show_MP, text=f'{Message_Properties[0]}.').place(x=2, y=2)
            Message(Show_MP, text=f'Transmitter : {Message_Properties[2]}', width=200).place(x=100, y=2)
            Message(Show_MP, text=f'Title : {Message_Properties[3]}', width=100).place(x=2, y=30)
            Message(Show_MP, text=Message_Properties[4], width=250).place(x=12, y=60)
            Message(Show_MP, text=f'Time Send : {Message_Properties[1]}', width=200).place(x=80, y=320)
        except:
            messagebox.showerror('User Panel', 'You should be click a one message ')

    def Back():
        for widget2 in Frame.winfo_children(win):
            widget2.destroy()
        win.title('Registry/Enter')
        win.geometry('400x200')
        RB = Button(win, text='Registry', height=1, command=Registry)
        RB.place(x=150, y=80)
        Label(win, text='/', font=('mitraa', 20)).place(x=200, y=76)
        EB = Button(win, text='Enter', height=1, command=Enter)
        EB.place(x=220, y=80)

    def Remove():
        R1 = messagebox.askyesno('Delete account', 'Are you sure you want to delete your account ?')
        if R1:
            Backend.User.user_exit(User, UserP[5])
            Back()

    def Edit():
        def edit():
            R1 = User_Password.get() == User_Confirm_Password.get() and len(User_Password.get()) >= 6
            R2 = len(User_Phone.get()) == 11
            R3 = '@' in User_Email.get() and '.com' in User_Email.get()
            R4 = User_Answer.get() == User_result
            if R1 and R2 and R3 and R4:
                answer = messagebox.askyesno('Edit', 'Are you sure you want to change your profile')
                if answer:
                    Backend.User.user_edit(User, UserP[0], sha512(User_Password.get().encode()).hexdigest(), User_Phone.get(), User_Email.get(), User_National.get())
            else:
                messagebox.showerror('Edit', 'Someone has problem')

        global User_Password, User_Confirm_Password, User_National, User_Phone, User_Email, Admin_result, Admin_Answer
        Edit_win = TopLevel('Edit me', '210x250')

        Label(Edit_win, text= 'Password :').place(x= 0, y= 5)
        User_Password = Entry(Edit_win, width= 20, show='*')
        User_Password.place(x= 65, y= 7)

        Label(Edit_win, text= 'Confirm\npassword :').place(x= 0, y= 27)
        User_Confirm_Password = Entry(Edit_win, width= 20, show='*')
        User_Confirm_Password.place(x= 65, y= 37)

        Label(Edit_win, text= 'Country :').place(x= 0, y= 65)
        User_National = Spinbox(Edit_win, values= countries.split('-'), width= 23, state='readonly')
        User_National.place(x= 53, y= 67)

        Label(Edit_win,text= 'Phone :').place(x= 5, y= 95)
        User_Phone = Entry(Edit_win, width= 12)
        User_Phone.place(x= 50, y= 97)

        Label(Edit_win, text= 'Email :').place(x= 0, y= 125)
        User_Email = Entry(Edit_win, width= 27)
        User_Email.place(x= 39, y= 127)

        Label(Edit_win, text= '-----------I`m not a robot !!-----------').place(x= 4, y= 155)
        num1 = randint(0, 9)
        num2 = randint(0, 9)
        num3 = randint(0, 9)
        User_result = str(num1 + num2 - num3)
        Label(Edit_win, text= f'Write the result of {num1} + {num2} - {num3} :').place(x= 10, y= 185)
        User_Answer = Entry(Edit_win, width= 5)
        User_Answer.place(x= 165, y= 187)

        UE_Button = Button(Edit_win, text= 'Edit', command= edit)
        UE_Button.place(x= 75, y= 215)

    def Message_Refresh():
        View_Messages.delete(*View_Messages.get_children())
        Messages = Backend.User.message_view(User, UserP[5])
        for message in Messages:
            View_Messages.insert('', END,values= message.split(','))

    def Send_Message():
        def Send():
            R = messagebox.askyesno('Send Message', 'Are you want to send a message ??')
            if R:
                if Title_Enter.get():
                    Backend.Admin.send_message(Admin, User_Properties[2], Title_Enter.get(), Text_Enter.get('1.0', END))
                    SM_Win.destroy()
                else:
                    messagebox.showinfo('Send Message', 'You don`t fill title')
        SM_Win = TopLevel('Send Message', '243x300', False, False)
        Label(SM_Win, text= f'To {User_Properties[2]}').place(x= 5, y= 5)
        Label(SM_Win, text= 'Title :').place(x= 5, y= 30)
        Title_Enter = Entry(SM_Win, width= 20)
        Title_Enter.place(x= 40, y= 32)
        Text_Enter = Text(SM_Win, width= 28, height= 14)
        Text_Enter.place(x= 5, y= 55)
        Send_Button = Button(SM_Win, text= 'Send', height= 1, command= Send)
        Send_Button.place(x= 190, y= 29)

    def Star_Message():
        try:
            View_Messages.delete(Message_Properties[6])
            PMessage = Backend.User.message_view(User, UserP[5])[Message_Properties[0]-1].split(',')
            if Message_Properties[-2] == 'Star':
                View_Messages.insert('', Message_Properties[0]-1, values= [*PMessage[:-1], 'UnStar'])
                Backend.check.starring(Check, 'User', UserP[0], Message_Properties[0], 'UnStar')
            else:
                View_Messages.insert('', Message_Properties[0]-1, values= [*PMessage[:-1], 'Star'])
                Backend.check.starring(Check, 'User', UserP[0], Message_Properties[0], 'Star')
        except:
            messagebox.showerror('User Panel', 'You don`t select a message')

    def Delete_Message():
        R = messagebox.askokcancel('Delete Message', 'Are you sure you want delete this message')
        if R:
            Backend.check.deleting(Check, 'User', UserP[0], Message_Properties[0])
            Message_Refresh()

    # def Image_Select():
    #     pass

    main()

win = Tk()
win.title('Registry/Enter')
win.geometry('400x200')
win.resizable(0, 0)
path = path.dirname(modules['__main__'].__file__)+'\\'
countries = '''Afghanistan-Albania-Algeria-Andorra-Angola-Antigua and Barbuda-Argentina-Armenia-Australia-Austria-Azerbaijan-The Bahamas-Bahrain-Bangladesh-Barbados-Belarus-Belgium-Belize-Benin-Bhutan-
Bolivia-Bosnia and Herzegovina-Botswana-Brazil-Brunei-Bulgaria-Burkina Faso-Burundi-Cabo Verde-Cambodia-Cameroon-Canada-Central African Republic-Chad-Chile-China-Colombia-Comoros-Congo-Cute d’Ivory'-Croatia
-Cuba-Cyprus-Czech Republic-Denmark-Djibouti-Dominica-Dominican Republic-East Timor(Timor-Leste)-Ecuador-Egypt-El Salvador-Equatorial Guinea-Eritrea-Estonia-Eswatini-Ethiopia-Fiji-Finland-France-Gabon-
The Gambia-Georgia-Germany-Ghana-Greece-Grenada-Guatemala-Guinea-Guinea-Bissau-Guyana-Haiti-Honduras-Hungary-Iceland-India-Indonesia-Iran-Iraq-Ireland-Italy-Jamaica-Japan-Jordan-Kazakhstan-Kenya-
Kiribati-Korea,North-Korea,South-Kosovo-Kuwait-Kyrgyzstan-Laos-Latvia-Lebanon-Lesotho-Liberia-Libya-Liechtenstein-Lithuania-Luxembourg-Madagascar-Malawi-Malaysia-Maldives-Mali-Malta-Marshall Islands-
Mauritania-Mauritius-Mexico-Micronesia, Federated States of-Moldova-Monaco-Mongolia-Montenegro-Morocco-Mozambique-Myanmar(Burma)-Namibia-Nauru-Nepal-Netherlands-New Zealand-Nicaragua-Nigeria-Nigeria-
North Macedonia-Norway-Oman-Pakistan-Paula-Panama-Papua New Guinea-Paraguay-Peru-Philippines-Poland-Portugal-Qatar-Romania-Russia-Rwanda-Saint Kits and Nevis-Saint Lucia-Saint Vincent and the Grenadines-
Samoa-San Marino-Sao Tome and Principe-Saudi Arabia-Senegal-Serbia-Seychelles-Sierra Leone-Singapore-Slovakia-Slovenia-Solomon Islands-Somalia-South Africa-Spain-Sri Lanka-Sudan,South-Suriname-Sweden-
Switzerland-Syria-Taiwan-Tajikistan-Tanzania-Thailand-Togo-Tonga-Trinidad and Tobago-Tunisia-Turkey-Turkmenistan-Tuvalu-Uganda-Ukraine-United Arab Emirates-United Kingdom-United States-Uruguay-Uzbekistan-
Vanuatu-Vatican City-Venezuela-Vietnam-Yemen-Zambia-Zimbabwe'''
Admin = Backend.Admin()
User = Backend.User()
Check = Backend.check()
Registry_Button = Button(win, text= 'Registry', height= 1, command= Registry)
Registry_Button.place(x= 150, y= 80)
Label(win, text= '/', font= ('mitraa', 20)).place(x= 200, y= 76)
Enter_Button = Button(win, text= 'Enter', height= 1, command= Enter)
Enter_Button.place(x= 220, y= 80)
win.mainloop()
