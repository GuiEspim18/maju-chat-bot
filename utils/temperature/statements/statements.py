import random

def TEMP_STATEMENTS(temp, location) -> str:
    STATEMENTS: list[str] = [
        f"Em {location} faz {temp}.",
        f"Estão fazendo {temp} em {location}.",
        f"O termômetro marca {temp} em {location}.",
        f"Está {temp} em {location}.",
        f"Marcando {temp} em {location}.",
        f"A temperatura exata é {temp} em {location}.",
        f"Está fazendo {temp} em {location}.",
    ]
    STATEMENT: str = random.choice(STATEMENTS)
    return STATEMENT