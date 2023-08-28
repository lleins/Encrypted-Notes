from tkinter import *
import os.path
from os.path import exists
from datetime import datetime
from tkinter import scrolledtext  # For Beta Version the password is always "Pass"
import os
import time
import datetime
import requests
from email.message import EmailMessage
import smtplib
import ssl
import socket
import platform
import webbrowser
from os.path import exists
from cryptography.fernet import Fernet
import shutil
'''
Last Updated: January 2, 2023


*Windows now open in the center of the screen/Added a Delete Account function/Added a View accounts function
*Can now delete accounts/View accounts saved/Change Password*


'''



dir = os.path.join("C:\\","EncryptedNotes\\")

if os.path.exists(dir):
    ""
else:
    os.mkdir(dir)
    path = "C:\\EncryptedNotes\\"


def Read_File(File_Path):
    file_content = open(File_Path, "rb")
    if (exists(File_Path)):  # opens/reads a file with a given file path....
        return (file_content.read())
    else:
        raise Exception("Error, File not present or empty....")


def Get_Key():
    key = Fernet.generate_key()  # Generates a key
    return key


def Use_Key(key):
    Use_Key = Fernet(key)  # Instatiates the key to Encrypt/Decrypt
    return Use_Key


def Encrypt(key, text):  # Encrypts byte(text) with a given key
    Encrypted = key.encrypt(text)
    return Encrypted


def Decrypt(key, Encrypted_Text):
    Decrypted = key.decrypt(Encrypted_Text)  # Decrypts text with key
    return Decrypted


def Write_File(File_Path, Text_toFile):
    file_content = open(File_Path, "w")  # Writes text to a given .txt file
    file_content.write(Text_toFile)
    file_content.close()


def Convert_toByte(String):
    convert = String.encode('utf-8')  # Byte to String
    return convert


def Convert_toString(Byte):
    convert = Byte.decode()  # String to Byte
    return convert


def Write_KeytoFile(Key_Byte, File_Path):
    StringKey = Convert_toString(Key_Byte)  # Writes key in String format to file.....
    File = Write_File(File_Path, StringKey)
    return File


def Read_File(File_Path):
    file_content = open(File_Path, "r")
    if (exists(File_Path)):  # opens/reads a file with a given file path....
        return (file_content.read())
    else:
        raise Exception("Error, File not present or empty....")


def File_Exists(File_Name):
    exists = os.path.isfile("C:\\EncryptedNotes\\" + Userfld.get()+ "\\" + File_Name + ".txt")
    return exists


def CreateAccBtn():
    def Close_Account_Window():
        CreateAccountWindow.destroy()

    def Email_Valid(Email):
        email_address = Email
        response = requests.get("https://isitarealemail.com/api/email/validate", params={'email': email_address})
        status = response.json()['status']
        if status == "valid":
            return ("Valid")
        elif status == "invalid":
            return ("Not Valid")

    # dir = os.path.join("C:\\", "EncryptedNotes", Userfld2.get())
    def Create_Account():
        if (Email_Valid(Gmailfld2.get()) == "Not Valid"):
            lbl_User1 = Label(CreateAccountWindow, text="Gmail is not Valid", fg='red2',
                              font=("Calibri", 8, 'bold'), bg="grey15")
            lbl_User1.place(x=340, y=170)
            lbl_User1.after(2500, lambda: lbl_User1.destroy())

        elif ((Passfld2.get()) != (RePassfld2.get())):
            lbl_User2 = Label(CreateAccountWindow, text="Passwords don't match", fg='red2',
                              font=("Calibri", 8, 'bold'), bg="grey15")
            lbl_User2.place(x=340, y=170)
            lbl_User2.after(2500, lambda: lbl_User2.destroy())

        elif (os.path.exists("C:\\EncryptedNotes\\" + Userfld2.get())):
            lbl_User2 = Label(CreateAccountWindow, text="Username already exists", fg='red2',
                              font=("Calibri", 8, 'bold'), bg="grey15")
            lbl_User2.place(x=340, y=170)
            lbl_User2.after(2500, lambda: lbl_User2.destroy())


        else:
            dir = os.path.join("C:\\", "EncryptedNotes", Userfld2.get())

            if os.path.exists(dir):
                ""
            else:
                os.mkdir(dir)
                path = "C:\\EncryptedNotes\\" + Userfld2.get()
                DataPass_File_Path = "C:\\EncryptedNotes\\" + Userfld2.get() + "\\" + Userfld2.get() + " Data" + ".txt:Secret.txt"
                Data_File_Path = "C:\\EncryptedNotes\\" + Userfld2.get() + "\\" + Userfld2.get() + " Data" + ".txt"
                Open_DataFile = open(Data_File_Path, "w")
                Open_DataPassFile = open(DataPass_File_Path, "w")
                Open_DataFile.write(Gmailfld2.get())
                Open_DataPassFile.write(Passfld2.get())
                lbl_User3 = Label(CreateAccountWindow, text="Account Created", fg='green2',
                                  font=("Calibri", 8, 'bold'), bg="grey15")
                lbl_User3.place(x=340, y=170)
                lbl_User3.after(2500, lambda: lbl_User3.destroy())

            CreateAccountWindow.destroy()
            lbl_Create = Label(LoginWindow, text="Account Created", fg='green2', font=("Calibri", 10, 'bold'), bg="grey15")
            lbl_Create.place(x=380, y=181)
            lbl_Create.after(2500, lambda: lbl_Create.destroy())

    CreateAccountWindow = Tk()

    CreateAccountWindow_app_width = 500
    CreateAccountWindow_app_height = 400

    CreateAccountWindow_screen_width = CreateAccountWindow.winfo_screenwidth()
    CreateAccountWindow_screen_height = CreateAccountWindow.winfo_screenheight()

    CreateAccountWindow_x = int((CreateAccountWindow_screen_width / 2) - (CreateAccountWindow_app_width / 2))
    CreateAccountWindow_y = int((CreateAccountWindow_screen_height / 2) - (CreateAccountWindow_app_height / 2))

    lbl_Gmail2 = Label(CreateAccountWindow, text="Gmail:", fg='white', font=("Arial Black", 9, 'bold'), bg="grey15")
    lbl_Gmail2.place(x=110, y=30)

    Gmailfld2 = Entry(CreateAccountWindow, text="Gmail", bd=1, fg='white', bg="grey8", font=("Arial Black", 9, 'bold'),
                      width=35)
    Gmailfld2.place(x=110, y=50)
    Gmailfld2.config(insertbackground="white")


    lbl_User2 = Label(CreateAccountWindow, text="Username:", fg='white', font=("Arial Black", 9, 'bold'), bg="grey15")
    lbl_User2.place(x=110, y=110)

    Userfld2 = Entry(CreateAccountWindow, text="Username", bd=1, fg='white', bg="grey8",
                     font=("Arial Black", 9, 'bold'), width=35)
    Userfld2.place(x=110, y=130)
    Userfld2.config(insertbackground="white")


    lbl_Pass2 = Label(CreateAccountWindow, text="Password:", fg='white', font=("Arial Black", 9, 'bold'), bg="grey15")
    lbl_Pass2.place(x=110, y=190)

    Passfld2 = Entry(CreateAccountWindow, text="This is Password Widget", bd=1, fg='white',
                     font=("Arial Black", 9, 'bold'), bg="grey8", width=35)
    Passfld2.place(x=110, y=210)
    Passfld2.config(show="*")
    Passfld2.config(insertbackground="white")


    lbl_RePass2 = Label(CreateAccountWindow, text="Re-Enter Password:", fg='white', font=("Arial Black", 9, 'bold'),
                        bg="grey15")
    lbl_RePass2.place(x=110, y=270)

    RePassfld2 = Entry(CreateAccountWindow, text="This is RePassword Widget", bd=1, fg='white',
                       font=("Arial Black", 9, 'bold'), bg="grey8", width=35)
    RePassfld2.place(x=110, y=290)
    RePassfld2.config(show="*")
    RePassfld2.config(insertbackground="white")


    btn_Create2 = Button(CreateAccountWindow, text="Create Account", fg='white', font=("Arial Black", 9, 'bold'),
                         bg="grey8", command=Create_Account)
    btn_Create2.place(x=192, y=340)

    CreateAccountWindow.wm_attributes('-alpha')  # Transparency
    CreateAccountWindow.protocol("WM_DELETE_WINDOW",
                                 Close_Account_Window)  # controling the function of the close window icon (top right of window)
    CreateAccountWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
    CreateAccountWindow.title('Create Account')  # Add Username to top of WebPage
    CreateAccountWindow.geometry(f'{CreateAccountWindow_app_width}x{CreateAccountWindow_app_height}+{CreateAccountWindow_x}+{CreateAccountWindow_y}')
    CreateAccountWindow.configure(bg='grey15')
    CreateAccountWindow.mainloop()


