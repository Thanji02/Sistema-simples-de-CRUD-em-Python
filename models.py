import sqlite3

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Contato:
    id: int | None
    nome: str
    email: str
    telefone: str
    criado_em: datetime | None = None
