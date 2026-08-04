from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    sentecia_sql = """
            SELECT citas.fecha_cita, citas.hora_cita, medico.nombre, medico.historia_clinica
            FROM citas INNER JOIN medico ON citas.medico_asociado = medico.id_medico WHERE medico.id_medico = 1
        """
    cursor.execute(sentecia_sql)
    registro = cursor.fetchone()
    print(registro)