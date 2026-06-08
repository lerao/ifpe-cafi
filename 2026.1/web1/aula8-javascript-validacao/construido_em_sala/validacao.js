const form = document.getElementById('formCadastro');

form.addEventListener('submit', function(event) {
    
    event.preventDefault(); 

    let validoForm = true;
    const nome = document.getElementById('nome');
    if (nome.value.trim().length < 10) {
        validoForm = false;
        nome.classList.add("is-invalid");
        nome.classList.remove("is-valid");
    } else {
        nome.classList.add("is-valid");
        nome.classList.remove("is-invalid");
    }
    if (validoForm) {
        alert('Dados enviados!');
    }
});