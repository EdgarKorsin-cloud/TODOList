import tkinter as tk
from textwrap import fill

main_window = tk.Tk()
main_window.title("TODO List")
#main_window.geometry("500x500")
# Ask user  to enter a task->str
#provide input space
#provide common suggestions
#provide space to input start and due date, these fields are optional
#ask for task owner and task owner's email, owner name is required but email es optional(recommend if due date field is populated)
task_label = tk.Label(main_window, text="You can enter your task here: ",pady=10, padx=10)
task_label.grid(row=0, column=0)
task_entry = tk.Entry(main_window)
task_entry.grid(row=0, column=1)
star_date_label = tk.Label(main_window, text="Star Date(MM/DD/YYYY): ", pady=10, padx=10)
star_date_label.grid(row=0, column=2)
star_date_entry = tk.Entry(main_window)
star_date_entry.grid(row=0, column=3)
due_date_label = tk.Label(main_window, text="Due Date(MM/DD/YYYY): ", pady=10, padx=10)
due_date_label.grid(row=1, column=2)
due_date_entry = tk.Entry(main_window)
due_date_entry.grid(row=1, column=3)
owner_label = tk.Label(main_window, text="Owner(s): ", pady=10, padx=10)
owner_label.grid(row=2, column=0)
owner_entry = tk.Entry(main_window)
owner_entry.grid(row=2, column=1)
owner_email_label = tk.Label(main_window, text="Owner's Email(s): ", pady=10, padx=10)
owner_email_label.grid(row=2, column=2)
owner_email_entry = tk.Entry(main_window)
owner_email_entry.grid(row=2, column=3)
suggestions_label = tk.Label(text="Need an idea? Here are some suggestions:", pady=10, padx=10)
suggestions_label.grid(row=0, column=4)


main_window.mainloop()