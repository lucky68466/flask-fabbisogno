from flask import Flask, render_template, request

app = Flask(__name__)

def calcola_fabbisogno(peso, altezza, eta, genere, attivita):
    # Calcolo del metabolismo basale (BMR)
    if genere == "maschio":
        bmr = 88.36 + (13.4 * peso) + (4.8 * altezza) - (5.7 * eta)
    else:
        bmr = 447.6 + (9.2 * peso) + (3.1 * altezza) - (4.3 * eta)
    
    # Fabbisogno calorico totale
    fabbisogno = bmr * attivita
    return round(fabbisogno, 2)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        peso = float(request.form["peso"])
        altezza = float(request.form["altezza"])
        eta = int(request.form["eta"])
        genere = request.form["genere"]
        attivita = float(request.form["attivita"])

        risultato = calcola_fabbisogno(peso, altezza, eta, genere, attivita)
        return render_template("index.html", risultato=risultato)

    return render_template("index.html", risultato=None)

if __name__ == "__main__":
    app.run(debug=True)
