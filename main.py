import tkinter as tk
from tkinter import PhotoImage

print("input the location to the picture")
picinput = input()

main = tk.Tk()
main.title("snakepic")

img = PhotoImage(file=picinput)
label = tk.Label(main, image=img)
label.pack()
main.mainloop()
