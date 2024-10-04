import tkinter as tk

def open_file():
    try:
        # Error 1: Incorrect mode "w" (write mode) when trying to read a file
        with open("non_existent.txt", "w") as f:
            data = f.read()
            label['txt'] = data  # Error 2: Incorrect widget attribute 'txt' (should be 'text')
    except FileNotFoundError as e:
        label['text'] = f"FileNotFoundEror: {e}"  # Error 3: Typo in exception name

root = tk.Tk()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

label = tk.Label(root, text="No file opened yet")
label.pack(side=tk.LFT)  # Error 4: Typo in 'side=tk.LFT' (should be 'side=tk.LEFT' or 'side=tk.TOP')

root.geometry("400x300")
root.mainloop()
