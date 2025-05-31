/**
 * Inicializa los manejadores de eventos al cargar el contenido del DOM.
 */
document.addEventListener("DOMContentLoaded", () => {
  /** @type {HTMLButtonElement} Botón para iniciar juego sin registro */
  const btnIniciar = document.getElementById("btn-jugar-sin-registro");
  /** @type {HTMLElement} Contenedor donde se generará el tablero */
  const tableroContainer = document.getElementById("tablero-container");

  /**
   * Evento click para iniciar el juego. Valida entradas y hace petición al backend.
   */
  btnIniciar.addEventListener("click", async () => {
    /** @type {number} Ancho del tablero */
    const ancho = parseInt(document.getElementById("ancho").value);
    /** @type {number} Alto del tablero */
    const alto = parseInt(document.getElementById("alto").value);
    /** @type {number} Número de naves */
    const num_naves = parseInt(document.getElementById("num_naves").value);

    if (
      isNaN(ancho) || ancho < 1 ||
      isNaN(alto) || alto < 1 ||
      isNaN(num_naves) || num_naves < 1
    ) {
      alert("Por favor, ingresa valores válidos para el tamaño y número de naves.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/iniciar-juego", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ancho, alto, num_naves }),
      });

      if (!response.ok) throw new Error("Error al iniciar juego");
      alert("Juego iniciado. ¡Haz clic en una celda para disparar!");
      generarTablero(alto, ancho);
    } catch (error) {
      alert("No se pudo iniciar el juego.");
      console.error(error);
    }
  });

  /**
   * Genera dinámicamente un tablero de juego (tabla HTML) con filas y columnas indicadas.
   * Cada celda tiene un evento click para disparar.
   * @param {number} filas - Número de filas del tablero.
   * @param {number} columnas - Número de columnas del tablero.
   */
  function generarTablero(filas, columnas) {
    tableroContainer.innerHTML = "";
    const tabla = document.createElement("table");

    for (let i = 0; i < filas; i++) {
      const fila = document.createElement("tr");
      for (let j = 0; j < columnas; j++) {
        const celda = document.createElement("td");
        celda.textContent = "";
        celda.style.border = "1px solid black";
        celda.style.width = "30px";
        celda.style.height = "30px";
        celda.style.textAlign = "center";
        celda.style.cursor = "pointer";
        celda.addEventListener("click", () => disparar(i, j, celda));
        fila.appendChild(celda);
      }
      tabla.appendChild(fila);
    }

    tableroContainer.appendChild(tabla);
  }

  /**
   * Envía una petición al backend para disparar en la posición dada y actualiza la celda con el resultado.
   * @param {number} fila - Índice de la fila donde se dispara.
   * @param {number} columna - Índice de la columna donde se dispara.
   * @param {HTMLElement} celda - La celda del tablero que se actualiza visualmente.
   */
  async function disparar(fila, columna, celda) {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/disparo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fila, columna }),
      });

      const data = await response.json();
      if (response.ok) {
        celda.textContent = data.impacto === "agua" ? "🌊" : "💥";
        if (data.juego_terminado) {
          alert("¡Ganaste! Todas las naves han sido destruidas.");
        }
      } else {
        alert(data.error);
      }
    } catch (error) {
      alert("Error al disparar.");
      console.error(error);
    }
  }
});
