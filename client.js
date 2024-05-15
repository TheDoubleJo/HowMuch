const axios = require('axios');

// Informations d'authentification
const username = 'doublejo';
const password = '**********';

// Définir les identifiants du budget et de la catégorie
const budgetId = '**********';
const categoryId = '**********';

// URL de l'API
const apiUrl = 'https://howmuch.duckdns.org/';

// Endpoint pour obtenir le token
const tokenEndpoint = 'token';

// Endpoint à appeler
const endpoint = `left-in-budget/${budgetId}/${categoryId}`;

// Fonction pour obtenir le token d'authentification
async function getToken() {
    try {
        const headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        };

        // Effectuer une requête POST pour obtenir le token
        const response = await axios.post(apiUrl + tokenEndpoint, {
            grant_type: "password",
            username: username,
            password: password
        }, { headers: headers });

        // Récupérer le token depuis la réponse
        const token = response.data.access_token;

        // Retourner le token
        return token;
    } catch (error) {
        // En cas d'erreur, afficher l'erreur
        console.error('Une erreur s\'est produite lors de l\'obtention du token:', error.message);
        console.error(error);
        throw error;
    }
}

// Fonction pour effectuer la requête REST avec le token d'authentification
async function makeRequest() {
    try {
        // Obtenir le token
        const token = await getToken();

        // Configuration des en-têtes avec le token d'authentification
        const headers = {
            'Authorization': `Bearer ${token}`
        };

        // Effectuer la requête GET à l'endpoint spécifié avec les en-têtes d'authentification
        const response = await axios.get(apiUrl + endpoint, { headers });

        // Afficher la réponse
        console.log('Réponse de l\'API:', response.data);
    } catch (error) {
        // En cas d'erreur, afficher l'erreur
        console.error('Une erreur s\'est produite lors de la requête:', error.message);
    }
}

// Appeler la fonction pour effectuer la requête
makeRequest();

