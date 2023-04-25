import tkinter as tk



# Initialisation of Tkinter Object
root = tk.Tk()


# set the tile and window size
root.title("Slinky Blinky")
root.geometry("600x600")


screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = screen_w/2 - 600/2
y = screen_h/2 - 600/2

# Setting the window position
root.geometry("+" + str(int(x)) + "+" + str(int(y)))


def clear_widgets(f):
    """select all frame widgets and delete them"""
    for widget in f.winfo_children():
        widget.destroy()






# initialisation of the frames
f1 = tk.Frame(root, width=600, height=600, bg='#B8E8FC')
f2 = tk.Frame(root, width=600, height=600, bg= 'green')

# place frame widgets in window
for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky="nesw")

# load first frame
# load_frame1()

root.mainloop()