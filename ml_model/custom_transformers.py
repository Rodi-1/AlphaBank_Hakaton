# custom_transformers.py

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd

class MultiLabelBinarizerTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mlb = MultiLabelBinarizer()

    def fit(self, X, y=None):
        self.mlb.fit(X['availableMethods'])
        return self

    def transform(self, X):
        available_methods_encoded = self.mlb.transform(X['availableMethods'])
        available_methods_df = pd.DataFrame(
            available_methods_encoded,
            columns=['available_' + method for method in self.mlb.classes_],
            index=X.index
        )
        X = X.reset_index(drop=True).join(available_methods_df.reset_index(drop=True))
        X = X.drop(columns=['availableMethods'])
        return X
