import psycopg2

from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        
        sentencia_sql = "DELETE FROM citas WHERE id_cita IN %s"
        #Eliminar un solo registro
        #eliminacion = tuple(input("Ingrese el id de la cita a eliminar " ))
        #cursor.execute(sentencia_sql,eliminacion)

        #Eliminar varios registros
        entrada = input("Ingrese el id de las citas a eliminar separadas por una coma " )
        eliminacion = (tuple(entrada.split(",")),)
        cursor.execute(sentencia_sql,eliminacion)
        print(f"{cursor.rowcount} Registros eliminados")