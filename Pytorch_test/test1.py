import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = "cpu"

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512, 512))

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
'''
model = NeuralNetwork().to(device)
print(model)
x = torch.rand(1,28,28, device=device)
logits = model(x)
prediction = nn.Softmax(dim=1)(logits)
y_pred = prediction.argmax(1)
print(y_pred)'''

random_input_feed = torch.rand(3,28,28)
print(random_input_feed.size())