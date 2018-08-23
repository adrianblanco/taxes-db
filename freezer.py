from flask_frozen import Freezer
from app import app, Taxes

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def show():
    for country in Taxes.query.all():
        yield { 'index': country.index }

if __name__ == '__main__':
    freezer.freeze()
