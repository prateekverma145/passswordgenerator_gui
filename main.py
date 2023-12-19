
import tkinter as tk
from tkinter import messagebox
from random import randint,choice,shuffle
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
password=""
PATH="data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password_gen():
    password_entry.delete(0,tk.END) 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password=""
    for i in password_list:
        password+=i
    password_entry.insert(0,password) 
   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={website:{
        "email":email,
        "password":password
    }}

    if len(website) == 0 or len(password) == 0:
        tk.messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = tk.messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open(PATH,"r") as data_file:
                    old_data=json.load(data_file)
                    new_data.update(old_data)
                    with open(PATH,'w') as data_file:
                        json.dump(new_data,data_file,indent=4)
                        
            except FileNotFoundError:            
                with open(PATH, "w") as data_file:
                    json.dump(new_data,data_file,indent=4)
          
                        
            website_entry.delete(0, tk.END)
            password_entry.delete(0,tk. END)
# ---------------------------- search ------------------------------- #
def search():
    web=website_entry.get()
    if web!="":
        with open(PATH,"r") as dta:
            data=json.load(dta)
            try:
                sd=data[web]  
            except KeyError:
                tk.messagebox.showinfo(title="Oops", message=" Not found")
            else:
                sd=data[web]
                em=sd["email"]
                passd=sd["password"]    
                mess=f''' Email : {em}
                password : {passd}'''
                password_entry.delete(0,tk.END)
                password_entry.insert(0,passd)
                email_entry.delete(0,tk.END)
                email_entry.insert(0,em)
                
                    
        
    

# ---------------------------- UI SETUP ------------------------------- #

window =tk. Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas =tk. Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_l=tk.Label(text="webiste:",font=(FONT_NAME,))
web_l.grid(column=0,row=1)
email_l=tk.Label(text="Email/username:",font=(FONT_NAME,))
email_l.grid(column=0,row=2)
password_label = tk.Label(text="Password:",font=(FONT_NAME,))
password_label.grid(row=3, column=0)


website_entry =tk. Entry(width=35)
website_entry.grid(row=1, column=1, )
website_entry.focus()
email_entry = tk.Entry(width=57)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Your email id")
password_entry =tk. Entry(width=35)
password_entry.grid(row=3, column=1)

search_btn=tk.Button(text="Search",width=11,command=search)
search_btn.grid(row=1,column=2)
generate_password_button = tk.Button(text="Generate Password",command=random_password_gen)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=35,command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
 