from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from src.controller.controlador import Controlador
import os

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'login.kv')
Builder.load_file(os.path.abspath(kv_path))

class LoginScreen(Screen):
    """
    Pantalla de inicio de sesión que permite al usuario ingresar sus credenciales,
    validar el acceso mediante el controlador y navegar a la pantalla de juego.
    """

    mensaje = StringProperty("")

    def __init__(self, **kwargs):
        """
        Inicializa la pantalla y crea una instancia del controlador.
        """
        super(LoginScreen, self).__init__(**kwargs)
        self.controlador = Controlador()

    def on_enter(self):
        """
        Evento que se ejecuta al entrar a la pantalla, limpia los campos
        de usuario y contraseña y resetea el mensaje de estado.
        """
        if hasattr(self.ids, 'usuario_input'):
            self.ids.usuario_input.text = ""
        if hasattr(self.ids, 'contraseña_input'):
            self.ids.contraseña_input.text = ""

        self.mensaje = ""

    def iniciar_sesion(self):
        """
        Obtiene los valores de usuario y contraseña desde la interfaz,
        valida que no estén vacíos y llama al controlador para verificar
        las credenciales. Actualiza el mensaje de estado y navega a la pantalla
        de juego si el login es exitoso.
        """
        usuario = self.ids.usuario_input.text.strip()
        contraseña = self.ids.contraseña_input.text.strip()

        if not usuario or not contraseña:
            self.mensaje = "❌ Todos los campos son obligatorios."
            return

        if self.controlador.iniciar_sesion(usuario, contraseña):
            self.mensaje = "✅ Inicio de sesión exitoso."
            juego_screen = self.manager.get_screen("juego")
            juego_screen.controlador = self.controlador
            self.manager.current = "juego"
        else:
            self.mensaje = "❌ Credenciales incorrectas."

    def volver(self):
        """
        Cambia la pantalla actual a la pantalla del menú principal.
        """
        self.manager.current = "menu"
