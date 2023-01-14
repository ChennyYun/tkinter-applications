from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from numpy import genfromtxt


root = Tk()
root.geometry("800x600")
root.resizable(width=0, height=0)
root.title("CSV Converter")

a_var = StringVar()
b_var = StringVar()
result_var = StringVar()

e2 = Entry(root, textvar=a_var, justify=LEFT, font=("Calibri",11))
e2.place(x=170, y=40, height=30, width=500)


def select_file():
    e2.delete(0, END) 
    filetypes = (
    ('text files', "*.csv"),
    ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir='/',
        filetypes = filetypes
    )
    e2.insert(END, filename)

def opencsv():
    filename = a_var.get()
    my_data = genfromtxt(filename, delimiter=',', skip_header=1)

    lc = Label(root, text=my_data, wraplength=400,
               justify=LEFT, font=('Calibri', 15))
    lc.place(x=180, y=85, width=400, height=30)

def plot():
    filename = a_var.get() 
    fig = Figure(figsize = (4,4), dpi = 100)
   # y = [i**2 for i in range(101)] #incorporate csv into this line, inside y
    y =genfromtxt(filename, delimiter=',', skip_header=1) 
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
   
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(x=180, y=140)  
   
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
   

open_button = Button(root, text='Open a CSV File', command=select_file ) 

open_button.place(x=40, y=40, height=30, width=120)


btnadd = Button(root,  text='Import CSV', command=opencsv )
btnadd.place(x=40, y=80, height=30, width = 120)

plot_button = Button(root, text= 'plot', command = plot)
plot_button.place(x=40, y=240, height=30, width = 120)


root.mainloop()

