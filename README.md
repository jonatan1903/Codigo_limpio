# 🛳️ Batalla Naval - Proyecto Final

Este es un juego de **Batalla Naval** desarrollado como proyecto final. El sistema está estructurado siguiendo principios de código limpio y separa correctamente la lógica del backend, la interfaz gráfica y la interfaz web. Permite jugar tanto de manera local como a través de un navegador.

## 🎮 Características

- Juego completo de Batalla Naval.
- Interfaz gráfica hecha con **Kivy**.
- Versión web funcional usando **HTML, CSS y JavaScript**.
- Backend en **Python** (Flask) con sistema de puntuaciones.
- Registro e inicio de sesión de jugadores.
- Persistencia de datos usando archivos `.json`.
- Consultas y estructura para base de datos relacional.
- Pruebas unitarias para componentes clave del sistema.

## 📁 Estructura del Proyecto

Codigo_limpio-main/
├── app.py # Backend con Flask
├── main.py # Ejecutable principal
├── cli.py # Interfaz por línea de comandos
├── datos/ # Archivos JSON (jugadores y puntuaciones)
├── src/
│ ├── controller/ # Lógica central del sistema
│ ├── model/ # Clases: Campo, Nave, Jugador, etc.
│ ├── view/
│ │ ├── gui/ # Pantallas con Kivy (login, juego, etc.)
│ │ └── kv/ # Archivos .kv (diseño de pantallas Kivy)
│ └── web/ # Frontend Web (HTML, JS, CSS)
├── sql/ # Scripts SQL (estructura y consultas)
├── tests/ # Pruebas unitarias con Pytest
└── README.md

shell
Copiar
Editar

## 🧪 Cómo Ejecutar

### 🎲 Opción 1: Modo Gráfico (Kivy)
```bash
python main.py
🌐 Opción 2: Modo Web (Flask)
bash
Copiar
Editar
python app.py
Accede a la versión web desde tu navegador en http://localhost:5000.

⚙️ Requisitos
Python 3.x

Flask

Kivy

(Opcional) Pytest para pruebas

Instala las dependencias con:

bash
Copiar
Editar
pip install -r requirements.txt
✅ Funcionalidades Completas
 Registro y autenticación

 Jugar con registro o como invitado

 Juego funcional con tablero visual

 Guardado y consulta de puntuaciones

 Estructura limpia y modular

 Base de datos opcional integrada (SQL)

 Tests automatizados para lógica del juego

👨‍💻 Autor
Jonatan Noreña Grisales
Andrea Carolina Romero More
GitHub: @jonatan1903