import tkinter as tk
from tkinter import ttk, messagebox


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x400")

        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        frame_lista = tk.Frame(main_frame)
        frame_lista.pack(side="top", fill="both", expand=True, pady=10)

        self.tree = ttk.Treeview(
            frame_lista,
            columns=("Fecha", "Hora", "Descripción"),
            show="headings",
            height=10
        )
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=400, anchor="w")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        frame_entrada = tk.LabelFrame(main_frame, text="Nuevo Evento", padx=10, pady=10)
        frame_entrada.pack(side="top", fill="x", pady=10)

        # Fecha
        tk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.fecha_entry = tk.Entry(frame_entrada, width=12)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.descripcion_entry = tk.Entry(frame_entrada, width=50)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Botones a utilizar
        frame_botones = tk.Frame(main_frame, pady=10)
        frame_botones.pack(side="bottom", fill="x")

        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento, width=20)
        btn_agregar.pack(side="left", padx=10)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento, width=25)
        btn_eliminar.pack(side="left", padx=10)

        btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit, width=15)
        btn_salir.pack(side="right", padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get().strip()
        hora = self.hora_entry.get().strip()
        descripcion = self.descripcion_entry.get().strip()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # limpiar entradas
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Eliminar", "Seleccione un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            for item in seleccionado:
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
