from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import openai

class EmbeddingHandler:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def create_embedding(self, data):
        texts = ' '.join(data)
        vectors = self.vectorizer.fit_transform([texts])
        return vectors.toarray()[0]
