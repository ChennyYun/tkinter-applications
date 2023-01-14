
from tkinter import *
import math, cmath
from tkinter.messagebox import showinfo 
from PIL import Image
from PIL import ImageTk
  
root = Tk() # frame
root.geometry("400x300+10+10") # dimension of frame
root.title("converter")
la = Label(root, text = "Unit Converter") #label widge = Label
la.place(x =20, y=20)


lb = Label(root, text ="Celsius")
lb.place(x=20,y=50)


lc = Label(root, text ="Farenheit")
lc.place(x=20,y=170)

a = StringVar() #truncate, concatenate, delete, add, clear, diff...
b = StringVar()
c = StringVar()

e1 = Entry(root, textvar=a, justify = RIGHT)
e1.place(x = 20, y = 70, width=60,height = 30)

e2 = Entry(root, textvar=b, justify =RIGHT, state ="readonly")
e2.place(x = 20, y = 200, width = 110, height = 20)

options = ["Temperature", "Length", "Pressure", "Height","Mass"]
c.set("Temparature")


def selected(event):
    if c.get() == "Temperature":
        lb.config(text = "Celcius")
        lc.config(text = "Farenheit")
        b1["command"] = tempconv
    elif c.get() == "Length": 
        lb.config(text = "Meters")
        lc.config(text = "Feet")
        b1["command"] = lengthconv
    elif c.get() == "Pressure":
        lb.config(text = "Pascal")
        lc.config(text = "PSI")
        b1["command"] = pressureconv
    elif c.get() == "Height":
        lb.config(text = "Meters")
        lc.config(text = "Feet & Inches")
        b1["command"] = heightconv
    elif c.get() == "Mass":
        lb.config(text = "Kilograms")
        lc.config(text = "Pounds")
        b1["command"] = massconv

def tempconv():
    try:
        num = float(a.get())
        ans = num*1.8 + 32
        #b.set(str(ans))
        b.set("%5.2f"%(ans)) # alternative: '{: 5.2f}'.format(ans)
    #output formatting. f is float. 5 means integer.
    # 2 is the decimal place
    except:
        b.set("Enter number")
def lengthconv():
    try:
        num = float(a.get())
        ans = num*3.28084
        b.set("%5.2f"%(ans))
    except:
         b.set("Enter number")
def pressureconv():
    try:
        num = float(a.get())
        ans = num/6895
        b.set("%5.2f"%(ans))
    except:
         b.set("Enter number")
def heightconv():
    try:
        num = float(a.get())
        ans = num*3.28084
        decimal = ans % 1
        decimal *= 12
        ans = int(ans)
        b.set("%5d and %5.2f" %(ans,decimal))
    except:
         b.set("Enter number")
         
def massconv():
    try:
        num = float(a.get())
        ans = num*2.2046
        b.set("%5.2f"%(ans))
    except:
        b.set("Enter number")
        
b1 = Button(root, text = "Convert", command =tempconv)
b1.place(x=20,y=130, width =80, height = 20)
dropdown = OptionMenu(root,c,*options, command = selected)
dropdown.place(x = 200, y= 20)

