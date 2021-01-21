from tkinter import *
from tkinter import messagebox
# BACKGROUND_COLOR = "#f6f5f5"


window = Tk()
window.title = "Password Manger"
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200,)
image = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# save Password
def save():
    webstie = website_entry.get()
    email = email_entry.get()
    passwordd = password_entry.get()

    if len(webstie) ==0 or len(passwordd) == 0:
        messagebox.showinfo(title="Problems", message="Not all Boxes are Filled in")
    else:
        is_okay = messagebox.askokcancel(title=webstie, message=f" Are these details correct: \nEmail: {email}"
                                                                f"\nPassword: {passwordd} \n Is it okay to save")
        if is_okay:
            with open("pass.txt", "a") as pass_file:
                pass_file.write(f"\n{webstie} | {email} | {passwordd}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# Labels

website_txt = Label(text="Website:")
website_txt.grid(row=1, column=0)
email = Label(text="Email/Username")
email.grid(row=2, column=0)
password = Label(text="Password")
password.grid(row=3, column=0)

# input boxes
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
# For default autofill email enter your email below
# email_entry.insert(END, "EMAIL")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

#buttons
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()