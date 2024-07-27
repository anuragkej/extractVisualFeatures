import torch
from transformers import AutoModel, AutoImageProcessor
from torchvision.transforms import Resize, ToTensor
from torchvision.transforms.functional import to_pil_image


toTensor = [Resize((100, 100)), ToTensor()]

print(toTensor)
