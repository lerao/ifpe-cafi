const form = document.getElementById("formCadastro");

function marcarValido(campo) {
    campo.classList.remove("is-invalid");
    campo.classList.add("is-valid");
}

function marcarInvalido(campo) {
    campo.classList.remove("is-valid");
    campo.classList.add("is-invalid");
}

form.addEventListener("submit", function (event) {

    event.preventDefault();

    let valido = true;

    const nome = document.getElementById("nome");
    const email = document.getElementById("email");
    const cpf = document.getElementById("cpf");
    const idade = document.getElementById("idade");
    const dataNascimento = document.getElementById("dataNascimento");
    const estado = document.getElementById("estado");
    const senha = document.getElementById("senha");
    const confirmarSenha = document.getElementById("confirmarSenha");
    const biografia = document.getElementById("biografia");
    const aceite = document.getElementById("aceite");

    /* Nome */
    if (nome.value.trim().length >= 5) {
        marcarValido(nome);
    } else {
        marcarInvalido(nome);
        valido = false;
    }

    /* Email */
    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        marcarValido(email);
    } else {
        marcarInvalido(email);
        valido = false;
    }

    /* CPF */
    const cpfNumeros =
        cpf.value.replace(/\D/g, "");

    if (cpfNumeros.length === 11) {
        marcarValido(cpf);
    } else {
        marcarInvalido(cpf);
        valido = false;
    }

    /* Idade */
    const idadeValor =
        parseInt(idade.value);

    if (idadeValor >= 18 &&
        idadeValor <= 120) {

        marcarValido(idade);

    } else {

        marcarInvalido(idade);
        valido = false;
    }

    /* Data */
    if (dataNascimento.value) {
        marcarValido(dataNascimento);
    } else {
        marcarInvalido(dataNascimento);
        valido = false;
    }

    /* Select */
    if (estado.value !== "") {
        marcarValido(estado);
    } else {
        marcarInvalido(estado);
        valido = false;
    }

    /* Radio */
    const sexoSelecionado =
        document.querySelector(
            'input[name="sexo"]:checked'
        );

    document
        .getElementById("erroSexo")
        .classList.toggle(
            "d-none",
            sexoSelecionado
        );

    if (!sexoSelecionado) {
        valido = false;
    }

    /* Checkbox múltiplo */
    const linguagens =
        document.querySelectorAll(
            ".linguagem:checked"
        );

    document
        .getElementById("erroLinguagens")
        .classList.toggle(
            "d-none",
            linguagens.length > 0
        );

    if (linguagens.length === 0) {
        valido = false;
    }

    /* Senha */
    if (senha.value.length >= 8) {
        marcarValido(senha);
    } else {
        marcarInvalido(senha);
        valido = false;
    }

    /* Confirmar senha */
    if (senha.value === confirmarSenha.value &&
        confirmarSenha.value !== "") {

        marcarValido(confirmarSenha);

    } else {

        marcarInvalido(confirmarSenha);
        valido = false;
    }

    /* Textarea */
    const tamanhoBio =
        biografia.value.trim().length;

    if (tamanhoBio >= 20 &&
        tamanhoBio <= 500) {

        marcarValido(biografia);

    } else {

        marcarInvalido(biografia);
        valido = false;
    }

    /* Termos */
    document
        .getElementById("erroAceite")
        .classList.toggle(
            "d-none",
            aceite.checked
        );

    if (!aceite.checked) {
        valido = false;
    }

    if (valido) {

        alert(
            "Formulário validado com sucesso!"
        );

        console.log("Dados válidos.");
    }
});