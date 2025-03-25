// JavaScript for employee/index.html modal actions

function openEditForm() {
  document.getElementById('editFormModal').style.display = 'block';
}
  
function closeEditForm() {
  document.getElementById('editFormModal').style.display = 'none';
}
  
function openAddForm() {
  // Placeholder - can open a different modal or reuse the edit one
  alert('Open add employee form (to be implemented)');
}
  
function confirmDelete() {
  if (confirm("Are you sure you want to delete this employee? This action cannot be undone.")) {
    alert("Employee deleted (placeholder logic)");
  }
}
  
// JavaScript for Shift/index.html

document.addEventListener("DOMContentLoaded", function () {
  const startDate = new Date("2024-12-29"); // Green (Day), Red (Night)
  const shiftNames = {
    Day: ["Green", "Green", "Green", "Green", "Blue", "Blue", "Blue", "Blue"],
    Night: ["Red", "Red", "Red", "Red", "Yellow", "Yellow", "Yellow", "Yellow"]
  };
  
  const cells = document.querySelectorAll(".shift-name");
  
  cells.forEach(cell => {
    const date = new Date(cell.dataset.date);
    const type = cell.dataset.type;
  
    const diffDays = Math.floor((date - startDate) / (1000 * 60 * 60 * 24));
    const cycleIndex = diffDays % 8;
  
    const shift = shiftNames[type] ? shiftNames[type][cycleIndex] : "N/A";
    cell.textContent = shift;
  });
});
  

  // Modal open/close logic
document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('createShiftModal');
  const openBtn = document.getElementById('openCreateShiftModal');
  const closeBtn = document.getElementById('closeModalBtn');

  if (openBtn && closeBtn && modal) {
    openBtn.addEventListener('click', () => {
      modal.style.display = 'block';
    });

    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  }
});



// ----- Dynamically Insert Dates into Table Header -----
function generateDateHeaders() {
  const theadRow = document.querySelector('#holiday-table thead tr');
  const startDate = new Date('2025-01-01');
  const endDate = new Date('2025-12-31');

  while (startDate <= endDate) {
      const th = document.createElement('th');
      th.textContent = startDate.toLocaleDateString('en-GB');
      theadRow.appendChild(th);
      startDate.setDate(startDate.getDate() + 1);
  }
}

// ----- Open/Close Modal -----
document.getElementById("openModalBtn").addEventListener("click", () => {
  document.getElementById("leaveModal").style.display = "block";
});
document.querySelector(".closeModal").addEventListener("click", () => {
  document.getElementById("leaveModal").style.display = "none";
});

// ----- Submit Holiday Request -----
document.getElementById("leaveRequestForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const gpid = "11111111"; // Placeholder
  const name = "Example Employee";
  const shift = "Red";
  const role = "General Operator";
  const area = "Process";
  const leaveType = document.getElementById("leaveType").value;
  const leaveDate = document.getElementById("leaveDate").value;

  const newRow = document.createElement("tr");
  newRow.innerHTML = `
      <td>${gpid}</td>
      <td>${name}</td>
      <td>${shift}</td>
      <td>${role}</td>
      <td>${area}</td>
  `;

  // Loop through 365 dates and insert blank or leave label
  const start = new Date('2025-01-01');
  const end = new Date('2025-12-31');
  while (start <= end) {
      const td = document.createElement("td");
      if (start.toISOString().slice(0, 10) === leaveDate) {
          td.textContent = leaveType;
      }
      newRow.appendChild(td);
      start.setDate(start.getDate() + 1);
  }

  document.getElementById("holidayTableBody").appendChild(newRow);
  document.getElementById("leaveModal").style.display = "none";
  this.reset();
});

// ----- Run on Page Load -----
window.addEventListener("DOMContentLoaded", generateDateHeaders);
