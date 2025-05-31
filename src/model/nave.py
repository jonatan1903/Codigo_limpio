class Nave:
    """
    Clase que representa una nave en el juego.

    Atributos:
        posicion (list or tuple): Lista o tupla de coordenadas que ocupan la nave en el campo.
    """
    def __init__(self, posicion):
        """
        Inicializa una nave con su posición en el campo de juego.

        Args:
            posicion (list or tuple): Coordenadas que indican la ubicación de la nave.
        """

        self.posicion = posicion

    def verificar_impacto(self, coordenada):
        """
        Verifica si una coordenada corresponde a un impacto sobre la nave.

        Args:
            coordenada (tuple): Coordenada (fila, columna) del disparo.

        Returns:
            bool: True si la coordenada corresponde a la posición de la nave, False en caso contrario.
        """
        return coordenada in self.posicion
