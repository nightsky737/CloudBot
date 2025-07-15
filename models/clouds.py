#Python fxn that lets me predict stuff

import torch
import torchvision
from torchvision import datasets, transforms, models
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import os
from pathlib import Path

class convNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.all_pooling = nn.MaxPool2d(2, 2)
        self.conv1 = nn.Conv2d(3, 6, 5) #Conv layer 1. Padding is 0
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.conv3 = nn.Conv2d(16, 32, 5)

        self.conv_layers = [self.conv1, self.conv2, self.conv3] #Put all conv layers and fcs into a list for ease of iteration through later?
 
        self.flatten = nn.Flatten() #Defaults to leaving the first (batch dim) alone
        
        flattened_size = 25088
        self.fc1 = nn.Linear(flattened_size, 120)
        self.fc2 = nn.Linear(120, 180)
        self.fcs = [self.fc1, self.fc2]
        self.final_fc = nn.Linear(180, 11)


    def forward(self, x):
        for conv_layer in self.conv_layers:
            x = self.all_pooling(F.relu(conv_layer(x)))
   
        x = self.flatten(x)
        # print(x.shape)
        for fc in self.fcs:
            x = F.relu(fc(x))
        x = self.final_fc(x)

        return x

# def load_model(model_fp="models/clouds.pth"):
# #Just stick the best/highest acc model in here
#     # return torch.load(model_fp, weights_only=False)
#     model = convNet()
#     model.load_state_dict(torch.load(model_fp))
#     return model

def load_model(model_fp):
    model = models.resnet50(pretrained=False) #gonna start small ish so my computer doesnt blow up
    model.fc = nn.Linear(model.fc.in_features, 11)
    model.load_state_dict(torch.load(model_fp))
    return model

model = load_model("models/resnet_attempt2.pth") #resnet 1 said everything was cirrostratus. im losing my damn mind

# model_transforms = transforms.Compose([
#     transforms.Resize((256, 256)),
#     transforms.ToTensor()
#     ]
# )

#Resnet transforms
model_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456,0.406],
                         [0.229, 0.224, 0.225]), 
                         ]
) 

human_labels = ["Altocumulus", "Altostratus", "Cumulonimbus","Cirrocumulus", "Cirrus", "Cirrostratus", "Contrail", "Cumulus",
                 "Nimbus", "Stratocumulus", "Stratus" ] #human readable labels

def predict(model, img, display = False, should_log = False): 
    '''
    img takes a PIL image. Display is for debugging purposes
    '''
    tensored_img = torch.unsqueeze(model_transforms(img), 0)

    if should_log:
        log_folder = Path("models") / "logs"
        log_num  = int(len(os.listdir(log_folder)) / 2)
        img.save(log_folder/ f"og{log_num}.jpg")
        # transformed_img.save(log_folder/ f"transformed{log_num}.jpg") Fix later.

    with torch.no_grad():
        prediction = model(tensored_img)

    # prediction = torch.softmax(prediction, 0)
    #also wana do something if its not sure. I would probably do that with softmax but uh idk how

    if display: 
        img.show()

    return human_labels[torch.argmax(prediction)]

# print(predict(Image.open("models\data\cloud_data\Ci\Ci-N139.jpg"), display=True))
