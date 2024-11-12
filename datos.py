import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["admin"]  # Cambiar 'BaseDeDatos' al nombre correcto si es necesario
collection = db["datos1"]  # Cambiar 'Santiago1' si tu colección tiene otro nombre

# Obtener datos de la colección y convertirlos en un DataFrame
data = list(collection.find({}))
df = pd.DataFrame(data)

# Verificar las columnas disponibles
print("Columnas en el DataFrame:", df.columns)

# Asegúrate de que los campos relevantes están presentes en el DataFrame
if not df.empty and 'Tematica' in df.columns:
    # Agrupar por la columna 'Tematica' y contar la cantidad de eventos por cada tematica
    df_grouped = df.groupby('Tematica').size().reset_index(name='Cantidad')

    # Mostrar las primeras filas de df_grouped para ver cómo quedó el agrupamiento
    print(df_grouped.head())

    # Gráfico de barras para mostrar la cantidad de eventos por temática
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Tematica'], df_grouped['Cantidad'], color='orange')
    plt.title("Cantidad de eventos por Temática")
    plt.xlabel("Temática")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("El campo 'Tematica' no está presente en los datos.")
