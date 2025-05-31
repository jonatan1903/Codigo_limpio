class Puntuaciones:
    """
    Clase encargada de manejar las puntuaciones de un jugador, ya sea utilizando un sistema
    externo (`sistema_usuario`) o directamente una base de datos vía SQLAlchemy (`session`).

    Atributos:
        jugador (Jugador): Instancia del jugador cuyas puntuaciones se administran.
        session (Session, opcional): Sesión SQLAlchemy para acceso directo a la base de datos.
        sistema_usuario (obj, opcional): Sistema externo para manejar puntuaciones (debe implementar `actualizar_puntuacion` y `obtener_puntuaciones`).
    """

    def __init__(self, jugador, session=None, sistema_usuario=None):
        """
        Inicializa el sistema de puntuaciones para un jugador. Intenta obtener el sistema de usuario
        automáticamente si no se proporciona explícitamente.

        Args:
            jugador (Jugador): El jugador asociado.
            session (Session, opcional): Sesión de base de datos.
            sistema_usuario (obj, opcional): Sistema externo para gestión de puntuaciones.
        """
        self.jugador = jugador
        self.session = session
        self.sistema_usuario = sistema_usuario

        if not self.sistema_usuario and self.session:
            try:
                from src.controller.controlador import Controlador
                self.sistema_usuario = Controlador().sistema_usuario
            except Exception as e:
                print(f"No se pudo obtener el sistema de usuarios: {e}")

        if not self.sistema_usuario and not self.session:
            try:
                from src.controller.controlador import Controlador
                self.sistema_usuario = Controlador().sistema_usuario
            except Exception as e:
                print(f"No se pudo obtener el sistema de usuarios: {e}")

    def actualizar_puntuacion(self, puntos):
        """
        Actualiza el puntaje del jugador y lo guarda usando el sistema disponible
        (sistema_usuario o base de datos directa).

        Args:
            puntos (int): Puntos a agregar al puntaje del jugador.

        Returns:
            int: Nuevo puntaje del jugador.
        """
        if not self.jugador:
            return None

        nuevo_puntaje = self.jugador.actualizar_puntaje(puntos)

        if self.sistema_usuario:
            try:
                return self.sistema_usuario.actualizar_puntuacion(self.jugador, puntos)
            except Exception as e:
                print(f"Error al actualizar puntuación con sistema_usuario: {str(e)}")

        if self.session:
            try:
                from src.model.sistema_usuario import JugadorDB, PuntuacionDB
                jugador_db = self.session.query(JugadorDB).filter_by(nombre_usuario=self.jugador.nombre_usuario).first()

                if not jugador_db:
                    print(f"No se encontró el jugador {self.jugador.nombre_usuario} en la base de datos.")
                    return nuevo_puntaje

                puntuacion = PuntuacionDB(
                    id_jugador=jugador_db.id_jugador,
                    puntos=nuevo_puntaje
                )
                self.session.add(puntuacion)
                self.session.commit()

                print(f"Puntuación registrada: {nuevo_puntaje} puntos para {self.jugador.nombre_usuario}")
            except Exception as e:
                print(f"Error al actualizar puntaje en la base de datos: {str(e)}")
                import traceback
                traceback.print_exc()
                if self.session:
                    self.session.rollback()

        return nuevo_puntaje

    def mostrar_puntuaciones(self, limite=10):
        """
        Devuelve una lista de las puntuaciones más altas, usando el sistema disponible.

        Args:
            limite (int): Número máximo de puntuaciones a devolver.

        Returns:
            list[dict]: Lista de diccionarios con nombre de usuario y puntaje.
        """
        if self.sistema_usuario:
            try:
                return self.sistema_usuario.obtener_puntuaciones(limite)
            except Exception as e:
                print(f"Error al obtener puntuaciones con sistema_usuario: {str(e)}")

        if self.session:
            try:
                from src.model.sistema_usuario import PuntuacionDB, JugadorDB

                resultados = self.session.query(
                    PuntuacionDB, JugadorDB
                ).join(
                    JugadorDB, PuntuacionDB.id_jugador == JugadorDB.id_jugador
                ).order_by(
                    PuntuacionDB.puntos.desc()
                ).limit(limite).all()

                puntuaciones = []
                for puntuacion, jugador in resultados:
                    puntuaciones.append({
                        'nombre_usuario': jugador.nombre_usuario,
                        'puntaje': puntuacion.puntos
                    })

                return puntuaciones
            except Exception as e:
                print(f"Error al obtener puntuaciones de la base de datos: {str(e)}")
                import traceback
                traceback.print_exc()

        return []
