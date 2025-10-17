import sqlite3

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Table clients
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    adresse TEXT,
    telephone TEXT,
    email TEXT
)
""")

# Table interventions
cursor.execute("""
CREATE TABLE IF NOT EXISTS interventions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    date TEXT,
    description TEXT
)
""")

# Table devis
cursor.execute("""
CREATE TABLE IF NOT EXISTS devis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    description TEXT,
    montant REAL,
    statut TEXT
)
""")

conn.commit()
conn.close()
print("✅ Base de données initialisée avec succès.")