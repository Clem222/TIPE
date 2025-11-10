import torch
from torch import nn
import numpy as np
from torch.nn import CrossEntropyLoss, BCELoss
from torch.utils.data import TensorDataset
import math
import random

#TODO : corriger les entrées attendues du réseau qui doivent etre des scalaires
# (méthode forward de Neural_network et learn qui doit maintenant faire apprendre sur des scalaires, et virer Flatten de nn.Sequential)

device = "cpu"
function_interval = (0,20)
X_values = np.linspace(function_interval[0],function_interval[1], num=5000)
Y_values = np.sin(X_values)

Label = (Y_values >=0).astype(float)

train_data = np.column_stack((X_values, Label))

print(train_data)
class Neural_network(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 2),
            nn.ReLU(),
            nn.Linear(2,2),
            nn.ReLU(),
            nn.Linear(2,1),
            nn.Sigmoid()
        )

    def forward(self, input):
        self.output = self.network(input)
        return self.output

train_dataset = TensorDataset(
    torch.from_numpy(X_values).float().unsqueeze(1),
    torch.from_numpy(Label).float().unsqueeze(1)
)
print(train_dataset)


def learn(model_instance, train_data, lr, epochs, batch_size):
    loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
    optimizer = torch.optim.Adam(model_instance.parameters(), lr=lr)
    loss_function = BCELoss()
    losses = []
    for epoch in range(epochs):
        for batch_value, batch_label in loader:
            optimizer.zero_grad()
            batch_loss = 0.0
            for value, label in zip(batch_value, batch_label):
                prediction = model_instance(value)
                loss = loss_function(prediction, label)
                batch_loss += loss
            total_loss = batch_loss / len(batch_value)
            total_loss.backward()
            optimizer.step()

def test_model(model_instance, test_data, test_amount):
    for test in range(test_amount):
        pass

def accuracy_test(iterations, nn):
    results = []
    success = 0
    test_values = [random.random() for x in range(iterations)]
    for value in test_values:
        print(torch.tensor(value))
        print(torch.tensor(value).float().unsqueeze(0).unsqueeze(1))
        returned_value = nn(torch.tensor(value).float().unsqueeze(0).unsqueeze(1))
        print(returned_value)
    '''
    for value in test_values:
        results.append(((nn(torch.tensor(value).float().unsqueeze(0).unsqueeze(1))>=0.5), (math.sin(value) >= 0)))
    print(results)
    for x in range(iterations):
        success += int(results[x][0].item() == results[x][1])

    print('accuracy : ', (success/iterations)*100,' %')'''


Basic_NN = Neural_network()
print(Basic_NN)

learn(Basic_NN, train_dataset, 0.02, 1, 32)
test_value = torch.tensor(math.pi*(3/2) / function_interval[1]).float().unsqueeze(0).unsqueeze(1)
print(math.sin(math.pi*(3/2)))
print("valeur pour sin 8 : ", Basic_NN(test_value))
accuracy_test(5, Basic_NN)