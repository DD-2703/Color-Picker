from tkinter import Tk, colorchooser, Frame, ttk
import pyperclip as pc

ask = Tk()
ask.title("ColorPicker")
# ask.iconbitmap("#")
ask.withdraw()

def copy():
	if menu.get() == "RGB":
		pc.copy(colorRGB)
	elif menu.get() == "Hex":
		pc.copy(colorHex)
	else:
		menu.current(0)
	quit()

main = colorchooser.askcolor()

colorRGB = str(main[0]).replace("(", "").replace(")", "")
colorHex = main[1]

ask.deiconify()
ask.geometry("235x200")
ask.iconbitmap("icon.ico")
ask.resizable(False, False)

options = ["RGB", "Hex"]

askFrame = Frame(ask).grid(row=1, column=0)

lbl = ttk.Label(askFrame, text="Copy the ").grid(row=0, column=0, pady=10)
menu = ttk.Combobox(askFrame, value=options)
menu.current(0)
menu.grid(row=0, column=1, pady=10)
lbl2 = ttk.Label(askFrame, text="Code").grid(row=0, column=2, pady=10)

btn = ttk.Button(askFrame, text="Copy", command=copy)
btn.grid(row=1, column=0, columnspan=2, pady=20)

ask.mainloop()