from utils.hours.questions.hours_questions import HOUR_QUESTIONS
from utils.temperature.questions.temp_questions import TEMP_QUESTIONS

# types
from typing import *

QUESTIONS: dict[str, dict[str, Any]] = {
    "hours": {
        "questions": HOUR_QUESTIONS,
        "variation": ["SCONJ NOUN AUX", "DET NOUN AUX"]
    },
    "temp": {
        "questions": TEMP_QUESTIONS,
        "variation": ["SCONJ NOUN AUX", "DET NOUN AUX", "PRON NOUN AUX"]
    },
}