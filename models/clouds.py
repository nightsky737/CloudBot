#Python fxn that lets me predict stuff

import torch
import torchvision
from torchvision import datasets, transforms, models
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import os
from pathlib import Path
from torchvision.transforms.functional import to_pil_image
from collections import OrderedDict

# human_labels = ["Altocumulus", "Altostratus", "Cumulonimbus","Cirrocumulus", "Cirrus", "Cirrostratus", "Contrail", "Cumulus",
#                  "Nimbus", "Stratocumulus", "Stratus" ] #human readable labels

human_labels = ["Altocumulus", "Altostratus", "Cumulonimbus","Cirrocumulus", "Cirrus", "Contrail", "Cumulus",
                 "Nimbus", "Stratocumulus", "Stratus" ] #human readable labels
def load_model(model_fp):
    model = models.resnet152(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, len(human_labels))
    model.load_state_dict(torch.load(model_fp, map_location=torch.device('cpu')))
    return model

model = load_model("models/resnet_pretty_decent.pth") 

#Resnet transforms
model_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456,0.406],
                         [0.229, 0.224, 0.225]), 
                         ]
) 

def predict(model, img, top_p=.4, display = False, should_log = False): 
    '''
    img takes a PIL image. Display is for debugging purposes
    '''
    tensored_img = torch.unsqueeze(model_transforms(img), 0)

    if should_log:
        log_folder = Path("models") / "logs"
        log_num  = int(len(os.listdir(log_folder)) / 2)
        img.save(log_folder/ f"og{log_num}.jpg")
        transformed_img = to_pil_image(tensored_img[0])
        transformed_img.save(log_folder/ f"transformed{log_num}.jpg") 

    with torch.no_grad():
        prediction = model(tensored_img)

    if display: 
        img.show()

    softmaxxed = torch.softmax(prediction, dim=1)
    #uh how do I want to do this? top p = 50%?
    #sure i guess we can also pass top p in as arg and default to 50%?
    labels = [i for i in range(len(human_labels))]

    labels.sort(key= lambda x: softmaxxed[0][x], reverse=True)

    total_probs = 0
    return_dict = OrderedDict()
    for label in labels:
        total_probs += softmaxxed[0][label]
        return_dict[human_labels[label]] = softmaxxed[0][label]
        if total_probs >= top_p:
            break
    return return_dict

# print(predict(model, Image.open("models\data\cloud_data\Ci\Ci-N139.jpg")))
