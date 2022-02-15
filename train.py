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
    
# Load data and preprocess data (grey images and rescaled)
pp_data = pp.resize_greyscale(path = 'data/ceviche/*.jpg:data/donuts/*.jpg')

# Prepare labels
pp_data['labels'] = np.array(['ceviche' for label in range(1000)] + ['donuts' for label in range(1000)])

# Train test split
X = pp_data['data_pp']
y = pp_data['labels']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=40, stratify = y)

# Feature extraction
pca = PCA(n_components = 94, random_state = 40)

# Fit model
f1_scorer = make_scorer(f1_score, pos_label="donut")
svc = SVC(C=1, gamma=0.005)
sv_model = make_pipeline(pca, svc)
sv_model.fit(Xtrain,ytrain)

# Save model
pkl_filename = "model/svm_classifier.pkl"

with open(pkl_filename, 'wb') as file:
    pickle.dump(sv_model, file)
    
print('Trained model in model directory: model/svm.classifier.pkl')