# Usage if running bot from code:
Run pip install -r requirements.txt
If you want to train the models, run pip intall -r training_requirements.txt
Create a .env file
Invite the bot to the server
Run python main.py

# To add bot to server:
i will do this later

# How to use this bot:
Call !help for instructions 
Call !cloudId to identify clouds
This will return a list of the clouds that the model thinks it is. Try to get only one cloud in each picture, and not crop it weirdly (try to keep it roughly square ish). 
!info \[cloudname\] will give more info on the clouds. !cloudnames will give a list of valid cloudnames

# Datasets I used to train 
https://www.kaggle.com/datasets/mmichelli/cirrus-cumulus-stratus-nimbus-ccsn-database

I do not have these in the github because otherwise that would be too much storage. However, I have stored them in a folder in this directory called "data" under "clouds".

# Other notes:
Data and models that are not the final model might not be on github, as those are big and eat storage.
Clouds are also pretty hard to classify. There's a lot of variation between them (definitely not making excuses for my inability to train a CNN) and I spent a LOT of unlogged time on colab trying to train it but I am pretty happy with my compromise

It also doesn't help that there are typically multiple clouds in a picture. I will probably add image segmentation using grad cam after finishing my other projects.

I also removed cirrostratus clouds from the classifier to help it learn. (so it doesnt identify cirrostratus)

# Me notes:
i was honestly stuck on the classifier for like so long like half a week without significant improvement. Probably should have "given up" earlier and done the modified version that yall are seeing here and go w/ the low acc one. So maybe not fixating on one solution kind of could have been good.
But I did learn how to do the cnn and integrate it into something else which was cool, and also hopefully the API calls?