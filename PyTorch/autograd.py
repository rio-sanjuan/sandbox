import torch
from torchvision.models import resnet18, ResNet18_Weights

model = resnet18(weights=ResNet18_Weights.DEFAULT)

# random image with 3 channels, and height & width of 64
data = torch.rand(1, 3, 64, 64)

# the label is also initialized to some random value
labels = torch.rand(1, 1000)

# forward pass
prediction = model(data)

# Cost function measures how far off we were from correct label
loss = (prediction - labels).sum()
loss.backward()


# Load an optimizer
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)

# Run gradient descent
optim.step()

a = torch.tensor([2.0, 3.0], requires_grad=True)
b = torch.tensor([6.0, 4.0], requires_grad=True)

# When we call `.backward()` on `Q`, autograd calculates these gradients and
# stores them in the respective tensors' `.grad` attribute.
Q = 3 * a**3 - b**2


# We need to explicitly pass a `gradient` argument in `Q.backward()` because
# it is a vector. `gradient` is a tensor of the same shape as `Q`, and it
# represents the gradient of `Q` w.r.t. itself
external_grad = torch.ones(Q.shape, dtype=Q.dtype)
Q.backward(gradient=external_grad)
a.grad
(9 * a**2 == a.grad)
