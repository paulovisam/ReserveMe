// saveButton = document.querySelector('#editModal #editForm button[type="submit"]');
let saveButton;
function loadEditForm(id, name, amount, description, status) {
   document.getElementById('edit-name').value = name;
   document.getElementById('edit-amount').value = amount;
   document.getElementById('edit-description').value = description;
   document.getElementById('edit-status').value = status;
   
   var myModal = new bootstrap.Modal(document.getElementById('editModal'));
   myModal.show();
   
   myModal._element.addEventListener('shown.bs.modal', function() {
      saveButton = myModal._element.querySelector('#editModal #editForm button[type="submit"]');
      saveButton.addEventListener('click', function(event) {
         event.preventDefault();
         console.log('alterado');
         saveChanges(id);
         myModal.hide();
      });
   });
}




const tableBodyEdit = document.querySelector('#hardware-table tbody');
tableBodyEdit.addEventListener('click', function(event) {
   if (event.target.id === 'edit') {
      console.log('click edit');
      var row = event.target.closest('tr');
      var id = row.cells[0].textContent;
      var name = row.cells[1].textContent;
      var description = row.cells[2].textContent;
      var amount = row.cells[3].textContent;
      var status = row.cells[4].textContent;
      console.log(id, name, description, amount, status);
      loadEditForm(id, name, amount, description, status)
   }
});



async function saveChanges(id) {
   const name = document.querySelector('#editModal #edit-name').value;
   const description = document.querySelector('#editModal #edit-description').value;
   const amount = document.querySelector('#editModal #edit-amount').value;
   const status = document.querySelector('#editModal #edit-status').value;

   const requestBody = {
      id: id,
      name: name,
      description: description,
      amount: amount,
      status: status
   };

   const response = await fetch('http://127.0.0.1:8000/api/v1/hardware', {
      method: 'PUT',
      body: JSON.stringify(requestBody),
      headers: {
         'Content-Type': 'application/json'
      }
   });

   const data = await response.json();

   if (response.ok) {
      console.log('Equipamento atualizado com sucesso!');
      // fechar o modal e atualizar a tabela
   } else {
      console.error(data.message);
   }
}




