from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

# Definir el SQL para crear la tabla
eliminar_tabla_paciente_sql = """
INSERT INTO medico(id_medico, nombre, fecha_nacimiento, tipo_identificacion,
    eps, historia_clinica)
VALUES (?, ?, ?, ?, ?, ?);
"""

valores = [(1,"Adolfo Paredes", "2008/12/07", "DNI", "EPS 1", "Tuvo gripe ayer"),
           (2,"Ricardo Paredes", "2008/12/06", "DNI", "EPS 2", "Tuvo artritis ayer"),
           (3,"Andres Paredes", "2008/12/04", "DNI", "EPS 3", "Tuvo asma ayer"),
             (4,"Gonzalo Paredes", "2008/12/10", "DNI", "EPS 4", "Tuvo colera ayer")]

# Ejecutar consulta
cursor.executemany(eliminar_tabla_paciente_sql, valores)

# Haciendo commit
conexion.commit()

print(f"Se han insertado {cursor.rowcount} registros ")

# Cerrando objetos
conexion.close()
