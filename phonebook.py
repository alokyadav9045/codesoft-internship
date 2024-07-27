import tkinter as tk
from tkinter import messagebox
import sqlite3

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")

        # Create or connect to an SQLite database
        self.conn = sqlite3.connect("contacts.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
        self.conn.commit()

        self.name_label = tk.Label(root, text="Name:",font=('calibre',20,'bold'),width=40,)
        self.name_label.pack()
        self.name_entry = tk.Entry(root,width=40,)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:",font=('calibre',20,'bold'),width=40,)
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root,width=40,)
        self.phone_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact,font=('calibre',15,'bold'),)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact,font=('calibre',15,'bold'),)
        self.delete_button.pack()

        self.contacts_listbox = tk.Listbox(root,width=40,)
        self.contacts_listbox.pack()

        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            self.cursor.execute("INSERT INTO contacts VALUES (?, ?)", (name, phone))
            self.conn.commit()
            self.load_contacts()
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def delete_contact(self):
        name_to_delete = self.name_entry.get()

        if name_to_delete:
            self.cursor.execute("DELETE FROM contacts WHERE name=?", (name_to_delete,))
            self.conn.commit()
            self.load_contacts()
            messagebox.showinfo("Success", f"Contact {name_to_delete} deleted successfully!")
        else:
            messagebox.showerror("Error", "Please enter a name to delete.")

    def load_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT name FROM contacts")
        contacts = self.cursor.fetchall()
        for contact in contacts:
            self.contacts_listbox.insert(tk.END, contact[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
