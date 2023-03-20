from flask import Flask, render_template

app = Flask (__name__)

lampotilat =[
    {'x':1, 'y':14},
    {'x':2, 'y':10},
    {'x':2, 'y':15}
]
paivat = ['maanantai', 'tiistai', 'keskiviikko']

@app.route('/', methods=['GET'])
def index():
    return render_template("mittaukset.html", taulukko=lampotilat, paivat=paivat)






if __name__ ==  "__main__":
    app.run(debug=True)
