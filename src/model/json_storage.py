import json
import os
from datetime import datetime

class JSONStorage:
    """
    Clase encargada de gestionar el almacenamiento de datos en archivos JSON para jugadores y puntuaciones.

    Atributos:
        json_dir (str): Directorio donde se guardan los archivos JSON.
        jugadores_file (str): Ruta al archivo JSON que contiene los datos de los jugadores.
        puntuaciones_file (str): Ruta al archivo JSON que contiene las puntuaciones.
    """
    def __init__(self, json_dir='datos'):
        """
        Inicializa una instancia de JSONStorage, creando los archivos y directorio si no existen.

        Args:
            json_dir (str): Directorio donde se almacenarán los archivos JSON. Por defecto es 'datos'.

        Archivos creados:
            - jugadores.json: Inicializado con una lista vacía si no existe.
            - puntuaciones.json: Inicializado con una lista vacía si no existe.
        """
        self.json_dir = json_dir
        self.jugadores_file = os.path.join(json_dir, 'jugadores.json')
        self.puntuaciones_file = os.path.join(json_dir, 'puntuaciones.json')
        
        # Crear directorio si no existe
        os.makedirs(json_dir, exist_ok=True)
        
        # Inicializar archivos JSON si no existen
        if not os.path.exists(self.jugadores_file):
            self._guardar_jugadores([])
        
        if not os.path.exists(self.puntuaciones_file):
            self._guardar_puntuaciones([])
    
    def _cargar_jugadores(self):
        """
        Carga la lista de jugadores desde el archivo jugadores.json.

        Returns:
            list: Lista de diccionarios con los datos de los jugadores.
                  Retorna una lista vacía si el archivo no existe o está corrupto.
        """
        try:
            with open(self.jugadores_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _guardar_jugadores(self, jugadores):
        """
        Guarda una lista de jugadores en el archivo jugadores.json.

        Args:
            jugadores (list): Lista de diccionarios con los datos de los jugadores.
        """
        with open(self.jugadores_file, 'w') as f:
            json.dump(jugadores, f, indent=4)
    
    def _cargar_puntuaciones(self):
        """
        Carga la lista de puntuaciones desde el archivo puntuaciones.json.

        Returns:
            list: Lista de diccionarios con las puntuaciones.
                  Retorna una lista vacía si el archivo no existe o está corrupto.
        """
        try:
            with open(self.puntuaciones_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _guardar_puntuaciones(self, puntuaciones):
        """
        Guarda una lista de puntuaciones en el archivo puntuaciones.json.

        Args:
            puntuaciones (list): Lista de diccionarios con las puntuaciones a guardar.
        """
        with open(self.puntuaciones_file, 'w') as f:
            json.dump(puntuaciones, f, indent=4)
    
    def registrar_jugador(self, nombre_usuario, contraseña):
        """
        Registra un nuevo jugador si el nombre de usuario no está en uso.

        Args:
            nombre_usuario (str): Nombre de usuario único del jugador.
            contraseña (str): Contraseña del jugador.

        Returns:
            bool: True si el jugador fue registrado correctamente.
                  False si el nombre de usuario ya está en uso.
        """
        jugadores = self._cargar_jugadores()
        
        # Verificar si el jugador ya existe
        for jugador in jugadores:
            if jugador['nombre_usuario'] == nombre_usuario:
                return False
        
        # Crear nuevo jugador
        nuevo_jugador = {
            'id': len(jugadores) + 1,
            'nombre_usuario': nombre_usuario,
            'contraseña': contraseña
        }
        
        jugadores.append(nuevo_jugador)
        self._guardar_jugadores(jugadores)
        return True
    
    def iniciar_sesion(self, nombre_usuario, contraseña):
        jugadores = self._cargar_jugadores()
        
        for jugador in jugadores:
            if jugador['nombre_usuario'] == nombre_usuario and jugador['contraseña'] == contraseña:
                return jugador
        
        return None
    
    def actualizar_puntuacion(self, id_jugador, puntos):
        """
        Registra una nueva puntuación para un jugador dado.

        Args:
            id_jugador (int): ID del jugador que obtuvo la puntuación.
            puntos (int): Puntuación obtenida por el jugador.

        Returns:
            int: La puntuación registrada.
        """
        puntuaciones = self._cargar_puntuaciones()
        
        nueva_puntuacion = {
            'id': len(puntuaciones) + 1,
            'id_jugador': id_jugador,
            'puntos': puntos,
            'fecha': datetime.now().isoformat()
        }
        
        puntuaciones.append(nueva_puntuacion)
        self._guardar_puntuaciones(puntuaciones)
        return puntos
    
    def obtener_puntuaciones(self, limite=10):
        """
        Obtiene una lista de puntuaciones ordenadas de mayor a menor.

        Args:
            limite (int): Número máximo de resultados a devolver. Por defecto es 10.

        Returns:
            list: Lista de diccionarios con las puntuaciones, cada uno contiene:
                - 'nombre_usuario': Nombre del jugador.
                - 'puntaje': Puntos obtenidos.
                - 'fecha': Fecha del registro.
        """
        puntuaciones = self._cargar_puntuaciones()
        jugadores = self._cargar_jugadores()
        
        jugadores_dict = {j['id']: j['nombre_usuario'] for j in jugadores}
        
        resultado = []
        for p in puntuaciones:
            nombre_usuario = jugadores_dict.get(p['id_jugador'], 'Desconocido')
            resultado.append({
                'nombre_usuario': nombre_usuario,
                'puntaje': p['puntos'],
                'fecha': p['fecha']
            })
        
        resultado.sort(key=lambda x: x['puntaje'], reverse=True)
        
        return resultado[:limite]
