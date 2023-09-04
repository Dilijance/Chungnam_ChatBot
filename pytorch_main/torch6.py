import torchvision.transforms as transforms

mnist_transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5),(1.0))])

from torchvision.datasets import MNIST
import requests
download_root = 'pytorch_main/data/MNIST_DATASET'

train_dataset = MNIST(download_root, transform=mnist_transform, train=True, download=True)
train_dataset = MNIST(download_root, transform=mnist_transform, train=False, download=True)
train_dataset = MNIST(download_root, transform=mnist_transform, train=False, download=True)
