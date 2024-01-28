import tkinter as tk
from tkinter import ttk, messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("400x200")  # Set initial window size

        # Create a style for better widget appearance
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#333')
        self.style.configure('TLabel', background='#333', foreground='#fff', font=('Arial', 12))
        self.style.configure('TEntry', fieldbackground='#444', font=('Arial', 12))
        self.style.configure('TButton', background='#4CAF50', font=('Arial', 12))

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill='both')

        self.location_label = ttk.Label(self.frame, text="Enter location:")
        self.location_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.location_entry = ttk.Entry(self.frame)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        self.get_weather_button = ttk.Button(self.frame, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

    def get_weather(self):
        location = self.location_entry.get()
        # Call the function to get weather data (similar to the basic app)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
