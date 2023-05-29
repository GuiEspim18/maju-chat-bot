from typing import *
from maju.maju_thinking import MajuThinking
import datetime
from utils.hours.statements.statements import HOURS_STATEMENTS
from utils.hours.hours_principal_noun import HOURS_PRINCIPAL_NOUN

class MajuSkills:

    # Vars
    MAJU_THINKING: MajuThinking = MajuThinking()

    # Initing class
    def __init__(self, command: str) -> None:
        self.command: str = command

    # Processing the command
    def process_command(self) -> bool:
        value: str = self.command
        if self.__check_hour(value):
            RESULT: bool = self.MAJU_THINKING.hours(self.command)
            if RESULT:
                CURRENT_HOURS: str = datetime.datetime.now().strftime('%H:%M')
                print(HOURS_STATEMENTS(CURRENT_HOURS))
                return True
            else:
                return False

    # Checking if in the statement contains the words related in hours request   
    def __check_hour(self, value: str) -> bool:
        for i in HOURS_PRINCIPAL_NOUN:
            if i in value: 
                return True
        return False
