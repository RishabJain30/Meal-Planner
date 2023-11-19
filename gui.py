import tkinter as tk
from tkinter import ttk
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import a9trial_1
import b10trial_2
import c11trial_3
import d12trial_4

def suggest(has_diabetes):

    results_1,int1 = a9trial_1.run_recommendations(5,has_diabetes)
    results_2,int2 = b10trial_2.run_recommendations(5,has_diabetes)
    results_3,int3 = c11trial_3.run_recommendations(5,has_diabetes)
    results_4,int4 = d12trial_4.run_recommendations(5,has_diabetes)

    int_result_mapping = {
    int1: results_1,
    int2: results_2,
    int3: results_3,
    int4: results_4
    }

    # Find the largest integer
    max_int = max(int1, int2, int3, int4)

    print(max_int)
    
    return int_result_mapping[max_int]

choice = ['yes','no']
def button_click():
    has_diabetes = ans.get()
    answer = suggest(has_diabetes)
    print("Suggested recipe: ", end=" ")
    for i in range(5):  # Assuming you want to display the first 5 recipes
        recipe_label.config(text="{}".format(answer[i]['Recommended Recipe']))
    all_recipes_text = "\n".join(answer[i]['Recommended Recipe'] for i in range(5))
    recipe_label.config(text=all_recipes_text)

root = tk.Tk()
root.title("recipe suggestor")
root.geometry("1200x800")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

ans = tk.StringVar(value=choice[0])

has_diabetes_label = ttk.Label(root, text="Do you have Diabetes:", background="#f2f2f2", foreground="#000000", font=("Helvetica", 12))
has_diabetes_label.place(relx=0.3, rely=0.2, anchor="center")

has_diabetes_dropdown = ttk.Combobox(root, textvariable=ans, values=choice)
has_diabetes_dropdown.place(relx=0.7, rely=0.2, anchor="center")

button = ttk.Button(root, text="Suggest", command=button_click)
button.place(relx=0.5, rely=0.6, anchor="center")

recipe_label = ttk.Label(root, text=" ", background="#f2f2f2", foreground="#000000", font=("Helvetica", 16))
recipe_label.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
