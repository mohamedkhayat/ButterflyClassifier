import torch
import torch.nn as nn
from torch.optim import Adam
from torchvision.models import vgg16
from torchvision.models import VGG16_Weights
from torch.utils.data import DataLoader
import torchvision.transforms.v2 as transforms
from dataset import ButterflyDataset
from torch.utils.data import random_split
from utils import train,validate

vgg_weights = VGG16_Weights.DEFAULT
vgg_model = vgg16(weights=vgg_weights)

for param in vgg_model.features.parameters():
    param.requires_grad = False

vgg_model.classifier[6]=nn.Linear(4096,75)
print(vgg_model)
imagenet_norm_mean = [0.485, 0.456, 0.406]
imagenet_norm_std = [0.229, 0.224, 0.225]
pre_process = transforms.Compose([    
        transforms.Resize(224),
        transforms.CenterCrop(224),
            transforms.Normalize(mean=imagenet_norm_mean, std=imagenet_norm_std)

])
# Define the data augmentation transforms
data_transforms = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(20),  # Randomly rotate the image by up to 20 degrees
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),  # Randomly change the brightness, contrast, saturation and hue
        transforms.Normalize(mean=imagenet_norm_mean, std=imagenet_norm_std),

])

bfd = ButterflyDataset("data/Training_set.csv","data/train")
train_size = int(len(bfd) * 0.8)
test_size = len(bfd) - train_size
train_set,test_set = random_split(bfd,(train_size,test_size))

train_loader = DataLoader(train_set, batch_size=32, shuffle=True,num_workers=4)
test_loader = DataLoader(test_set, batch_size=32,num_workers=4)

device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')

optimizer = Adam(vgg_model.parameters(),lr=0.0001)
criterion = nn.CrossEntropyLoss()
model = vgg_model.to(device)

epochs = 10
for epoch in range(epochs):
  print('Epoch : {}'.format(epoch+1))
  train(device,model,train_loader,optimizer,criterion,data_transforms)
  validate(device,model,test_loader,criterion,pre_process)
  