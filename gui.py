import tkinter as tk
from tkinter import ttk, messagebox
from logic import system_logic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AppGUI:
    def __init__(self):
        self.sistema = system_logic()
        self.window = tk.Tk()
        self.window.title('Sistema de Gestión Deportiva')
        self.setup_gui()

    def setup_gui(self):
        # Marco principal
        self.main_frame = ttk.Frame(self.window, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Botones principales
        ttk.Button(
            self.main_frame,
            text="Registrar Participante",
            command=self.show_registry
        ).pack(pady=5, fill=tk.X)

        ttk.Button(
            self.main_frame,
            text="Reporte General",
            command=self.show_general_report
        ).pack(pady=5, fill=tk.X)

        ttk.Button(
            self.main_frame,
            text="Reporte Individual",
            command=self.show_search
        ).pack(pady=5, fill=tk.X)

    def show_registry(self):
        """Ventana de registro de participantes"""
        registro_window = tk.Toplevel(self.window)
        registro_window.title("Registro")

        # Campos de entrada
        ttk.Label(registro_window, text="Nombre:").pack(pady=5)
        nombre_entry = ttk.Entry(registro_window)
        nombre_entry.pack(pady=5)

        ttk.Label(registro_window, text="Puntajes (0-100)").pack(pady=5)

        pruebas = ['Resistencia', 'Fuerza', 'Velocidad']
        entries = []
        for prueba in pruebas:
            frame = ttk.Frame(registro_window)
            frame.pack(pady=2, fill=tk.X)
            ttk.Label(frame, text=f"{prueba}:", width=10).pack(side=tk.LEFT)
            entry = ttk.Entry(frame)
            entry.pack(side=tk.LEFT, expand=True)
            entries.append(entry)

        def save_data():
            try:
                nombre = nombre_entry.get().strip()
                puntajes = [int(entry.get()) for entry in entries]
                if any(not 0 <= p <= 100 for p in puntajes):
                    raise ValueError
                
                self.sistema.register_logic(nombre, puntajes)
                messagebox.showinfo("Éxito", "Participante registrado correctamente")
                registro_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Ingrese puntajes válidos (0-100)")

        ttk.Button(registro_window, text="Guardar", command=save_data).pack(pady=10)


    def iniciar(self):
        self.window.mainloop()