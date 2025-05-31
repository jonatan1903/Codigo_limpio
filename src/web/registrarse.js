/**
 * Ejecuta el script una vez que el DOM se ha cargado completamente.
 * Maneja el proceso de registro de un nuevo usuario mediante un formulario HTML.
 */
document.addEventListener("DOMContentLoaded", () => {
  /** @type {HTMLFormElement} Formulario de registro */
  const form = document.getElementById("form-registrarse");

  /**
   * Evento que se ejecuta al enviar el formulario.
   * Valida los campos y envía los datos al servidor para registrar al usuario.
   *
   * @param {Event} e - Evento de envío del formulario
   */
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    /** @type {string} Nombre ingresado por el usuario */
    const nombre = document.getElementById("nombre").value.trim();
    
    /** @type {string} Contraseña ingresada por el usuario */
    const contraseña = document.getElementById("contraseña").value;

    if (!nombre || !contraseña) {
      alert("Por favor, completa todos los campos.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/registrar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ nombre, contraseña }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Registro exitoso. Ahora puedes iniciar sesión.");
        window.location.href = "iniciar_sesion.html";
      } else {
        alert("Error en registro: " + data.error);
      }
    } catch (error) {
      alert("Error de conexión con el servidor.");
      console.error(error);
    }
  });
});
