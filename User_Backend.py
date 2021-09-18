import sqlite3 as sql
from time import strftime

class check:
    def property(self, UserName, UserFamily, UserBerth):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT * FROM User WHERE Name= ? AND Family= ? AND Berth= ?', (UserName, UserFamily, UserBerth))
        self.result = self.cur.fetchall()
        self.cur.execute('SELECT * FROM Admin WHERE Name= ? AND Family= ? AND Berth= ?', (UserName, UserFamily, UserBerth))
        self.result2 = self.cur.fetchall()
        self.Database.close()
        if self.result == [] and self.result2 == []:
            return False
        else:
            return True

    def username(self, Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT * FROM User WHERE Localname= ?', (Username, ))
        self.result = self.cur.fetchall()
        self.cur.execute('SELECT * FROM Admin WHERE Localname= ?', (Username, ))
        self.result2 = self.cur.fetchall()
        self.Database.close()
        if self.result == [] and self.result2 == []:
            return False
        else:
            return True

    def get_user(self, UserId):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT * FROM User WHERE id= ?', (UserId,))
        self.User = self.cur.fetchall()
        self.Database.close()
        return self.User[0]

    def search(self, User_Name, User_Family, User_Username, User_Phone, User_Email, User_Country):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT * FROM User WHERE Name= ? OR Family= ? OR Localname= ? OR Phone= ? OR Email= ? OR Country= ?'
                         , (User_Name, User_Family, User_Username, User_Phone, User_Email, User_Country))
        self.User = self.cur.fetchall()
        self.Database.close()
        return self.User

    def starring(self, User_Type:str, UserId:int, Index:int, Status:str):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.New_Message = [item for items in self.cur.execute(f'SELECT Message FROM {User_Type} WHERE id= {UserId}').fetchall()[0][0].split('-') for item in items.split(',')]
        self.New_Message[6*Index-1] = Status
        New_Text = ''
        for item in self.New_Message:
            if self.New_Message.index(item) in range(6, len(self.New_Message)+1, 6):
                New_Text += f'-{item}'
            else:
                New_Text += f',{item}'
        self.cur.execute(f"UPDATE {User_Type} SET Message= ? WHERE id= ?", (New_Text[1:], UserId))
        self.Database.commit()
        self.Database.close()

    def deleting(self, User_Type:str, UserId:int, Index:int):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.New_Message =  self.cur.execute(f'SELECT Message FROM {User_Type} WHERE id= ?', (UserId,)).fetchall()[0][0].split('-')
        self.Numbers = int(self.New_Message.pop(Index-1)[0])
        self.New_Text = ''
        for item in self.New_Message:
            if self.Numbers > int(item[0]):
                if int(item[0]) == 1:
                    self.New_Text += item
                else:
                    self.New_Text += f'-{item}'
            else:
                if self.Numbers == 1 and int(item[0]) == 2:
                    self.New_Text += f'{self.Numbers}{item[1:]}'
                    self.Numbers += 1
                else:
                    self.New_Text += f'-{self.Numbers}{item[1:]}'
                    self.Numbers += 1
            self.cur.execute(f'UPDATE {User_Type} SET Message= ? WHERE id= ?', (self.New_Text, UserId))
        self.Database.commit()
        self.Database.close()

