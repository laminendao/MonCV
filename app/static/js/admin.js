document.addEventListener("DOMContentLoaded", function () {
    chargerPublications();
    chargerCompetences();
    chargerProjets();
});

/** 🔍 CHARGER LES PUBLICATIONS **/
function chargerPublications() {
    fetch("http://127.0.0.1:5000/api/publications")
        .then(response => response.json())
        .then(data => {
            let liste = document.getElementById("publication-list");
            liste.innerHTML = "";
            data.forEach(pub => {
                let li = document.createElement("li");
                li.innerHTML = `${pub.titre} - ${pub.conference} 
                    <button onclick="supprimerPublication(${pub.id})">❌</button>`;
                liste.appendChild(li);
            });
        });
}

/** ➕ AJOUTER UNE PUBLICATION **/
function ajouterPublication() {
    let titre = document.getElementById("titre").value;
    let conference = document.getElementById("conference").value;

    fetch("http://127.0.0.1:5000/api/publications", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titre: titre, conference: conference })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById("titre").value = "";
        document.getElementById("conference").value = "";
        chargerPublications();
    });
}

/** ❌ SUPPRIMER UNE PUBLICATION **/
function supprimerPublication(id) {
    fetch(`http://127.0.0.1:5000/api/publications/${id}`, { method: "DELETE" })
    .then(() => chargerPublications());
}

/** 🔍 CHARGER LES COMPÉTENCES **/
function chargerCompetences() {
    fetch("http://127.0.0.1:5000/api/competences")
        .then(response => response.json())
        .then(data => {
            let liste = document.getElementById("competence-list");
            liste.innerHTML = "";
            data.forEach(comp => {
                let li = document.createElement("li");
                li.innerHTML = `${comp.description} 
                    <button onclick="supprimerCompetence(${comp.id})">❌</button>`;
                liste.appendChild(li);
            });
        });
}

/** ➕ AJOUTER UNE COMPÉTENCE **/
function ajouterCompetence() {
    let competence = document.getElementById("competence").value;

    fetch("http://127.0.0.1:5000/api/competences", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description: competence })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById("competence").value = "";
        chargerCompetences();
    });
}

/** ❌ SUPPRIMER UNE COMPÉTENCE **/
function supprimerCompetence(id) {
    fetch(`http://127.0.0.1:5000/api/competences/${id}`, { method: "DELETE" })
    .then(() => chargerCompetences());
}

/** 🔍 CHARGER LES PROJETS **/
function chargerProjets() {
    fetch("http://127.0.0.1:5000/api/projets")
        .then(response => response.json())
        .then(data => {
            let liste = document.getElementById("projet-list");
            liste.innerHTML = "";
            data.forEach(proj => {
                let li = document.createElement("li");
                li.innerHTML = `${proj.description} 
                    <button onclick="supprimerProjet(${proj.id})">❌</button>`;
                liste.appendChild(li);
            });
        });
}

/** ➕ AJOUTER UN PROJET **/
function ajouterProjet() {
    let projet = document.getElementById("projet").value;

    fetch("http://127.0.0.1:5000/api/projets", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description: projet })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById("projet").value = "";
        chargerProjets();
    });
}

/** ❌ SUPPRIMER UN PROJET **/
function supprimerProjet(id) {
    fetch(`http://127.0.0.1:5000/api/projets/${id}`, { method: "DELETE" })
    .then(() => chargerProjets());
}
