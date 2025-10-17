from flask import Flask, render_template, request, redirect, jsonify
from database import (
    get_clients,
    get_client_by_id,
    ajouter_client,
    ajouter_intervention,
    get_interventions_by_client,
    get_devis_by_client
)

app = Flask(__name__)

# 🏠 Page d'accueil
@app.route('/accueil')
def accueil():
    return render_template("accueil.html")

# 📊 Tableau de bord
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# 👥 Liste des clients
@app.route('/clients')
def clients():
    clients = get_clients()
    return render_template("clients.html", clients=clients)

# 📁 Fiche client
@app.route('/client/<int:client_id>')
def fiche_client(client_id):
    client = get_client_by_id(client_id)
    client['devis'] = get_devis_by_client(client_id)
    return render_template("client.html", client=client)

# ➕ Ajouter un nouveau client
@app.route('/nouveau-client', methods=['GET', 'POST'])
def nouveau_client():
    if request.method == 'POST':
        nom = request.form['nom']
        adresse = request.form['adresse']
        telephone = request.form['telephone']
        email = request.form['email']
        ajouter_client(nom, adresse, telephone, email)
        return redirect('/clients')
    return render_template("nouveau_client.html")

# 🛠️ Ajouter une intervention
@app.route('/ajouter-intervention/<int:client_id>', methods=['GET', 'POST'])
def ajouter_intervention_route(client_id):
    client = get_client_by_id(client_id)
    if request.method == 'POST':
        date = request.form['date']
        description = request.form['description']
        ajouter_intervention(client_id, date, description)
        return redirect(f'/client/{client_id}')
    return render_template("ajouter_intervention.html", client=client)

# 📅 Planning des interventions
@app.route('/calendrier')
def calendrier():
    return render_template("calendrier.html")

# 📡 API JSON pour FullCalendar
@app.route('/api/events')
def api_events():
    all_clients = get_clients()
    events = []

    for client in all_clients:
        interventions = get_interventions_by_client(client['id'])
        for intervention in interventions:
            events.append({
                "title": f"Intervention - {client['nom']}",
                "start": intervention['date'],  # Format YYYY-MM-DD
                "description": intervention['description']
            })

    return jsonify(events)

# 🚀 Lancement de l'app (debug désactivé pour Render)
if __name__ == '__main__':
    app.run()