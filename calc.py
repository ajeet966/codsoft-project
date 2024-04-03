from tkinter import *
import math

def click(value):
    current = entryField.get()
    if value == 'C':
        entryField.delete(0, END)
    elif value == '=':
        try:
            # Here, you'd need to preprocess the input if it contains a square root operation
            result = str(eval(current))  # Still dangerous to use eval() like this
            entryField.delete(0, END)
            entryField.insert(0, result)
        except:
            entryField.delete(0, END)
            entryField.insert(0, "Error")
    elif value == '√':
        try:
            # Assuming the square root operation applies to the entire current value
            sqrt_result = math.sqrt(float(current))
            entryField.delete(0, END)
            entryField.insert(0, str(sqrt_result))
        except:
            entryField.delete(0, END)
            entryField.insert(0, "Error")
    else:
        entryField.insert(END, value)

root = Tk()
root.title('Calculator')
root.config(bg='dodgerblue3')
root.geometry('372x550+100+100')
root.resizable(False, False)


entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, width=22)
entryField.grid(row=0, column=0, columnspan=4, pady=10)

button_text_list = [
    "C", "%", "√", "÷",
    "1", "2", "3", "*",
    "4", "5", "6", "-",
    "7", "8", "9", "+",
    "00", "0", ".", "="
]

rowvalue = 1
columnvalue = 0

for i in button_text_list:
    button = Button(root, width=5, height=2, bd=1, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 20, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=5)
    columnvalue += 1
    if columnvalue > 3:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
