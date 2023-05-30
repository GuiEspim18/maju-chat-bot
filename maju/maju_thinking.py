import spacy

from utils.hours.hours_adj import HOURS_ADJ
from utils.hours.hours_adp import HOURS_ADP
from utils.hours.hours_adv import HOURS_ADV
from utils.hours.hours_aux import HOURS_AUX
from utils.hours.hours_det import HOURS_DET
from utils.hours.hours_noun import HOURS_NOUN
from utils.hours.hours_pron import HOURS_PRON
from utils.hours.hours_sconj import HOURS_SCONJ
from utils.hours.hours_verb import HOURS_VERB
from utils.hours.type.hours_types import HOURS_TYPES

from utils.temperature.temp_adj import TEMP_ADJ
from utils.temperature.temp_adp import TEMP_ADP
from utils.temperature.temp_adv import TEMP_ADV
from utils.temperature.temp_aux import TEMP_AUX
from utils.temperature.temp_det import TEMP_DET
from utils.temperature.temp_noun import TEMP_NOUN
from utils.temperature.temp_pron import TEMP_PRON
from utils.temperature.temp_sconj import TEMP_SCONJ
from utils.temperature.temp_verb import TEMP_VERB
from utils.temperature.type.temp_types import TEMP_TYPES

from utils.punct import PUNCT

# types
from spacy import Language
from typing import *

class MajuThinking:

    # Vars
    PUNCT: list[str] = PUNCT

    # Initting the class
    def __init__(self) -> None:
        pass
    
    # Identificationg if the statement makes sense in hours skill
    def hours(self, command: str) -> bool:
        nlp: Language = spacy.load("pt_core_news_sm")
        doc = nlp(command)
        neural: list[bool] = []
        for token in doc:
            if str(token) not in self.PUNCT and str(token).lower() != "maju": 
                neural.append(self.__hours_nlp(str(token.pos_), str(token)))
        if False in neural: 
            return False
        else:
            return True

    # Checking word per word
    def __hours_nlp(self, pos: str, token: str) -> bool:
        ALL_WORDS: dict[str, list[str]] = {
           "adj": HOURS_ADJ,
            "adp": HOURS_ADP,
            "adv": HOURS_ADV,
            "aux": HOURS_AUX,
            "det": HOURS_DET,
            "noun": HOURS_NOUN,
            "pron": HOURS_PRON,
            "sconj": HOURS_SCONJ,
            "verb": HOURS_VERB
        }
        TYPES: list[str] = HOURS_TYPES
        neural: bool = False
        for i in range(len(TYPES)):
            if TYPES[i] == pos:
                index: str = TYPES[i].lower()
                words = ALL_WORDS[index]
                neural = token in words
        return neural
    
    # Identificationg if the statement makes sense in temperature skill
    def temperature(self, command: str) -> bool:
        nlp: Language = spacy.load("pt_core_news_sm")
        doc: spacy.tokens.doc.Doc = nlp(command)
        neural: list[bool] = []
        for token in doc:
            if str(token) not in self.PUNCT and str(token).lower() != "maju": 
                neural.append(self.__temp_nlp(str(token.pos_), str(token)))
        self.__correct_statement(doc, neural)
        if False in neural: 
            return False
        else:
            return True
        
    def __correct_statement(self, value: spacy.tokens.doc.Doc, neural: list[bool]) -> None:
        statement: str = ""
        cond: list = []
        if neural[-1] == False: 
            del(neural[-1])
            statement = str(value).replace(str(value[-1]), "")
            cond.append(True)
        if neural[0] == False: 
            del(neural[0])
            statement = str(value).replace(str(value[0]), "")
            cond.append(True)
        if True in cond: print(f"Você quis dizer: {statement[1:]}?")

    def __temp_nlp(self, pos, token) -> bool:
        ALL_WORDS: dict[str, list[str]] = {
           "adj": TEMP_ADJ,
            "adp": TEMP_ADP,
            "adv": TEMP_ADV,
            "aux": TEMP_AUX,
            "det": TEMP_DET,
            "noun": TEMP_NOUN,
            "pron": TEMP_PRON,
            "sconj": TEMP_SCONJ,
            "verb": TEMP_VERB
        }
        TYPES: list[str] = TEMP_TYPES
        neural: bool = False
        for i in range(len(TYPES)):
            if TYPES[i] == pos:
                index: str = TYPES[i].lower()
                words = ALL_WORDS[index]
                neural = token in words
        return neural