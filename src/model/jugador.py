class Jugador:
    """
    Clase que representa a un jugador del juego.

    Atributos:
        nombre_usuario (str): Nombre de usuario del jugador.
        contraseña (str): Contraseña del jugador.
        puntaje (int): Puntaje acumulado del jugador.
    """
    def __init__(self, nombre_usuario, contraseña):
        """
        Inicializa un nuevo jugador con nombre de usuario y contraseña.

        Args:
            nombre_usuario (str): Nombre de usuario del jugador.
            contraseña (str): Contraseña del jugador.

        Raises:
            ValueError: Si el nombre de usuario o la contraseña están vacíos.
        """
        if not nombre_usuario:
            raise ValueError("El nombre de usuario no puede estar vacío")
        if not contraseña:
            raise ValueError("La contraseña no puede estar vacía")

        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0

    def actualizar_puntaje(self, puntos):
        """
        Suma puntos al puntaje total del jugador.

        Args:
            puntos (int): Número de puntos a agregar.

        Returns:
            int: Puntaje total actualizado del jugador.
        """
        self.puntaje += puntos
        return self.puntaje

    def __str__(self):
        """
        Retorna una representación legible del jugador.

        Returns:
            str: Cadena con el nombre de usuario y puntaje actual.
        """
        return f"Jugador: {self.nombre_usuario}, Puntaje: {self.puntaje}"
