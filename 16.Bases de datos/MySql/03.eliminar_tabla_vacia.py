from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS citas")
cursor.execute("DROP TABLE IF EXISTS medico")

conexion.commit()

cursor.close()
conexion.close()
