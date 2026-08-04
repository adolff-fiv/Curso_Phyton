import psycopg2

from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:

        # Definir el SQL para insertar elementos
        insercion_tabla_citas_sql = """
        INSERT INTO citas(
            medico_asociado ,
            paciente_asociado ,
            fecha_cita ,
            hora_cita
        ) VALUES(%s, %s, %s, %s);
        """
        valores = ((1, 2, "2026-12-12",4.50),
                (2, 1, "2026-12-12",5.50),
                (3, 3, "2026-12-12",6.50),
                (4, 4, "2026-12-12",7.50))

        cursor.executemany(insercion_tabla_citas_sql,valores)
