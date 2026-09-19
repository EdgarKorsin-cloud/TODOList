import tkinter as tk
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime

#database
SQLite: 'sqlite:///relative_path.db'
engine = create_engine('sqlite:///database.db')

Base = declarative_base()
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task_description = Column(String)
    task_start = Column(DateTime)
    task_end = Column(DateTime)
    owner_name = Column(String)
    owner_email = Column(String)
Base.metadata.create_all(engine)

main_window = tk.Tk()
main_window.title("TODO List")
#functions
#func to add suggestion to task input
def adding_suggestion(button):
    button_text = button
    task_entry.delete(0, tk.END)
    task_entry.insert(0, button_text)
    pass
# Ask user  to enter a task->str
#provide input space
#provide common suggestions
#provide space to input start and due date, these fields are optional
#ask for task owner and task owner's email, owner name is required but email es optional(recommend if due date field is populated)
task_label = tk.Label(main_window, text="You can enter your task here: ",pady=10, padx=10)
task_label.grid(row=0, column=0)
task_entry = tk.Entry(main_window, width=40)
task_entry.grid(row=0, column=1,columnspan=2)
star_date_label = tk.Label(main_window, text="Star Date(MM/DD/YYYY): ", pady=10, padx=10)
star_date_label.grid(row=0, column=3)
star_date_entry = tk.Entry(main_window)
star_date_entry.grid(row=0, column=4)
due_date_label = tk.Label(main_window, text="Due Date(MM/DD/YYYY): ", pady=10, padx=10)
due_date_label.grid(row=1, column=3)
due_date_entry = tk.Entry(main_window)
due_date_entry.grid(row=1, column=4)
owner_label = tk.Label(main_window, text="Owner(s): ", pady=10, padx=10)
owner_label.grid(row=2, column=0)
owner_entry = tk.Entry(main_window,width=40)
owner_entry.grid(row=2, column=1)
owner_entry.grid(row=2, column=1, columnspan=2)
owner_email_label = tk.Label(main_window, text="Owner's Email(s): ", pady=10, padx=10)
owner_email_label.grid(row=2, column=3)
owner_email_entry = tk.Entry(main_window)
owner_email_entry.grid(row=2, column=4)
suggestions_label = tk.Label(text="Need an idea? Here are some suggestions:", pady=10, padx=10)
suggestions_label.grid(row=0, column=5)
suggestion_1_button = tk.Button(text="Exercise for 15 minutes",padx=10,pady=10,command=lambda: adding_suggestion(button_1_text), width=20)
button_1_text = suggestion_1_button.cget("text")
suggestion_1_button.grid(row=1, column=5)
suggestion_2_button = tk.Button(text="Clean the bathroom(s)",padx=10,pady=10,command=lambda: adding_suggestion(button_2_text), width=20)
button_2_text = suggestion_2_button.cget("text")
suggestion_2_button.grid(row=2, column=5)
suggestion_3_button = tk.Button(text="Clean the kitchen",padx=10,pady=10, command=lambda: adding_suggestion(button_3_text), width=20)
button_3_text = suggestion_3_button.cget("text")
suggestion_3_button.grid(row=3, column=5)
suggestion_4_button = tk.Button(text="Clean the bedroom",padx=10,pady=10,command=lambda: adding_suggestion(button_4_text), width=20)
button_4_text = suggestion_4_button.cget("text")
suggestion_4_button.grid(row=4, column=5)
suggestion_5_button = tk.Button(text="Finish \"the book\" ",padx=10,pady=10,command=lambda: adding_suggestion(button_5_text), width=20)
button_5_text = suggestion_5_button.cget("text")
suggestion_5_button.grid(row=5, column=5)

add_task_button = tk.Button(text="Create task", padx=10,pady=10)
add_task_button.grid(row=3, column=2)

main_window.mainloop()