import numpy as np
import pandas as pd
import torch
from torch import nn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class NewsClassifier(nn.Module):
    def _init(self):
        super()._init_(NewsClassifier, self)    

    def forward(self, X):
        return X

    def fit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=40, test_size=0.2, shuffle=True)
        vectorizer = TfidfVectorizer(stop_words='english', max_features=100)

        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        return None
    
    def predict(self, batch):
        y_predict = batch # do something with batch here
        return y_predict

def get_model():
    return NewsClassifier()