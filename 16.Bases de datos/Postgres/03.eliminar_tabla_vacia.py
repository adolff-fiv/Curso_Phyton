import psycopg2

from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:

        # Definir el SQL para crear la tabla
        eliminar_tabla_citas_sql = """
        INSERT INTO citas;
        """

        cursor.execute(eliminar_tabla_citas_sql)

        # Haciendo commit
        conexion.commit()

        # Cerrando objetos
        cursor.close()
        conexion.close()
