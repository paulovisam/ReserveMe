document.addEventListener("DOMContentLoaded", async () => {
   const url = "http://127.0.0.1:8000/api/v1/hardware";

   try {
   const response = await fetch(url);

   if (response.ok) {
      const equipamentos = await response.json();
      const tableBody = document.querySelector("#hardware-table tbody");

      equipamentos.forEach((equipamento) => {
         const row = document.createElement("tr");
         row.style.color = "rgb(255, 255, 255)";
         row.style.textAlign = "center";

         const idCell = document.createElement("td");
         idCell.textContent = equipamento.id;
         row.appendChild(idCell);

         const nameCell = document.createElement("td");
         nameCell.textContent = equipamento.name;
         row.appendChild(nameCell);

         const descriptionCell = document.createElement("td");
         descriptionCell.textContent = equipamento.description;
         row.appendChild(descriptionCell);

         const amountCell = document.createElement("td");
         amountCell.textContent = equipamento.amount;
         row.appendChild(amountCell);
         const actionsCell = document.createElement("td");

         const statusCell = document.createElement("td");
         statusCell.textContent = equipamento.status;
         row.appendChild(statusCell);

         const divButton = document.createElement("div");
         divButton.style.color = "rgb(255,255,255)";

         const editButton = document.createElement("button");
         editButton.id = "edit"
         editButton.classList.add("btn", "btn-secondary", "btn-sm");
         editButton.type = "button";
         editButton.style.marginRight = "5px";
         editButton.style.padding = "4px";
         const editIcon = document.createElement("i");
         editIcon.classList.add("far", "fa-edit");
         editIcon.style.fontSize = "15px";
         editIcon.style.color = "rgb(255,255,255)";
         editIcon.href = "#";
         editButton.appendChild(editIcon);

         const deleteButton = document.createElement("button");
         deleteButton.id = 'trash'
         deleteButton.classList.add("btn", "btn-danger", "btn-sm");
         const deleteIcon = document.createElement("i");
         deleteIcon.classList.add("far", "fa-trash-alt");
         deleteIcon.style.fontSize = "15px";
         deleteIcon.style.marginLeft = "0";
         deleteIcon.style.color = "rgb(255,255,255)";
         deleteIcon.style.padding = "1px";
         deleteButton.appendChild(deleteIcon);
         divButton.appendChild(editButton);
         divButton.appendChild(deleteButton);

         actionsCell.appendChild(divButton);
         row.appendChild(actionsCell);
         tableBody.appendChild(row);
      });
   } else {
      console.error("Erro ao buscar os equipamentos");
   }
   } catch (error) {
   console.error("Erro ao buscar os equipamentos", error);
   }
});
