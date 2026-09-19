import tkinter as tk
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tkinter import messagebox

#save entry,dates and owner's info
#Create and save to DB
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
#func to save to db
def adding_task(task,start,due,owner,email):
    try:
        start_date_obj = datetime.strptime(start,"%m/%d/%Y")
        due_date_obj = datetime.strptime(due,"%m/%d/%Y")
    except:
        messagebox.showerror("Error", "Please use the correct date format: YYYY-MM-DD")
        return

    Session = sessionmaker(bind=engine)
    session = Session()
    new_task = Task(task_description=task,
                    task_start=start_date_obj,
                    task_end=due_date_obj,
                    owner_name=owner,
                    owner_email=email)
    session.add(new_task)
    session.commit()

    task_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    owner_entry.delete(0, tk.END)
    owner_email_entry.delete(0, tk.END)
    messagebox.showinfo(f"Task added to list. Remember its due {due}")
    session.close()

#func to populate task list from db
def populating_task_list():
    Session = sessionmaker(bind=engine)
    session = Session()
    all_tasks = session.query(Task).all()
    for index,task in enumerate(all_tasks):
        task_frame = tk.Frame(todo_frame)
        task_frame.grid(row=index,column=0,sticky="ew", pady=2)
        task_frame.columnconfigure(0, weight=1)
        task_text = (
            f"ID: {task.id} | {task.task_description}\n"
            f"Schedule: {task.task_start} to {task.task_end}\n"
            f"Owner: {task.owner_name} ({task.owner_email})"
        )
        check_var = tk.BooleanVar()
        chk = tk.Checkbutton(
            task_frame,
            text=task_text,
            variable=check_var,
            justify="left",
            command=lambda tf=task_frame, cv=check_var: toggle_task_location(tf, cv)
        )
        chk.grid(sticky="w")
        divider = tk.Frame(task_frame, height=1, bg="lightgrey")
        divider.grid(row=1, column=0, sticky="ew", pady=5)
    session.close()
#func to move task from to do to done
def toggle_task_location(task_frame, check_var):
    task_frame.grid_forget()

    if check_var.get():
        next_row = todo_frame.grid_info()[1]
        task_frame.grid(in_=done_frame,row=next_row,column=0,sticky="ew",pady=2)
    else:
        next_row = todo_frame.grid_size()[1]
        task_frame.grid(in_=todo_frame,row=next_row, column=0, sticky="ew",pady=2)

todo_frame = tk.LabelFrame(main_window, text="To Do", padx=10, pady=10)
todo_frame.grid(row=7,column=0,fill="both", expand=True, padx=10, pady=5)

done_frame = tk.LabelFrame(main_window, text="Done", padx=10, pady=10)
done_frame.grid(row=7,column=2,fill="both", expand=True, padx=10, pady=5)

# Ask user  to enter a task->str
#provide input space
#provide common suggestions
#provide space to input start and due date, these fields are optional
#ask for task owner and task owner's email, owner name is required but email is optional(recommend if due date field is populated)
task_label = tk.Label(main_window, text="You can enter your task here: ",pady=10, padx=10)
task_label.grid(row=0, column=0)
task_entry = tk.Entry(main_window, width=40)
task_entry.grid(row=0, column=1,columnspan=2)
start_date_label = tk.Label(main_window, text="Star Date(MM/DD/YYYY): ", pady=10, padx=10)
start_date_label.grid(row=0, column=3)
start_date_entry = tk.Entry(main_window)
start_date_entry.grid(row=0, column=4)
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
suggestion_1_button = tk.Button(text="Exercise for 15 minutes",padx=10,pady=10,
                                command=lambda: adding_suggestion(button_1_text), width=20)
button_1_text = suggestion_1_button.cget("text")
suggestion_1_button.grid(row=1, column=5)
suggestion_2_button = tk.Button(text="Clean the bathroom(s)",padx=10,pady=10,
                                command=lambda: adding_suggestion(button_2_text), width=20)
button_2_text = suggestion_2_button.cget("text")
suggestion_2_button.grid(row=2, column=5)
suggestion_3_button = tk.Button(text="Clean the kitchen",padx=10,pady=10,
                                command=lambda: adding_suggestion(button_3_text), width=20)
button_3_text = suggestion_3_button.cget("text")
suggestion_3_button.grid(row=3, column=5)
suggestion_4_button = tk.Button(text="Clean the bedroom",padx=10,pady=10,
                                command=lambda: adding_suggestion(button_4_text), width=20)
button_4_text = suggestion_4_button.cget("text")
suggestion_4_button.grid(row=4, column=5)
suggestion_5_button = tk.Button(text="Finish \"the book\" ",padx=10,pady=10,
                                command=lambda: adding_suggestion(button_5_text), width=20)
button_5_text = suggestion_5_button.cget("text")
suggestion_5_button.grid(row=5, column=5)

add_task_button = tk.Button(text="Create task",
                            padx=10,pady=10, command=lambda:adding_task(task=task_entry.get(),
                                                                        start=start_date_entry.get(),
                                                                        due=due_date_entry.get(),
                                                                        owner=owner_entry.get(),
                                                                        email=owner_email_entry.get()))
add_task_button.grid(row=3, column=2)

#print list of tasks, show description, start, due, owner, owner's email
tasks_data_string = populating_task_list()
list_label = tk.Label(main_window, text="TASK LIST: ",pady=10, padx=10)
list_label.grid(row=6, column=2,columnspan=2)
# tasks_list = tk.Label(main_window, width=60,text=tasks_data_string, justify=tk.LEFT,pady=10, padx=10,anchor="nw")
# tasks_list.grid(row=7, column=0,columnspan=3)


main_window.mainloop()