class Celda:
    """
    Representa una celda individual en el campo de batalla del juego.

    Atributos:
        nave (bool): Indica si hay una nave en esta celda.
        disparada (bool): Indica si esta celda ya ha sido disparada.
    """
    def __init__(self):
        """
        Inicializa una celda sin nave y sin haber sido disparada.
        """
        self.nave = False
        self.disparada = False

    def recibir_disparo(self):
        """
      Indica que la celda fue disparada y retorna si había una nave.

        Returns:
            bool: True si la celda contenía una nave, False en caso contrario.

        Raises:
            ValueError: Si la celda ya fue disparada.
        """
        if self.disparada:
            raise ValueError("Esta celda ya ha sido impactada")

        self.disparada = True
        return self.nave
