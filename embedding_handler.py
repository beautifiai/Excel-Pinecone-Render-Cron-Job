import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import openai

class EmbeddingHandler:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_KEY')

        # Initialize OpenAI client
        openai.api_key = self.openai_key

    def create_embedding(self, data):
        """
        Uses the OpenAI API to generate text based on the data, then converts the text
        to a TF-IDF vector and returns it.
        """
        # Generate text using OpenAI API
        text = self.generate_text(data)

        # Convert text to TF-IDF vector
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([text])

        # Return the TF-IDF vector as a numpy array
        return X.toarray()[0]

    def generate_text(self, data):
        """
        Uses the OpenAI API to generate text based on the data.
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=data,
            max_tokens=60
        )

        return response.choices[0].text.strip()
