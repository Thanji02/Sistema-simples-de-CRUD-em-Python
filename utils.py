import re

EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

def email_valido(email: str) -> bool:
    return bool(EMAIL_RE.match(email))

def telefone_valido(telefone: str) -> bool:
    digitos = ''.join(ch for ch in telefone if ch.isdigit())
    return 8 <= len(digitos) <= 15