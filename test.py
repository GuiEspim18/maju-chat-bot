import spacy

nlp = spacy.load('pt_core_news_sm')
texto = input("->")

doc = nlp(texto)

for token in doc:
    print(token.text, token.pos_)

