from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastzero.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}

@app.get("/mensagem", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def mensagemHTML():
    return """
    <html>
      <head>
        <title> Olá mundo em HTML </title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""