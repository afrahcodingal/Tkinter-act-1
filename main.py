import tkinter as tk
root=tk.Tk()
root.title("My first Tkinter project")
label=tk.Label(root,text="Hello World")
label.pack()
def my_function():
    print("Hello World")
button=tk.Button(root,text="Click Me",command="my_function")
button.pack()
root.mainloop()