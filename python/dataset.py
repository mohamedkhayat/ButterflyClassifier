from torch.utils.data import Dataset
import os
import pandas as pd
import torchvision.io as tv_io

class ButterflyDataset(Dataset):
    def __init__(self, csv, path):
      self.data = pd.read_csv(csv)
      self.path = path
      unique_values = self.data['label'].unique()
      self.label_map = {label: i for i, label in enumerate(unique_values)}


    def __getitem__(self, index):
      img_path = os.path.join(self.path, self.data.iloc[index, 0])
      image = tv_io.read_image(img_path).float() /255.0
      label = self.label_map[self.data.iloc[index, 1]]
      return image, label

    def __len__(self):
      return len(self.data)