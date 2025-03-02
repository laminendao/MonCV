import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS publications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    conference TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS competences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS projets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
);
""")

# Ajout de données initiales (format tuple pour SQLite)
cursor.executemany("INSERT INTO publications (titre, conference) VALUES (?, ?)", [
    ("Enhancing Explainability in Predictive Maintenance", "FLAIRS-37, 2024"),
    ("Consensus de partitions en NLP", "SFC'2023"),
    ("Systematic review on XAI bias and fairness", "CNIA'2023"),
    ("Improving predictive maintenance", "Engineering Applications of AI, 2025")
])

cursor.executemany("INSERT INTO competences (description) VALUES (?)", [
    ("Machine Learning, Deep Learning, NLP, IA Explicable (XAI)",),
    ("Python, R, SQL, Spark, MLOps",),
    ("Analyse de données et modélisation prédictive",),
    ("DataViz, analyses descriptives, reportings, contrôle de qualité",),
    ("Collecte de données (ODK, Web Scraping)",),
    ("Modélisation supervisée et non supervisée",),
    ("Détection d’anomalies et maintenance prédictive",),
    ("Optimisation et systèmes de recommandation",)
])

cursor.executemany("INSERT INTO projets (description) VALUES (?)", [
    ("Prédiction de durée de vie des moteurs (RUL)",),
    ("Analyse NLP pour les publications sur XAI",),
    ("Détection d’anomalies en maintenance prédictive",),
    ("Optimisation des modèles d’apprentissage automatique",),
    ("Explication de modèles IA avec SHAP, LIME",)
])

# Sauvegarde et fermeture
conn.commit()
conn.close()

print("✅ Base de données initialisée avec succès !")