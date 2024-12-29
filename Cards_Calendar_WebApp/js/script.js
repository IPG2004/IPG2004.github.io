document.addEventListener("DOMContentLoaded", () => {
  const noteText = document.querySelector('.note-text');
  const noteDay = document.querySelector('.note-day');
  const dateInput = document.getElementById('date');
  const prevButton = document.getElementById('prev-btn');
  const nextButton = document.getElementById('next-btn');

  const minDate = "2024-01-01"; // Fecha mínima
  const today = new Date().toISOString().split('T')[0]; // Fecha máxima (hoy)
  dateInput.value = today;
  dateInput.setAttribute('min', minDate);
  dateInput.setAttribute('max', today);

  // Función para actualizar nota
  const actualizarNota = (fecha) => {
      fetch('json/frases.json')
          .then(response => response.json())
          .then(frases => {
              const fraseDelDia = frases[fecha] || "No hay frase para este día.";
              noteText.textContent = fraseDelDia;

              const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
              const fechaSeleccionada = new Date(fecha).toLocaleDateString('es-ES', opciones);
              noteDay.textContent = fechaSeleccionada;
          })
          .catch(error => console.error("Error cargando las frases:", error));

      // Habilitar/deshabilitar botones según el rango de fechas
      prevButton.disabled = fecha === minDate;
      nextButton.disabled = fecha === today;
  };

  // Cargar frase del día actual
  actualizarNota(today);

  // Avanzar un día
  const avanzarDia = (incremento) => {
    const fechaActual = new Date(dateInput.value + "T00:00:00Z"); // Asegura el formato UTC
    fechaActual.setUTCDate(fechaActual.getUTCDate() + incremento); // Incrementa en UTC
    const nuevaFecha = fechaActual.toISOString().split('T')[0];
    dateInput.value = nuevaFecha;
    actualizarNota(nuevaFecha);
  };

  // Evento para cambio manual de fecha
  dateInput.addEventListener('change', (event) => {
      actualizarNota(event.target.value);
  });

  // Eventos para botones de navegación
  prevButton.addEventListener('click', () => avanzarDia(-1));
  nextButton.addEventListener('click', () => avanzarDia(1));
});

