from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letter=[random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols=[random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list=password_numbers+password_symbols+password_letter
    random.shuffle(password_list)

    password="".join(password_list)
    pas.insert(0,password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    wbst=webe.get()
    email=emtr.get()
    pad=pas.get()
    new_data={
        wbst:{"Email":email,
                 "Password":pad }
             }

    if len(wbst) == 0 or len(pad) == 0:
        messagebox.showinfo(title="OOOPs", message="you forgot to fill the enail and password")
    else:
            try:
                with open("data.json","r")  as f:
                      d=json.load(f)


            except(FileNotFoundError, json.decoder.JSONDecodeError):

                with open('data.json', 'w') as f:
                    json.dump(new_data, f, indent=4)

            else:

                d.update(new_data)
                with open("d.json", "w") as f:
                    json.dump(d, f,indent=4)


            webe.delete(0,END)
            emtr.delete(0,END)
            pas.delete(0,END)


def search():
    wbst = webe.get()
    email = emtr.get()
    try:
        with open("d.json") as f:
            x=json.load(f)

    except FileExistsError:
        messagebox.showinfo(title="Error", message="you forgot to fill the enail and password")
    else:
        if wbst in x:
                email=x[wbst]["Email"]
                pas=x[wbst]["Password"]
                messagebox.showinfo(title="Get it 😀😀 " ,message=f" ur Email is {email}, your password is {pas} ")
        else:
            messagebox.showinfo(title="Error ", message=f"No Records found ")


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=45,pady=45)
canvas=Canvas(width=200,height=200)
ig=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=ig)
canvas.grid(column=1,row=0)

web=Label(text="Website:",font=("Arial",10,"bold"))
web.grid(column=0,row=1)


webe=Entry(width=34)
webe.grid(column=1,row=1, columnspan=2,sticky="w")
webe.focus()

search=Button(text="search",width= 16, font=("Arial",10,"bold"),command=search)
search.grid(column=2,row=1,sticky="w")


email=Label(text="Email/Username:",font=("Arial",10,"bold"))
email.grid(column=0,row=2)





emtr=Entry(width=58)
emtr.grid(column=1,row=2,sticky="w",columnspan=2)
emtr.insert(0,"maxpame@yahoo.fr")

passwrd=Label(text="Password:",font=("Arial",10,"bold"))
passwrd.grid(column=0,row=3,sticky="w")


pas=Entry(width=35)
pas.grid(column=1,row=3,sticky="w")

gpass=Button(text="Generate Password",font=("Arial",10,"bold"),command=generate)
gpass.grid(column=2,row=3,sticky="w")

add=Button(text="ADD",width=43,font=("Arial",10,"bold"),command=save)
add.grid(column=1,row=4 ,columnspan=2)













window.mainloop()
