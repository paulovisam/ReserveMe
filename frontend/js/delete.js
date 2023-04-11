// seletor para o elemento pai que já existe no momento em que a página é carregada
const tableBody = document.querySelector('#hardware-table tbody');

// manipulador de eventos delegado para o botão com id="trash"
tableBody.addEventListener('click', async function(event) {
  if (event.target.id === 'trash') {
    const row = event.target.closest("tr");
    const id = row.querySelector("td:first-child").textContent;
    const url = `http://127.0.0.1:8000/api/v1/hardware/?id=${id}`;
    const response = await fetch(url, {
      method: 'DELETE',
    });
    if (response.ok) {
      row.remove();
      console.log(`Equipamento com ID ${id} removido com sucesso!`);
    } else {
      console.error(`Erro ao remover equipamento com ID ${id}!`);
    }
  }
});


// const deleteButtons = document.querySelectorAll("#trash");

// deleteButtons.forEach((button) => {
//   button.addEventListener("click", async (event) => {
//     console.log('');
//     const row = event.target.closest("tr");
//     const id = row.querySelector("td:first-child").textContent;

    // const response = await fetch(url, {
    //   method: "DELETE",
    // });

    // if (response.ok) {
    //   row.remove();
    //   console.log(`Equipamento com ID ${id} removido com sucesso!`);
    // } else {
    //   console.error(`Erro ao remover equipamento com ID ${id}!`);
    // }
  // });
// });
