import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Register import RegisterClass
from Login import LoginClass

def center_window(width=300, height=200, window=None):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("FlexiFit App")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        custom_font = ("Helvetica", 20, "bold")
        # Title Label
        title_label = ttk.Label(self.root, text="Welcome to FlexiFit!", font= custom_font)
        title_label.pack(side=tk.TOP, pady=50)

        # Login Button
        login_button = ttk.Button(self.root, text="Login", command=self.login)
        login_button.pack(side=tk.TOP, pady=10)

        # Register Button
        register_button = ttk.Button(self.root, text="Register", command=self.register)
        register_button.pack(side=tk.TOP, pady=10)

    def login(self):
        new_window = tk.Tk()
        center_window(300, 200, new_window)
        login = LoginClass(new_window, lambda: start_gym_app(new_window))

    def register(self):
        new_window2 = tk.Tk()
        center_window(300, 200, new_window2)
        register = RegisterClass(new_window2)

def start_gym_app(root):
    new_window = tk.Tk()
    # new_window.geometry("300x500")
    center_window(350, 500, new_window)
    gym_app = GymApp(new_window)

class GymApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Workout Tracker")

        # Variables to store workout data
        self.exercise_var = tk.StringVar()
        self.sets_var = tk.StringVar()
        self.reps_var = tk.StringVar()

        # List to store workout history
        self.workout_history = []

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Exercise Dropdown
        exercise_label = ttk.Label(self.root, text="Exercise:")
        exercise_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        exercises = ["Push-ups", "Pull-ups", "Squats", "Deadlifts", "Planks"]
        exercise_dropdown = ttk.Combobox(self.root, values=exercises, textvariable=self.exercise_var)
        exercise_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Sets Entry
        sets_label = ttk.Label(self.root, text="Sets:")
        sets_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        sets_entry = ttk.Entry(self.root, textvariable=self.sets_var)
        sets_entry.grid(row=1, column=1, padx=10, pady=10)

        # Reps Entry
        reps_label = ttk.Label(self.root, text="Reps:")
        reps_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        reps_entry = ttk.Entry(self.root, textvariable=self.reps_var)
        reps_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Button
        add_button = ttk.Button(self.root, text="Add Workout", command=self.add_workout)
        add_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Workout History Listbox
        history_label = ttk.Label(self.root, text="Workout History:")
        history_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.history_listbox = tk.Listbox(self.root, height=10, width=40)
        self.history_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_workout(self):
        exercise = self.exercise_var.get()
        sets = self.sets_var.get()
        reps = self.reps_var.get()

        if exercise and sets and reps:
            workout_entry = f"{exercise} - Sets: {sets}, Reps: {reps}"
            self.workout_history.append(workout_entry)
            self.update_history_listbox()

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for workout in self.workout_history:
            self.history_listbox.insert(tk.END, workout)


if __name__ == "__main__":
    root = tk.Tk()
    # bgimg = tk.PhotoImage(file="/home/dragos/FlexiFit/background.png")
    #    bgimg = tk.PhotoImage(file='background.jpg')
    # background_label = tk.Label(root, image=bgimg)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # background_label.pack()
    main_window = Main(root)
    center_window(400, 300, root)
    # login = LoginClass(root, lambda: start_gym_app(root))
    root.mainloop()
