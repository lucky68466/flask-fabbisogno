from flask import Flask, render_template, request

app = Flask(__name__)

def calcola_fabbisogno(peso, altezza, eta, genere, attivita):
    if genere == "Maschio":
        bmr = 88.36 + (13.4 * peso) + (4.8 * altezza) - (5.7 * eta)
    else:
        bmr = 447.6 + (9.2 * peso) + (3.1 * altezza) - (4.3 * eta)
    
    livelli_attivita = {
        "Sedentario": 1.2,
        "Leggermente attivo": 1.375,
        "Moderatamente attivo": 1.55,
        "Molto attivo": 1.725,
        "Estremamente attivo": 1.9
    }
    
    tdee = bmr * livelli_attivita[attivita]
    return round(tdee, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    risultato = None
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altezza = float(request.form['altezza'])
            eta = int(request.form['eta'])
            genere = request.form['genere']
            attivita = request.form['attivita']
            risultato = calcola_fabbisogno(peso, altezza, eta, genere, attivita)
        except ValueError:
            risultato = "Errore nei dati inseriti."
    return render_template('index.html', risultato=risultato)

if __name__ == '__main__':
    app.run(debug=True)


