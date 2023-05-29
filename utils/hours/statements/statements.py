import random

def HOURS_STATEMENTS(hours) -> str:
    STATEMENTS: list[str] = [
        f"Agora são {hours}.",
        f"São exatamente {hours}.",
        f"O relógio marca {hours}.",
        f"A hora certa é {hours}.",
        f"Marcando {hours} no relógio.",
        f"A hora exata é {hours}.",
        f"Tempo de horas é {hours}.",
    ]
    STATEMENT: str = random.choice(STATEMENTS)
    return STATEMENT