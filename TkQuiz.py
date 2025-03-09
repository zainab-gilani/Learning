import tkinter as tk
from tkinter import messagebox


# Function to check the selected answer
def check_answer():
    selected = answer_var.get()
    if selected == correct_answer:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", "Incorrect! The correct answer is: " + options[correct_answer])

# Create the main window
root = tk.Tk()

root.title("Multiple Choice Question")

# Define the question and options
question = "What is the capital of France?"
options = ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"]
correct_answer = 2  # Index of the correct answer (C) Paris

# Create a label for the question
question_label = tk.Label(root, text=question)
question_label.pack(pady=10)

# Variable to store the selected answer
answer_var = tk.IntVar()

# Create radio buttons for the options
for index, option in enumerate(options):
    radio_button = tk.Radiobutton(root, text=option, variable=answer_var, value=index)
    radio_button.pack(anchor='w')

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
