from tkinter import * 

# functions
from binary_decimal import BinDec
from decimal_binary import DecBin

def calculate_bin_dec():
    bin = int(textbox1.get())
    dec = BinDec(bin)
    return final.set(dec)


def calculate_dec_bin():
    dec = int(textbox2.get())
    bin = DecBin(dec)
    return final_2.set(bin)

# GUI
root = Tk()
root.title('Binary-Decimal Conversor')

final = StringVar()

final_2 = StringVar()

# widgets
label1 = Label(root, text = 'Binary to Decimal:')
textbox1 = Entry(root)
button1 = Button(root, text = 'Calculate', command = calculate_bin_dec)
label_result = Label(root, textvariable = final)

label2 = Label(root, text = 'Decimal to Binary:')
textbox2 = Entry(root)
button2 = Button(root, text = 'Calculate', command = calculate_dec_bin)
label_result2 = Label(root, textvariable = final_2)



# layout

root.geometry('200x250+300+300')

root.iconbitmap('images\icon1.ico')

label1.grid()
textbox1.grid()
button1.grid()
label_result.grid()

label2.grid()
textbox2.grid()
button2.grid()
label_result2.grid()

root.mainloop()