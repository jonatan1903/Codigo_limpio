from src.model.sistema_usuario import SistemaUsuario
from src.model.juego import Juego
from src.model.puntuaciones import Puntuaciones

class Controlador:
    """
    Clase Controlador que maneja la lógica principal del juego, la gestión de usuarios y las puntuaciones.
    """

    def __init__(self):
        """
        Inicializa el controlador con un sistema de usuarios, y sin juego ni jugador activos ni puntuaciones.
        """
        self.sistema_usuario = SistemaUsuario()
        self.juego = None
        self.jugador_activo = None
        self.puntuaciones = None

    def registrar_jugador(self, nombre, contraseña):
        """
        Registra un nuevo jugador en el sistema.

        Args:
            nombre (str): Nombre del jugador.
            contraseña (str): Contraseña del jugador.

        Returns:
            bool: True si el registro fue exitoso, False en caso contrario.
        """
        return self.sistema_usuario.registrar_jugador(nombre, contraseña)

    def iniciar_sesion(self, nombre, contraseña):
        """
        Intenta iniciar sesión con el nombre y contraseña proporcionados.

        Args:
            nombre (str): Nombre del jugador.
            contraseña (str): Contraseña del jugador.

        Returns:
            bool: True si la sesión se inició correctamente, False en caso contrario.
        """
        jugador = self.sistema_usuario.iniciar_sesion(nombre, contraseña)
        if jugador:
            self.jugador_activo = jugador
            self.puntuaciones = Puntuaciones(jugador, self.sistema_usuario.session, self.sistema_usuario)
            return True
        return False

    def iniciar_juego(self, ancho, alto, num_naves):
        """
        Crea una nueva instancia del juego con las dimensiones y cantidad de naves especificadas.

        Args:
            ancho (int): Ancho del tablero.
            alto (int): Alto del tablero.
            num_naves (int): Número de naves a colocar en el tablero.
        """
        self.juego = Juego(ancho, alto, num_naves)

    def realizar_disparo(self, fila, columna):
        """
        Realiza un disparo en la posición especificada y actualiza el estado del juego.

        Args:
            fila (int): Fila del disparo.
            columna (int): Columna del disparo.

        Returns:
            dict: Diccionario con las claves:
                - 'impacto': 'nave' si fue impacto, 'agua' si no.
                - 'hundida': bool indicando si una nave fue hundida (actualmente siempre False).
                - 'juego_terminado': bool indicando si el juego ha terminado.
        """
        if not self.juego:
            raise ValueError("No hay un juego activo")

        impacto_bool = self.juego.realizar_disparo(fila, columna)

        impacto = "nave" if impacto_bool else "agua"
        juego_terminado = self.juego.verificar_ganador()
        hundida = False  

        if juego_terminado and self.jugador_activo and self.puntuaciones:
            self.puntuaciones.actualizar_puntuacion(10)

        return {
            "impacto": impacto,
            "hundida": hundida,
            "juego_terminado": juego_terminado
        }

    def obtener_puntuaciones(self, limite=10):
        """
        Obtiene una lista con las mejores puntuaciones hasta un límite especificado.

        Args:
            limite (int, opcional): Número máximo de puntuaciones a obtener. Por defecto es 10.

        Returns:
            list: Lista con las puntuaciones.
        """
        if self.puntuaciones:
            return self.puntuaciones.mostrar_puntuaciones(limite)
        elif self.sistema_usuario:
            return self.sistema_usuario.obtener_puntuaciones(limite)
        return []

    def obtener_representacion_tablero(self):
        """
        Obtiene una representación visual o textual del tablero actual del juego.

        Returns:
            str: Representación del tablero o mensaje indicando que no hay juego activo.
        """
        if self.juego:
            return self.juego.campo.mostrar_campo()
        return "No hay un juego activo"

    def reiniciar_juego(self):
        """
        Reinicia el juego actual, reseteando el estado del tablero y las naves.

        Returns:
            bool: True si el juego fue reiniciado, False si no hay juego activo.
        """
        if self.juego:
            self.juego.reiniciar_juego()
            return True
        return False

    def juego_terminado(self):
        """
        Verifica si el juego actual ha terminado.

        Returns:
            bool: True si el juego terminó, False en caso contrario o si no hay juego activo.
        """
        if self.juego:
            return self.juego.verificar_ganador() is not None
        return False
