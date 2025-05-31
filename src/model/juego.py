from src.model.campo import Campo

class Juego:
    """
    Clase que representa una partida del juego de batalla naval.

    Atributos:
        ancho (int): Ancho del campo de juego.
        alto (int): Alto del campo de juego.
        num_naves (int): Número total de naves a colocar en el campo.
        campo (Campo): Objeto que representa el campo de juego con las naves.
    """
    def __init__(self, ancho, alto, num_naves):
        """
        Inicializa una nueva partida del juego con el campo de juego generado aleatoriamente.

        Args:
            ancho (int): Ancho del campo de juego.
            alto (int): Alto del campo de juego.
            num_naves (int): Número de naves que se colocarán aleatoriamente.
        """
        self.ancho = ancho
        self.alto = alto
        self.num_naves = num_naves
        self.campo = Campo(ancho, alto, num_naves)

    def realizar_disparo(self, fila, columna):
        """
        Realiza un disparo en una celda específica del campo de juego.

        Args:
            fila (int): Fila donde se realiza el disparo.
            columna (int): Columna donde se realiza el disparo.

        Returns:
            bool: True si el disparo impactó una nave, False si fue agua.

        Raises:
            ValueError: Si la celda ya fue disparada o si las coordenadas son inválidas.
        """
        return self.campo.verificar_impacto(fila, columna)

    def verificar_ganador(self):
        """
        Verifica si el jugador ha ganado la partida (es decir, si todas las naves han sido hundidas).

        Returns:
            bool or None: True si no quedan naves, None en caso contrario.
        """
        if self.campo.naves_restantes == 0:
            return True
        return None

    def reiniciar_juego(self):
        """
        Reinicia la partida creando un nuevo campo con las mismas dimensiones y número de naves.
        """
        self.campo = Campo(self.ancho, self.alto, self.num_naves)
