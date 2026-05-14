# Import do FastAPI e HTTPException para tratar requisições
from fastapi import FastAPI, HTTPException

# Definição do modelo de dados usando Pydantic
from pydantic import BaseModel

# Ajuda na tipagem de dados, como listas e valores opcionais
from typing import List, Optional

# Criação da aplicação FastAPI
app = FastAPI(title="API de Gerenciamento de Tarefas", description="Uma API simples para gerenciar tarefas", version="1.0.0")

# Modelo de dados
class Task(BaseModel):
    id: Optional[int] = None # ID opcional, será gerado automaticamente
    titulo: str
    descricao: str
    concluida: bool = False

# Banco em memória para armazenar as tarefas
db_tasks = []

# Rota para listar todas as tarefas
@app.get("/tarefas", response_model=List[Task])
async def list_tasks():
    return db_tasks

# Rota para criar nova tarefa
@app.post("/tarefas", response_model=Task, status_code=201)
async def create_task(task: Task):
    task.id = len(db_tasks) + 1 # Gerar ID automático
    db_tasks.append(task)
    return task

# Buscar tarefa por ID
@app.get("/tarefas/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for t in db_tasks:
        if t.id == task_id:
            return t
    """
    Se use exceção para retornar um erro 404 personalizado, não se deve deixar o erro que
    acontece no seu servidor aparecer na resposta, pois isso pode expor detalhes do código ou
    ambiente do projeto
    """
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para alterar tarefa
@app.put("/tarefas/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    for id, t in enumerate(db_tasks):
        if t.id == task_id:
            db_tasks[id] = task
            return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para deletar tarefa
@app.delete("/tarefas/{task_id}", status_code=204)
async def delete_task(task_id: int):
    for t in enumerate(db_tasks):
        if t.id == task_id:
            db_tasks.remove(t)
            return
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")