import tkinter as tk

root = tk.Tk()
root.title("Tk Example")
root.minsize(200, 200)
root.geometry("300x300+50+50")

# Create two labels
tk.Label(root, text="Login Screen").pack()
tk.Label(root, text="Boot Screen").pack()

# Display an image
image = tk.PhotoImage(file="./gui/load.gif")
tk.Label(root, image=image).pack()

root.mainloop()
