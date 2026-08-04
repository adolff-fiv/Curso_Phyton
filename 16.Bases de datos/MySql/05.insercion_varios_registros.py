import mysql.connector

from Conexion import Conexion

conexion= Conexion.obtener_conexion_mysql()

cursor = conexion.cursor()

# Definir el SQL para insertar registros
insertar_tabla_paciente_sql = """
INSERT INTO medico(
    
    nombre,
    tipo_identificacion,
    numero_tarjeta_profesional,
    anios_experiencia,
    especialidad,
    hora_inicio_atencion,
    hora_fin_atencion
) VALUES( %s, %s, %s,%s, %s, %s, %s );
"""
valores = (("Adolf Medico", "DNI", "ns", "5.3", "Derma", "8.30", "16.40"),
           ("SUSY Medico", "DNIE", "xd", "5.1", "Trauma", "9.30", "16.50"))


# Ejecutar consulta
cursor.executemany(insertar_tabla_paciente_sql, valores)

# Haciendo commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()

