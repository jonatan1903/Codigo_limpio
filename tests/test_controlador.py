import pytest
from src.controller.controlador import Controlador

# Pruebas normales
def test_creacion_controlador():
    controlador = Controlador()
    assert controlador.juego is None
    assert controlador.jugador_activo is None
    assert controlador.puntuaciones is None

def test_iniciar_juego():
    controlador = Controlador()
    controlador.iniciar_juego(10, 10, 5)
    assert controlador.juego is not None
    assert controlador.juego.ancho == 10
    assert controlador.juego.alto == 10
    assert controlador.juego.num_naves == 5

def test_registrar_jugador():
    controlador = Controlador()
    import random
    nombre_usuario = f"JugadorTest{random.randint(1000, 9999)}"
    resultado = controlador.registrar_jugador(nombre_usuario, "password123")
    assert isinstance(resultado, bool)

# Pruebas extremas
def test_iniciar_sesion():
    controlador = Controlador()
    controlador.registrar_jugador("JugadorLogin", "password123")
    resultado = controlador.iniciar_sesion("JugadorLogin", "password123")
    assert resultado == True
    assert controlador.jugador_activo is not None
    assert controlador.jugador_activo.nombre_usuario == "JugadorLogin"

def test_realizar_disparo():
    controlador = Controlador()
    controlador.iniciar_juego(10, 10, 5)
    try:
        controlador.realizar_disparo(2, 2)
        assert True  
    except Exception:
        assert False  

def test_obtener_representacion_tablero():
    controlador = Controlador()
    representacion = controlador.obtener_representacion_tablero()
    assert representacion == "No hay un juego activo"

    controlador.iniciar_juego(10, 10, 5)
    representacion = controlador.obtener_representacion_tablero()
    assert isinstance(representacion, str)
    assert len(representacion) > 0

# Pruebas de error
def test_realizar_disparo_sin_juego():
    controlador = Controlador()
    with pytest.raises(ValueError):
        controlador.realizar_disparo(2, 2)

def test_reiniciar_juego_sin_juego():
    controlador = Controlador()
    resultado = controlador.reiniciar_juego()
    assert resultado == False

def test_juego_terminado_sin_juego():
    controlador = Controlador()
    resultado = controlador.juego_terminado()
    assert resultado == False
