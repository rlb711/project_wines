# PUTF21 Final Project - Rebecca Bang

from numpy import float64
import pandas as pd
import os
from wines import *
import pytest

path2 = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(path2 + '\\data\\wines.csv', encoding='utf8')

def test_wine_year():
    """Test year length is 4"""
    assert df.year.apply(lambda n: len(str(n))).eq(4).all()

def test_wine_price():
    """Test price for comma and dot separators"""
    test_price = df['price'].str.replace(',', '.').astype(float)
    assert test_price.dtypes == float64

def test_currency():
    test_curr = df['currency'].isnull().values.any()
    assert test_curr == False

# future implementations
# - looking for corrupted characters from character languages
