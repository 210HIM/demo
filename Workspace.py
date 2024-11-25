import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a canvas
# canvas = tk.Canvas(root, width=200, height=100, bg="red")
# canvas.pack()
butt_frame = tk.Frame(root)
butt_frame.place(width=100, height=200, x=0, y=0)
# Load the image (replace 'rounded_button.png' with your image file)
load_image = tk.PhotoImage(file="Images/Admin.png")

# Create the button using the image
rounded_button = tk.Button(butt_frame, image=load_image, borderwidth=0, command=lambda: print("Button clicked!"))
rounded_button.place(x=0, y=0)

root.mainloop()
