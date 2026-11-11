from http import HTTPStatus

from fastapi.testclient import TestClient

from fastzero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Olá Mundo!"}

def test_mensagem_html_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    resposta = client.get('/mensagem')
    assert resposta.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in resposta.text
