document.addEventListener("DOMContentLoaded", function () {
    // Fonction pour récupérer les données de l'API
    function fetchData(endpoint, elementId, formatItem) {
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                let listElement = document.getElementById(elementId);
                listElement.innerHTML = "";
                data.forEach(item => {
                    let li = document.createElement("li");
                    li.innerHTML = formatItem(item);
                    listElement.appendChild(li);
                });
            })
            .catch(error => console.error("Erreur API :", error));
    }

    // Chargement des sections dynamiquement
    fetchData("http://127.0.0.1:5000/api/publications", "publication-list", 
              item => `<strong>${item.titre}</strong> - ${item.conference}`);
    
    fetchData("http://127.0.0.1:5000/api/competences", "competence-list", 
              item => `${item.description}`);
    
    fetchData("http://127.0.0.1:5000/api/projets", "projet-list", 
              item => `${item.description}`);
});
