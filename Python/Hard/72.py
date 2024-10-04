import tkinter as tk

def on_click():
    try:
        label['text'] = entry.get()
    except Exception as e:
        label['text'] = f"Error: {e}"

root = tk.Tk()
label = tk.Label(root, text="Enter something:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=on_click)
button.pack()

label.pack()  

root.geometry("300x200")
root.mainloop()
