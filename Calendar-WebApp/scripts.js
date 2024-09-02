// script.js

document.addEventListener("DOMContentLoaded", function() {
    const calendar = document.getElementById("calendar");
    const monthYear = document.getElementById("month-year");
    const prevMonthButton = document.getElementById("prev-month");
    const nextMonthButton = document.getElementById("next-month");

    let currentDate = new Date();

    function renderCalendar(date) {
        calendar.innerHTML = "";

        const month = date.getMonth();
        const year = date.getFullYear();
        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        monthYear.textContent = date.toLocaleDateString('es-ES', { month: 'long', year: 'numeric' });

        const daysOfWeek = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];
        const headerRow = document.createElement("tr");

        daysOfWeek.forEach(day => {
            const th = document.createElement("th");
            th.textContent = day;
            headerRow.appendChild(th);
        });

        calendar.appendChild(headerRow);

        let row = document.createElement("tr");
        for (let i = 0; i < (firstDay === 0 ? 6 : firstDay - 1); i++) {
            const cell = document.createElement("td");
            row.appendChild(cell);
        }

        for (let day = 1; day <= daysInMonth; day++) {
            if (row.children.length === 7) {
                calendar.appendChild(row);
                row = document.createElement("tr");
            }

            const cell = document.createElement("td");

            // Crear el número del día y añadirlo a la celda
            const dayNumber = document.createElement("div");
            dayNumber.textContent = day;
            dayNumber.className = "day-number";
            cell.appendChild(dayNumber);

            // Crear el contenedor de labels
            const labelContainer = document.createElement("div");
            labelContainer.className = "label-container";

            // Crear los tres labels
            const label1 = document.createElement("label");
            label1.textContent = "Tarea1";
            label1.className = "label"; // Clase común
            label1.style.backgroundColor = "blue"; // Color específico

            const label2 = document.createElement("label");
            label2.textContent = "Tarea2";
            label2.className = "label label-yellow"; // Clase común y específica

            const label3 = document.createElement("label");
            label3.textContent = "Tarea3";
            label3.className = "label label-red"; // Clase común y específica

            const label4 = document.createElement("label");
            label4.textContent = "Tarea4";
            label4.className = "label label-green"; // Clase común y específica
            
            const label5 = document.createElement("label");
            label5.textContent = "Tarea5";
            label5.className = "label label-yellow"; // Clase común y específica

            // Añadir los labels al contenedor
            labelContainer.appendChild(label1);
            labelContainer.appendChild(label2);
            labelContainer.appendChild(label3);
            // labelContainer.appendChild(label4);

            // Añadir el contenedor de labels a la celda
            cell.appendChild(labelContainer);
            row.appendChild(cell);
        }

        if (row.children.length > 0) {
            calendar.appendChild(row);
        }
    }

    prevMonthButton.addEventListener("click", function() {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar(currentDate);
    });

    nextMonthButton.addEventListener("click", function() {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar(currentDate);
    });

    renderCalendar(currentDate);
});
