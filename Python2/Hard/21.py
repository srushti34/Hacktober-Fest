import tkinter as tk

def draw_circle(event):
    try:
        
        canvas.create_oval(pos_x - 25, pos_y - 25, pos_x + 25, pos_y + 25, fill="blue")
    except AttributeError as e:
        print(f"AttributeError: {e}")

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


canvas.bind("<Buton-1>", draw_circle)


canvas.bind("<KeyPress>", draw_circle)

root.mainloop()
