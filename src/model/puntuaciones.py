class Puntuaciones:
    def __init__(self, jugador, session=None, sistema_usuario=None):
        self.jugador = jugador
        self.session = session
        self.sistema_usuario = sistema_usuario

        # Si no tenemos sistema_usuario pero tenemos session, intentamos obtener el sistema_usuario
        if not self.sistema_usuario and self.session:
            try:
                from src.controller.controlador import Controlador
                self.sistema_usuario = Controlador().sistema_usuario
            except Exception as e:
                print(f"No se pudo obtener el sistema de usuarios: {e}")

        # Si no tenemos sistema_usuario y no tenemos session, intentamos obtener el sistema_usuario
        if not self.sistema_usuario and not self.session:
            try:
                from src.controller.controlador import Controlador
                self.sistema_usuario = Controlador().sistema_usuario
            except Exception as e:
                print(f"No se pudo obtener el sistema de usuarios: {e}")

    def actualizar_puntuacion(self, puntos):
        if not self.jugador:
            return None

        nuevo_puntaje = self.jugador.actualizar_puntaje(puntos)

        # Primero intentamos usar el sistema_usuario si está disponible
        if self.sistema_usuario:
            try:
                return self.sistema_usuario.actualizar_puntuacion(self.jugador, puntos)
            except Exception as e:
                print(f"Error al actualizar puntuación con sistema_usuario: {str(e)}")
                # Si falla, continuamos con el siguiente método

        # Si tenemos session, intentamos usar la base de datos directamente
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

        # Si todo lo demás falla, simplemente devolvemos el nuevo puntaje
        return nuevo_puntaje

    def mostrar_puntuaciones(self, limite=10):
        # Primero intentamos usar el sistema_usuario si está disponible
        if self.sistema_usuario:
            try:
                return self.sistema_usuario.obtener_puntuaciones(limite)
            except Exception as e:
                print(f"Error al obtener puntuaciones con sistema_usuario: {str(e)}")
                # Si falla, continuamos con el siguiente método

        # Si tenemos session, intentamos usar la base de datos directamente
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

        # Si todo lo demás falla, devolvemos una lista vacía
        return []
