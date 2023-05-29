from maju_skills import MajuSkills
from utils.erros.statements.statements import ERROS_STATEMENTS
from utils.goodbye.statements.statements import GOOD_BYE_STATEMENTS
import random
import os

class Maju:

    # Initing class
    def __init__(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_home()
        pass

    # Print home message
    def print_home(self) -> None:
        print("Olá eu sou a Maju!")
        self.__start()

    # Start scripts
    def __start(self) -> None:
        QUEST: str = self.input()
        self.process(QUEST)

    def __input(self) -> str:
        return input("-> ").lower()
    
    def process(self, value: str) -> None:
        try:
            while "tchau" not in value:
                if len(value) > 0:
                    SKILLS: bool = MajuSkills(value).process_command()
                    if not SKILLS: 
                        STATEMENT: str = random.choice(ERROS_STATEMENTS)
                        raise ValueError(STATEMENT)
                    value = self.__input()
                else:
                    raise ValueError("Por favor digite alguma coisa!")
            GOOD_BYE: str = random.choice(GOOD_BYE_STATEMENTS)
            print(GOOD_BYE)
        except ValueError as err:
            print(err)
            self.__start()

    def goodbye(self) -> None:
        GOOD_BYE: str = random.choice(GOOD_BYE_STATEMENTS)
        print(GOOD_BYE)

    

Maju()