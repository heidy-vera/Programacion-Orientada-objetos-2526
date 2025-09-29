import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.pack(pady=10)
        self.entry_task.bind("<Return>", self.add_task)  # Añadir con Enter

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)

        self.btn_add = tk.Button(frame_buttons, text="Añadir Tarea", command=self.add_task)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", command=self.complete_task)
        self.btn_complete.grid(row=0, column=1, padx=5)

        self.btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        self.btn_delete.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox_tasks = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox_tasks.pack(pady=10)

        # Doble clic para marcar como completada
        self.listbox_tasks.bind("<Double-Button-1>", self.complete_task)

    def add_task(self, event=None):
        task = self.entry_task.get().strip()
        if task:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        try:
            index = self.listbox_tasks.curselection()[0]
            task = self.listbox_tasks.get(index)

            # Verificar si ya está completada
            if task.startswith("[✔] "):
                messagebox.showinfo("Información", "La tarea ya está marcada como completada.")
            else:
                self.listbox_tasks.delete(index)
                self.listbox_tasks.insert(index, "[✔] " + task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        try:
            index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
