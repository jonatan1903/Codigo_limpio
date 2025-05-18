-- Tabla de jugadores
CREATE TABLE jugador (
    id_jugador SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);

-- Tabla de puntuaciones
CREATE TABLE puntuacion (
    id_puntuacion SERIAL PRIMARY KEY,
    id_jugador INT NOT NULL,
    puntos INT DEFAULT 0,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_jugador) REFERENCES jugador(id_jugador) ON DELETE CASCADE
);

-- Las siguientes tablas están definidas para una futura implementación
-- donde se almacenen los juegos en la base de datos.

-- Tabla de juegos
CREATE TABLE juego (
    id_juego SERIAL PRIMARY KEY,
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'en curso'
);

-- Relación entre jugadores y juegos
CREATE TABLE jugador_juego (
    id_jugador INT NOT NULL,
    id_juego INT NOT NULL,
    PRIMARY KEY (id_jugador, id_juego),
    FOREIGN KEY (id_jugador) REFERENCES jugador(id_jugador) ON DELETE CASCADE,
    FOREIGN KEY (id_juego) REFERENCES juego(id_juego) ON DELETE CASCADE
);

-- Tabla de campos de juego
CREATE TABLE campo (
    id_campo SERIAL PRIMARY KEY,
    id_jugador INT NOT NULL,
    id_juego INT NOT NULL,
    tamaño INT NOT NULL,
    FOREIGN KEY (id_jugador) REFERENCES jugador(id_jugador) ON DELETE CASCADE,
    FOREIGN KEY (id_juego) REFERENCES juego(id_juego) ON DELETE CASCADE
);

-- Tabla de celdas del campo
CREATE TABLE celda (
    id_celda SERIAL PRIMARY KEY,
    id_campo INT NOT NULL,
    fila INT NOT NULL,
    columna INT NOT NULL,
    tiene_nave BOOLEAN DEFAULT FALSE,
    fue_disparada BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_campo) REFERENCES campo(id_campo) ON DELETE CASCADE
);

-- Tabla de naves
CREATE TABLE nave (
    id_nave SERIAL PRIMARY KEY,
    id_campo INT NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    tamaño INT NOT NULL,
    FOREIGN KEY (id_campo) REFERENCES campo(id_campo) ON DELETE CASCADE
);

-- Relación entre naves y celdas
CREATE TABLE nave_celda (
    id_nave INT NOT NULL,
    id_celda INT NOT NULL,
    PRIMARY KEY (id_nave, id_celda),
    FOREIGN KEY (id_nave) REFERENCES nave(id_nave) ON DELETE CASCADE,
    FOREIGN KEY (id_celda) REFERENCES celda(id_celda) ON DELETE CASCADE
);