class User:
    def user_register(self, UserName, UserFamily, UserBerth, UserLocalname, UserPassword, UserPhone, UserEmail, UserCountry):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (strftime('%Y/%m/%d %H:%M:%S'), UserName, UserFamily, UserBerth, UserLocalname, UserPassword, UserPhone, UserEmail, UserCountry, ''))
        self.Database.commit()
        self.Database.close()

    def user_input(self, UserLocalname, UserPassword):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.User = self.cur.execute('SELECT * FROM User WHERE Localname=? AND Password=?',(UserLocalname, UserPassword)).fetchall()
        self.Database.close()
        return self.User

    def message_view(self, Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.Messages = self.cur.execute('SELECT Message FROM User WHERE Localname= ?', (Username,)).fetchall()[0][0].split('-')
        self.Database.close()
        return self.Messages

    def user_edit(self, UserId, UserPassword, UserPhone, UserEmail, UserCountry):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('UPDATE Users SET  Password= ?, Phone= ?, Email= ?, Country= ? WHERE id= ?',
                         (UserPassword, UserPhone, UserEmail, UserCountry, UserId))
        self.Database.commit()
        self.Database.close()

    def user_exit(self, Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('DELETE FROM User WHERE Localname= ?', (Username,))
        self.Database.commit()
        self.Database.close()

class Admin:
    def admin_register(self, AdminName, AdminFamily, AdminBerth, AdminLocalname, AdminPassword, AdminPhone, AdminEmail, AdminCountry):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('INSERT INTO Admin VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (strftime('%Y/%m/%d %H:%M:%S'), AdminName, AdminFamily, AdminBerth, AdminLocalname, AdminPassword, AdminPhone, AdminEmail, AdminCountry))
        self.Database.commit()
        self.Database.close()

    def admin_input(self, AdminLocalname, AdminPassword):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT * FROM Admin WHERE Localname=? AND Password=?', (AdminLocalname, AdminPassword))
        self.Admin = self.cur.fetchall()
        self.Database.close()
        print(self.Admin)
        return self.Admin

    def profile_image(self, UserId, Image):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('UPDATE Admin SET Profile_image= ? WHERE id= ?', (Image, UserId))
        self.Database.commit()
        self.cur.close()

    def get_id(self, Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT * FROM Admin WHERE Localname= ?', (Username, ))
        self.AdminId = self.cur.fetchall()[0][0]
        self.Database.close()
        return self.AdminId

    def add_user(self, UserName, UserFamily, UserBerth, UserLocalname, UserPassword, UserPhone, UserEmail, UserCountry):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (strftime('%Y/%m/%d %H:%M:%S'), UserName, UserFamily, UserBerth, UserLocalname, UserPassword, UserPhone, UserEmail, UserCountry, ''))
        self.Database.commit()
        self.Database.close()

    def admin_edit(self, AdminId, AdminPassword, AdminPhone, AdminEmail, AdminCountry):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute(
            'UPDATE Admin SET Password= ?, Phone= ?, Email= ?, Country= ? WHERE id= ?',
            (AdminPassword, AdminPhone, AdminEmail, AdminCountry, AdminId))
        self.Database.commit()
        self.Database.close()

    def user_view(self):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('SELECT Id, Registry_Time, Name, Family, Berth, Localname, Email, Phone, Country FROM User')
        self.Users = self.cur.fetchall()
        self.Database.close()
        return self.Users

    def send_message(self, Transmitter, Title, Text):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.Old_Message = self.cur.execute(f'SELECT Message FROM User WHERE Localname= ?',(Transmitter,)).fetchall()[0][0]
        if self.Old_Message == '':
            self.New_Message = f"1,{strftime('%Y/%m/%d %H:%M:%S')},{Transmitter},{Title},{Text},UnStar"
        else:
            self.New_Message = self.Old_Message + f"-{int(self.Old_Message.split('-')[-1][0])+1},{strftime('%Y/%m/%d %H:%M:%S')},{Transmitter},{Title},{Text},UnStar"
        self.cur.execute('UPDATE User SET Message= ? WHERE Localname= ?', (self.New_Message, Transmitter))
        self.Database.commit()
        self.Database.close()

    def user_reset_password(self, UserId, New_Password):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('UPDATE User SET Password= ? WHERE id= ?', (New_Password, UserId))
        self.Database.commit()
        self.Database.close()

    def user_remove(self, Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('DELETE FROM User WHERE Localname= ?', (Username,))
        self.Database.commit()
        self.Database.close()

    def message_view(self, Admin_Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.Message = self.cur.execute('SELECT Message FROM Admin WHERE Localname= ?', (Admin_Username,)).fetchall()[0][0]
        self.Database.close()
        return self.Message

    def admin_exit(self, Username):
        self.Database = sql.connect('Server.db')
        self.cur = self.Database.cursor()
        self.cur.execute('DELETE FROM Admin WHERE Localname= ?', (Username,))
        self.Database.commit()
        self.Database.close()

def connect():
    Database = sql.connect('Server.db')
    cur = Database.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Admin (
            Id INTEGER PRIMARY KEY,
            Registry_Time VARCHAR (20),
            Name VARCHAR (20),
            Family VARCHAR (15),
            Berth VARCHAR (10),
            Localname VARCHAR (20),
            Password VARCHAR (512),
            Phone INTEGER (11),
            Email VARCHAR (35),
            Country VARCHAR (20),
            Message text
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS User (
            Id INTEGER PRIMARY KEY,
            Registry_Time VARCHAR (20),
            Name VARCHAR (20),
            Family VARCHAR (15),
            Berth VARCHAR (10),
            Localname VARCHAR (20),
            Password VARCHAR (512),
            Phone INTEGER (11),
            Email VARCHAR (35),
            Country VARCHAR (20),
            Message text
        );
    ''')
    Database.commit()
    Database.close()

connect()
