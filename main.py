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
