import nltk
nltk.download('punkt')
nltk.download('floresta')

def verifica_frase(frase):
    palavras = nltk.word_tokenize(frase, language='portuguese')
    for palavra in palavras:
        if palavra.lower() not in nltk.corpus.floresta.words():
            return False
    return True

frase = "Esta é uma frase de exemplo"
if verifica_frase(frase):
    print("A frase é válida.")
else:
    print("A frase contém palavras inválidas.")
