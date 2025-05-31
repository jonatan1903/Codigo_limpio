import pytest
from src.model.juego import Juego

# Pruebas normales
def test_creacion_juego():
    juego = Juego(10, 10, 5)
    assert juego.ancho == 10
    assert juego.alto == 10
    assert juego.num_naves == 5
    assert juego.campo is not None

def test_realizar_disparo():
    juego = Juego(10, 10, 5)
    juego.campo.celdas[2][2] = 1  
    impacto = juego.realizar_disparo(2, 2)
    assert impacto == True

def test_verificar_ganador_no_ganador():
    juego = Juego(10, 10, 5)
    assert juego.verificar_ganador() is None

# Pruebas extremas
def test_verificar_ganador_con_ganador():
    juego = Juego(10, 10, 1)
    juego.campo.celdas[2][2] = 1  
    juego.realizar_disparo(2, 2)
    assert juego.verificar_ganador() is True

def test_reiniciar_juego():
    juego = Juego(10, 10, 5)
    juego.campo.celdas[2][2] = 1 
    juego.realizar_disparo(2, 2)
    juego.reiniciar_juego()
    assert juego.campo.naves_restantes == 5
    assert juego.verificar_ganador() is None

def test_juego_con_dimensiones_grandes():
    juego = Juego(20, 20, 10)
    assert juego.ancho == 20
    assert juego.alto == 20
    assert juego.num_naves == 10

# Pruebas de error
def test_realizar_disparo_sin_juego():
    juego = Juego(10, 10, 5)
    with pytest.raises(ValueError):
        juego.realizar_disparo(10, 10) 

def test_realizar_disparo_celda_ya_disparada():
    juego = Juego(10, 10, 5)
    juego.realizar_disparo(2, 2)
    with pytest.raises(ValueError):
        juego.realizar_disparo(2, 2)

def test_realizar_disparo_con_coordenadas_negativas():
    juego = Juego(10, 10, 5)
    with pytest.raises(ValueError):
        juego.realizar_disparo(-1, 5)
