const salvarBtn = document.querySelector("#save");
salvarBtn.addEventListener("click", async () => {
   const nameInput = document.querySelector("#name");
   const amountInput = document.querySelector("#amount");
   const descriptionInput = document.querySelector("#description");

   const name = nameInput.value;
   const amount = amountInput.value;
   const description = descriptionInput.value;

   const url = "http://127.0.0.1:8000/api/v1/hardware";
   const data = { "name": name, "description": description, "amount": amount, "status": "disponivel"};

   const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
   });

   if (response.ok) {
      const responseData = await response.json();
      console.log(responseData);
      const tbody = document.querySelector("tbody");
      const novaLinha = `
      <tr>
         <td style="color: rgb(255,255,255);text-align: center;">${responseData.id}</td>
         <td style="color: rgb(255,255,255);text-align: center;">${responseData.name}</td>
         <td style="color: rgb(255,255,255);text-align: center;">${responseData.amount}</td>
         <td style="color: rgb(255,255,255);text-align: center;">
            <div style="color: rgb(255,255,255);">
               <button id="edit" class="btn btn-secondary btn-sm" type="button" style="margin-right: 0;padding: 4px;">
                  <i class="far fa-edit" style="font-size: 15px;color: rgb(255,255,255);" href="#"></i>
               </button>
               <button id="trash" class="btn btn-danger btn-sm">
                  <i class="far fa-trash-alt" style="font-size: 15px;margin-left: 0;color: rgb(255,255,255);padding: 1px;"></i>
               </button>
            </div>
         </td>
      </tr>
      `;
      tbody.innerHTML += novaLinha;
   } else {

   }
});
