import sqlite3

# Crear o conectar a la base de datos
conn = sqlite3.connect('entidades.db')
cursor = conn.cursor()

# Crear las tablas para las entidades
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clinicas (
    id_clinica INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    telefono TEXT NOT NULL,
    especialidades TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Parques (
    id_parque INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    ubicacion TEXT NOT NULL,
    capacidad INTEGER,
    horarios TEXT
)
''')

# Insertar datos en las tablas
cursor.executemany('''
INSERT INTO Clinicas (nombre, direccion, telefono, especialidades)
VALUES (?, ?, ?, ?)
''', [
    ('Clínica San Rafael', 'Av. Central 123',
     '0987654321', 'Pediatría, Cardiología'),
    ('Clínica Los Ángeles', 'Calle 5 #45',
     '0976543210', 'Medicina General, Traumatología')
])

cursor.executemany('''
INSERT INTO Parques (nombre, ubicacion, capacidad, horarios)
VALUES (?, ?, ?, ?)
''', [
    ('Parque La Libertad', 'Centro Histórico', 500, '8:00 AM - 6:00 PM'),
    ('Parque Los Pinos', 'Barrio Norte', 300, '9:00 AM - 7:00 PM')
])

# Consultar datos
print("Datos de Clínicas:")
cursor.execute('SELECT * FROM Clinicas')
for row in cursor.fetchall():
    print(row)

print("\nDatos de Parques:")
cursor.execute('SELECT * FROM Parques')
for row in cursor.fetchall():
    print(row)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
