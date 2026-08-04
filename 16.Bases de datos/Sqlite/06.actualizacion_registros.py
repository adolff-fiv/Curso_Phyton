from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()


with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor() 
    sentencia_sql = """
            UPDATE medico  SET NOMBRE = ?, 
            FECHA_NACIMIENTO = ?
            WHERE ID_MEDICO = ?
"""
    #Actualizar un solo registro
    #valores = ("YONNI", '2023-04-12', 1)
    #cursor.execute(sentencia_sql, valores)

    # Actualizar varios registros
    valores = (("YONNI", '2023-07-12', 1)
                   ,("YONNI", '2023-05-12', 2)
                   ,("YONNI", '2023-06-12', 3))
    cursor.executemany(sentencia_sql, valores)

print(f"Registros actualizados {cursor.rowcount}")