def selectFrame( option, prev = root):
    
    if option == "quad":
        prev.destroy()
        quadFrame = Tk()
        quadFrame.geometry("400x300+12+12")
        quadFrame.title("")
        
        avar = StringVar()
        bvar = StringVar()
        cvar = StringVar()
        rvar = StringVar()
        rv2r = StringVar()
        
        # ax**2+b*x+c = 0
        
        def quad():
            try:
                a = float(avar.get())
                b = float(bvar.get())
                c = float(cvar.get())
                indi = (b)**2 - (4*a)*(c)
                if indi > 0:
                        ans1 = (-1*b + math.sqrt(indi))/(2*a)
                        ans2 = (-1*b - math.sqrt(indi))/(2*a)
                        rvar.set('%5.2f' %(ans1))
                        rv2r.set('%5.2f'%(ans2))
                elif indi == 0:
                        ans1 = (-1*b)/(2*a)
                        rvar.set('%5.2f' %(ans1))
                else:
                        ans1 = (-1*b + cmath.sqrt(indi))/(2*a)
                        ans2 = (-1*b - cmath.sqrt(indi))/(2*a)
                        rvar.set('%5.2f + %5.2fi' %(ans1.real, ans1.imag))
                        rv2r.set('%5.2f + %5.2fi' %(ans1.real, ans1.imag))
            
            except:
                #rvar.set('more input needed')
                showinfo(
                   title = 'Input Alert',
                   message="Please provide inputs or type numbers" 
                   )
        
        la = Label(quadFrame, text='A')
        la.place(x=40, y=50)
        
        e1 = Entry(quadFrame, textvar=avar, justify=RIGHT)
        e1.place(x=40, y=20, height=30, width=50)
        
        lb = Label(quadFrame, text='B')
        lb.place(x=90, y=50)
        
        e2 = Entry(quadFrame, textvar=bvar, justify=RIGHT)
        e2.place(x=90, y=20, height=30, width=50)
        
        lc = Label(quadFrame, text='C')
        lc.place(x=140, y=50)
        
        e3 = Entry(quadFrame, textvar=cvar, justify=RIGHT)
        e3.place(x=140, y=20, height=30, width=50)
        
        btnadd = Button(quadFrame, text='find solution(s)', command=quad)
        btnadd.place(x=90, y=90, height=30, width=100)
        
        ladd = Label(quadFrame, text='the solution(s): ')
        ladd.place(x=90, y=170)
        
        e3 = Entry(quadFrame, textvar=rvar, justify=RIGHT, state="readonly")
        e3.place(x=40, y=130, height=30, width=300)
        
        e4 = Entry(quadFrame, textvar=rv2r, justify=RIGHT, state="readonly")
        e4.place(x=40, y=170, height=30, width=300)
        
        b2 = Button(quadFrame,text = "Temperature Converter", command = lambda: selectFrame("temp",quadFrame))
        b2.place(x = 140, y = 240)
    
        b3 = Button(quadFrame,text = "Distance Calculator", command = lambda: selectFrame("distance",quadFrame))
        b3.place(x = 280, y = 240)
        quadFrame.mainloop()
        
    elif option == "distance":
        prev.destroy()
        dist = Tk()
        dist.geometry("400x300+12+12")
        dist.title("")
        
        x1 = StringVar()
        x2 = StringVar()
        y1 = StringVar()
        y2 = StringVar()
        ans = StringVar()
        def dis():
            try:
                a = float(x1.get())
                b = float(y1.get())
                c = float(x2.get())
                d = float(y2.get())
                anf = (((a-c)**2)+((b-d)**2))**0.5
                ans.set("%5.2f" %(anf))
            except:
                ans.set('more input needed')
        
        la = Label(dist, text='x1')
        la.place(x=40, y=50)
        
        e1 = Entry(dist, textvar=x1, justify=RIGHT)
        e1.place(x=40, y=20, height=30, width=50)
        
        lb = Label(dist, text='y1')
        lb.place(x=90, y=50)
        
        e2 = Entry(dist, textvar=y1, justify=RIGHT)
        e2.place(x=90, y=20, height=30, width=50)
        
        lc = Label(dist, text='x2')
        lc.place(x=140, y=50)
        
        e3 = Entry(dist, textvar=x2, justify=RIGHT)
        e3.place(x=140, y=20, height=30, width=50)
        
        ld = Label(dist, text='y2')
        ld.place(x=190, y=50)
        
        e4 = Entry(dist, textvar=y2, justify=RIGHT)
        e4.place(x=190, y=20, height=30, width=50)
        
        btnadd = Button(dist, text='find distance', command=dis)
        btnadd.place(x=90, y=90, height=30, width=100)
        
        ladd = Label(dist, text='the distance: ')
        ladd.place(x=90, y=170)
        
        e5 = Entry(dist, textvar=ans, justify=RIGHT, state="readonly")
        e5.place(x=40, y=130, height=30, width=150)
        
        b2 = Button(dist,text = "Quadratic Solver", command = lambda: selectFrame("quad",dist))
        b2.place(x = 160, y = 240)
    
        b3 = Button(dist,text = "Temperature Converter", command = lambda: selectFrame("temp",dist))
        b3.place(x = 260, y = 240)
        dist.mainloop()
    
    elif option == "temp":
        prev.destroy()
        root = Tk() # frame
        root.geometry("400x300+10+10") # dimension of frame
        root.title("converter")
        la = Label(root, text = "Unit Converter") #label widge = Label
        la.place(x =20, y=20)
        
        
        lb = Label(root, text ="Celsius")
        lb.place(x=20,y=50)
        
        
        lc = Label(root, text ="Farenheit")
        lc.place(x=20,y=170)
        
        a = StringVar() #truncate, concatenate, delete, add, clear, diff...
        b = StringVar()
        c = StringVar()
        
        e1 = Entry(root, textvar=a, justify = RIGHT)
        e1.place(x = 20, y = 70, width=60,height = 30)
        
        e2 = Entry(root, textvar=b, justify =RIGHT, state ="readonly")
        e2.place(x = 20, y = 200, width = 110, height = 20)
        
        options = ["Temperature", "Length", "Pressure", "Height","Mass"]
        c.set("Temparature")
        
        
        def selected(event):
            if c.get() == "Temperature":
                lb.config(text = "Celcius")
                lc.config(text = "Farenheit")
                b1["command"] == tempconv
            elif c.get() == "Length": 
                lb.config(text = "Meters")
                lc.config(text = "Feet")
                b1["command"] = lengthconv
            elif c.get() == "Pressure":
                lb.config(text = "Pascal")
                lc.config(text = "PSI")
                b1["command"] = pressureconv
            elif c.get() == "Height":
                lb.config(text = "Meters")
                lc.config(text = "Feet & Inches")
                b1["command"] = heightconv
            elif c.get() == "Mass":
                lb.config(text = "Kilograms")
                lc.config(text = "Pounds")
                b1["command"] = massconv
        
        def tempconv():
            try:
                num = float(a.get())
                ans = num*1.8 + 32
                b.set("%5.2f"%(ans)) # alternative: '{: 5.2f}'.format(ans)
            #output formatting. f is float. 5 means integer.
            # 2 is the decimal place
            except:
                b.set("Enter number")
        def lengthconv():
            try:
                num = float(a.get())
                ans = num*3.28084
                b.set("%5.2f"%(ans))
            except:
                 b.set("Enter number")
        def pressureconv():
            try:
                num = float(a.get())
                ans = num/6895
                b.set("%5.2f"%(ans))
            except:
                 b.set("Enter number")
        def heightconv():
            try:
                num = float(a.get())
                ans = num*3.28084
                decimal = ans % 1
                decimal *= 12
                ans = int(ans)
                b.set("%5d and %5.2f" %(ans,decimal))
            except:
                 b.set("Enter number")
        b1 = Button(root, text = "Convert", command =tempconv)
        b1.place(x=20,y=130, width =80, height = 20)
        
        b2 = Button(root,text = "Quadratic Solver", command = lambda: selectFrame("quad",root))
        b2.place(x = 180, y = 240)

        b3 = Button(root,text = "Distance Calculator", command = lambda: selectFrame("distance",root))
        b3.place(x = 280, y = 240)
        dropdown = OptionMenu(root,c,*options, command = selected)
        dropdown.place(x = 200, y= 20)
        root.mainloop()
b2 = Button(root,text = "Quadratic Solver", command = lambda: selectFrame("quad"))
b2.place(x = 180, y = 240)

b3 = Button(root,text = "Distance Calculator", command = lambda: selectFrame("distance"))
b3.place(x = 280, y = 240)

root.mainloop()


