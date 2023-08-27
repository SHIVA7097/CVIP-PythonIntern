import tkinter
from tkinter import * 
import random

window = tkinter.Tk()
window.title('Random Password Generator')
window.geometry('450x450')  # specify the size of the window

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+='

characters = alpha + numbers + symbols

label_characters = Label(window, text="Number of characters", font=("ComicSansMS", 14)).pack(padx=10)
character_length = Entry(window, font="ComicSansMS 16")
character_length.pack(padx=10)

# function to generate password
def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text='' + password,bg='white')   

# function to display the generated password
Button(window, text="Generate Password", command=generate_password, font=("ComicSansMS", 14)).pack(padx=10)
label_password = Label(window, font=("ComicSansMS", 14))
label_password.pack()

window.mainloop()

