import sqlite3
import json

# Conexión a la base de datos
conn = sqlite3.connect('entidades_no_relacional.db')
cursor = conn.cursor()

# Crear una tabla para almacenar JSON
cursor.execute('''
CREATE TABLE IF NOT EXISTS entidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    datos TEXT NOT NULL
)
''')

# Datos para las entidades
clinica1 = {
    "nombre": "Clínica Vida",
    "direccion": "Av. Central 123",
    "telefono": "0991234567",
    "especialidades": ["Pediatría", "Cardiología"]
}
parque1 = {
    "nombre": "Parque Central",
    "ubicacion": "Centro de la ciudad",
    "horario": "8:00 AM - 8:00 PM",
    "actividades": ["Caminata", "Juegos para niños"]
}

# Insertar datos como JSON
cursor.execute("INSERT INTO entidades (tipo, datos) VALUES (?, ?)",
               ("clinica", json.dumps(clinica1)))
cursor.execute("INSERT INTO entidades (tipo, datos) VALUES (?, ?)",
               ("parque", json.dumps(parque1)))

# Confirmar cambios
conn.commit()

# Consultar y mostrar datos
print("Clínicas registradas:")
cursor.execute("SELECT datos FROM entidades WHERE tipo = ?", ("clinica",))
for row in cursor.fetchall():
    print(json.loads(row[0]))

print("\nParques registrados:")
cursor.execute("SELECT datos FROM entidades WHERE tipo = ?", ("parque",))
for row in cursor.fetchall():
    print(json.loads(row[0]))

# Cerrar conexión
conn.close()
