# import all the required packages
# Visit : codewithcurious.com for more projects
from tkinter import *
import random

# To create a root window of GUI in python
tk=Tk()
tk.title('Password Generate')
tk.geometry('400x220+100+100')
tk.configure(background='Green')
tk.resizable(False, False)


# To store/retrieve the string value entered by user
pswd=StringVar()

# To store/retrieve the Integer value entered by user
passlen=IntVar()
passlen.set('Enter Length')

# Function to generate a random password
def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
    password=''
    if passlen.get()>=0:
        for i in range(passlen.get()):
            password+=random.choice(characters)
        pswd.set(password)

# Function to copy generated password to clipboard
def copyclipboard():
    random_password = pswd.get()
    Label(tk,text="Copied to Clipboard",bg="red").pack(pady=6)

# Label to display the primary instruction to user to enter the length of passwod he requires
Label(tk,  font=('arial', 15, 'bold'),bg='green', text="Enter the number to get password)",fg='white').pack(pady=10)

# To store the entry of user
Entry(tk, width=30, bd=2, textvariable=passlen).pack(pady=6)

# To generate Random password and confirmation by the button click
Button(tk, text="Generate Password", width=15,height=1,bd=2, command=password_generator,bg='black',fg='white').pack(pady=4)
Entry(tk,width=30, bd=2, textvariable=pswd).pack(pady=3)

Button(tk, text="Copy",width=7,height=1,bd=2, command=copyclipboard,bg='black',fg='white').pack()
# To initiate and display the root window we created
tk.mainloop()