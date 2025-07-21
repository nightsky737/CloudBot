# Usage if running bot from code:
Run pip install -r requirements.txt
If you want to train the models, run pip intall -r training_requirements.txt
Create a .env file
Invite the bot to the server
Run python main.py

# To add bot to server:
1. Visit this (link)[] in your browser
2. Select server you want to add it to
3. Enjoy identifying clouds!

# How to use this bot:
Call !help for instructions 
Call !cloudId to identify clouds
This will return a list of the clouds that the model thinks it is. Try to get only one cloud in each picture, and not crop it weirdly (try to keep it roughly square ish). 
!info \[cloudname\] will give more info on the clouds. !cloudnames will give a list of valid cloudnames

# Credits
Dataset used to train: https://www.kaggle.com/datasets/mmichelli/cirrus-cumulus-stratus-nimbus-ccsn-database
Image used for the discord bot's pfp: https://stock.adobe.com/search/video?k=anime+clouds&asset_id=1107084586
# Other notes:
Clouds are also pretty hard to classify. There's a lot of variation between them (definitely not making excuses for my inability to train a CNN) and I spent a LOT of unlogged time on colab trying to train it but I am pretty happy with my compromise

It also doesn't help that there are typically multiple clouds in a picture. I will probably add image segmentation using grad cam after finishing other projects, but I would say that the current version is pretty functional.

I also removed cirrostratus clouds from the classifier to help it learn. (so it doesnt identify cirrostratus)
