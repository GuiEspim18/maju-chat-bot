from typing import *
from maju_thinking import MajuThinking
import datetime
from utils.hours.statements.statements import HOURS_STATEMENTS

class MajuSkills:

    maju_thinking: MajuThinking = MajuThinking()

    # Initing class
    def __init__(self, command: str) -> None:
        self.command: str = command

    # Processing the command
    def process_command(self) -> bool:
        value: str = self.command
        if "horas" in value or "horário" in value:
            RESULT: bool = self.maju_thinking.hours(self.command)
            if RESULT:
                CURRENT_HOURS: str = datetime.datetime.now().strftime('%H:%M')
                print(HOURS_STATEMENTS(CURRENT_HOURS))
                return True
            else:
                return False
