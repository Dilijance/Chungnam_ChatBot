import torch.nn as nn
import torch
import matplotlib.pyplot as plt

m = nn.Sigmoid()
input = torch.randn(3)
output = m(input)
print(output)