import tkinter as tk

## test
# tk._test()

def label_change() -> None:
    label.config(text="Button clicked")

root = tk.Tk()
root.title("Hello")

label = tk.Label(root, 
                 text="Im nothing"
                 )
label.grid(row=1, column=1)
# print(label.config().keys())

button = tk.Button(root, 
                   text="click me", 
                   command=label_change
                   )
button.grid(row=0, column=0)

root.mainloop()