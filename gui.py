#Librerias
import tkinter as tk

from tkinter import ttk, messagebox
"""About: ttk es una funcionalidad extra, similar a lo que es seaborn con matplotlib. 
En resumen, añade diversos widgets tematizados que mejoran la visualización que por lo 
general funcionan exactamente igual a los de Tk original, también añade algunas funcionalidades extra que 
facilitaron mucho la creación de sub-interfaces:
 
ttk funcionalidades y sintaxis: https://docs.python.org/es/3.13/library/tkinter.ttk.html"""

from logic import system_logic
import matplotlib.pyplot as plt

"""ABOUT: FigureCanvasTkAgg es una funcionalidad extra que permite la integración de gráficos de Matplotlib en interfaces gráficas como Tkinter
    Documentación y funcionalidad: https://matplotlib.org/stable/tutorials/artists.html"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Clase específica para las interfaces
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
        #Ventana de registro de participantes
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
        
    def show_general_report(self):
        
        # Ventana de reporte general
        df = self.sistema.make_report()
        if df is None:
            messagebox.showwarning("Advertencia", "No hay participantes registrados")
            return

        reporte_window = tk.Toplevel(self.window)
        reporte_window.title("Reporte General")
        tree = ttk.Treeview(reporte_window, columns=list(df.columns), show='headings')
        
        """ Treeview es un widget que permite visualizar datos en listas jerárquicas proveniente de ttk. Gracias a este,
        widget la sub-interfaz es mucho más fácil de codificar.
        Funcionalidad y documentación: https://recursospython.com/guias-y-manuales/vista-de-arbol-treeview-en-tkinter/"""
        
        for col in df.columns:
            tree.heading(col, text=col)
        for _, row in df.iterrows():
            tree.insert('', tk.END, values=list(row))
        tree.pack(fill=tk.BOTH, expand=True)

        # Gráfico de clasificación
        plt = self.sistema.classification_graph()
        if plt:
            canvas = FigureCanvasTkAgg(plt.gcf(), master=reporte_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            plt.close()
            
    def show_search(self):
        # Ventana de búsqueda individual
        search_window = tk.Toplevel(self.window)
        search_window.title("Buscar Participante")

        ttk.Label(search_window, text="Nombre del participante:").pack(pady=5)
        search_entry = ttk.Entry(search_window)
        search_entry.pack(pady=5)

        def search():
            nombre = search_entry.get().strip()
            participante = next(
                (p for p in self.sistema.participantes if p.nombre.lower() == nombre.lower()),
                None
            )
            if participante:
                self.show_individual_report(participante)
                search_window.destroy()
            else:
                messagebox.showerror("Error", "Participante no encontrado")

        ttk.Button(search_window, text="Buscar", command=search).pack(pady=10)
    def show_individual_report(self, participante):
            #Muestra reporte individual con gráficos
            reporte_window = tk.Toplevel(self.window)
            reporte_window.title(f"Reporte de {participante.nombre}")

            # Información básica
            info_frame = ttk.Frame(reporte_window)
            info_frame.pack(pady=10, fill=tk.X)
            
            ttk.Label(info_frame, text=f"Nombre: {participante.nombre}").pack(anchor='w')
            ttk.Label(info_frame, text=f"Puntaje Final: {participante.puntaje_final}").pack(anchor='w')
            ttk.Label(info_frame, text=f"Clasificado: {'Sí' if participante.clasificado else 'No'}").pack(anchor='w')

            # Gráficos
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
            
            # Gráfico 1: Puntajes por prueba
            pruebas = list(participante.pruebas.keys())
            puntajes = [p['puntaje'] for p in participante.pruebas.values()]
            ax1.bar(pruebas, puntajes, color='skyblue')
            ax1.set_title('Puntajes por Prueba')
            
            # Gráfico 2: Dificultad por prueba
            dificultades = [p['dificultad'] for p in participante.pruebas.values()]
            ax2.bar(pruebas, dificultades, color='lightgreen')
            ax2.set_title('Dificultad por Prueba')
            
            plt.tight_layout()
            
            canvas = FigureCanvasTkAgg(fig, master=reporte_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def iniciar(self):
        self.window.mainloop()