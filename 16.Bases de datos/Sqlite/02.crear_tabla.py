from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

        # Definir el SQL para crear la tabla
    cursor.execute( """
        CREATE TABLE IF NOT EXISTS medico (
            id_medico INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            tipo_identificacion TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            eps TEXT UNIQUE,
            historia_clinica TEXT(50) NOT NULL
        );
    """)
    
    cursor.execute( """
        CREATE TABLE IF NOT EXISTS citas (
            id_cita INTEGER PRIMARY KEY,
            medico_asociado INTEGER NOT NULL,
            paciente_asociado INTEGER NOT NULL,
            fecha_cita DATE,
            hora_cita DECIMAL(4,2),
            FOREIGN KEY (medico_asociado) REFERENCES medico(id_medico)
        );
    """)

    
    conexion.commit

