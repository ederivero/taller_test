from base_de_datos import conexion
from sqlalchemy import Column, types

class TareaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(40), nullable=False)
    habilitado = Column(type_=types.Boolean, default= True)

    __tablename__='tareas'