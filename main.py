from tkinter import *
import tkinter
from tkinter import messagebox
from secret_password import Password
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def save_email_username_for_next_time():
    """Saves email in txt file, so it can be used the next time that app is open"""
    email_username_data = email_username_entry.get()
    if len(email_username_data) == 0:
        messagebox.showerror(title="Error", message="Please, enter an email address or username")
    else:
        with open("email.txt", "w") as email_file:
            email_file.write(f"{email_username_data}")
            messagebox.showinfo(title="Success!", message="Email address was saved to be used the next time")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# This creates password mechanism
encrypted_password = Password()
# ---------------------------- SAVE PASSWORD ------------------------------- #

def register_text():
    """Registers every input by user. If any entry is empty, user will not be able to continue.
    Once all entries are saved in data.txt file, they will by empty again to enter another data
    """
    website_data = website_entry.get()
    email_username_data = email_username_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data:{
            "email": email_username_data,
            "password": password_data
        }
    }
    with open("data.json") as json_file:
        loaded_data = json.load(json_file)  # Read old data
        if website_data in loaded_data:
            messagebox.showwarning(title="Website is already in database", message="If you decide to continue, be aware that "
                                         "details for this website will be overwritten")

    if len(website_data) == 0 or len(email_username_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Error", message="Please, fill all the required spaces")
    else:
        ask_if_continue = messagebox.askyesno(title="Are you sure?", message="Are you sure you want to save this information?")
        if ask_if_continue:
            try:
                with open("data.json", "r") as file:
                    loaded_data = json.load(file)  # Read old data
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=3)  # Saving new data
                    messagebox.showinfo(message="A new Json file was created to store your information")

            except json.decoder.JSONDecodeError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
                    messagebox.showinfo(message="Information was added successfully")
            else:
                loaded_data.update(new_data)  # Updating old data with new data
                with open("data.json", "w") as file:
                    json.dump(loaded_data, file, indent=3)  # Saving new data
                messagebox.showinfo(message="Information was added successfully")
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

        else:
            messagebox.showinfo(message="Information was not added")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def add_password():
    """Adds encrypted password created in secret_password.py """
    password_entry.delete(0, END)
    password_entry.insert(0, f"{encrypted_password.generate_password()}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_data():
    website_data = website_entry.get()
    try:
        with open("data.json", "r") as json_file:
            loaded_data = json.load(json_file)  # Read old data
    except:
        messagebox.showerror("There is no json file to look into for your request")

    else:
        if website_data in loaded_data:
            email = loaded_data[website_data]["email"]
            password = loaded_data[website_data]["password"]
            messagebox.showinfo(title="Website information", message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="No info found", message=f"There are no details for '{website_data}'")


# ---------------------------- UI SETUP ------------------------------- #

# Set up screen
wn = Tk()
wn.config(pady=20, padx=20)
wn.title("Password Manager")

# Set up canvas
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website", padx=10)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username", padx=10)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password", padx=10)
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=35, bg="white", highlightthickness=0)
website_entry.grid(column=1, row=1,columnspan=2, sticky=tkinter.W)
website_entry.focus()

# Uses username or email saved in email.txt to place it in email_username_entry
with open("email.txt") as email_username_file:
    email_or_username = email_username_file.readline()
    email_username_entry = Entry(width=35, bg="white", highlightthickness=0)
    email_username_entry.insert(0, string=email_or_username)
    email_username_entry.grid(column=1, row=2, sticky=tkinter.W)

password_entry = Entry(width=21, bg="white", highlightthickness=0)
password_entry.grid(column=1, row=3, sticky=tkinter.EW)

#Buttons
generate_password_button = Button(text="Generate Password", command=add_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=register_text)
add_button.grid(column=1, row=4, columnspan=2, sticky=tkinter.EW)

save_email_button = Button(text="Save email", command=save_email_username_for_next_time)
save_email_button.grid(column=2, row=2, sticky=tkinter.EW)

search_button = Button(text="Search", command=find_data)
search_button.grid(column=2, row=1, sticky=tkinter.EW)
# Scale
encrypted_password.scale()


wn.mainloop()
