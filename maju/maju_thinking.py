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

from utils.questions.questions import QUESTIONS

from utils.punct import PUNCT

import openai

# types
from spacy import Language
from typing import *

class MajuThinking:

    # Vars
    PUNCT: list[str] = PUNCT
    QUESTS: dict[str, dict[str, Any]] = QUESTIONS

    # Initting the class
    def __init__(self) -> None:
        pass
    
    # Identificationg if the statement makes sense in hours skill
    def hours(self, command: str) -> bool:
        # initializing nlp
        nlp: Language = spacy.load("pt_core_news_sm")
        doc: spacy.tokens.doc.Doc = nlp(command)
        neural: list[bool] = []    
        for token in range(len(doc)):
            pos = doc[token].pos_
            word = doc[token]
            if str(word) not in self.PUNCT and str(word).lower() != "maju": 
                # appending the result of the words
                neural.append(self.__hours_nlp(str(pos), str(word)))
        return self.__check_if_correct(neural, doc)

    # Checking word per word of hours
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
        # initializing nlp
        nlp: Language = spacy.load("pt_core_news_sm")
        doc: spacy.tokens.doc.Doc = nlp(command)
        neural: list[bool] = []
        for token in range(len(doc)):
            pos = doc[token].pos_
            word = doc[token]
            if str(word) not in self.PUNCT and str(word).lower() != "maju": 
                # appending the result of the words
                neural.append(self.__temp_nlp(str(pos), str(word)))
        return self.__check_if_correct(neural, doc)
        
    # Correcting statement that was written wrong
    def __correct_statement(self, value: spacy.tokens.doc.Doc, neural: list[bool]) -> None:
        statement: str = ""
        cond: list = []
        for i in range(len(neural)):
            if neural[i] == True:
                if i != 0:
                    statement += f" {str(value[i])}"
                else:
                    statement += str(value[i])
            else:
                cond.append(True)
        if True in cond: print(f"Você quis dizer: {statement}?")

    # Checking word per word of temperature
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
    
    # Checking if the statement make sense and can be understand
    def __check_if_correct(self, neural: list[bool], doc: spacy.tokens.doc.Doc) -> bool:
        TRUE_NUM: int = neural.count(True)
        FALSE_NUM: int = neural.count(False)
        if False in neural and ((FALSE_NUM > TRUE_NUM) or (FALSE_NUM >= 2)): 
            return False
        else:
            self.__correct_statement(doc, neural)
            return False
        
    def __consult_gpt(self, value, context) -> bool:
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": value},
                ]
        )
        result = '' 
        for choice in response.choices:
            result += choice.message.content
        print(result)
        if result.find("True") == -1:
            return False
        return True