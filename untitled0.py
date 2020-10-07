qu
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import torchvision
from torch.autograd import Variable
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

transform = transforms.Compose(
[transforms.Totensor(),
transforms.Normalize((0.1307),(0.3081))
]}