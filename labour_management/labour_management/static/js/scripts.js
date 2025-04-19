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
  // --- Existing shift‐name calculation ---
  const startDate = new Date("2024-12-29"); // Green (Day), Red (Night)
  const shiftNames = {
    Day:   ["Green","Green","Green","Green","Blue","Blue","Blue","Blue"],
    Night: ["Red","Red","Red","Red","Yellow","Yellow","Yellow","Yellow"]
  };

  document.querySelectorAll(".shift-name").forEach(cell => {
    const date = new Date(cell.dataset.date);
    const type = cell.dataset.type;
    const diffDays = Math.floor((date - startDate) / (1000 * 60 * 60 * 24));
    const cycleIndex = diffDays % 8;
    cell.textContent = shiftNames[type]?.[cycleIndex] ?? "N/A";
  });

  // --- Modal open/close logic ---
  const modal    = document.getElementById('createShiftModal');
  const openBtn  = document.getElementById('openCreateShiftModal');
  const closeBtn = document.getElementById('closeModalBtn');
  if (modal && openBtn && closeBtn) {
    openBtn.addEventListener('click', () => modal.style.display = 'block');
    closeBtn.addEventListener('click', () => modal.style.display = 'none');
    window.addEventListener('click', e => { if (e.target === modal) modal.style.display = 'none'; });
  }

  // --- Create Shift form submission handler ---
  const form = document.getElementById('createShiftForm');
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();

      // 1. Read date & shift type
      const date      = encodeURIComponent(this.querySelector('#shiftDate').value);
      const shiftType = encodeURIComponent(this.querySelector('#shiftType').value);

      // 2. Gather scenario selections for lines 1–4
      const params = [];
      [1,2,3,4].forEach(i => {
        const sel = this.querySelector(`#scenario${i}`);
        if (sel && sel.value) {
          params.push(`scenario${i}=${encodeURIComponent(sel.value)}`);
        }
      });

      // 3. Build query string and redirect
      const qs = params.join('&');
      window.location.href = `/shifts/rota/${date}/${shiftType}/?${qs}`;
    });
  }
});

document.addEventListener('DOMContentLoaded', () => {
  // 1) Hide every scenario block up front
  document.querySelectorAll('.scenario-block').forEach(el => {
    el.style.display = 'none';
  });

  // 2) Grab the query params
  const params = new URLSearchParams(window.location.search);

  // 3) For each line, un-hide the matching scenario
  [1, 2, 3, 4].forEach(lineNum => {
    const chosen = params.get(`scenario${lineNum}`);
    if (!chosen) return;    // nothing selected for this line

    document
      .querySelectorAll(`.line-column[data-line="${lineNum}"] .scenario-block`)
      .forEach(block => {
        if (block.dataset.scenario === chosen) {
          block.style.display = '';    // show matching block
        }
      });
  });
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


// JavaScript for skills/index.html modal actions

function openAddSkillModal() {
  document.getElementById('addSkillModal').style.display = 'block';
}

function closeAddSkillModal() {
  document.getElementById('addSkillModal').style.display = 'none';
}

function openEditSkillModal() {
  document.getElementById('editSkillModal').style.display = 'block';
}

function closeEditSkillModal() {
  document.getElementById('editSkillModal').style.display = 'none';
}

function confirmDeleteSkill() {
  if (confirm("Are you sure you want to delete this skill profile? This action cannot be undone.")) {
    alert("Skill profile deleted (placeholder logic)");
  }
}
