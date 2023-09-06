import torch
import pandas as pd
import matplotlib as plt
import numpy as np


# ##SCALAR
# scalar = torch.tensor(7)
# # Get dimensions
# scalar.ndim
# #Get int from object
# scalar.item()
# print_me(scalar)

# ## VECTOR
# vector = torch.tensor([7, 7])
# vector.ndim
# print(vector.shape)

# ##MATRIX
# matrix = torch.tensor([[7,7], [7,7]])
# print(matrix[1])

# ##TENSOR

# tensor = torch.tensor([[[1, 2, 3],
#                         [4, 5, 6],
#                         [7, 8, 9]]])
# print(tensor.ndim)

# print(tensor.shape)

# rand_tensor = torch.rand(3, 3)
# rand_image_size_tensor = torch.rand(size=(3, 244, 244))
# print(rand_image_size_tensor.shape)
# print(rand_image_size_tensor.ndim)

## ZEROS AND ONES

#create a tensor of all zeros

# zeros = torch.zeros(3, 4)
# print(zeros)

# ones = torch.ones(3, 4)
# print(ones.dtype)

## CREATE RANGE OF TENSORS

# a = torch.arange(0, 100, 5)

## CREATE TENSOR LIKE

# b = torch.zeros_like(a)

## Manipulate tensor

# tensor = torch.tensor([1, 2, 3])
# tensor += 10
# tensor -= 10
# tensor *= 10 #or torch.mul(tensor, 10) strange one. dont use it

# print(tensor)

##Matrix multiplication(dot product - Google it!)

tensor = torch.tensor([1, 2, 3])
matrix = torch.matmul(tensor, tensor) # |tensor @ tensor| same result
# ! multiplication goes 1 * 1 + 2 * 2 + 3 * 3 = 14

# To multiplicate two matrix their inner dimensions should be similar
# (3, 2) @ (3, 2) shapes WONT WORK
# (3, 2) @ (2, 3) shapes WILL WORK
# (2, 3) @ (3, 2) shapes WILL WORK
# Like mirrored image

# http://matrixmultiplication.xyz/