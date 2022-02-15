#!/usr/local/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, f1_score, make_scorer
from sklearn.model_selection import train_test_split, GridSearchCV
import skimage.io as io
from skimage.transform import resize, rescale, rotate
import src.preprocess as pp
import pickle

# Load arbitrary image and preprocess
pp_data = pp.resize_greyscale(path = 'data/ceviche/1006106.jpg')

# Load model
with open("model/svm_classifier.pkl", 'rb') as file:
    svm_model = pickle.load(file)
    
predictions = svm_model.predict(pp_data['data_pp'])

print(predictions)
