import sqlite3

conexion = sqlite3.connect("./16.Bases de datos/Sqlite/prueba_sqlite.db")

print(conexion)

conexion.close()