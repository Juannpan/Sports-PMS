Sistema de Gestión de Rendimiento en Pruebas Deportivas
Un centro deportivo está organizando una competencia donde se evalúa el rendimiento físico de sus participantes en tres pruebas diferentes. Cada prueba tiene un nivel de dificultad aleatorio, lo que influye en el cálculo del puntaje final ponderado de cada participante.
El sistema debe implementarse como una interfaz gráfica utilizando tkinter y debe ofrecer el siguiente menú:
1. Registrar participante
2. Mostrar reporte general
3. Mostrar reporte individual por participante
4. Salir
1. Registrar participante
Los datos pueden almacenarse en listas o en un diccionario.

- El usuario ingresa el nombre del participante.
- Ingresa los resultados (puntajes entre 0 y 100) en tres pruebas físicas: resistencia, fuerza y velocidad.
- Para cada prueba, el programa genera automáticamente un nivel de dificultad decimal aleatorio entre 1.0 y 1.3 usando random.
- Se calcula el puntaje final ponderado con la fórmula:
  Puntaje Final = (∑ (puntaje × dificultad)) / (∑ dificultades)
- El puntaje se redondea a un entero usando round() o math.ceil().
- Si el puntaje es mayor o igual a 70, el participante clasifica. De lo contrario, no clasifica.
2. Mostrar reporte general
Debe incluir:
- Nombre de cada participante
- Puntaje final
- Estado: Clasificó / No clasificó

Además, debe mostrar:
-estadísticas importantes (describe en pandas)
- Puntaje promedio del grupo
- Gráfico de torta con el total de clasificados y no clasificados
- Matriz de correlación de los puntajes (si se usó pandas)
3. Mostrar reporte individual por participante
- El usuario ingresa el nombre del participante.
- Se debe mostrar:
  - Puntaje final
  - Estado
  - Resultados por prueba en un histograma con matplotlib
  - Nivel de dificultad aplicado en cada prueba en un histograma con matplotlib
  - Puntaje ponderado por prueba en un histograma con matplotlib
