CREATE table IF NOY EXISTS contactos(
    id_contacto INT AUTOINCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);

INSERT INTO contactos (nombre, email, telefono)
VALUES 
    ("Orlando", "orlando18@gmail.com", "123 123 1234")
    ("Armando", "armando19@gmail.com", "789 789 7894")