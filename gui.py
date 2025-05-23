import tkinter as tk
import numpy as np
import math 
import matplotlib.pyplot as plt
import pandas as pd
import random
from tkinter import messagebox

class app_gui:
    def __init__(self, report_callback = None):
        self.participantes = {}
        self.window = tk.Tk()
        self.window.title('Sistema de Gestión Deportiva')
        self.make_gui()
        
    def make_gui(self):
        #gui básica
        self.frame = tk.Frame(self.window).pack(paddy=20)
        
        #Label básico
        tk.Label(self.window, text='Sistema de Gestión Deportiva', font='calibri').pack(paddy=10)
        
        #botones básicos
        self.register_btn = tk.Button(self.window, text='Registrar participante', command=self.show_register_gui, width=25).pack(paddy=5)
        self.report_btn = tk.Button(self.window, text='Mostrar Reporte General', command=self.show_report, width=25).pack(paddy=5)
        
        
        
        
    def show_report(self):
        messagebox.showinfo("Advertencia.", "Usted está accediendo a esta función desde la clase base")
        
    def show_register_gui(self):
        messagebox.showinfo("Advertencia", "Usted está accediendo a esta función desde la clase base")
        
    def boot(self):
        self.window.mainloop()