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
