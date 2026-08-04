import mysql.connector

from Conexion import Conexion

conexion= Conexion.obtener_conexion_mysql()
   
# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()
sentencia_sql = """ SELECT * FROM medico """
registros = cursor.execute(sentencia_sql)
registros = cursor.fetchall()
print(registros)
for medico in registros:
    print(f"cita N: {medico.index} {medico}")
