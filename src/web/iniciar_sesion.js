/**
 * Maneja el evento submit del formulario de inicio de sesión.
 * Previene el envío tradicional, recoge los datos del formulario,
 * realiza una petición POST al backend para iniciar sesión y procesa la respuesta.
 */
const form = document.getElementById("form-iniciar-sesion");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  /** @type {string} Nombre de usuario ingresado */
  const nombre = document.getElementById("nombre").value.trim();
  /** @type {string} Contraseña ingresada */
  const contraseña = document.getElementById("contraseña").value;

  fetch("http://127.0.0.1:5000/api/iniciar-sesion", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, contraseña }),
  })
  /** 
   * Procesa la respuesta en formato JSON 
   * @param {Object} data - Objeto JSON devuelto por el servidor
   */
  .then(res => res.json())
  .then(data => {
    if (data.mensaje) {
      alert(data.mensaje);
      window.location.href = "jugar.html";
    } else if (data.error) {
      alert(data.error);
    } else {
      alert("Respuesta inesperada del servidor");
    }
  })
  /** 
   * Captura errores en la petición fetch 
   * @param {Error} err - Error ocurrido en la petición
   */
  .catch(err => {
    console.error("Error en la petición:", err);
    alert("Error de conexión con el servidor.");
  });
});
