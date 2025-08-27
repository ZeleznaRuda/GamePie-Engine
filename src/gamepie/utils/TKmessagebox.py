import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.withdraw()
    
def info( title, msg):
        messagebox.showinfo(title, msg)
    
def warning( title, msg):
        messagebox.showwarning(title, msg)
    
def error( title, msg):
        messagebox.showerror(title, msg)
    
def askyesno( title, msg):
        return messagebox.askyesno(title, msg)
    
def skokcancel( title, msg):
        return messagebox.askokcancel(title, msg)
    
def destroy():
        root.destroy()


