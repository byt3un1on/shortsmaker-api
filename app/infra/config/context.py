from contextvars import ContextVar
from typing import Optional

from sqlmodel import Session

# Variável de contexto para armazenar a sessão do banco de dados por requisição
db_session_context: ContextVar[Optional[Session]] = ContextVar(
    "db_session_context", default=None
)
