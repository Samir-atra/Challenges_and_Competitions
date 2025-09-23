# Import
import pandas as pd
import csv
import numpy as np
import tensorflow as tf
import time

# load and create dataset
features = []
labels = []
counter = 0
file = r"train.csv"

train =  tf.data.experimental.CsvDataset(
"/home/samer/Desktop/Beedoo/ML_Olympiad/ml-olympiad-predicting-earthquake-damage/train.csv")
print(len(train))
for vec, label in train:
    vectors = features.append(vec)
    labes = labels.append(label)
    counter +=1
    if counter %500 == 0:
        time.sleep(5)
        print("sleeping")
dataset = tf.data.Dataset.from_tensor_slices((vectors, labels))

with open("train.csv", "r") as train_set:
    next(train_set)
    for row in train_set:
        features.append(row.split(',')[0:35])
        labels.append(row.strip().split(',')[36])
print(set(labels))

# preprocessing
features = np.array(features)
labels = np.array(labels)
labels = np.reshape(labels,(4000,1))

# building model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation = "sigmoid"),
    tf.keras.layers.Dense(32,activation= 'sigmoid'),
    tf.keras.layers.Dense(3, activation = 'sigmoid')
])

model.compile(
    loss = 'mse',
    optimizer = tf.keras.optimizers.Adam(learning_rate= 0.0001),
    metrics= ['accuracy'],
)

model.fit(
    dataset,
    epochs = 100
)
