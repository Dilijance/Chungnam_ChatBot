import torch
import torch.nn as nn
import pandas as pd
import matplotlib as plt

weight = 0.5
bias = 0.2

start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias
print(len(X), len(y))

## Create a train/test split

train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

print(len(X_train), len(y_train), len(X_test), len(y_test))


def plot_predictions(train_data=X_train,
                     train_labels = y_train,
                     test_data = X_test,
                     test_label = y_test,
                     prediction = None):
    '''
    Plots training data, test data and compares predictions.
    '''
    plt.(figsize=(10, 7))

    #Plot training data in Blue
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training Data")

    #Plot test data in Green
    plt.scatter(test_data, test_label, c="g", s=4, label="Test Data")

    #Are there any predictions
    if prediction is not None:
        #Plot the predictions if they exist
        plt.scatter(test_data, prediction, c="r", s=4, label="Predictions")

    #Show the legend
    plt.legend(prop={"size":14})

plot_predictions()