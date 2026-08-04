from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

# Definir el SQL para crear la tabla
insertar_tabla_medico_sql = """
INSERT INTO medico(id_medico, nombre, fecha_nacimiento, tipo_identificacion,
    eps, historia_clinica)
VALUES (?, ?, ?, ?, ?, ?);
"""

valores = (1,"Adolfo Paredes", "2008/12/08", "DNIff", "EPS 56", "Tuvo gripe ayer" )

# Ejecutar consulta
cursor.execute(insertar_tabla_medico_sql, valores)

# Definir el SQL para crear la tabla
insertar_tabla_citas_sql = """
INSERT INTO citas(id_cita, medico_asociado, paciente_asociado, fecha_cita, hora_cita )
VALUES (?, ?, ?, ?, ?);
"""

valores = (1, 1, 1, "03/12/2020", 3 )

# Ejecutar consulta
cursor.execute(insertar_tabla_citas_sql, valores)

conexion.commit()
# Cerrando objetos
cursor.close()

