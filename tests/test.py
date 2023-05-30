import spacy

nlp = spacy.load('pt_core_news_lg')
texto = input("->")

doc = nlp(texto)

for token in doc:
    print(token.text, token.pos_)


"""

que SCONJ
são AUX
horas NOUN

que SCONJ
horas NOUN
são AUX

qual DET
horário NOUN
é AUX

qual DET
horário NOUN
é AUX

--temperatura--

que SCONJ
clima NOUN
está AUX
fazendo VERB

qual PRON
temperatura NOUN
está AUX
fazendo VERB

quantos DET
graus NOUN
está AUX
fazendo VERB

qual DET
o DET
tempo NOUN
em ADP
minha DET
cidade NOUN

"""