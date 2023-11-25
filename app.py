from flask import Flask, send_from_directory
from controllers.home import home
from config.config import Config_Dev
from sqlalchemy import create_engine
from config.db import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config_Dev)
db.init_app(app)
migrate = Migrate(app, db)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Configurar la ruta estática para archivos CSS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

# Configurar la ruta estática para archivos de imágenes
@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

# Configurar la ruta estática para archivos Js
@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

app.register_blueprint(home)