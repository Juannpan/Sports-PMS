import random
import pandas as pd
import matplotlib.pyplot as plt

class Participante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pruebas = {
            'resistencia': {'puntaje': 0, 'dificultad': round(random.uniform(1.0, 1.3), 1)},
            'fuerza': {'puntaje': 0, 'dificultad': round(random.uniform(1.0, 1.3), 1)},
            'velocidad': {'puntaje': 0, 'dificultad': round(random.uniform(1.0, 1.3), 1)}
        }
        self.puntaje_final = 0
        self.clasificado = False

    def score(self):
        suma_ponderada = sum(p['puntaje'] * p['dificultad'] for p in self.pruebas.values())
        suma_dificultades = sum(p['dificultad'] for p in self.pruebas.values())
        self.puntaje_final = round(suma_ponderada / suma_dificultades)
        self.clasificado = self.puntaje_final >= 70
        return self.puntaje_final
    
class system_logic:
    def __init__(self):
        self.participantes = []

    def register_logic(self, nombre, puntajes):
        """Registra participantes 
           **SOLO LOS ALMACENA EN LA SESIÓN ACTUAL** """
        p = Participante(nombre)
        p.pruebas['resistencia']['puntaje'] = puntajes[0]
        p.pruebas['fuerza']['puntaje'] = puntajes[1]
        p.pruebas['velocidad']['puntaje'] = puntajes[2]
        p.score()
        self.participantes.append(p)
        return p

    def make_report(self):
        """Genera DataFrame con estadísticas"""
        if not self.participantes:
            return None

        data = {
            'Nombre': [p.nombre for p in self.participantes],
            'Puntaje': [p.puntaje_final for p in self.participantes],
            'Clasificación': ['Sí' if p.clasificado else 'No' for p in self.participantes]
        }
        return pd.DataFrame(data)

    def classification_graph(self):
        """Genera gráfico circular"""
        if not self.participantes:
            return None

        df = self.make_report()
        counts = df['Clasificación'].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
        plt.title('Distribución de Clasificación')
        return plt