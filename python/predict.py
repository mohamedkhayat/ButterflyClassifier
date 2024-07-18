import torch
import torch.nn as nn
import torchvision.transforms.v2 as transforms
from torchvision.models import vgg16
from torchvision.models import VGG16_Weights
import torchvision.io as tv_io
from dataset import ButterflyDataset

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

dict = torch.load('butterfly_model.pth')
vgg_model = vgg16(weights = VGG16_Weights.DEFAULT)
vgg_model.classifier[6]=nn.Linear(4096,75)
vgg_model.load_state_dict(dict)
vgg_model.to(device)

imagenet_norm_mean = [0.485, 0.456, 0.406]
imagenet_norm_std = [0.229, 0.224, 0.225]
pre_process = transforms.Compose([    
        transforms.Resize(224),
        transforms.CenterCrop(224),
            transforms.Normalize(mean=imagenet_norm_mean, std=imagenet_norm_std)

])
bfd = ButterflyDataset("data/Training_set.csv","data/train")
def predict_butterfly(img_path,DEVICE=device,model=vgg_model,label_map=bfd.label_map):
    inverted_label_map = {v: k for k, v in label_map.items()}
    img = tv_io.read_image(img_path,tv_io.ImageReadMode.RGB).float() / 255.0
    img = pre_process(img)
    img = img.unsqueeze(0)
    img = img.to(device)
    model.eval()
    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output, 1)
        predicted_label = inverted_label_map[predicted.item()]
        softmax_output = torch.softmax(output,dim = 1)
        confidence = softmax_output[0,predicted.item()].item()
    return confidence,predicted_label

