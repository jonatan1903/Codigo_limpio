/**
 * Ejecuta la carga de las puntuaciones cuando el DOM está listo.
 * Obtiene la lista de puntuaciones del servidor y las muestra en pantalla.
 */
document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/api/puntuaciones")
    .then(res => res.json())
    .then(data => {
      /** @type {HTMLElement} Elemento UL donde se mostrarán las puntuaciones */
      const lista = document.getElementById("lista-puntuaciones");
      lista.innerHTML = "";

      // Si no hay puntuaciones, muestra mensaje indicándolo
      if (data.length === 0) {
        lista.innerHTML = "<li>No hay puntuaciones.</li>";
        return;
      }

      // Por cada puntuación, crea un <li> y lo añade a la lista
      data.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.nombre} - ${item.puntos} pts`;
        lista.appendChild(li);
      });
    })
    .catch(err => {
      console.error("Error al cargar puntuaciones:", err);
    });
});
