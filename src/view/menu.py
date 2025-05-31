from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

kv_path = os.path.join(os.path.dirname(__file__), 'kv', 'menu.kv')
Builder.load_file(os.path.abspath(kv_path))

class MenuScreen(Screen):
    """
    Pantalla principal del menú que permite la navegación entre las diferentes secciones de la aplicación.
    """
    pass
