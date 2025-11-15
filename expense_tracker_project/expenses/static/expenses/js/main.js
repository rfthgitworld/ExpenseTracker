// main.js - small helpers for modals and edit buttons
document.addEventListener('DOMContentLoaded', function() {
  // attach event listeners to edit buttons (on dashboard recent list)
  document.querySelectorAll('.edit-expense-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
      const id = btn.dataset.id;
      const title = btn.dataset.title;
      const amount = btn.dataset.amount;
      const date = btn.dataset.date;
      const notes = btn.dataset.notes;

      // populate modal fields
      document.getElementById('edit-expense-id').value = id;
      document.getElementById('edit-title').value = title;
      document.getElementById('edit-amount').value = amount;
      document.getElementById('edit-date').value = date;
      document.getElementById('edit-notes').value = notes;

      // set form action to edit endpoint
      const form = document.getElementById('editExpenseForm');
      form.action = `/expenses/${id}/edit/`;

      // show modal
      const modal = new bootstrap.Modal(document.getElementById('editExpenseModal'));
      modal.show();
    });
  });
});
