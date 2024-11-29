import torch
import numpy as np

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

np_array = np.array(data)
np_data = torch.from_numpy(np_array)


x_ones = torch.ones_like(x_data)
x_rand = torch.rand_like(x_data, dtype=torch.float)

shape = (2, 3)
torch.rand(shape)
torch.ones(shape)
torch.zeros(shape)

tensor = torch.rand(2, 2)
tensor.shape
tensor.dtype
tensor.device

if torch.cuda.is_available():
    tensor.to("cuda")

tensor = torch.ones(4, 4)
tensor[:, 1] = 0
tensor2 = torch.rand(4, 4)
torch.cat([tensor, tensor, tensor], dim=1)


tensor * tensor2  # element-wise
tensor @ tensor2

tensor.add(5)
tensor.add_(5)
tensor
