// JavaScript for Shift/index.html

document.addEventListener("DOMContentLoaded", () => {
  //
  // 1) Calculate and fill shift names (Day/Night cycle)
  //
  const startDate = new Date("2024-12-29");
  const shiftNames = {
    Day:   ["Green","Green","Green","Green","Blue","Blue","Blue","Blue"],
    Night: ["Red","Red","Red","Red","Yellow","Yellow","Yellow","Yellow"]
  };

  document.querySelectorAll(".shift-name").forEach(cell => {
    const date    = new Date(cell.dataset.date);
    const type    = cell.dataset.type;
    const diff    = Math.floor((date - startDate) / (1000*60*60*24));
    const index   = ((diff % 8) + 8) % 8; // ensure positive
    cell.textContent = shiftNames[type]?.[index] ?? "N/A";
  });


  //
  // 2) Create‑Shift modal open/close
  //
  const modal    = document.getElementById('createShiftModal');
  const openBtn  = document.getElementById('openCreateShiftModal');
  const closeBtn = document.getElementById('closeModalBtn');

  if (modal && openBtn && closeBtn) {
    openBtn.addEventListener('click',  () => modal.style.display = 'block');
    closeBtn.addEventListener('click', () => modal.style.display = 'none');
    window.addEventListener('click', e => {
      if (e.target === modal) modal.style.display = 'none';
    });
  }


  //
  // 3) Handle Create‑Shift form submit → redirect with scenario params
  //
  const form = document.getElementById('createShiftForm');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();

      const date      = encodeURIComponent(form.querySelector('#shiftDate').value);
      const shiftType = encodeURIComponent(form.querySelector('#shiftType').value);

      // gather each scenario# value
      const params = [1,2,3,4].map(i => {
        const sel = form.querySelector(`#scenario${i}`);
        return sel && sel.value
          ? `scenario${i}=${encodeURIComponent(sel.value)}`
          : null;
      }).filter(x => x);

      const qs = params.join('&');
      window.location.href = `/shifts/rota/${date}/${shiftType}/?${qs}`;
    });
  }


  //
  // 4) Show only matching scenario‑blocks in manning_rota.html
  //
  console.log('Rota page loaded, URL:', window.location.search);

  // 4.1) Hide all scenarios up front
  document.querySelectorAll('.scenario-block').forEach(el => {
    el.style.display = 'none';
  });
  console.log('All scenario-blocks are now hidden.');

  // 4.2) Read the chosen scenarios from the query string
  const qsParams = new URLSearchParams(window.location.search);

  [1,2,3,4].forEach(lineNum => {
    const chosen = qsParams.get(`scenario${lineNum}`);
    console.log(`Line ${lineNum} → chosen scenario =`, chosen);

    if (!chosen) {
      console.log(`  → skipping line ${lineNum} (no param)`);
      return;
    }

    const selector = `.line-column[data-line="${lineNum}"] .scenario-block`;
    const blocks = document.querySelectorAll(selector);
    console.log(`  → found ${blocks.length} blocks for line ${lineNum}`);

    blocks.forEach(block => {
      console.log('    • block scenario =', block.dataset.scenario);
      if (block.dataset.scenario === chosen) {
        block.style.display = 'block';   // explicitly un-hide
        console.log('      ✔ showing this block');
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
