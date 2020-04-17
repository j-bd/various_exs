#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:30:05 2020

@author: j-bd
"""

import os

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from sklearn.metrics import confusion_matrix



path = "/home/latitude/Documents/Yotta/yotta_exs/yotta_p1/data"

DATA = os.path.join(path, "data.csv")
SOCIO = os.path.join(path, "socio_eco.csv")

df_data = pd.read_csv(DATA)
df_socio = pd.read_csv(SOCIO)

# =============================================================================
# Overview
# =============================================================================
print(df_data.shape)
print(df_data.describe())
print(df_data.info())
print(df_data.columns)
print(df_data.isnull().sum(axis=0) *100 / len(df_data))
print(df_data.head())
print(df_data.nunique(dropna = False))


# =============================================================================
# Clean data
# =============================================================================

df_data.drop(columns=["DATE", "DURATION_CONTACT", "RESULT_LAST_CAMPAIGN"], inplace=True)

numeric_variables = df_data.select_dtypes(include=[np.number])
cat_variables = df_data.select_dtypes(include=[object])

# =============================================================================
# Visualisation
# =============================================================================
df_data.skew()
df_data.kurtosis()
numeric_variables_variance = numeric_variables.var()
print(numeric_variables_variance)

# univariee quantitative
for col in numeric_variables.columns:
    plt.figure()
    graph = sns.countplot(x=col, hue='SUBSCRIPTION', data=df_data)
    graph.set_yscale("log")


# multivarie quantitative avec quantitative
sns.pairplot(df_data, hue='SUBSCRIPTION')
df_data.plotting.scatter_matrix() # method : {‘pearson’, ‘kendall’, ‘spearman’}


#univariee qualitative
for col in cat_variables.columns:
    plt.figure()
    graph = sns.countplot(x=col, hue='SUBSCRIPTION', data=cat_variables)
    graph.set_yscale("log")


# multivarie qualitative avec qualitative
for cat in cat_variables.columns:
    for num in numeric_variables.columns:
        plt.figure()
        sns.boxplot(x=num, y=cat, data=df_data)


sns.heatmap(df_data.corr(), nominal_columns=cat_variables.columns, annot=True)



# =============================================================================
# Valeurs manquantes et aberrantes
# =============================================================================
print(df_data.isnull().sum(axis=0) *100 / len(df_data))
for col in df_data.columns:
    df_data[col].fillna(df_data[col].mode()[0],inplace = True)
print(df_data.isnull().sum(axis=0) *100 / len(df_data))

df_data.shape
for col in df_data.select_dtypes(include=[np.number]).columns:
    df_data = df_data[
            np.abs(df_data[col] - df_data[col].mean()) <= (3 * df_data[col].std())
    ]
df_data.shape


# =============================================================================
# Train test split
# =============================================================================
ys = df_data['SUBSCRIPTION']
xs = df_data.drop(columns='SUBSCRIPTION')

x_train, x_test, y_train, y_test = train_test_split(
    xs, ys, test_size=0.2, random_state=42, stratify=ys
)


# =============================================================================
# Encodage
# =============================================================================

x_train = pd.get_dummies(x_train, drop_first=True)
y_train = pd.get_dummies(y_train, drop_first=True)

# =============================================================================
# Mise a l'echelle
# =============================================================================
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)


# =============================================================================
# Entrainement
# =============================================================================
classifier = LogisticRegression()
classifier_trained = classifier.fit(x_train, y_train)


# =============================================================================
# Prediction
# =============================================================================

x_test = pd.get_dummies(x_test, drop_first=True)
y_test = pd.get_dummies(y_test, drop_first=True)

x_test = scaler.fit_transform(x_test)

y_pred = classifier_trained.predict(x_test)


# =============================================================================
# Estimation de performance
# =============================================================================

# calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, y_pred)

# calculate F1 score
f1 = f1_score(y_test, y_pred)

# calculate precision-recall AUC
pr_auc = auc(recall, precision)

# calculate average precision score
ap = average_precision_score(y_test, y_pred)
print('f1=%.3f auc=%.3f ap=%.3f' % (f1, pr_auc, ap))
# plot no skill
plt.plot([0, 1], [0.5, 0.5], linestyle='--')
# plot the precision-recall curve for the model
plt.plot(recall, precision, marker='.')
# show the plot
plt.show()

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm,annot=True)
classifier_trained.score(x_test, y_test)

ys_rate = pd.get_dummies(ys, drop_first=True)
print(f"Taux d'acceptation sur l'ensemble du dataset: {1 - ys_rate.sum() / len(df_data)}"\
    f"Taux predit : {classifier_trained.score(x_test, y_test)}")
