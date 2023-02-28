import pytest
from flask import Flask
from app import app 

@pytest.fixture()
def variable():
    yield 10

@pytest.fixture()
def cliente():
    yield app.test_client()


def test_prueba(variable):
    assert variable == 10


def test_listar_tareas(cliente: Flask):
    respuesta = cliente.get('/tareas')

    content = respuesta.json.get('content')

    assert 'content' in respuesta.json
    assert len(content) == 0

def test_crear_tarea(cliente: Flask):
    respuesta = cliente.post('/tareas', json= {
        'nombre': 'Montar caballo'
    })

    assert 'message' in respuesta.json
    assert respuesta.json.get('message') == 'Tarea creada exitosamente.'
    assert respuesta.status_code == 201

def test_fallo_crear_tarea(cliente: Flask):
    respuesta = cliente.post('/tareas', json= {
        'nombrecito': 'Montar caballo'
    })

    assert 'message' in respuesta.json
    assert respuesta.json.get('message') == 'Error al crear la tarea'
    assert respuesta.json.get('content')[0] == {
        'nombre': 
                ['Missing data for required field.'], 
        'nombrecito': ['Unknown field.']
        }
    assert respuesta.status_code == 400

def test_listar_tareas_nuevo(cliente: Flask):
    respuesta = cliente.get('/tareas')

    content = respuesta.json.get('content')

    assert 'content' in respuesta.json
    assert len(content) == 1