import csv
import random

# Abre el archivo CSV en modo escritura
with open('datos_iris.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Escribe los encabezados
    writer.writerow(['id', 'Sepal Largo', 'Sepal Ancho', 'Petalo Largo', 'Petalo Ancho', 'Clase'])

    # Genera 800 líneas de datos
    for i in range(1, 100):
        clase = random.choice(['setosa', 'versicolor', 'virginica'])

        if clase == 'setosa':
            sepalo_largo = round(random.uniform(4.0, 5.0), 1)
            sepalo_ancho = round(random.uniform(3.0, 3.5), 1)
            petalo_largo = round(random.uniform(1.0, 3.0), 1)
            petalo_ancho = round(random.uniform(0.1, 1.0), 1)
        elif clase == 'versicolor':
            sepalo_largo = round(random.uniform(6.0, 7.0), 1)
            sepalo_ancho = round(random.uniform(3.5, 4.0), 1)
            petalo_largo = round(random.uniform(3.0, 4.5), 1)
            petalo_ancho = round(random.uniform(1.1, 1.5), 1)
        else:  # clase == 'virginica'
            sepalo_largo = round(random.uniform(5.5, 6.0), 1)
            sepalo_ancho = round(random.uniform(0.2, 3.0), 1)
            petalo_largo = round(random.uniform(5.0, 6.0), 1)
            petalo_ancho = round(random.uniform(1.5, 2.0), 1)

        writer.writerow([i, sepalo_largo, sepalo_ancho, petalo_largo, petalo_ancho, clase])

print("Archivo CSV generado exitosamente.")

