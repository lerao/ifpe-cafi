const steps = document.querySelectorAll(".step");
const nextButtons = document.querySelectorAll(".next-btn");
const prevButtons = document.querySelectorAll(".prev-btn");
const progressBar = document.getElementById("progressBar");
const form = document.getElementById("formCadastro");

let currentStep = 0;

/*
 * Exibe a etapa atual
 */
function showStep(stepIndex) {

    steps.forEach(step => {
        step.classList.add("d-none");
    });

    steps[stepIndex].classList.remove("d-none");

    const percentual =
        ((stepIndex + 1) / steps.length) * 100;

    progressBar.style.width = percentual + "%";
    progressBar.innerText =
        `Etapa ${stepIndex + 1} de ${steps.length}`;
}

/*
 * Valida os campos da etapa atual
 */
function validateCurrentStep() {

    const inputs =
        steps[currentStep].querySelectorAll("input");

    let valid = true;

    inputs.forEach(input => {

        input.classList.remove("is-invalid");
        input.classList.remove("is-valid");

        if (!input.checkValidity()) {

            input.classList.add("is-invalid");
            valid = false;

        } else {

            input.classList.add("is-valid");
        }
    });

    /*
     * Validação extra:
     * confirmar senha
     */
    if (currentStep === 2) {

        const senha =
            document.getElementById("senha");

        const confirmarSenha =
            document.getElementById("confirmarSenha");

        if (senha.value !== confirmarSenha.value) {

            confirmarSenha.classList.remove("is-valid");
            confirmarSenha.classList.add("is-invalid");

            valid = false;
        }
    }

    return valid;
}

/*
 * Próximo
 */
nextButtons.forEach(button => {

    button.addEventListener("click", () => {

        if (!validateCurrentStep()) {
            return;
        }

        currentStep++;

        showStep(currentStep);
    });
});

/*
 * Voltar
 */
prevButtons.forEach(button => {

    button.addEventListener("click", () => {

        currentStep--;

        showStep(currentStep);
    });
});

/*
 * Submit final
 */
form.addEventListener("submit", event => {

    event.preventDefault();

    if (!validateCurrentStep()) {
        return;
    }

    const dados = {
        nome: document.getElementById("nome").value,
        email: document.getElementById("email").value,
        cidade: document.getElementById("cidade").value,
        estado: document.getElementById("estado").value
    };

    console.log(dados);

    alert("Cadastro realizado com sucesso!");

    form.reset();

    document.querySelectorAll("input").forEach(input => {
        input.classList.remove("is-valid");
        input.classList.remove("is-invalid");
    });

    currentStep = 0;

    showStep(currentStep);
});

/*
 * Inicialização
 */
showStep(0);