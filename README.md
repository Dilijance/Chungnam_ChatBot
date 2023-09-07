 Chungnam_ChatBot / 2023 September

#  DataSets
### Training set
    The whole idea of training is for a model to move from some *unknown* parameters (these may be random) to some *known* parameters
    
    One way to measure how poor or how wrong your models predictions are is to use a LOSS function

    Loss functions also may be called as COST function or CRITERION.

    Things we need to train:
        • Loss Function: Measure how wrong your prediction model
        • Optimizer: Adjust model's parameters by looking at loss function (https://pytorch.org/docs/stable/optim.html)
            •> Inside Optimizer you have to set two parameters:
                •> params - the model parameters you'd like to optimize (params=model_0.parameters())
                •> lr (learning rate) - hyperparameter that defines how big/small the optimizer changes the parameters with each step

    Specifically for PyTorch:
        • A training loop
        • A testing loop
#### Its important to divide data to Testing & Test Models

---

### Validation set
    ???
### Test set
    ???


## Torch
* Types of storing data
    * Scalar - One point/ 0 Dim / Dot in space
    * Vector - Line of data / 1 Dim
    * Matrix - 2D screen 
    * Tensor - Main Building block for PyTorch!(3D++)
        * Tensors can use basic operations(+, -, *..etc)
            * Also possible to multiplicate one tensor to another by torch.matmul()
            * http://matrixmultiplication.xyz/ fun and easy to understand it!
        * Batch_size: Controlling size of an output tensor(Torch5)
        * Shuffle True/False: Random order of data(Torch5)
        * DType=float/int(16 & 32): Precision of storing data in memory(less precision of number -> more speed of calculating vise-versa) 

### PyTorch model building essentials
* torch.nn - contains all important stuff for computational graphs
* torch.nn.Parameter - Which parameters model should try
* torch.nn.Module - Base class for all neural network modules
* torch.optim - optimize your model by looking at losses
* def forward() - This method defines whar happens in the forward computation

# Useful Imports

```python
#text.csv files can be read by pandas
import pandas as pd
import torch

#By Datasets & pandas you can get access and sort data from csv files
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

#Numpy_array are more friendly with other modules than Tensors
import numpy as np

#Re-make array into Tensor
import torchvision.transforms as transforms

# # MNIST most actively using DATASET

#Get something through internet by URL
import requests

#Data visualizer (Visualize, visualize, visualize!)
import matplotlib.pyplot as plt

#Allows you to use paths in your os
from pathlib import Path
```

# OOP

```python
#Class creating & most useful def's

# BluePrint 
#           vvv
    class Test:
        def __init__(self):
            pass
        
        def __len__(self):
            pass

        def __getitem__ (self)
            pass
```

# Machine Learning
## LinearRegression Code --- 2023-09-07
```python
# Create a train/test split
weight, bias = 0.7, 0.5

# Step size between 0.1 - 0.001 best choice!
X = torch.arange(start=0, end=1, step=0.01).unsqueeze(dim=1)
y = weight * X + bias # Formula of LinearRegression

# To multiplicate two matrix their inner dimensions should be similar
# (3, 2) @ (3, 2) shapes WONT WORK
# (3, 2) @ (2, 3) shapes WILL WORK
# (2, 3) @ (3, 2) shapes WILL WORK
# Like mirrored image
# Thats why we need to .unsqueeze X

# Actual Data Split
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]



# Visualize Data in Dot Graph
def plot_predictions(train_data=X_train,
                     train_labels = y_train,
                     test_data = X_test,
                     test_label = y_test,
                     prediction = None):
    '''
    Plots training data, test data and compares predictions.
    '''
    plt.figure(figsize=(10, 7))

    plt.scatter(train_data, train_labels, c="b", s=4, label="Training Data") # Dots for training data
    plt.scatter(test_data, test_label, c="g", s=4, label="Test Data") # Dots for test data

    if prediction is not None:
        plt.scatter(test_data, prediction, c="r", s=4, label="Predictions")

    plt.legend(prop={"size":14})
    plt.show()



# Making Model for Linear Regression
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float32)) #Long Version
        self.bias = nn.Parameter(torch.randn(1)) #Short Version
# nn.Parameter is a Tensor in def

#Forward method to define the computation in module
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weight * x + self.bias



# Control of randomness of our future testing cases
torch.manual_seed(42)
model_0 = LinearRegressionModel()

# Make predictions with model
# Inference_mode() using to get better performance while testing
with torch.inference_mode():
    y_preds = model_0(X_test)



#Setup a loss function
loss_fn = nn.L1Loss()
#Setup an optimizer (stochastic gradient descent)
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01)



# Building a training loop (and a testing loop) in PyTorch

# An epoch amount loops through the data
epochs = 300

epoch_count = []
loss_values = []
test_loss_value = []

# Steps to make a good Training looop!
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



# Visualize loss per epoch
    plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Train loss")
    plt.plot(epoch_count, test_loss_value, label="Test loss")
    plt.title("Training and test loss values")
    plt.ylabel("Loss")
    plt.xlabel("Epochs")



# After Training results
    with torch.inference_mode():
        y_preds_new = model_0(X_test)

        test_pred = model_0(X_test)
        test_loss = loss_fn(test_pred, y_test)

        # Print SomeData & Mapping for loss per epoch
        if epoch % 100 == 0:
            epoch_count.append(epoch)
            loss_values.append(loss)
            test_loss_value.append(test_loss)
            print(f"Epoch: {epoch} | Test: {loss} | Test loss: {test_loss}")

            print(model_0.state_dict())

# Start the Show!
plot_predictions(prediction=y_preds_new)



# Three main steps for saving
# 1. torch.save - allows save a PyTorch object in Pythons pickle format
# 2. torch.load = allows load a saved PyTorch object
# 3. torch.nn.Module.load_state_dict() - this allows to load a model's saved state dictionary

## PyTorch Save and Load Model


# 1. Create Model directory

MODEL_PATH = Path("models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

# 2. Create a model save path
MODEL_NAME = "01_pytorch_workflow_model_0.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

# 3. Save the model state dict
torch.save(obj=model_0.state_dict(), f=MODEL_SAVE_PATH)



# Load a model.state_dict

# To load in a saved state_dict we have to instantiate a new instance of our model class

loaded_model_0 = LinearRegressionModel()

loaded_model_0.load_state_dict(torch.load(f=MODEL_SAVE_PATH))
```