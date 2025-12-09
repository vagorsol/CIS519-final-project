import numpy as np
import pandas as pd
import torch
from torch import nn
from sklearn.model_selection import train_test_split

class NewsClassifier(nn.Module):
    def _init(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
    
    def eval(self):
        return None
    
    def predict(self, batch):
        return None

    
def get_model():
    return NewsClassifier()