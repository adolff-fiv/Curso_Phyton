from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = """ SELECT * FROM citas WHERE id_cita IN %s """
        datos = input("Ingrese las citas a consultar separadas por coma ")
        datos_a_buscar = (tuple(datos.split(",")),)
        registros = cursor.execute(sentencia_sql, datos_a_buscar)
        registros = cursor.fetchall()
        print(registros)
        for citas in registros:
            print(f"cita N: {citas.index} {citas}")