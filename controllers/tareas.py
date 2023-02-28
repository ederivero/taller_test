from flask_restful import Resource, request
from dtos.tareas_dto import TareaDto
from models.tareas import TareaModel
from base_de_datos import conexion

class TareaController(Resource):
    def get(self):
        # SELECT * FROM tareas
        tareas = conexion.session.query(TareaModel).all()        
        serializador = TareaDto()
        # Convierte las instancias de la clase a un diccionario o una lista de diccionarios para enviarlas al front
        resultado =serializador.dump(tareas, many=True)

        return {
            'content': resultado
        }


    def post(self):
        data = request.get_json()
        serializador = TareaDto()
        try:
            data_serializada = serializador.load(data)
            nueva_tarea = TareaModel(**data_serializada)
            conexion.session.add(nueva_tarea)
            conexion.session.commit()

            return {
                'message': 'Tarea creada exitosamente',
                'content': serializador.dump(nueva_tarea)
            }

        except Exception as e:
            return {
                'message': 'Error al crear la tarea',
                'content': e.args
            }