import tkinter as tk
from time import strftime

w = tk.Tk()
w.title("Relogio")

def relogio():
	hora = strftime("%H: %M: %S")
	label.config(text=hora)
	label.after(1000, relogio)

label = tk.Label(w,font=('Helvetica', 48), background='black', foreground='cyan')

label.pack(anchor='center')
relogio()
w.mainloop()