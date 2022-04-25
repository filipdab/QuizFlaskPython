from flask import Flask, request, redirect, url_for, flash
from  flask import  render_template
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzotajnawartosc',
))

DANE = [{
    'pytanie': 'Stolica Haiszpani to:',
    'odpowiedzi': ['Madryt', 'Warszawa', 'Berlin'],
    'odpok' : 'Madryt'},
{
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', 18],
    'odpok': '216'},
{
    'pytanie': 'Symbol pierwiastka Helu to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'
},]

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1
        flash('Liczba poprawnych odpowiedzi to: {0}'.format(punkty))
    return render_template('index.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)
