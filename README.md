 Chungnam_ChatBot
My first git
## 202_09_04
my first touch
*  나의 첫 깃허브
    * Test

AI, Machine Learning, Deep Learning etc..
* DataSets
    * Training set
    * Validation set
    * Test set
* Learning Process
    * learn by TRAINING MODEL
    * test through TEST MODEL

* Torch
    * Types of storing data
        * Scalar - One point/ 0 Dim / Dot in space
        * Vector - Line of data / 1 Dim
        * Matrix - 2D screen 
        * Tensor - Main Building block for PyTorch!
            * Tensors can use basic operations(+, -, *..etc)
                * Also possible to multiplicate one tensor to another by torch.matmul()
                * http://matrixmultiplication.xyz/ fun and easy to understand it!
            * Batch_size: Controlling size of an output tensor(Torch5)
            * Shuffle True/False: Random order of data(Torch5)
            * DType=float/int(16 & 32): Precision of storing data in memory(less precision of number -> more speed of calculating vise-versa) 

```python
#Class creating & most useful def's
class Test:
    def __init__(self):
        pass
    
    def __len__(self):
        pass

    def __getitem__ (self)
        pass


#text.csv files can be read by pandas
import pandas as pd
import torch

#By Datasets & pandas you can get access and sort data from csv files
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

#Numpy quite similar with Tensor data type
import numpy as np

#Re-make array into Tensor
import torchvision.transforms as transforms

# # MNIST most actively using DATASET

#Get something through internet by URL
import requests

#Data visualizer (seems like the most fun)
import matplotlib.pyplot as plt

#Creating Tensor
My_tensor = torch.tensor(dtype=, shape= , device=)

#