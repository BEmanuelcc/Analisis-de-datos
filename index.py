import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
archivo_excel = 'C:\\Users\\Usuario\\Desktop\\Registro de Ventas.xlsx'
# Reemplaza con la ubicación de tu archivo Excel
df = pd.read_excel(archivo_excel)

# Calcular el promedio de ventas y consumos de producción
promedio_ventas = df['Ventas'].mean()
promedio_consumos = df['Consumo Produccion'].mean()

# Calcular la tasa de crecimiento de ventas (puedes ajustar este valor)
tasa_crecimiento_ventas = 0.1

# Calcular la proyección de ventas futuras
proyeccion_ventas = []
for i in range(1, 13):  # Proyectar para los próximos 12 meses
    proyeccion_ventas.append(promedio_ventas * (1 + tasa_crecimiento_ventas) ** i)

# Crear un DataFrame para la proyección de inventario
proyeccion_df = pd.DataFrame({
    'Mes': pd.date_range(start=df['Fecha'].max(), periods=12, freq='M'),
    'Proyeccion_Ventas': proyeccion_ventas,
    'Proyeccion_Consumo': promedio_consumos
})

# Calcular el inventario proyectado
proyeccion_df['Inventario_Proyectado'] = proyeccion_df['Proyeccion_Consumo'].cumsum() - proyeccion_df['Proyeccion_Ventas'].cumsum()

# Graficar la proyección de inventario
plt.figure(figsize=(10, 6))
plt.plot(proyeccion_df['Mes'], proyeccion_df['Inventario_Proyectado'], marker='o')
plt.xlabel('Mes')
plt.ylabel('Inventario Proyectado')
plt.title('Proyección de Inventario')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
