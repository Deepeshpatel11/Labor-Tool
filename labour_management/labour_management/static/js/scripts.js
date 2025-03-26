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


// Modal open/close logic - create shift rota
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


// Holiday Table Dynamic Header & Row Fill

document.addEventListener('DOMContentLoaded', () => {
  const tableHeader = document.querySelector('.holiday-table thead tr');
  const tableBody = document.getElementById('holidayTableBody');

  const today = new Date('2025-01-01');
  const daysToShow = 31; // Example: show January 2025

  // Insert dynamic headers
  for (let i = 0; i < daysToShow; i++) {
    const date = new Date(today);
    date.setDate(today.getDate() + i);
    const dateStr = date.toLocaleDateString('en-GB', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    }).replace(/\//g, '/');

    const th = document.createElement('th');
    th.textContent = dateStr;
    tableHeader.appendChild(th);
  }

  // Populate one example row dynamically
  const row = tableBody.querySelector('tr');
  for (let i = 0; i < daysToShow; i++) {
    const td = document.createElement('td');
    if (i === 22) td.textContent = 'Holiday';
    row.appendChild(td);
  }



  // Sticky Style Functions for Holiday Table
  function applyStickyStyle() {
    document.querySelectorAll(".holiday-table tr").forEach(row => {
      row.querySelectorAll("td:nth-child(-n+5), th:nth-child(-n+5)").forEach(cell => {
        cell.style.backgroundColor = "#f0f9fa"; // Match your header background
        cell.style.zIndex = "1";
      });
    });
  }

  function revertStickyStyle() {
    document.querySelectorAll(".holiday-table tr").forEach(row => {
      row.querySelectorAll("td:nth-child(-n+5), th:nth-child(-n+5)").forEach(cell => {
        cell.style.backgroundColor = "";
        cell.style.zIndex = "";
      });
    });
  }

  // Modal logic for holiday request
  const modal = document.getElementById('leaveModal');
  const openBtn = document.getElementById('btnAdd');
  const closeBtn = document.getElementById('closeModal');

  if (openBtn && modal && closeBtn) {
    openBtn.addEventListener('click', () => {
      modal.style.display = 'block';
      applyStickyStyle();
    });

    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
      revertStickyStyle();
    });

    window.addEventListener('click', (event) => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  }

  // Holiday approval modal

  document.getElementById("approveLeaveBtn").addEventListener("click", function () {
    document.getElementById("approveModal").style.display = "block";
    applyStickyStyle();
  });

  document.getElementById("closeApproveModal").addEventListener("click", function () {
    document.getElementById("approveModal").style.display = "none";
    revertStickyStyle();
  });
});




// Holiday filter logic
document.addEventListener("DOMContentLoaded", () => {
  const nameFilter = document.getElementById("filterName");
  const shiftFilter = document.getElementById("filterShift");
  const roleFilter = document.getElementById("filterRole");
  const areaFilter = document.getElementById("filterArea");
  const statusFilter = document.getElementById("filterStatus");

  const filterRows = () => {
    const rows = document.querySelectorAll("#holidayTableBody tr");
    rows.forEach(row => {
      const name = row.querySelector("td:nth-child(2)")?.textContent.toLowerCase() || "";
      const shift = row.querySelector("td:nth-child(3)")?.textContent || "";
      const role = row.querySelector("td:nth-child(4)")?.textContent || "";
      const area = row.querySelector("td:nth-child(5)")?.textContent || "";

      const hasPending = row.innerHTML.includes('Pending');
      const hasApproved = row.innerHTML.includes('Approved');

      let statusMatch = true;
      if (statusFilter.value === "Pending") statusMatch = hasPending;
      if (statusFilter.value === "Approved") statusMatch = hasApproved;

      const isVisible =
        name.includes(nameFilter.value.toLowerCase()) &&
        (shiftFilter.value === "" || shift === shiftFilter.value) &&
        (roleFilter.value === "" || role === roleFilter.value) &&
        (areaFilter.value === "" || area === areaFilter.value) &&
        statusMatch;

      row.style.display = isVisible ? "" : "none";
    });
  };

  [nameFilter, shiftFilter, roleFilter, areaFilter, statusFilter].forEach(input => {
    input.addEventListener("input", filterRows);
    input.addEventListener("change", filterRows);
  });
});
