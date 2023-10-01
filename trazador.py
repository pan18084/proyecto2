import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Datos completos
dias = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
precios = np.array([25686.8, 25969.57, 25812.42, 25779.98, 25753.24, 26240.2, 25905.65, 25895.68, 25832.23, 25162.65, 25833.34, 26228.32, 26539.67, 26608.69, 26568.28])

# Selección de los primeros 3 y los últimos 3 puntos para el ajuste
primeros_dias = dias[:3]
primeros_precios = precios[:3]
ultimos_dias = dias[-3:]
ultimos_precios = precios[-3:]

# Combinar los puntos seleccionados
dias_ajuste = np.concatenate((primeros_dias, ultimos_dias))
precios_ajuste = np.concatenate((primeros_precios, ultimos_precios))

# Crear el trazador cúbico utilizando los puntos seleccionados
trazador_cubico = CubicSpline(dias_ajuste, precios_ajuste)

# Evaluar el trazador en un rango de días
dias_evaluacion = np.linspace(min(dias), max(dias), 100)  # Rango de días completo
precios_evaluacion = trazador_cubico(dias_evaluacion)

# Graficar los puntos de ajuste y el trazador cúbico proyectado
plt.figure(figsize=(10, 6))
plt.scatter(dias_ajuste, precios_ajuste, label=f'3 Primeros y 3 Últimos Datos (Usados en Ajuste)', color='blue')
plt.plot(dias_evaluacion, precios_evaluacion, label='Trazador Cúbico Proyectado', color='red')
plt.xlabel('Día')
plt.ylabel('Precio de Bitcoin')
plt.title(f'Trazador Cúbico de Bitcoin (Ajuste con 3 Primeros y 3 Últimos Puntos)')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir el porcentaje de error respecto a todos los puntos
error_porcentaje = np.abs(precios - trazador_cubico(dias)) / precios * 100
for dia, error in zip(dias, error_porcentaje):
    print(f"Día {dia}: Porcentaje de Error = {error:.2f}%")
