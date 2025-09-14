import tkinter as tk
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar_dato():
    dato = entrada.get()
    if dato.strip() != "":
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_datos():
    seleccion = lista.curselection()
    if seleccion:
        for i in seleccion[::-1]:
            lista.delete(i)
    else:
        lista.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos con GUI - Tkinter")
ventana.geometry("400x300")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón Agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Botón Limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
