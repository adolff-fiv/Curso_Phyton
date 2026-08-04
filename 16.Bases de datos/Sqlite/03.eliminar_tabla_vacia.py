from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

# Definir el SQL para crear la tabla
eliminar_tabla_medico_sql = """
DROP TABLE IF EXISTS medico;
"""

# Ejecutar consulta
cursor.execute(eliminar_tabla_medico_sql)

# Haciendo commit
conexion.commit()

# Cerrando objetos
conexion.close()
