from maju.maju_thinking import MajuThinking
import datetime
from utils.hours.statements.statements import HOURS_STATEMENTS
from utils.hours.hours_principal_noun import HOURS_PRINCIPAL_NOUN
from utils.temperature.statements.statements import TEMP_STATEMENTS
from utils.temperature.temp_principal_noun import TEMP_PRINCIPAL_NOUN

import geocoder
from bs4 import BeautifulSoup
import requests

# typing
from requests import Response
from typing import *
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
        elif self.__check_temp(value):
            RESULT: bool = self.MAJU_THINKING.temperature(self.command)
            if RESULT:
                HEADERS: dict[str, str] = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
                CITY: str = self.__get_current_location()
                CURRENT_LOCATION: str = f"{CITY} weather"
                TEMP: str = self.__get_weather(CURRENT_LOCATION, HEADERS)
                print(TEMP_STATEMENTS(TEMP, CITY))
                return True
            else:
                return False
        else: 
            return False

    # Checking if in the statement contains the words related in hours request   
    def __check_hour(self, value: str) -> bool:
        for i in HOURS_PRINCIPAL_NOUN:
            if i in value: 
                return True
        return False
    
    # Checking if in the statement contains the words related in temp request
    def __check_temp(self, value: str) -> bool:
        for i in TEMP_PRINCIPAL_NOUN:
            if i in value:
                return True
        return False
    
    # Getting the current wheater with the current location
    def __get_weather(self, value: str, headers: dict[str, str]) -> str:
        CITY: str = value.replace(" ","+")
        RES: Response = requests.get(f'https://www.google.com/search?q={CITY}&oq={CITY}'f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='f'chrome&ie=UTF-8',headers=headers)
        SOUP: BeautifulSoup = BeautifulSoup(RES.text,'html.parser')
        STATEMENT: str = SOUP.select('.BNeawe.iBp4i.AP7Wnd')[1].getText()
        return STATEMENT
    
    # Getting the current location
    def __get_current_location(self)-> str:
        LOCATION: Any = geocoder.ip('me')
        return LOCATION

