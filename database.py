import sqlite3

def get_clients():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, adresse, telephone, email FROM clients")
    rows = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'nom': r[1], 'adresse': r[2], 'telephone': r[3], 'email': r[4]} for r in rows]

def get_client_by_id(client_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, adresse, telephone, email FROM clients WHERE id = ?", (client_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'nom': row[1],
            'adresse': row[2],
            'telephone': row[3],
            'email': row[4]
        }
    return None

def ajouter_client(nom, adresse, telephone, email):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (nom, adresse, telephone, email) VALUES (?, ?, ?, ?)",
                   (nom, adresse, telephone, email))
    conn.commit()
    conn.close()

def ajouter_intervention(client_id, date, description):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO interventions (client_id, date, description) VALUES (?, ?, ?)",
                   (client_id, date, description))
    conn.commit()
    conn.close()

def get_interventions_by_client(client_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date, description FROM interventions WHERE client_id = ?", (client_id,))
    rows = cursor.fetchall()
    conn.close()
    return [{'date': r[0], 'description': r[1]} for r in rows]

def get_devis_by_client(client_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT description, montant, statut FROM devis WHERE client_id = ?", (client_id,))
    rows = cursor.fetchall()
    conn.close()
    return [{'description': r[0], 'montant': r[1], 'statut': r[2]} for r in rows]