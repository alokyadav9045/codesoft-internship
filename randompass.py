 

import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    desired_length = int(length_entry.get())
    generated_password = generate_password(desired_length)
    password_label.config(text=f"Generated password: {generated_password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
# Create widgets
length_label = tk.Label(root, text="Desired password length:",font=('calibre',20,'bold'),width=40,)
length_entry = tk.Entry(root,font=('calibre',15,'bold'),width=10,background="gray")
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password,font=('calibre',10,'bold'),width=20,background="gray")
password_label = tk.Label(root, text="",font=('calibre',20,'bold'),width=40)

# Arrange widgets
length_label.pack()
length_entry.pack()
generate_button.pack()
password_label.pack()

# Start the GUI event loop
root.mainloop()
