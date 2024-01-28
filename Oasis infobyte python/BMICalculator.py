import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import json
import os

class BMIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        self.label_weight = tk.Label(master, text="Enter your weight (kg):")
        self.label_height = tk.Label(master, text="Enter your height (m):")
        self.entry_weight = tk.Entry(master)
        self.entry_height = tk.Entry(master)
        self.button_calculate = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.result_label = tk.Label(master, text="")
        
        self.label_weight.pack()
        self.entry_weight.pack()
        self.label_height.pack()
        self.entry_height.pack()
        self.button_calculate.pack()
        self.result_label.pack()

        # Load and display historical data
        self.load_data()

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Invalid input. Weight and height must be positive values.")
            return

        bmi = weight / (height ** 2)
        category = self.classify_bmi(bmi)

        self.result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

        # Save data
        self.save_data(weight, height, bmi)

        # Update and display historical data
        self.load_data()

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def save_data(self, weight, height, bmi):
        data = {"weight": weight, "height": height, "bmi": bmi}
        filename = "bmi_data.json"

        if not os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump([data], file)
        else:
            with open(filename, "r") as file:
                existing_data = json.load(file)
            
            existing_data.append(data)

            with open(filename, "w") as file:
                json.dump(existing_data, file)

    def load_data(self):
        filename = "bmi_data.json"

        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)

            if data:
                # Display historical data
                print("\nHistorical BMI Data:")
                for entry in data:
                    print(f"Weight: {entry['weight']} kg, Height: {entry['height']} m, BMI: {entry['bmi']:.2f}")
                
                # Visualize historical data
                weights = [entry['weight'] for entry in data]
                heights = [entry['height'] for entry in data]
                bmis = [entry['bmi'] for entry in data]

                plt.figure(figsize=(8, 4))
                plt.subplot(1, 2, 1)
                plt.scatter(weights, bmis)
                plt.title("Weight vs BMI")
                plt.xlabel("Weight (kg)")
                plt.ylabel("BMI")

                plt.subplot(1, 2, 2)
                plt.scatter(heights, bmis)
                plt.title("Height vs BMI")
                plt.xlabel("Height (m)")
                plt.ylabel("BMI")

                plt.tight_layout()
                plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
