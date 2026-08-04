import sqlite3

class Conexion:
    __DATABASE = "./16.Bases de datos/Sqlite/prueba_sqlite.db"

    @classmethod
    def obtener_conexion_sqlite(self):
        return sqlite3.connect(self.__DATABASE)



