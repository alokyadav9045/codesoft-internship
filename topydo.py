import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showerror("Error", "No task selected!")

 
 
ws = tk.Tk()
ws.title("To-Do List")
ws['bg']="gray"




frame = tk.Frame(ws)
listbox = tk.Listbox(frame, selectmode=tk.SINGLE,height=14,width=70,font=('bold'),background="skyblue")
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
entry = tk.Entry(ws,font=('calibre',20,'bold'),width=40,background="skyblue")
add_button = tk.Button(ws, text="Add Task", command=add_task,font=('calibre',20,'bold'),width=20,background="skyblue")
delete_button = tk.Button(ws, text="Delete Task", command=delete_task,font=('calibre',20,'bold'),width=20,background="skyblue")




listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
frame.pack(padx=10, pady=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
entry.pack(pady=20)
add_button.pack(pady=10)
delete_button.pack(pady=10)



ws.mainloop()
