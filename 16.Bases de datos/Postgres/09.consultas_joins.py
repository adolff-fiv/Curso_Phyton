from Conexion import conexion

with conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentecia_sql = """
            SELECT citas.fecha_cita, citas.hora_cita, medico.nombre_medico, medico.especialidad 
            FROM citas INNER JOIN medico ON citas.medico_asociado = medico.id_medico WHERE id_medico = 1
        """
        cursor.execute(sentecia_sql)
        registro = cursor.fetchone()
        print(registro)