import json
from tkinter import * #this only import the classes, the consatant
from tkinter import messagebox
import random
import os
from dotenv import load_dotenv

load_dotenv()

Minimum=8 # we must have at least 8 caracteres for a password
Maximum=15


#functions

def add():
    web_data = website.get().title()
    mail_data = mail.get()
    password_data = password_entry.get()

    e_mail=os.getenv("MAIL")
    password=os.getenv("PASSWORD")
    data={web_data:{
        e_mail:mail_data,
        password:password_data
    }
    }

    if web_data=="" or mail_data=="" or password_data==" ": #preventing errors
        messagebox.showinfo(title='warning',message="make sure that you have fill all the boxes")
        website.delete(0, END)
        mail.delete(0, END)
        password_entry.delete(0, END)

    else:
        confirm=messagebox.askokcancel(title="confirmation",message="are you sure that all the informations are correct")
        if confirm:
            path=os.getenv("DATA_PATH")
            #print(path)
            try: #we try it because if it's the first time we can get an error by reading a file that doesn't exist
                with open(path,"r") as data_file:
                    read_data=json.load(data_file)
                    data.update(read_data)#we update our data dictionnary in order to have a valid data structure
            except:
                with open(path,"w") as data_file:
                    json.dump(data,data_file,indent=4)
            else:
                with open(path,"w") as data_file:
                    json.dump(data,data_file,indent=4)

        #we clear entry boxes
        website.delete(0, END)
        mail.delete(0, END)
        password_entry.delete(0, END)


def generate():
    global Maximum,Minimum
    if password_entry.get() == "":  # this condition allows us to generate only one password even when we double click generate password button
        l1=[chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)] #alphabet list using ascii
        l2 = [
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
            ',', '.', ':', ';', "'", '"', '<', '>', '/', '\\', '?', '!',
            '+', '-', '*', '/', '%',
            '$', '€', '£', '¥',
            '↑', '↓', '←', '→',
            '@', '#', '&', '_', '~',
            '...', '–', '—'
        ]
        l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        l=l1+l2+l3
        number=random.randint(Minimum,Maximum+1)
        password=""
        for i in range(0,number+1):
            password+=str(random.choice(l))

        password_entry.insert(END, string=password) #we insert it onto the password entry



def search(): #this function allows us to search our mail and password just by writing the name of the website
    web_data = website.get().title()
    if web_data!="":
        path=os.getenv("DATA_PATH")
        try:#the user can try it at the first time (when the json file does not exist)
            with open(path,"r") as data_file: #we open our json file to search our data
                read_data=json.load(data_file)
        except:
            messagebox.showinfo(title="password manager",message="your password manager is empty")
        else:
            if web_data in read_data.keys(): # si le site est dans le dictionnaire de donnees(json file)
                mail=read_data[web_data][os.getenv("MAIL")]
                password=read_data[web_data][os.getenv("PASSWORD")]
                messagebox.showinfo(title=web_data,message=f"mail: {mail}\npassword: {password}")
            else:
                messagebox.showinfo(title=web_data,message=f"you have not registered with {web_data}")
    else:
            messagebox.showinfo(title="oops",message="please fill the website box")
#window
window=Tk()
window.title("password manager")
window.config(padx=30,pady=30,bg="#C7B7A3")
#canvas
canvas=Canvas(width=360,height=360,bg="#C7B7A3")
image=PhotoImage(file="background.png")
canvas.create_image(180,180,image=image)
canvas.grid(column=1,row=1)
#label
label=Label()
label.config(text="password manager",fg="blue",font=("Helvetica", 24, "bold"))
label.grid(column=1,row=3)
web_label=Label()
web_label.config(text="Website :",bg="#C7B7A3")
web_label.grid(row=4,column=0)
mail_label=Label()
mail_label.config(text="user_name/mail :",bg="#C7B7A3")
mail_label.grid(row=6,column=0)
password_label=Label()
password_label.config(text="password :",bg="#C7B7A3")
password_label.grid(row=8,column=0)
#Entry
website=Entry(width=35)
website.grid(row=4,column=1)
mail=Entry(width=35)
mail.grid(row=6,column=1)
password_entry=Entry(width=35)
password_entry.grid(row=8,column=1)
#buttons
add=Button(text="add",width=35,command=add)#we will add the command
generate_password=Button(text="generate password",command=generate) #we will add a command
add.grid(row=10,column=1)
generate_password.grid(row=8,column=2)
search=Button(text="search",width=35,command=search)
search.grid(row=4,column=2)


window.mainloop()