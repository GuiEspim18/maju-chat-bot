import spacy
from spacy import Language
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
from utils.punct import PUNCT

class MajuThinking:

    # Vars
    PUNCT: list[str] = PUNCT

    # Initting the class
    def __init__(self) -> None:
        pass
    
    # Identificationg if the statement makes sense
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
    def __hours_nlp(self, pos, token) -> bool:
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