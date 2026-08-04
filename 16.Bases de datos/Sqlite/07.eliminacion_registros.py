from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

sentencia_sql = "DELETE FROM medico WHERE id_medico =  ?"
eliminacion = tuple(input("Ingrese el id del médico a eliminar " ))
cursor.execute(sentencia_sql,eliminacion)


print(f"{cursor.rowcount} Registros eliminados")

# Haciendo commit
conexion.commit()

# Cerrando objetos
conexion.close()    