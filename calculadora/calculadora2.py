import tkinter as tk
import funciones  # Asegúrate de que este módulo tiene las funciones correctamente definidas

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Entrada de números
entrada1 = tk.Entry(ventana, width=10, font=("Arial", 18))
entrada1.pack(pady=5)
entrada2 = tk.Entry(ventana, width=10, font=("Arial", 18))
entrada2.pack(pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado: ", font=("Arial", 16))
resultado_label.pack(pady=10)

# Función para realizar cálculos
def calcular(operacion):
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = getattr(funciones, operacion)(num1, num2)  # Llama la función del módulo
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Ingresa números válidos.")

# Botones de operación
for operacion in ["suma", "resta", "multiplicacion", "division"]:
    tk.Button(ventana, text=operacion.capitalize(), command=lambda o=operacion: calcular(o)).pack(pady=5)

# Botón para salir
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
