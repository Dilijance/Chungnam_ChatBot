import torch
import pandas as pd

data = pd.read_csv('pytorch_main/test.csv')
print(data.keys())

torch_data = torch.from_numpy(data['kor'].values)
print(torch_data)