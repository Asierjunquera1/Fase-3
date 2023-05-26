import csv

# Nombre del archivo CSV
csv_filename = 'users.csv'

# Lista de encabezados para el archivo CSV
header = ['id', 'name', 'email']

# Abre el archivo en modo escritura y crea un objeto writer de CSV
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Escribe los encabezados en el archivo
    writer.writerow(header)

    # Escribe los registros en el archivo
    for user in users:
        writer.writerow([user.id, user.name, user.email])
