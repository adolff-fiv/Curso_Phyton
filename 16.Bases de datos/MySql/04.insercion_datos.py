import mysql.connector

from Conexion import Conexion

conexion= Conexion.obtener_conexion_mysql()
   
# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para insertar datos
_tabla_medico_sql = """
INSERT INTO medico(
    id_medico,
    nombre,
    tipo_identificacion,
    numero_tarjeta_profesional,
    anios_experiencia,
    especialidad,
    hora_inicio_atencion,
    hora_fin_atencion
) VALUES(%s, %s, %s, %s,%s, %s, %s, %s );
"""
valores = (9, "Adolf Medico", "DNI", "NosADA", "5.3", "Derma", "8.30", "16.40")

# Ejecutar consulta
cursor.execute(_tabla_medico_sql, valores)

# Haciendo commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()

