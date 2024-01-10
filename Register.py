import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RegisterClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Page")

        # Variables to store register data
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Username Entry
        username_label = ttk.Label(self.root, text="Username:")
        username_label.pack(pady=10)

        username_entry = ttk.Entry(self.root, textvariable=self.username_var)
        username_entry.pack(pady=10)

        # Password Entry
        password_label = ttk.Label(self.root, text="Password:")
        password_label.pack(pady=10)

        password_entry = ttk.Entry(self.root, textvariable=self.password_var)
        password_entry.pack(pady=10)

        # Confirm Password Entry
        confirm_password_label = ttk.Label(self.root, text="Confirm Password:")
        confirm_password_label.pack(pady=10)

        confirm_password_entry = ttk.Entry(self.root, textvariable=self.confirm_password_var)
        confirm_password_entry.pack(pady=10)

        # Register Button
        register_button = ttk.Button(self.root, text="Register", command=self.register)
        register_button.pack(pady=20)

    def register(self):
        username = self.username_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if username and password and confirm_password:
            if password == confirm_password:
                tk.messagebox.showinfo(title="Register Success", message="You have successfully registered")
                self.root.destroy()
            else:
                tk.messagebox.showerror(title="Register Failed", message="Passwords do not match")
        else:
            tk.messagebox.showerror(title="Register Failed", message="Please fill in all fields")