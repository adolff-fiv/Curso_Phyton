import psycopg2

from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:

        # Definir el SQL para crear la tabla
        insercion_tabla_citas_sql = """
        INSERT INTO citas(
            medico_asociado ,
            paciente_asociado ,
            fecha_cita ,
            hora_cita
        ) VALUES(%s, %s, %s, %s);
        """
        valores = (56, 96, "2020-12-12",3.50)

        cursor.execute(insercion_tabla_citas_sql,valores)

