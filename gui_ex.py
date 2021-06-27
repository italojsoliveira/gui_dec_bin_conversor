from tkinter import *

home = Tk()
home.title('GUI TEST')

home.geometry('500x250+300+300') # size and position

home.resizable(True, True) # Width and height, 1 or 0 also works

#home.minsize(width = 500, height = 250)
#home.maxsize(700, 400) # Note that width and height are optional

home.state("zoomed") # app starts maximized

# home.state("iconic") # app starts minimized

home.iconbitmap('images\icon1.ico')

home['bg'] = 'blue' # background color

btn = Button(home, text = 'Execute')
btn.pack()

home.mainloop()