import torch
from torch import nn
from torch.utils.data import Dataloader
from torchvision import datasets, transforms

device = "cpu"
batch_size = 64

transform = transforms.Compose([
	transforms.ToTensor()])

train_dataset = torchvision.datasets.MNIST(
	root = './mnist',
	train = True,
	download = True,
	transform=transform)

test_data = torchvision.datasets.MNIST(
	root='./mnist',
	train = False,
	download = True,
	transform = transform)

train_dataloader = Dataloader(train_dataset, batch_size=batch_size)
test_dataloader = Dataloader(test_dataset, batch_size=batch_size)
'''
class Nn(nn.Module):
	def __init__(self):
		super.__init__()
		self.flatten = nn.Flatten()
		self.sequential = nn.Sequential(
			nn.Conv2d(32, kernel_size=(3,3), activation="relu"),
			nn.Conv2d(32, kernel_size=(3,3), activation="relu"),
			nn.Maxpooling)
	def forward(self, x):
		x = self.flatten(x)
		self.output = self.squential(x)
		return self.output

def learn(model_instance, train_data, lr, epochs, batch_size):
	#load data
	optimizer = torch.optim.Adam(model_instance.parameters(), lr=lr)
	lossfunction = BCEloss()

	for epoch in range(epochs):
		batch_loss = 0.0
		for batch in len(train_data)//batch_size:
			optimizer.zero_grad()
			prediction = model_instance()#value from train_data
			loss = lossfunction(prediction, )#label from train_data
			batch_loss += loss
'''