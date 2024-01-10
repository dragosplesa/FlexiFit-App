import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class LoginClass:
    def __init__(self, root, login_success):
        self.root = root
        self.root.title("Login Page")
        self.login_success = login_success

        # Variables to store login data
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

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

        # Login Button
        login_button = ttk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username == "user" and password == "user":
            tk.messagebox.showinfo(title="Login Success", message="You have successfully logged in")
            self.root.destroy()
            self.login_success()
        else:
            tk.messagebox.showerror(title="Login Failed", message="Incorrect username or password")
