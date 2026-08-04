from Conexion import Conexion

conexion= Conexion.obtener_conexion_mysql()

cursor = conexion.cursor()
sentencia_sql = """
UPDATE medico  SET 
    nombre = %s,
    tipo_identificacion = %s,
    numero_tarjeta_profesional =%s,
    anios_experiencia = %s,
    especialidad = %s,
    hora_inicio_atencion = %s,
    hora_fin_atencion = %s
    WHERE id_medico = %s  """

valores = (("Adolf Medicos", "DNT", "Ds", 6.3, "DENTISTA", 8.30, 16.40, 2),
           ("SUSY MedicoS", "DNIH", "Pd", 6.1, "ONCOLOGO", 9.30, 16.50, 1))

cursor.executemany(sentencia_sql, valores)

# Haciendo commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
