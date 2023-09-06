import torch
from torch import nn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

weight = 0.7
bias = 0.5

start = 0
end = 1
step = 0.01

X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias

## Create a train/test split

train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

def plot_predictions(train_data=X_train,
                     train_labels = y_train,
                     test_data = X_test,
                     test_label = y_test,
                     prediction = None):
    '''
    Plots training data, test data and compares predictions.
    '''
    plt.figure(figsize=(10, 7))

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
    plt.show()

# ### Building model

#Linear Regression model

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        self.bias = nn.Parameter(torch.randn(1))

#Forward method to define the computation in module

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weight * x + self.bias
    

# Create a random seed
torch.manual_seed(42)

# Create an instance of the model (this is a subclass of nn.Module)
model_0 = LinearRegressionModel()

# Check out the parameters
# print(list(model_0.parameters()))

# Making prediction using 'torch.inference_mode()'

# Make predictions with model

with torch.inference_mode():
    y_preds = model_0(X_test)

# plot_predictions(prediction=y_preds)

#Setup a loss function
loss_fn = nn.L1Loss()

#Setup an optimizer (stochastic gradient descent)
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01)


# Building a training loop (and a testing loop) in PyTorch

# An epoch is one loop through the data
epochs = 300

epoch_count = []
loss_values = []
test_loss_value = []

# 0. Loop through data
for epoch in range(epochs):
    model_0.train()
    # 1. Forward pass
    y_preds = model_0(X_train)

    # 2. Calculate loss
    loss = loss_fn(y_preds, y_train)
    print(f"Loss: {loss}")

    # 3. Optimizer zero grad
    optimizer.zero_grad()

    # 4. Perform backpropagation on the loss with respect of the parameters of the model
    loss.backward()

    # 5. Step the optimizer (perform gradient descent)
    optimizer.step()

    model_0.eval()

    plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Train loss")
    plt.plot(epoch_count, test_loss_value, label="Test loss")
    plt.title("Training and test loss values")
    plt.ylabel("Loss")
    plt.xlabel("Epochs")

    with torch.inference_mode():
        y_preds_new = model_0(X_test)

        test_pred = model_0(X_test)
        test_loss = loss_fn(test_pred, y_test)

        if epoch % 100 == 0:
            epoch_count.append(epoch)
            loss_values.append(loss)
            test_loss_value.append(test_loss)
            print(f"Epoch: {epoch} | Test: {loss} | Test loss: {test_loss}")

            print(model_0.state_dict())

plot_predictions(prediction=y_preds_new)