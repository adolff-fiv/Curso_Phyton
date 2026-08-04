import psycopg2

from Conexion import Conexion


with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = """
            UPDATE citas  SET MEDICO_ASOCIADO = %s, 
            PACIENTE_ASOCIADO = %s,
            FECHA_CITA = %s,
            HORA_CITA = %s
            WHERE ID_CITA = %s
"""
        # Actualizar un solo registro
        #valores = (5, 5, '2023-04-11', 5.30, 1)
        #cursor.execute(sentencia_sql, valores)

        # Actualizar varios registros
        valores = ((5, 5, '2023-04-11', 5.30, 2)
                   ,(5, 5, '2023-04-11', 5.30, 3)
                   ,(5, 5, '2023-04-11', 5.30, 4))
        cursor.executemany(sentencia_sql, valores)

print(f"Registros actualizados {cursor.rowcount}")