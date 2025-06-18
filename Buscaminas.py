import tkinter as tk
from tkinter import messagebox
import random

class BuscaMinas:
    def __init__(self, master, filas=8, columnas=8, minas=6):
        self.master = master
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.botones = {}
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.revelado = [[False for _ in range(columnas)] for _ in range(filas)]
        self.colocar_minas()
        self.contar_minas()
        self.crear_widgets()

    def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            f = random.randint(0, self.filas - 1)
            c = random.randint(0, self.columnas - 1)
            if self.tablero[f][c] != -1:
                self.tablero[f][c] = -1
                minas_colocadas += 1

    def contar_minas(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.tablero[f][c] == -1:
                    continue
                minas_cerca = 0
                for i in range(max(0, f-1), min(self.filas, f+2)):
                    for j in range(max(0, c-1), min(self.columnas, c+2)):
                        if self.tablero[i][j] == -1:
                            minas_cerca += 1
                self.tablero[f][c] = minas_cerca

    def crear_widgets(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                b = tk.Button(self.master, width=3, height=1,
                              command=lambda f=f, c=c: self.revelar(f, c))
                b.bind("<Button-3>", lambda e, f=f, c=c: self.marcar(f, c))
                b.grid(row=f, column=c)
                self.botones[(f, c)] = b

    def revelar(self, f, c):
        if self.revelado[f][c]:
            return
        self.revelado[f][c] = True
        self.botones[(f, c)]['relief'] = tk.SUNKEN
        if self.tablero[f][c] == -1:
            self.botones[(f, c)]['text'] = '💣'
            self.game_over(False)
        elif self.tablero[f][c] == 0:
            self.botones[(f, c)]['text'] = ''
            for i in range(max(0, f-1), min(self.filas, f+2)):
                for j in range(max(0, c-1), min(self.columnas, c+2)):
                    if not self.revelado[i][j]:
                        self.revelar(i, j)
        else:
            self.botones[(f, c)]['text'] = str(self.tablero[f][c])
        self.botones[(f, c)]['state'] = tk.DISABLED
        if self.comprobar_victoria():
            self.game_over(True)

    def marcar(self, f, c):
        b = self.botones[(f, c)]
        if not self.revelado[f][c]:
            if b['text'] == '🚩':
                b['text'] = ''
            else:
                b['text'] = '🚩'

    def comprobar_victoria(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.tablero[f][c] != -1 and not self.revelado[f][c]:
                    return False
        return True

    def game_over(self, victoria):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.tablero[f][c] == -1:
                    self.botones[(f, c)]['text'] = '💣'
                self.botones[(f, c)]['state'] = tk.DISABLED
        if victoria:
            messagebox.showinfo("Victoria", "Has ganado")
        else:
            messagebox.showerror("Perdiste", "Has pisado una mina")

def main():
    root = tk.Tk()
    root.title("Busca Minas")
    BuscaMinas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
