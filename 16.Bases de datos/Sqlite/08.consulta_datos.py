from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    sentencia_sql = """ SELECT * FROM medico """
    registros = cursor.execute(sentencia_sql)
    registros = cursor.fetchall()
    print(registros)
    for medico in registros:
        print(f"cita N: {medico.index} {medico}")