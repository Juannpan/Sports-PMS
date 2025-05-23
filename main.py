import numpy as np
import math 
import matplotlib.pyplot as plt
import pandas as pd
import random

#App backend

class participantes:
    
    def __init__(self, nombre):
        #Pruebas almacena el puntaje por prueba y la dificultad asignada.
        #Se utilizará una clasificación booleana
        self.nombre = nombre
        self.pruebas = {
            'resistencia': {'puntaje': 0.0, 'dificultad': 0.0},
            'fuerza': {'puntaje': 0.0, 'dificultad': 0.0},
            'velocidad': {'puntaje': 0.0, 'dificultad': 0.0} 
        }
        self.puntaje_final = 0
        self.clasificacion = False
        
    def calcular_puntaje_final(self):
        ponderado = sum(
            prueba["puntaje"] * prueba["dificultad"]
            for prueba in self.pruebas.values()
        )
        sum_dificultades = sum(
            prueba["dificultad"] for prueba in self.pruebas.values()
        )
        
class reports:
    def __init__(self):
        pass
    def make_report(self):
        pass
        