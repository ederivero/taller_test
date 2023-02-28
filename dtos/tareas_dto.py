from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.tareas import TareaModel

class TareaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = TareaModel