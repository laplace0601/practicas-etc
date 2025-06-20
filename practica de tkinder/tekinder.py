import tkinter as tk
ventana = tk.Tk()
ventana.title("mi primera interfaz con esto")
ventana.geometry("300x300")
boton = tk.Button (ventana, text = "hola mundo", command = lambda: print("hola mundo"))
boton.pack(pady=20)
ventana.mainloop()
