from flask import Flask, request, jsonify
from flask_cors import CORS
from src.controller.controlador import Controlador

app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS
controlador = Controlador()

@app.route("/api/registrar", methods=["POST"])
def registrar_usuario():
    try:
        datos = request.get_json()
        nombre = datos.get("nombre")
        contraseña = datos.get("contraseña")

        if not nombre or not contraseña:
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        exito = controlador.registrar_jugador(nombre, contraseña)
        if exito:
            return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
        else:
            return jsonify({"error": "El usuario ya existe"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/iniciar-sesion", methods=["POST"])
def iniciar_sesion():
    try:
        datos = request.get_json()
        nombre = datos.get("nombre")
        contraseña = datos.get("contraseña")

        if not nombre or not contraseña:
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        exito = controlador.iniciar_sesion(nombre, contraseña)
        if exito:
            return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
        else:
            return jsonify({"error": "Nombre o contraseña incorrectos"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/iniciar-juego", methods=["POST"])
def iniciar_juego():
    try:
        datos = request.get_json()
        ancho = datos.get("ancho")
        alto = datos.get("alto")
        num_naves = datos.get("num_naves")

        if not all([ancho, alto, num_naves]):
            return jsonify({"error": "Faltan datos para iniciar el juego"}), 400

        controlador.iniciar_juego(ancho, alto, num_naves)
        return jsonify({"mensaje": "Juego iniciado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/disparo", methods=["POST"])
def disparar():
    try:
        datos = request.get_json()
        fila = datos.get("fila")
        columna = datos.get("columna")

        if fila is None or columna is None:
            return jsonify({"error": "Coordenadas no válidas"}), 400

        resultado = controlador.realizar_disparo(fila, columna)

        if resultado is None:
            return jsonify({"error": "Error al realizar disparo"}), 400

        return jsonify({
            "impacto": resultado["impacto"],           # "agua" o "nave"
            "hundida": resultado.get("hundida", False), # True si hundida
            "juego_terminado": resultado["juego_terminado"]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/puntuaciones", methods=["GET"])
def obtener_puntuaciones():
    lista_puntuaciones = controlador.obtener_puntuaciones()  # Debe devolver lista de dicts con 'nombre' y 'puntuacion'
    return jsonify(lista_puntuaciones), 200


if __name__ == "__main__":
    app.run(debug=True)
