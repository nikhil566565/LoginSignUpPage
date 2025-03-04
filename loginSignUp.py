
import mysql.connector as ms
from tkinter import messagebox
import tkinter as tk 
from PIL import Image, ImageTk

def connectDatabase():
    try:    
        return ms.connect(
            host="localhost",
            user="root",
            password="root",
            database="login_sign"
        )
    except ms.Error as err:
        messagebox.showerror("Database Error", str(err))
        return None
    
def login() :
    UserName1 = e1.get()
    Password1 = e2.get()

    if(UserName1 == "" and Password1 == ""): 
        messagebox.showerror("Error", "Please enter both UserName and Password")
        return
    
    conn = connectDatabase()
  
    try :
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM login_sign WHERE userIn = %s AND passIn = %s",(UserName1, Password1))
        user = mycursor.fetchone()

        if(user) :
            messagebox.showinfo("Successfully", "Successfully logged in Your Account")
        else :
            messagebox.showerror("Error", "Invalid UserName or Password !")

    except Exception as e :
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
        mycursor.close()
    # root.destroy() # Destroy Panel

    
def submit_signup(firstIn, lastIn, userIn, passIn, confirmIn) :
    conn = connectDatabase()
    if(not conn) :
        return
    
    first = firstIn.get()
    last = lastIn.get()
    user = userIn.get()
    password = passIn.get()
    confirm_pwd = confirmIn.get()

    if(not first and last and user and password and confirm_pwd) :
        messagebox.showerror("Error", "Please fill all the fields")
        return
    if(password != confirm_pwd) :
        messagebox.showerror("Error", "Your password is incorrect")
        return

    try :
        mycursur = conn.cursor()
        query = "INSERT INTO login_sign(firstIn, lastIn, userIn, passIn) VALUES (%s, %s, %s, %s)"   
        values = (first,last,user,password)
        mycursur.execute(query, values)
        conn.commit()
        messagebox.showinfo("Succcues","Your Account has been created successfully")
        root1.destroy()
    except ms.Error as err :
        messagebox.showinfo("Data Base Error",str(err))
    finally :
        mycursur.close()
        conn.close()
              

def signup() :
    root.destroy()
    global root1
    root1 = tk.Tk()
    root1.title("Sign-Up")
    root1.config(bg = '#D9EAFD')
    root1.geometry("500x400")
    headlineSignup = tk.Label(root1, text="Sign-Up",font=("Georgia","18"), bg="#D9EAFD").pack(pady=10)
    
    firstName = tk.Label(root1, text="FirstName : ", font=("Georgia", 10),bg="#D9EAFD").place(x=110, y=123)
    lastName = tk.Label(root1, text="LastName : ", font=("Georgia", 10), bg="#D9EAFD").place(x=110, y=153)
    userName = tk.Label(root1, text="UserName : ", font=("Georgia", 10), bg="#D9EAFD").place(x=110, y=183)
    Password = tk.Label(root1, text="Password : ", font=("Georgia", 10), bg="#D9EAFD").place(x=110, y=213)
    confirmPassword = tk.Label(root1, text="ConfirmPassword: ",  font=("Georgia", 10), bg="#D9EAFD").place(x=110, y=243) 
    
    firstIn = tk.Entry()
    lastIn = tk.Entry()
    userIn = tk.Entry()
    passIn = tk.Entry(show="*")
    confirmIn = tk.Entry(show="*")
    
    firstIn.place(x=235, y=123)
    lastIn.place(x=235, y=153)
    userIn.place(x=235, y=183)
    passIn.place(x=235, y=213)
    confirmIn.place(x=235, y=243)
    Sign_In_Button = tk.Button(root1, text="Sign_In", font=("Georgia", 9), bg="#A1D6CB",padx=30, pady=5, command=signInButton).place(x=120,y=70)
    Sign_Up_Button = tk.Button(root1, text="Sign_Up", font=("Georgia", 9), bg="#A1D6CB",padx=30, pady=5).place(x=250,y=70)

    submit = tk.Button(root1, text="Submit", font=("Georgia", 9), bg="#A1D6CB",padx=80, pady=10, command=lambda: submit_signup(firstIn, lastIn, userIn, passIn, confirmIn)).place(x=130,y=290)

def signInButton() :
    root1.destroy()
    signIn()

def signIn() :

    global root
    root = tk.Tk()
    root.config(bg = '#D9EAFD')
    root.geometry("500x400")
    root.title("Login From")
    
    user_image = Image.open("./Images/4160457-512-removebg-preview(1).png")
    resize_image = user_image.resize((15, 15))
    user_logo = ImageTk.PhotoImage(resize_image)
    root.logo = user_logo
    
    username_logo = tk.Label(root, image=root.logo, bg="#d4e1f5")
    username_logo.place(x=87, y=152)
    
    # pass_image = Image.open("./Images/16205-512-removebg-preview.png")
    # resize_pass_image = user_image.resize((15, 15))
    # pass_logo = ImageTk.PhotoImage(resize_pass_image)
    # root.logo = pass_logo
    
    # pass_logo = tk.Label(root, image=root.pass_logo, bg="#d4e1f5")
    # pass_logo.place(x=87, y=152)

    # boldFont = font.Font(family="Georgia",size="14")
    headline = tk.Label(root, text="Login From", font=("Georgia","18"), bg="#D9EAFD")  # Set the window title
    headline.pack() # Place the label in the window

    User = tk.Label(root, text="UserName :", font=("Georgia", 10), bg="#D9EAFD").place(x=110, y=150)
    password = tk.Label(root, text="Password :", font=("Georgia", 10), bg="#D9EAFD").place(x = 110, y=180)
    global e1
    global e2
    
    e1 = tk.Entry(width=25)
    e2 = tk.Entry(show="*",width=25)
    e1.place(x=200, y=153)
    e2.place(x=200, y=183)

    b1 = tk.Button(root, text="SignIn", font=("Georgia", 9), bg='#A1D6CB',  fg="black", padx=30, pady=5).place(x=125, y=80)
    b2 = tk.Button(root, text="SignUp", font=("Georgia", 9), bg='#A1D6CB',  fg="black", padx=20, pady=5, command=signup).place(x=250, y=80)

    b3 = tk.Button(root, text="Login", font=("Georgia", 9), bg='#A1D6CB', padx=60, pady=10, fg="black" ,command=login).place(x=155, y=230)

    root.mainloop()
      
signIn()
