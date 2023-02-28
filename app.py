from flask import Flask
from flask_restful import Api
from base_de_datos import conexion
from controllers.tareas import TareaController
from os import environ
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
api = Api(app)

conexion.init_app(app)

@app.before_first_request
def inicializadora():
    conexion.create_all()


api.add_resource(TareaController, '/tareas')

if __name__ == '__main__':
    app.run(debug=True)