# -*- coding: utf-8 -*-
"""data_preprocessing.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pX4TwDlqy1yHnpteTLlqHQ_Lt3ofm9tI
"""

import pandas as pd

def clean_text(text):
    # Implement text cleaning
    # Remove '\n' from each word in the dataset
    questions = [word.replace('\n', '') for word in questions]
    questions = pd.Series(questions)
    return questions


def tokenize(text):

  tokenized_docs = [word_tokenize(doc.lower()) for doc in questions]

  return tokenized_docs


def sample(text, n):
  text_sample = reindexed_summary.sample(n=n, random_state=42).values
  return text_sample

def perform_eda(dataframe):
    # Implement exploratory data analysis
    pass

def vectorize_text(data, vectorizer_type='count', max_features=10000):

    if vectorizer_type == 'count':
        vectorizer = CountVectorizer(stop_words='english', max_features=max_features)
    elif vectorizer_type == 'tfidf':
      vectorizer = TfidfVectorizer(stopwords='english', max_features = max_features)
    else:
      raise ValueError('Invalid vectorizer type. Choose count or tfidf')

    vectorized_data = vectorizer.fit_transform(data)
    return vectorized_data, vectorizer