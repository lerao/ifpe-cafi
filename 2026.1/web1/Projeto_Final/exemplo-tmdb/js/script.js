// Configurações da API (Chave de exemplo - em um projeto real, use variáveis de ambiente ou oculte-a)
const API_KEY = 'bc92298d50dc8e55966ed65364788848'; 
const BASE_URL = 'https://api.themoviedb.org/3';
const IMG_URL = 'https://image.tmdb.org/t/p/w500';

// Elementos do DOM
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const moviesContainer = document.getElementById('movies-container');
const loadingText = document.getElementById('loading');
const movieModal = document.getElementById('movie-modal');
const modalTitle = document.getElementById('modal-title');
const modalDescription = document.getElementById('modal-description');
const closeModal = document.getElementById('close-modal');

// Função para buscar filmes (RF01)
async function searchMovies(query) {
    showLoading();
    moviesContainer.innerHTML = ''; // Limpa os resultados anteriores

    try {
        const url = query 
            ? `${BASE_URL}/search/movie?api_key=${API_KEY}&query=${query}&language=pt-BR`
            : `${BASE_URL}/movie/popular?api_key=${API_KEY}&language=pt-BR`;

        const response = await fetch(url);
        const data = await response.json();

        renderMovies(data.results);
    } catch (error) {
        console.error("Erro ao buscar filmes:", error);
        moviesContainer.innerHTML = '<p>Erro ao carregar filmes. Tente novamente.</p>';
    } finally {
        hideLoading();
    }
}

// Função para exibir os cards na tela (RF03)
function renderMovies(movies) {
    if (movies.length === 0) {
        moviesContainer.innerHTML = '<p>Nenhum filme encontrado.</p>';
        return;
    }

    // Usando map e Template Literals para simplicidade
    moviesContainer.innerHTML = movies.map(movie => `
        <div class="movie-card" onclick="openModal('${movie.title.replace(/'/g, "\\'")}', '${movie.overview.replace(/'/g, "\\'")}')">
            <img src="${movie.poster_path ? IMG_URL + movie.poster_path : 'https://via.placeholder.com/500x750?text=Sem+Imagem'}" alt="${movie.title}">
            <div class="movie-info">
                <h3>${movie.title}</h3>
                <span class="rating">⭐ ${movie.vote_average.toFixed(1)}</span>
            </div>
        </div>
    `).join('');
}

// Funções de Loading (RF04)
function showLoading() {
    loadingText.classList.remove('hidden');
}

function hideLoading() {
    loadingText.classList.add('hidden');
}

// Função do Modal (Diferencial)
function openModal(title, overview) {
    modalTitle.innerText = title;
    modalDescription.innerText = overview || "Sinopse não disponível.";
    movieModal.showModal();
}

// Event Listeners (RF02)
searchButton.addEventListener('click', () => {
    const query = searchInput.getText(); // ERRO PROPOSITAL para o estudante aprender a ler erros no console ou usar .value
    // Correção para o exemplo:
    // searchMovies(searchInput.value);
});

// Correção do erro acima para que o código funcione de imediato no exemplo
searchButton.onclick = () => {
    searchMovies(searchInput.value);
};

closeModal.onclick = () => {
    movieModal.close();
};

// Carregar filmes populares ao iniciar
searchMovies('');
