import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("TO DO TASK")
root.geometry('400x650+100+100')
root.resizable(False,False)

task_list=[]

def openTaskFile():
    global task_list
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                if task.strip():
                    task_list.append(task.strip())
                    listbox.insert(END, task.strip())
    except FileNotFoundError:
        open("tasklist.txt", "w").close()

def addTask():
    task = task_entry.get()
    if task != "":
        if task not in task_list:
            task_list.append(task)
            listbox.insert(END, task)
            task_entry.delete(0, END)  # Clear the entry widget
            saveTasks()
        else:
            messagebox.showwarning("Duplicate Task", "Task already exists.")
    else:
        messagebox.showwarning("Empty Task", "The task cannot be empty.")

def deleteTask():
    try:
        selected_task = listbox.curselection()[0]
        task_text = listbox.get(selected_task)
        if messagebox.askyesno("Delete Task", "Do you want to delete this task?"):
            listbox.delete(selected_task)
            task_list.remove(task_text)
            saveTasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def saveTasks():
    with open("tasklist.txt", "w") as taskfile:
        for task in task_list:
            taskfile.write(f"{task}\n")


# icon
Image_icon=PhotoImage(file="img/task.png")
root.iconphoto(False,Image_icon)

# top bar
TopImage=PhotoImage(file="img/topbar.png")
Label(root,image=TopImage).pack()

# dockImage=PhotoImage(file="img/dock.png")
# Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

# noteImage=PhotoImage(file="img/task.png")
# Label(root,image=noteImage,bg="#32405b").place(x=340,y=25)


headling=Label(root,text='ALL TASK',font="arial 20 bold",fg='black',bg='#168DE5')
headling.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=2)
task_entry.place(x=10,y=7)

button=Button(frame,text="ADD",font="arial 20 bold", width=6,bg='#168DE5',fg="black",bd=2,command=addTask)
button.place(x=300,y=0)

# lastbox
frame= Frame(root,bd=3,width=700,height=280,bg="black")
frame.pack(pady=(160,0))

listbox = Listbox(frame, font=('arial', 12), width=40, height=16, bg='#168DE5',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame)
scrollbar.pack(side= RIGHT,fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


# delete
Delete_icon=PhotoImage(file="img/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

openTaskFile()

root.mainloop()