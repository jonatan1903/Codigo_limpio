/**
 * Inicializa el juego cuando el contenido del DOM está cargado.
 */
document.addEventListener("DOMContentLoaded", () => {
  /** @type {HTMLFormElement} Formulario para iniciar el juego */
  const form = document.getElementById("form-juego");
  /** @type {HTMLElement} Contenedor donde se generará el tablero */
  const tableroContainer = document.getElementById("tablero-container");

  /**
   * Maneja el evento submit del formulario para iniciar el juego.
   * Envía datos al servidor y genera el tablero si es exitoso.
   * @param {SubmitEvent} e - Evento de envío del formulario.
   */
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    /** @type {number} Ancho del tablero */
    const ancho = parseInt(document.getElementById("ancho").value);
    /** @type {number} Alto del tablero */
    const alto = parseInt(document.getElementById("alto").value);
    /** @type {number} Número de naves */
    const num_naves = parseInt(document.getElementById("num_naves").value);

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
   * Genera el tablero de juego como una tabla HTML.
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
        celda.style.fontSize = "20px";
        celda.addEventListener("click", () => disparar(i, j, celda));
        fila.appendChild(celda);
      }
      tabla.appendChild(fila);
    }

    tableroContainer.appendChild(tabla);
  }

  /**
   * Realiza un disparo en la posición especificada y actualiza la celda según el resultado.
   * @param {number} fila - Índice de la fila donde se dispara.
   * @param {number} columna - Índice de la columna donde se dispara.
   * @param {HTMLElement} celda - Elemento de la celda que se actualiza visualmente.
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
        if (data.impacto === "agua") {
          celda.textContent = "🌊";
        } else if (data.hundida) {
          celda.textContent = "💀";
        } else {
          celda.textContent = "💥";
        }

        // Evita que se pueda volver a clicar la misma celda
        celda.style.pointerEvents = "none";

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
