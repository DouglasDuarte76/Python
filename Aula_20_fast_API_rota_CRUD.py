# Passo 1: Instalar FastAPI e Uvicorn
pip install fastapi uvicorn

# Passo 2: Criar uma aplicação FastAPI com rotas CRUD
echo "
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str = None
    completa: bool = False

tarefas = []

@app.post('/tarefas/', response_model=Tarefa)
async def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return tarefa

@app.get('/tarefas/', response_model=List[Tarefa])
async def listar_tarefas():
    return tarefas

@app.get('/tarefas/{tarefa_id}', response_model=Tarefa)
async def obter_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
    raise HTTPException(status_code=404, detail='Tarefa não encontrada')

@app.put('/tarefas/{tarefa_id}', response_model=Tarefa)
async def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            tarefas[i] = tarefa_atualizada
            return tarefa_atualizada
    raise HTTPException(status_code=404, detail='Tarefa não encontrada')

@app.delete('/tarefas/{tarefa_id}')
async def deletar_tarefa(tarefa_id: int):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[i]
            return {"message": "Tarefa deletada"}
    raise HTTPException(status_code=404, detail='Tarefa não encontrada')
" > main.py

# Passo 4: Executar a API com Uvicorn
uvicorn main:app --reload

# Passo 5: Acessar Swagger UI em http://127.0.0.1:8000/docs para testar as operações CRUD
