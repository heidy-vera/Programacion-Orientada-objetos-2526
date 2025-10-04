import tkinter as tk
from tkinter import messagebox, simpledialog

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("400x400")
        self.root.configure(bg="#F0F0F0")

        self.entry_tarea = tk.Entry(root, width=40, font=("Arial", 11))
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.focus()

        frame_botones = tk.Frame(root, bg="#F0F0F0")
        frame_botones.pack()

        self.btn_agregar = tk.Button(frame_botones, text=" Agregar", width=12, command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.btn_completar = tk.Button(frame_botones, text="Completar", width=12, command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=1, padx=5, pady=5)

        self.btn_eliminar = tk.Button(frame_botones, text="🗑 Eliminar", width=12, command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

        self.lista_tareas = tk.Listbox(root, selectmode=tk.SINGLE, width=45, height=15, font=("Arial", 11))
        self.lista_tareas.pack(pady=10)

        # ---- Atajos de teclado ----
        self.root.bind("<Return>", lambda event: self.agregar_tarea())       # Enter para agregar
        self.root.bind("<c>", lambda event: self.marcar_completada())        # C para completar
        self.root.bind("<C>", lambda event: self.marcar_completada())        # Mayúscula C también
        self.root.bind("<d>", lambda event: self.eliminar_tarea())           # D para eliminar
        self.root.bind("<D>", lambda event: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())      # Tecla Supr
        self.root.bind("<Escape>", lambda event: self.cerrar_aplicacion())   # Escape para salir

        self.tareas = []

    def agregar_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea == "":
            messagebox.showwarning("Atención", "Por favor, escribe una tarea antes de agregarla.")
            return
        self.tareas.append({"texto": tarea, "completada": False})
        self.actualizar_lista()
        self.entry_tarea.delete(0, tk.END)

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "Selecciona una tarea para marcarla como completada.")
            return
        indice = seleccion[0]
        self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
        self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminarla.")
            return
        indice = seleccion[0]
        del self.tareas[indice]
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                self.lista_tareas.insert(tk.END, f"✔ {texto}")
                self.lista_tareas.itemconfig(tk.END, fg="gray", selectbackground="#A0A0A0")
            else:
                self.lista_tareas.insert(tk.END, f"• {texto}")
                self.lista_tareas.itemconfig(tk.END, fg="black", selectbackground="#C0E8FF")

    def cerrar_aplicacion(self):
        if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()


# ---- Ejecución principal ----
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
