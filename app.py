from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes depuis le frontend
@app.route('/')
def home():
    return "<h1>Bienvenue sur l'API de gestion du CV !</h1><p>Accédez aux données via les routes : /api/publications, /api/competences, /api/projets.</p>"

from flask import Flask, jsonify, request, session
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes depuis le frontend

app.secret_key = "secret123"  # Clé secrète pour gérer les sessions

# Vérifier l'authentification
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "password123":  # Remplace par tes infos
        session['logged_in'] = True
        return jsonify({"message": "Connexion réussie"}), 200
    else:
        return jsonify({"message": "Identifiants incorrects"}), 401

# Vérifier si l'utilisateur est connecté
@app.route('/api/check-auth', methods=['GET'])
def check_auth():
    if 'logged_in' in session:
        return jsonify({"authenticated": True})
    return jsonify({"authenticated": False})

# Déconnexion
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return jsonify({"message": "Déconnexion réussie"}), 200



# Fonction pour exécuter des requêtes SQL
def execute_query(query, params=()):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Fonction pour récupérer les données
def fetch_data(query, params=()):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data

### 🔍 ROUTES GET : Récupération des données ###
@app.route('/api/publications', methods=['GET'])
def get_publications():
    publications = fetch_data("SELECT id, titre, conference FROM publications")
    return jsonify([{"id": p[0], "titre": p[1], "conference": p[2]} for p in publications])

@app.route('/api/competences', methods=['GET'])
def get_competences():
    competences = fetch_data("SELECT id, description FROM competences")
    return jsonify([{"id": c[0], "description": c[1]} for c in competences])

@app.route('/api/projets', methods=['GET'])
def get_projets():
    projets = fetch_data("SELECT id, description FROM projets")
    return jsonify([{"id": p[0], "description": p[1]} for p in projets])

### ✍️ ROUTES POST : Ajouter ###
@app.route('/api/publications', methods=['POST'])
def add_publication():
    data = request.json
    execute_query("INSERT INTO publications (titre, conference) VALUES (?, ?)", (data['titre'], data['conference']))
    return jsonify({"message": "Publication ajoutée avec succès"}), 201

@app.route('/api/competences', methods=['POST'])
def add_competence():
    data = request.json
    execute_query("INSERT INTO competences (description) VALUES (?)", (data['description'],))
    return jsonify({"message": "Compétence ajoutée avec succès"}), 201

@app.route('/api/projets', methods=['POST'])
def add_projet():
    data = request.json
    execute_query("INSERT INTO projets (description) VALUES (?)", (data['description'],))
    return jsonify({"message": "Projet ajouté avec succès"}), 201

### ✏ ROUTES PUT : Modifier ###
@app.route('/api/publications/<int:id>', methods=['PUT'])
def update_publication(id):
    data = request.json
    execute_query("UPDATE publications SET titre = ?, conference = ? WHERE id = ?", (data['titre'], data['conference'], id))
    return jsonify({"message": "Publication mise à jour"}), 200

@app.route('/api/competences/<int:id>', methods=['PUT'])
def update_competence(id):
    data = request.json
    execute_query("UPDATE competences SET description = ? WHERE id = ?", (data['description'], id))
    return jsonify({"message": "Compétence mise à jour"}), 200

@app.route('/api/projets/<int:id>', methods=['PUT'])
def update_projet(id):
    data = request.json
    execute_query("UPDATE projets SET description = ? WHERE id = ?", (data['description'], id))
    return jsonify({"message": "Projet mis à jour"}), 200

### ❌ ROUTES DELETE : Supprimer ###
@app.route('/api/publications/<int:id>', methods=['DELETE'])
def delete_publication(id):
    execute_query("DELETE FROM publications WHERE id = ?", (id,))
    return jsonify({"message": "Publication supprimée"}), 200

@app.route('/api/competences/<int:id>', methods=['DELETE'])
def delete_competence(id):
    execute_query("DELETE FROM competences WHERE id = ?", (id,))
    return jsonify({"message": "Compétence supprimée"}), 200

@app.route('/api/projets/<int:id>', methods=['DELETE'])
def delete_projet(id):
    execute_query("DELETE FROM projets WHERE id = ?", (id,))
    return jsonify({"message": "Projet supprimé"}), 200

if __name__ == '__main__':
    app.run(debug=True)