def LoginBtn():
    if os.path.exists("C:\\EncryptedNotes\\" + Userfld.get()) == False:
        lbl_Fail = Label(LoginWindow, text="Error", fg='red2', font=("Calibri", 10, 'bold'), bg="grey15")
        lbl_Fail.place(x=380, y=181)
        lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

    elif Userfld.get() == "":
        lbl_Fail = Label(LoginWindow, text="Error", fg='red2', font=("Calibri", 10, 'bold'), bg="grey15")
        lbl_Fail.place(x=380, y=181)
        lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

    elif Passfld.get() == "":
        lbl_Fail = Label(LoginWindow, text="Error", fg='red2', font=("Calibri", 10, 'bold'), bg="grey15")
        lbl_Fail.place(x=380, y=181)
        lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

    elif (Read_File("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Userfld.get() + " Data.txt:Secret.txt") == Passfld.get()) and (os.path.exists("C:\\EncryptedNotes\\" + Userfld.get()) == True):
        lbl_Fail = Label(LoginWindow, text="Login Succesful", fg='green', font=("Calibri", 10, 'bold'), bg="grey15")
        lbl_Fail.place(x=380, y=181)
        lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

        LoginWindow.wm_attributes('-alpha', 0.0)  # Transparency

        def Check_txt_Files():
            dir_path = "C:\\EncryptedNotes\\" + Userfld.get()
            res = []
            for file in os.listdir(dir_path):
                if (file.endswith(".txt")) and (file != Userfld.get() + " Data.txt") and ((file.endswith(" Key.txt")) == False):
                    file = file.replace(".txt", "")
                    res.append(file + "\n")
            return (''.join(res))

        def Close_Note_Window():
            MainWindow.destroy()
            LoginWindow.wm_attributes('-alpha', 1.0)  # Transparency

        def New_Btn():

            def Create_Note():
                if Enterfld.get() == "":
                    lbl_Error = Label(NameWindow, text="Error", fg='red', font=("Arial Black", 8, 'bold'), bg="grey15")
                    lbl_Error.place(x=200, y=70)
                    lbl_Error.after(2500, lambda: lbl_Error.destroy())

                elif (File_Exists(Enterfld.get()) == True):
                    lbl_Error = Label(NameWindow, text="File already Exists", fg='red', font=("Arial Black", 8, 'bold'), bg="grey15")
                    lbl_Error.place(x=150, y=70)
                    lbl_Error.after(2500, lambda: lbl_Error.destroy())

                else:
                    New_File_Creation = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() +" Key.txt:Secret.txt"
                    Open_Gmail_File = open(New_File_Creation, "w")
                    Open_Gmail_File.close()
                    New_File_Creation = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() + ".txt"
                    Open_Gmail_File = open(New_File_Creation, "w")
                    Open_Gmail_File.close()
                    MainWindow.wm_attributes('-alpha', 0.0)
                    NameWindow.wm_attributes('-alpha', 0.0)


                    def Save():
                        Write_File("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() + ".txt", Note_fld.get(1.0, "end-1c"))
                        lbl_top_header = Label(NoteWindow, text="Saved..", bd=1, fg='green2', font=("Arial", 8, 'bold'),
                                               bg="grey15", anchor="w")
                        lbl_top_header.place(x=800, y=60)
                        lbl_top_header.after(2500, lambda: lbl_top_header.destroy())

                    def Close_Note_Window():

                        Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='white', font=("Arial", 11, 'bold'),
                                                             bg="grey8",
                                                             width=30,
                                                             height=22)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                        Note_fld.place(x=35, y=30)
                        Note_fld.insert(1.0, Check_txt_Files())
                        Note_fld.config(insertbackground="white")
                        Note_fld.config(state=DISABLED)

                        Key_File_Path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() + " Key.txt:Secret.txt"
                        myFilePath = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() + ".txt"

                        File_Text = Read_File(myFilePath)  # Open and convert file content to Bytes
                        b = Convert_toByte(File_Text)

                        Raw_Key = Get_Key()  # Generate Raw Key
                        KEY = Use_Key(Raw_Key)  # Initiates Key

                        Write_KeytoFile(Raw_Key, Key_File_Path)  # Writes Raw Key to file

                        String_Text = Read_File(myFilePath)  # Read File content
                        Byte_Text = Convert_toByte(String_Text)  # Convert to Bytes to enrypt

                        Enc = Encrypt(KEY, Byte_Text)  # Encrypts Text

                        g = Convert_toString(Enc)  # Converts Encrypted text to String format
                        Write_File(myFilePath, g)  # writes to file
                        NoteWindow.destroy()
                        MainWindow.wm_attributes('-alpha', 1.0)               #New Note Section ----- Need to add Rename and Delete still.....
                        NameWindow.destroy()

                    def Delete():

                        def Remove_File(File_Name):
                            path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + File_Name
                            os.remove(path)

                        def Close_Delete_Window():
                            ConfirmDelete.destroy()

                        def Confirm_Delete():
                            Remove_File(Enterfld.get() + ".txt")
                            Remove_File(Enterfld.get() + " Key.txt")
                            ConfirmDelete.destroy()
                            Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='white',
                                                                 font=("Arial", 11, 'bold'),
                                                                 bg="grey8",
                                                                 width=30,
                                                                 height=22)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                            Note_fld.place(x=35, y=30)
                            Note_fld.insert(1.0, Check_txt_Files())
                            Note_fld.config(insertbackground="white")
                            Note_fld.config(state=DISABLED)
                            NoteWindow.destroy()
                            MainWindow.wm_attributes('-alpha', 1.0)
                            openfld.delete(0, END)
                            NameWindow.destroy()

                        ConfirmDelete = Toplevel()

                        ConfirmDelete_app_width = 300
                        ConfirmDelete_app_height = 200

                        ConfirmDelete_screen_width = ConfirmDelete.winfo_screenwidth()
                        ConfirmDelete_screen_height = ConfirmDelete.winfo_screenheight()

                        ConfirmDelete_x = int((ConfirmDelete_screen_width / 2) - (ConfirmDelete_app_width / 2))
                        ConfirmDelete_y = int((ConfirmDelete_screen_height / 2) - (ConfirmDelete_app_height / 2))


                        lbl_Access5 = Label(ConfirmDelete, text="Are You Sure?", fg='white',
                                            font=("Arial Black", 12, 'bold'),
                                            bg="grey15")
                        lbl_Access5.place(x=80, y=40)

                        btn_Open = Button(ConfirmDelete, text="Yes", font=("Arial Black", 9, 'bold'), fg='white',
                                          bg="grey8", padx=3, command=Confirm_Delete)
                        btn_Open.place(x=170, y=110)

                        btn_Open = Button(ConfirmDelete, text="No", font=("Arial Black", 9, 'bold'), fg='white',
                                          bg="grey8", padx=5, command=Close_Delete_Window)
                        btn_Open.place(x=80, y=110)

                        ConfirmDelete.wm_attributes('-alpha')  # Transparency
                        ConfirmDelete.protocol("WM_DELETE_WINDOW",
                                               Close_Delete_Window)  # controlling the function of the close window icon (top right of window)
                        ConfirmDelete.resizable(False, False)  # Cannot change size of the Window(It is locked)
                        ConfirmDelete.title('Delete')  # Add Username to top of WebPage
                        ConfirmDelete.geometry(f'{ConfirmDelete_app_width}x{ConfirmDelete_app_height}+{ConfirmDelete_x}+{ConfirmDelete_y}')
                        ConfirmDelete.configure(bg='grey15')
                        ConfirmDelete.mainloop()

                    def Rename3():
                        def Close_Rename_Window():
                            RenameWindow.destroy()

                        def File_Exists(File_Name):
                            exists = os.path.isfile("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + File_Name + ".txt")
                            return exists

                        def Rename_btn():

                            def Remove_File3(File_Name):
                                path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + File_Name + " Key.txt"
                                os.remove(path)

                            if (Renamefld.get() == ""):
                                lbl_Fail = Label(RenameWindow, text="Error", fg='red', font=("Calibri", 9, 'bold'),
                                                 bg="grey15")
                                lbl_Fail.place(x=200, y=50)
                                lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

                            elif (File_Exists(Renamefld.get()) == True):
                                lbl_Fail = Label(RenameWindow, text="Name Already Exists", fg='red',
                                                 font=("Calibri", 9, 'bold'), bg="grey15")
                                lbl_Fail.place(x=180, y=60)
                                lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

                            elif (File_Exists(Renamefld.get()) == False):
                                Original = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() + ".txt"
                                New = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + ".txt"
                                os.rename(Original, New)

                                Remove_File3(Enterfld.get())

                                New_Key_File = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + " Key" + ".txt:Secret.txt"
                                Open_New_Key_File = open(New_Key_File, "w")
                                Open_New_Key_File.write("")

                                Key_File_Path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + " Key.txt:Secret.txt"
                                myFilePath = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + ".txt"

                                File_Text = Read_File(myFilePath)  # Open and convert file content to Bytes
                                b = Convert_toByte(File_Text)

                                Raw_Key = Get_Key()  # Generate Raw Key
                                KEY = Use_Key(Raw_Key)  # Initiates Key

                                Write_KeytoFile(Raw_Key, Key_File_Path)  # Writes Raw Key to file

                                String_Text = Read_File(myFilePath)  # Read File content
                                Byte_Text = Convert_toByte(String_Text)  # Convert to Bytes to enrypt

                                Enc = Encrypt(KEY, Byte_Text)  # Encrypts Text

                                g = Convert_toString(Enc)  # Converts Encrypted text to String format
                                Write_File(myFilePath, g)  # writes to file

                                RenameWindow.destroy()
                                NoteWindow.destroy()
                                Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='white',
                                                                     font=("Arial", 11, 'bold'), bg="grey8",
                                                                     width=30,
                                                                     height=22)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                                Note_fld.place(x=35, y=30)
                                Note_fld.insert(1.0, Check_txt_Files())
                                Note_fld.config(insertbackground="white")
                                Note_fld.config(state=DISABLED)
                                MainWindow.wm_attributes('-alpha', 1.0)
                                NameWindow.destroy()
                                openfld.delete(0, END)

                        RenameWindow = Tk()

                        RenameWindow_app_width = 300
                        RenameWindow_app_height = 200

                        RenameWindow_screen_width = RenameWindow.winfo_screenwidth()
                        RenameWindow_screen_height = RenameWindow.winfo_screenheight()

                        RenameWindow_x = int((RenameWindow_screen_width / 2) - (RenameWindow_app_width / 2))
                        RenameWindow_y = int((RenameWindow_screen_height / 2) - (RenameWindow_app_height / 2))


                        lbl_Access5 = Label(RenameWindow, text="Re-name", fg='white', font=("Arial Black", 12, 'bold'),
                                            bg="grey15")
                        lbl_Access5.place(x=110, y=30)

                        Renamefld = Entry(RenameWindow, text="Enterfld", bd=1, fg='white', bg="grey8",
                                          font=("Arial Black", 8, 'bold'),
                                          width=20)  # Gmail feild
                        Renamefld.place(x=75, y=80)
                        Renamefld.config(insertbackground="white")

                        btn_Enter = Button(RenameWindow, text="Enter", font=("Arial Black", 9, 'bold'), fg='white',
                                           bg="grey8", padx=3, command=Rename_btn)
                        btn_Enter.place(x=120, y=120)

                        RenameWindow.wm_attributes('-alpha')  # Transparency
                        RenameWindow.protocol("WM_DELETE_WINDOW",
                                              Close_Rename_Window)  # controlling the function of the close window icon (top right of window)
                        RenameWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                        RenameWindow.title('Delete')  # Add Username to top of WebPage
                        RenameWindow.geometry(f'{RenameWindow_app_width}x{RenameWindow_app_height}+{RenameWindow_x}+{RenameWindow_y}')
                        RenameWindow.configure(bg='grey15')
                        RenameWindow.mainloop()

                    NoteWindow = Tk()

                    NoteWindow_app_width = 1000
                    NoteWindow_app_height = 700

                    NoteWindow_screen_width = NoteWindow.winfo_screenwidth()
                    NoteWindow_screen_height = NoteWindow.winfo_screenheight()

                    NoteWindow_x = int((NoteWindow_screen_width / 2) - (NoteWindow_app_width / 2))
                    NoteWindow_y = int((NoteWindow_screen_height / 2) - (NoteWindow_app_height / 2))


                    Note_fld = scrolledtext.ScrolledText(NoteWindow, bd=1, fg='white', font=("Arial", 11, 'bold'),
                                                         bg="grey8", width=114,
                                                         height=30)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                    Note_fld.place(x=35, y=90)
                    Note_fld.config(insertbackground="white")  # Changes test cursor color
                    Note_fld.insert(1.0, Read_File("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Enterfld.get() + ".txt"))

                    lbl_top_header = Label(NoteWindow, text= Enterfld.get() + ".txt"  , bd=1, fg='white', font=("Arial", 14, 'bold'),
                                           bg="grey8", width=77, anchor="w")
                    lbl_top_header.place(x=38, y=25)

                    btn_Delete = Button(NoteWindow, text="Delete", font=("Arial", 10, 'bold'), fg='white', bg='grey8',
                                        height=1, padx=8, command=Delete)  # Azure3
                    btn_Delete.place(x=35, y=655)

                    btn_Save = Button(NoteWindow, text="Save", font=("Arial", 10, 'bold'), fg='white', bg='grey8',
                                      height=1, padx=8, command = Save)  # Azure3
                    btn_Save.place(x=912, y=655)

                    btn_Rename = Button(NoteWindow, text="Re-Name", font=("Arial", 10, 'bold'), fg='white', bg='grey8',
                                        height=1, padx=8, command=Rename3)
                    btn_Rename.place(x=470, y=655)

                    NoteWindow.wm_attributes('-alpha')  # Transparency
                    NoteWindow.protocol("WM_DELETE_WINDOW", Close_Note_Window)  # controlling the function of the close window icon (top right of window)
                    NoteWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                    NoteWindow.title('Notes')  # Add Username to top of WebPage
                    NoteWindow.geometry(f'{NoteWindow_app_width}x{NoteWindow_app_height}+{NoteWindow_x}+{NoteWindow_y}')
                    NoteWindow.configure(bg='grey15')
                    NoteWindow.mainloop()




            def Close_Rename_Window():
                NameWindow.destroy()

            NameWindow = Tk()

            NameWindow_app_width = 300
            NameWindow_app_height = 200

            NameWindow_screen_width = NameWindow.winfo_screenwidth()
            NameWindow_screen_height = NameWindow.winfo_screenheight()

            NameWindow_x = int((NameWindow_screen_width / 2) - (NameWindow_app_width / 2))
            NameWindow_y = int((NameWindow_screen_height / 2) - (NameWindow_app_height / 2))

            lbl_Access5 = Label(NameWindow, text="Enter Name:", fg='white', font=("Arial Black", 12, 'bold'),
                               bg="grey15")
            lbl_Access5.place(x=90, y=40)

            Enterfld = Entry(NameWindow, text="Enter Name", bd=1, fg='white', bg="grey8",
                            font=("Arial Black", 9, 'bold'))  # Gmail feild
            Enterfld.place(x=70, y=100)
            Enterfld.config(insertbackground="white")


            btn_Open = Button(NameWindow, text="Enter", font=("Arial Black", 9, 'bold'), fg='white', bg="grey8", command=Create_Note)
            btn_Open.place(x=127, y=140)

            NameWindow.wm_attributes('-alpha')  # Transparency
            NameWindow.protocol("WM_DELETE_WINDOW",
                                Close_Rename_Window)  # controlling the function of the close window icon (top right of window)
            NameWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
            NameWindow.title('Name')  # Add Username to top of WebPage
            NameWindow.geometry(f'{NameWindow_app_width}x{NameWindow_app_height}+{NameWindow_x}+{NameWindow_y}')
            NameWindow.configure(bg='grey15')
            NameWindow.mainloop()

        def Open_Note():
            if (openfld.get() == ""):
                lbl_error_main = Label(MainWindow, text="Error", bd=1, fg='red', font=("Arial", 8, 'bold'),
                                       bg="grey15", anchor="w")
                lbl_error_main.place(x=330, y=400)
                lbl_error_main.after(2500, lambda: lbl_error_main.destroy())

            elif (((File_Exists(openfld.get())) == False)):
                lbl_error_main = Label(MainWindow, text="Error", bd=1, fg='red', font=("Arial", 8, 'bold'),
                                       bg="grey15", anchor="w")
                lbl_error_main.place(x=330, y=400)
                lbl_error_main.after(2500, lambda: lbl_error_main.destroy())

            elif ((File_Exists(openfld.get())) == True):
                MainWindow.wm_attributes('-alpha', 0.0)
                def Read_File2(File_Path):
                    file_content = open(File_Path, "r")
                    if (exists(File_Path)):  # opens/reads a file with a given file path....
                        return (file_content.read())
                    else:
                        raise Exception("Error, File not present or empty....")

                def Read_FileKey2(File_Path):
                    file_content = open(File_Path, "r")
                    if (exists(File_Path)):  # opens/reads a file with a given file path....
                        return (file_content.read())
                    else:
                        raise Exception("Error, File not present or empty....")

                def Get_Key2():
                    key = Fernet.generate_key()  # Generates a key
                    return key

                def Use_Key2(key):
                    Use_Key = Fernet(key)  # Instatiates the key to Encrypt/Decrypt
                    return Use_Key

                def Encrypt2(key, text):  # Encrypts byte(text) with a given key
                    Encrypted = key.encrypt(text)
                    return Encrypted

                def Decrypt2(key, Encrypted_Text):
                    Decrypted = key.decrypt(Encrypted_Text)  # Decrypts text with key
                    return Decrypted

                def Write_File2(File_Path, Text_toFile):
                    file_content = open(File_Path, "w")  # Writes text to a given .txt file
                    file_content.write(Text_toFile)
                    file_content.close()

                def Write_FileKey2(File_Path, Text_toFile):
                    file_content = open(File_Path, "w")  # Writes text to a given .txt file
                    file_content.write(Text_toFile)
                    file_content.close()

                def Convert_toByte2(String):
                    convert = String.encode('utf-8')  # Byte to String
                    return convert

                def Convert_toString2(Byte):
                    convert = Byte.decode()  # String ot Byte
                    return convert

                def Write_KeytoFile2(Key_Byte, File_Path):
                    StringKey = Convert_toString(Key_Byte)  # Writes key in String format to file.....
                    File = Write_File(File_Path, StringKey)
                    return File

                Key_File_Path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + " Key.txt:Secret.txt"
                myFilePath = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + ".txt"

                Read_Key = Read_File2(Key_File_Path)
                ByteKey = Convert_toByte2(Read_Key)
                ReadFile = Read_File2(myFilePath)
                ByteFile = Convert_toByte2(ReadFile)
                dec = Decrypt2(Use_Key(ByteKey), ByteFile)
                Final_Write = Convert_toString2(dec)
                Write_File2(myFilePath, Final_Write)

                def Save2():
                    Write_File("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + ".txt",
                               Note_fld2.get(1.0, "end-1c"))
                    lbl_top_header = Label(NoteWindow2, text="Saved..", bd=1, fg='green2', font=("Arial", 8, 'bold'),
                                           bg="grey15", anchor="w")
                    lbl_top_header.place(x=800, y=60)
                    lbl_top_header.after(2500, lambda: lbl_top_header.destroy())

                def Close_NoteWindow2():
                    NoteWindow2.destroy()
                    MainWindow.wm_attributes('-alpha', 1.0)
                    Key_File_Path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + " Key.txt:Secret.txt"
                    myFilePath = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + ".txt"

                    File_Text = Read_File(myFilePath)  # Open and convert file content to Bytes
                    b = Convert_toByte(File_Text)

                    Raw_Key = Get_Key()  # Generate Raw Key
                    KEY = Use_Key(Raw_Key)  # Initiates Key

                    Write_KeytoFile(Raw_Key, Key_File_Path)  # Writes Raw Key to file

                    String_Text = Read_File(myFilePath)  # Read File content
                    Byte_Text = Convert_toByte(String_Text)  # Convert to Bytes to enrypt

                    Enc = Encrypt(KEY, Byte_Text)  # Encrypts Text

                    g = Convert_toString(Enc)  # Converts Encrypted text to String format
                    Write_File(myFilePath, g)  # writes to file

                def Delete2():
                    def Remove_File(File_Name):
                        path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + File_Name
                        os.remove(path)

                    def Close_Delete_Window():
                        ConfirmDelete.destroy()

                    def Confirm_Delete():
                        Remove_File(openfld.get() + ".txt")
                        Remove_File(openfld.get() + " Key.txt")

                        ConfirmDelete.destroy()
                        Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='white', font=("Arial", 11, 'bold'),
                                                             bg="grey8",
                                                             width=30,
                                                             height=22)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                        Note_fld.place(x=35, y=30)
                        Note_fld.insert(1.0, Check_txt_Files())
                        Note_fld.config(insertbackground="white")
                        Note_fld.config(state=DISABLED)
                        NoteWindow2.destroy()
                        MainWindow.wm_attributes('-alpha', 1.0)
                        openfld.delete(0, END)

                    ConfirmDelete = Tk()

                    ConfirmDelete_app_width = 300
                    ConfirmDelete_app_height = 200

                    ConfirmDelete_screen_width = ConfirmDelete.winfo_screenwidth()
                    ConfirmDelete_screen_height = ConfirmDelete.winfo_screenheight()

                    ConfirmDelete_x = int((ConfirmDelete_screen_width / 2) - (ConfirmDelete_app_width / 2))
                    ConfirmDelete_y = int((ConfirmDelete_screen_height / 2) - (ConfirmDelete_app_height / 2))

                    lbl_Access5 = Label(ConfirmDelete, text="Are You Sure?", fg='white',
                                        font=("Arial Black", 12, 'bold'),
                                        bg="grey15")
                    lbl_Access5.place(x=80, y=40)

                    btn_Open = Button(ConfirmDelete, text="Yes", font=("Arial Black", 9, 'bold'), fg='white',
                                      bg="grey8", padx=3, command=Confirm_Delete)
                    btn_Open.place(x=170, y=110)

                    btn_Open = Button(ConfirmDelete, text="No", font=("Arial Black", 9, 'bold'), fg='white',
                                      bg="grey8", padx=5, command=Close_Delete_Window)
                    btn_Open.place(x=80, y=110)

                    ConfirmDelete.wm_attributes('-alpha')  # Transparency
                    ConfirmDelete.protocol("WM_DELETE_WINDOW",
                                           Close_Delete_Window)  # controlling the function of the close window icon (top right of window)
                    ConfirmDelete.resizable(False, False)  # Cannot change size of the Window(It is locked)
                    ConfirmDelete.title('Delete')  # Add Username to top of WebPage
                    ConfirmDelete.geometry(f'{ConfirmDelete_app_width}x{ConfirmDelete_app_height}+{ConfirmDelete_x}+{ConfirmDelete_y}') #300x200
                    ConfirmDelete.configure(bg='grey15')
                    ConfirmDelete.mainloop()


                def Rename2():
                    def Close_Rename_Window():
                        RenameWindow.destroy()

                    def File_Exists(File_Name):
                        exists = os.path.isfile("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + File_Name + ".txt")
                        return exists

                    def Rename_btn():

                        def Remove_File3(File_Name):
                            path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + File_Name + " Key.txt"
                            os.remove(path)

                        if (Renamefld.get() == ""):
                            lbl_Fail = Label(RenameWindow, text="Error", fg='red', font=("Calibri", 9, 'bold'),
                                             bg="grey15")
                            lbl_Fail.place(x=200, y=50)
                            lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

                        elif (File_Exists(Renamefld.get()) == True):
                            lbl_Fail = Label(RenameWindow, text="Name Already Exists", fg='red',
                                             font=("Calibri", 9, 'bold'), bg="grey15")
                            lbl_Fail.place(x=180, y=60)
                            lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

                        elif (File_Exists(Renamefld.get()) == False):
                            Original = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + ".txt"
                            New = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + ".txt"
                            os.rename(Original, New)

                            Remove_File3(openfld.get())

                            New_Key_File = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + " Key" + ".txt:Secret.txt"
                            Open_New_Key_File = open(New_Key_File, "w")
                            Open_New_Key_File.write("")

                            Key_File_Path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + " Key.txt:Secret.txt"
                            myFilePath = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Renamefld.get() + ".txt"

                            File_Text = Read_File(myFilePath)  # Open and convert file content to Bytes
                            b = Convert_toByte(File_Text)

                            Raw_Key = Get_Key()  # Generate Raw Key
                            KEY = Use_Key(Raw_Key)  # Initiates Key

                            Write_KeytoFile(Raw_Key, Key_File_Path)  # Writes Raw Key to file

                            String_Text = Read_File(myFilePath)  # Read File content
                            Byte_Text = Convert_toByte(String_Text)  # Convert to Bytes to enrypt

                            Enc = Encrypt(KEY, Byte_Text)  # Encrypts Text

                            g = Convert_toString(Enc)  # Converts Encrypted text to String format
                            Write_File(myFilePath, g)  # writes to file

                            RenameWindow.destroy()
                            NoteWindow2.destroy()
                            Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='white',
                                                                 font=("Arial", 11, 'bold'), bg="grey8",
                                                                 width=30,
                                                                 height=22)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                            Note_fld.place(x=35, y=30)
                            Note_fld.insert(1.0, Check_txt_Files())
                            Note_fld.config(insertbackground="white")
                            Note_fld.config(state=DISABLED)
                            openfld.delete(0, END)
                            MainWindow.wm_attributes('-alpha', 1.0)

                    RenameWindow = Tk()

                    RenameWindow_app_width = 300
                    RenameWindow_app_height = 200

                    RenameWindow_screen_width = RenameWindow.winfo_screenwidth()
                    RenameWindow_screen_height = RenameWindow.winfo_screenheight()

                    RenameWindow_x = int((RenameWindow_screen_width / 2) - (RenameWindow_app_width / 2))
                    RenameWindow_y = int((RenameWindow_screen_height / 2) - (RenameWindow_app_height / 2))

                    lbl_Access5 = Label(RenameWindow, text="Re-name", fg='white', font=("Arial Black", 12, 'bold'),
                                        bg="grey15")
                    lbl_Access5.place(x=110, y=30)

                    Renamefld = Entry(RenameWindow, text="Enterfld", bd=1, fg='white', bg="grey8",
                                      font=("Arial Black", 8, 'bold'),
                                      width=20)  # Gmail feild
                    Renamefld.place(x=75, y=80)

                    btn_Enter = Button(RenameWindow, text="Enter", font=("Arial Black", 9, 'bold'), fg='white',
                                       bg="grey8", padx=3, command = Rename_btn)
                    btn_Enter.place(x=120, y=120)

                    RenameWindow.wm_attributes('-alpha')  # Transparency
                    RenameWindow.protocol("WM_DELETE_WINDOW",
                                          Close_Rename_Window)  # controlling the function of the close window icon (top right of window)
                    RenameWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                    RenameWindow.title('Delete')  # Add Username to top of WebPage
                    RenameWindow.geometry(f'{RenameWindow_app_width}x{RenameWindow_app_height}+{RenameWindow_x}+{RenameWindow_y}')
                    RenameWindow.configure(bg='grey15')
                    RenameWindow.mainloop()

                NoteWindow2 = Tk()

                NoteWindow2_app_width = 1000
                NoteWindow2_app_height = 700

                NoteWindow2_screen_width = NoteWindow2.winfo_screenwidth()
                NoteWindow2_screen_height = NoteWindow2.winfo_screenheight()

                NoteWindow2_x = int((NoteWindow2_screen_width / 2) - (NoteWindow2_app_width / 2))
                NoteWindow2_y = int((NoteWindow2_screen_height / 2) - (NoteWindow2_app_height / 2))

                Note_fld2 = scrolledtext.ScrolledText(NoteWindow2, bd=1, fg='white', font=("Arial", 11, 'bold'),
                                                     bg="grey8", width=114,
                                                     height=30)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                Note_fld2.place(x=35, y=90)
                Note_fld2.config(insertbackground="white")  # Changes test cursor color
                Note_fld2.insert(1.0, Read_File("C:\\EncryptedNotes\\" + Userfld.get() + "\\" + openfld.get() + ".txt"))

                lbl_top_header = Label(NoteWindow2, text=openfld.get() + ".txt", bd=1, fg='white',
                                       font=("Arial", 14, 'bold'),
                                       bg="grey8", width=77, anchor="w")
                lbl_top_header.place(x=38, y=25)

                btn_Delete = Button(NoteWindow2, text="Delete", font=("Arial", 10, 'bold'), fg='white', bg='grey8',
                                    height=1, padx=8, command = Delete2)  # Azure3
                btn_Delete.place(x=35, y=655)

                btn_Save = Button(NoteWindow2, text="Save", font=("Arial", 10, 'bold'), fg='white', bg='grey8',
                                  height=1, padx=8, command=Save2)  # Azure3
                btn_Save.place(x=912, y=655)

                btn_Rename = Button(NoteWindow2, text="Re-Name", font=("Arial", 10, 'bold'), fg='white', bg='grey8',
                                    height=1, padx=8, command = Rename2)
                btn_Rename.place(x=470, y=655)

                NoteWindow2.wm_attributes('-alpha')  # Transparency
                NoteWindow2.protocol("WM_DELETE_WINDOW", Close_NoteWindow2)  # controlling the function of the close window icon (top right of window)
                NoteWindow2.resizable(False, False)  # Cannot change size of the Window(It is locked)
                NoteWindow2.title('Notes')  # Add Username to top of WebPage
                NoteWindow2.geometry(f'{NoteWindow2_app_width}x{NoteWindow2_app_height}+{NoteWindow2_x}+{NoteWindow2_y}') #1000x700
                NoteWindow2.configure(bg='grey15')
                NoteWindow2.mainloop()


        def Settings_Btn():

            MainWindow.wm_attributes('-alpha', 0.0)


            def Close_Settings_Window():
                SettingsWindow.destroy()
                MainWindow.wm_attributes('-alpha', 1.0)

            def Read_File(File_Path):
                file_content = open(File_Path, "rb")
                if (exists(File_Path)):  # opens/reads a file with a given file path....
                    return (file_content.read())
                else:
                    raise Exception("Error, File not present or empty....")

            def Read_Gmail():
                Gmail = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Userfld.get() + " Data" + ".txt"
                return Read_File(Gmail)

            def Delete_Account():
                def Close_Confirm_Window():
                    ConfirmWindow.destroy()

                def Delete_Account_Actual():
                    dir_path = "C:\\EncryptedNotes\\" + Userfld.get()
                    shutil.rmtree(dir_path, ignore_errors=True)

                    Userfld.delete(0, END)
                    Passfld.delete(0, END)

                    ConfirmWindow.destroy()
                    SettingsWindow.destroy()
                    MainWindow.destroy()
                    LoginWindow.wm_attributes('-alpha', 1.0)

                    lbl_Deleted_success = Label(LoginWindow, text="Account Deleted", fg='green',
                                                font=("Calibri", 10, 'bold'), bg="grey15")
                    lbl_Deleted_success.place(x=380, y=181)
                    lbl_Deleted_success.after(2500, lambda: lbl_Deleted_success.destroy())

                ConfirmWindow = Tk()

                ConfirmWindow_app_width = 300
                ConfirmWindow_app_height = 200

                ConfirmWindow_screen_width = ConfirmWindow.winfo_screenwidth()
                ConfirmWindow_screen_height = ConfirmWindow.winfo_screenheight()

                ConfirmWindow_x = int((ConfirmWindow_screen_width / 2) - (ConfirmWindow_app_width / 2))
                ConfirmWindow_y = int((ConfirmWindow_screen_height / 2) - (ConfirmWindow_app_height / 2))

                lbl_TitleTop = Label(ConfirmWindow, text="Are you Sure?", font=("Arial Black", 15, "bold"), fg="white",
                                     bg="grey15")
                lbl_TitleTop.place(x=70, y=10)

                btn_No = Button(ConfirmWindow, text="No", fg='white', font=("Calibri", 11, 'bold'),
                                bg="grey8", command=Close_Confirm_Window, width=4)
                btn_No.place(x=90, y=100)

                btn_No = Button(ConfirmWindow, text="Yes", fg='white', font=("Calibri", 11, 'bold'),
                                bg="grey8", command=Delete_Account_Actual, width=4)
                btn_No.place(x=170, y=100)

                ConfirmWindow.wm_attributes('-alpha')  # Transparency
                ConfirmWindow.protocol("WM_DELETE_WINDOW", Close_Confirm_Window)
                ConfirmWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                ConfirmWindow.title('Settings')  # Add Username to top of WebPage
                ConfirmWindow.geometry(
                    f'{ConfirmWindow_app_width}x{ConfirmWindow_app_height}+{ConfirmWindow_x}+{ConfirmWindow_y}')  # 400x500
                ConfirmWindow.configure(bg='grey15')
                ConfirmWindow.mainloop()

            def Change_Password():
                SettingsWindow.wm_attributes('-alpha', 0.0)

                def Read_File(File_Path):
                    file_content = open(File_Path, "r")
                    if (exists(File_Path)):  # opens/reads a file with a given file path....
                        return (file_content.read())
                    else:
                        raise Exception("Error, File not present or empty....")

                def Write_File(File_Path, Text_toFile):
                    file_content = open(File_Path, "w")  # Writes text to a given .txt file
                    file_content.write(Text_toFile)
                    file_content.close()

                def Change_Password_Actual():
                    Path = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Userfld.get() + " Data" + ".txt:Secret.txt"
                    if (ChgPassfld.get() != ReChgPassfld.get()):
                        lbl_Fail = Label(ChangePasswordWindow, text="Passwords don't match", fg='red2',
                                         font=("Calibri", 8, 'bold'), bg="grey15")
                        lbl_Fail.place(x=260, y=225)
                        lbl_Fail.after(2500, lambda: lbl_Fail.destroy())

                    elif (ChgPassfld.get() == ReChgPassfld.get()):
                        if (ReChgPassfld.get() == Read_File(Path)):
                            lbl_Fail2 = Label(ChangePasswordWindow, text="New Password cant be\nsame as current one",
                                              fg='red2',
                                              font=("Calibri", 8, 'bold'), bg="grey15")
                            lbl_Fail2.place(x=260, y=220)
                            lbl_Fail2.after(3500, lambda: lbl_Fail2.destroy())

                        elif (ReChgPassfld.get() != Read_File(Path)):

                            Path2 = "C:\\EncryptedNotes\\" + Userfld.get() + "\\" + Userfld.get() + " Data" + ".txt:Secret.txt"
                            Write_File(Path2, ReChgPassfld.get())

                            ChangePasswordWindow.destroy()
                            SettingsWindow.destroy()
                            MainWindow.destroy()
                            LoginWindow.wm_attributes('-alpha', 1.0)
                            lbl_Success = Label(LoginWindow, text="Password Changed", fg='green',
                                                font=("Calibri", 10, 'bold'), bg="grey15")
                            lbl_Success.place(x=380, y=181)
                            lbl_Success.after(2500, lambda: lbl_Success.destroy())
                            Passfld.delete(0, END)
                            Userfld.delete(0, END)


                def Close_ChangePassword_Window():
                    ChangePasswordWindow.destroy()
                    SettingsWindow.wm_attributes('-alpha', 1.0)

                ChangePasswordWindow = Tk()

                ChangePasswordWindow_app_width = 400
                ChangePasswordWindow_app_height = 500

                ChangePasswordWindow_screen_width = ChangePasswordWindow.winfo_screenwidth()
                ChangePasswordWindow_screen_height = ChangePasswordWindow.winfo_screenheight()

                ChangePasswordWindow_x = int(
                    (ChangePasswordWindow_screen_width / 2) - (ChangePasswordWindow_app_width / 2))
                ChangePasswordWindow_y = int(
                    (ChangePasswordWindow_screen_height / 2) - (ChangePasswordWindow_app_height / 2))

                lbl_Title_Settings = Label(ChangePasswordWindow, text="Change Password",
                                           font=("Arial Black", 12, "bold"), bg='grey15',
                                           fg="white")
                lbl_Title_Settings.place(x=125, y=10)

                lbl_Password = Label(ChangePasswordWindow, text="Password:", fg='white',
                                     font=("Arial Black", 9, 'bold'), bg="grey15")
                lbl_Password.place(x=60, y=150)

                ChgPassfld = Entry(ChangePasswordWindow, text="This is Change Password Widget", bd=1, fg='white',
                                   font=("Arial Black", 9, 'bold'), bg="grey8", width=35)  # Passcode feild
                ChgPassfld.place(x=60, y=170)
                ChgPassfld.config(show="*")
                ChgPassfld.config(insertbackground="white")  # Changes test cursor color

                lbl_RePassword = Label(ChangePasswordWindow, text="Re-Enter Password:", fg='white',
                                       font=("Arial Black", 9, 'bold'), bg="grey15")
                lbl_RePassword.place(x=60, y=250)

                ReChgPassfld = Entry(ChangePasswordWindow, text="This is RePassword Widget", bd=1, fg='white',
                                     font=("Arial Black", 9, 'bold'), bg="grey8", width=35)  # Passcode feild
                ReChgPassfld.place(x=60, y=270)
                ReChgPassfld.config(show="*")
                ReChgPassfld.config(insertbackground="white")  # Changes test cursor color

                btn_Login = Button(ChangePasswordWindow, text="Change", padx=60, pady=1,
                                   font=("Arial Black", 9, 'bold'), fg='white', bg="grey8",
                                   command=Change_Password_Actual)
                btn_Login.place(x=112, y=370)

                ChangePasswordWindow.wm_attributes('-alpha')  # Transparency
                ChangePasswordWindow.protocol("WM_DELETE_WINDOW", Close_ChangePassword_Window)
                ChangePasswordWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                ChangePasswordWindow.title('Settings')  # Add Username to top of WebPage
                ChangePasswordWindow.geometry(
                    f'{ChangePasswordWindow_app_width}x{ChangePasswordWindow_app_height}+{ChangePasswordWindow_x}+{ChangePasswordWindow_y}')  # 400x500
                ChangePasswordWindow.configure(bg='grey15')
                ChangePasswordWindow.mainloop()

            def Show_All():
                lbl_Gmail_Show = Label(SettingsWindow, text=Read_Gmail(), font=("Arial Black", 12, "bold"), bg='grey8',
                                       fg="white")
                lbl_Gmail_Show.place(x=110, y=100)

                lbl_Username_Show = Label(SettingsWindow, text=Userfld.get(), font=("Arial Black", 12, "bold"),
                                          bg='grey8',
                                          fg="white")
                lbl_Username_Show.place(x=151, y=200)

                lbl_Password = Label(SettingsWindow, text=Passfld.get(), font=("Arial Black", 12, "bold"), bg='grey8',
                                     fg="white")
                lbl_Password.place(x=150, y=300)


            SettingsWindow = Tk()

            SettingsWindow_app_width = 400
            SettingsWindow_app_height = 500

            SettingsWindow_screen_width = SettingsWindow.winfo_screenwidth()
            SettingsWindow_screen_height = SettingsWindow.winfo_screenheight()

            SettingsWindow_x = int((SettingsWindow_screen_width / 2) - (SettingsWindow_app_width / 2))
            SettingsWindow_y = int((SettingsWindow_screen_height / 2) - (SettingsWindow_app_height / 2))

            lbl_Title_Settings = Label(SettingsWindow, text="Settings", font=("Arial Black", 12, "bold"), bg='grey15',
                                       fg="white")
            lbl_Title_Settings.place(x=160, y=10)

            lbl_Accent = Label(SettingsWindow, text="", font=("Arial Black", 12, "bold"), bg='grey8',
                               fg="white", relief="sunken", width=30, height=18)
            lbl_Accent.place(x=32, y=50)

            lbl_Gmail = Label(SettingsWindow, text="  Gmail:  ", font=("Arial Black", 12, "bold"), bg='grey8',
                              fg="grey85")
            lbl_Gmail.place(x=35, y=100)

            lbl_Username = Label(SettingsWindow, text="  Username:  ", font=("Arial Black", 12, "bold"), bg='grey8',
                                 fg="grey85")
            lbl_Username.place(x=35, y=200)

            lbl_Password = Label(SettingsWindow, text="  Password: ", font=("Arial Black", 12, "bold"), bg='grey8',
                                 fg="grey85")
            lbl_Password.place(x=35, y=300)

            btn_Show_Pass = Button(SettingsWindow, text=" Show All", fg='white', font=("Calibri", 8, 'bold'),
                                   bg="green", relief="flat", command=Show_All)
            btn_Show_Pass.place(x=175, y=355)

            btn_Delete_Account = Button(SettingsWindow, text=" Delete Account ", fg='white',
                                        font=("Calibri", 8, 'bold'),
                                        bg="red", relief="flat", command=Delete_Account)
            btn_Delete_Account.place(x=240, y=430)

            btn_Delete_Account = Button(SettingsWindow, text=" Change Password ", fg='white',
                                        font=("Calibri", 8, 'bold'),
                                        bg="blue", relief="flat", command=Change_Password)
            btn_Delete_Account.place(x=75, y=430)

            SettingsWindow.wm_attributes('-alpha')  # Transparency
            SettingsWindow.protocol("WM_DELETE_WINDOW", Close_Settings_Window)
            SettingsWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
            SettingsWindow.title('Settings')  # Add Username to top of WebPage
            SettingsWindow.geometry(
                f'{SettingsWindow_app_width}x{SettingsWindow_app_height}+{SettingsWindow_x}+{SettingsWindow_y}')  # 400x500
            SettingsWindow.configure(bg='grey15')
            SettingsWindow.mainloop()


        MainWindow = Tk()

        MainWindow_app_width = 400
        MainWindow_app_height = 500

        MainWindow_screen_width = MainWindow.winfo_screenwidth()
        MainWindow_screen_height = MainWindow.winfo_screenheight()

        MainWindow_x = int((MainWindow_screen_width / 2) - (MainWindow_app_width / 2))
        MainWindow_y = int((MainWindow_screen_height / 2) - (MainWindow_app_height / 2))

        Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='white', font=("Arial", 11, 'bold'), bg="grey8",
                                             width=30,
                                             height=22)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
        Note_fld.place(x=35, y=30)
        Note_fld.insert(1.0, Check_txt_Files())
        Note_fld.config(insertbackground="white")
        Note_fld.config(state=DISABLED)

        openfld = Entry(MainWindow, text="Username", bd=1, fg='white', bg="grey8", font=("Arial Black", 9, 'bold'),
                        width=24)  # Gmail feild
        openfld.place(x=35, y=445)
        openfld.config(insertbackground="white")

        btn_Open = Button(MainWindow, text="Open", padx=11, pady=1, font=("Arial Black", 7, 'bold'), fg='white',
                          bg="grey8", command=Open_Note)
        btn_Open.place(x=245, y=445)

        btn_Open = Button(MainWindow, text="+", font=("Arial", 15), fg='white', bg="grey8", width=3, height=1, command=New_Btn)
        btn_Open.place(x=335, y=445)

        btn_Settings = Button(MainWindow, text="Settings ⚙", font=("Arial Black", 7), fg='white', bg="grey8",
                          command=Settings_Btn)
        btn_Settings.place(x=317, y=30)


        MainWindow.wm_attributes('-alpha', 1.0)  # Transparency
        MainWindow.protocol("WM_DELETE_WINDOW", Close_Note_Window)  # controlling the function of the close window icon (top right of window)
        MainWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
        MainWindow.title('Notes')  # Add Username to top of WebPage
        MainWindow.geometry(f'{MainWindow_app_width}x{MainWindow_app_height}+{MainWindow_x}+{MainWindow_y}') #400x500
        MainWindow.configure(bg='grey15')
        MainWindow.mainloop()

    else:
        lbl_Fail = Label(LoginWindow, text="Error", fg='red', font=("Calibri", 10, 'bold'), bg="grey15")
        lbl_Fail.place(x=380, y=181)
        lbl_Fail.after(2500, lambda: lbl_Fail.destroy())


def Accounts():
    LoginWindow.wm_attributes('-alpha', 0.0)  # Transparency

    def Close_Accounts_Window():
        AccountsWindow.destroy()
        LoginWindow.wm_attributes('-alpha', 1.0)

    def Get_Accounts_Count():
        path = "C:\\EncryptedNotes"
        dir_list = os.listdir(path)
        return len(dir_list)

    def Get_Accounts():
        path = "C:\\EncryptedNotes"
        dir_list = os.listdir(path)
        i = 0
        while i < len(dir_list):
            Accounts_Viewfld.insert(1.0, dir_list[i] + "\n")
            i = i + 1

    AccountsWindow = Tk()

    AccountsWindow_app_width = 500
    AccountsWindow_app_height = 400

    AccountsWindow_screen_width = AccountsWindow.winfo_screenwidth()
    AccountsWindow_screen_height = AccountsWindow.winfo_screenheight()

    AccountsWindow_x = int((AccountsWindow_screen_width / 2) - (AccountsWindow_app_width / 2))
    AccountsWindow_y = int((AccountsWindow_screen_height / 2) - (AccountsWindow_app_height / 2))

    lbl_Title_View = Label(AccountsWindow, text="Accounts", font=("Arial Black", 12, "bold"), bg='grey15',
                           fg="white")
    lbl_Title_View.place(x=210, y=10)

    Accounts_Viewfld = scrolledtext.ScrolledText(AccountsWindow, bd=1, fg='white', font=("Arial Black", 10, 'bold'),
                                                 bg="black", width=33,
                                                 height=17)  # Encrypt_Viewfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
    Accounts_Viewfld.place(x=30, y=50)

    Get_Accounts()
    Accounts_Viewfld.config(state=DISABLED)
    Accounts_Viewfld.config(insertbackground="white")

    lbl_NumberCount_Acc = Label(AccountsWindow, text=Get_Accounts_Count(), font=("Arial Black", 9, "bold"),
                                bg='black', fg="white",
                                relief="sunken", height=3, width=7)  # Make text=Read_File
    lbl_NumberCount_Acc.place(x=390, y=160)

    AccountsWindow.wm_attributes('-alpha')  # Transparency
    AccountsWindow.protocol("WM_DELETE_WINDOW",
                            Close_Accounts_Window)  # controling the function of the close window icon (top right of window)
    AccountsWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
    AccountsWindow.title('Accounts')  # Add Username to top of WebPage
    AccountsWindow.geometry(
        f'{AccountsWindow_app_width}x{AccountsWindow_app_height}+{AccountsWindow_x}+{AccountsWindow_y}')  # 500x400
    AccountsWindow.configure(bg='grey15')
    AccountsWindow.mainloop()


def Close_Login_Window():
    LoginWindow.destroy()


LoginWindow = Tk()


LoginWindow_app_width = 500
LoginWindow_app_height = 400


LoginWindow_screen_width = LoginWindow.winfo_screenwidth()
LoginWindow_screen_height = LoginWindow.winfo_screenheight()


LoginWindow_x = int((LoginWindow_screen_width / 2) - (LoginWindow_app_width / 2))
LoginWindow_y = int((LoginWindow_screen_height / 2) - (LoginWindow_app_height / 2))


lbl_Gmail=Label(LoginWindow, text="Username:", fg='white', font=("Arial Black", 9, 'bold'), bg="grey15" )
lbl_Gmail.place(x=110, y=120)


Userfld=Entry(LoginWindow, text="Username", bd=1, fg='white',  bg="grey8" , font=("Arial Black", 9, 'bold'), width=35)   #Gmail feild
Userfld.place(x=110, y=140)
Userfld.config(show="x")
Userfld.config(insertbackground="white")


lbl_Access=Label(LoginWindow, text="Password:", fg='white', font=("Arial Black", 9, 'bold'), bg="grey15")
lbl_Access.place(x=110, y=200)

Passfld=Entry(LoginWindow, text="This is Password Widget", bd=1, fg='white', font=("Arial Black", 9, 'bold'), bg="grey8", width=35)    #Passcode feild
Passfld.place(x=110, y=220)
Passfld.config(show="*")
Passfld.config(insertbackground="white")#Changes test cursor color


btn_Login = Button(LoginWindow, text="Login", padx = 60, pady=1 , font=("Arial Black", 9, 'bold'), fg='white', bg="grey8" , command =LoginBtn)
btn_Login.place(x=170, y=270)


btn_Create=Button(LoginWindow, text="Create Account", fg='white', font=("Arial Black", 9, 'bold'), bg="grey8", command=CreateAccBtn)
btn_Create.place(x=380, y=360)



btn_Create=Button(LoginWindow, text="Accounts", fg='white', font=("Arial Black", 9, 'bold'), bg="grey8", command = Accounts)
btn_Create.place(x=10, y=360)




LoginWindow.wm_attributes('-alpha', 1.0)  # Transparency
LoginWindow.protocol("WM_DELETE_WINDOW",Close_Login_Window)  # controling the function of the close window icon (top right of window)
LoginWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
LoginWindow.title('Login')  # Add Username to top of WebPage
LoginWindow.geometry(f'{LoginWindow_app_width}x{LoginWindow_app_height}+{LoginWindow_x}+{LoginWindow_y}') #500x400
LoginWindow.configure(bg='grey15')
LoginWindow.mainloop()


















