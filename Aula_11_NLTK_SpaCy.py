pip install nltk spacy

_______________________________________________

python -m spacy download en_core_web_sm

_______________________________________________

import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

# Carregar o modelo de linguagem do SpaCy
nlp = spacy.load('en_core_web_sm')

_______________________________________________

texto = "Natural Language Processing with Python is interesting and challenging."
palavras = word_tokenize(texto)
print("Tokenização:", palavras)

_______________________________________________

stop_words = set(stopwords.words('english'))
palavras_filtradas = [palavra for palavra in palavras if not palavra.lower() in stop_words]
print("Após remoção de Stop Words:", palavras_filtradas)

_______________________________________________

doc = nlp(" ".join(palavras_filtradas))
lematizado = [token.lemma_ for token in doc]
print("Lematização:", lematizado)

_______________________________________________

from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()
sentimento = sia.polarity_scores(texto)
print("Análise de Sentimentos:", sentimento)

_______________________________________________


