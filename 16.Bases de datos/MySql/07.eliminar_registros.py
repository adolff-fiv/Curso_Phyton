import mysql.connector

from Conexion import Conexion

conexion= Conexion.obtener_conexion_mysql()
   
# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

sentencia_sql = "DELETE FROM medico WHERE id_medico =  %s"
eliminacion = tuple(input("Ingrese el id del médico a eliminar " ))
cursor.execute(sentencia_sql,eliminacion)


print(f"{cursor.rowcount} Registros eliminados")

# Haciendo commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
