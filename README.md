# Usage if running bot from code:
Run pip install -r requirements.txt
If you want to train the models, run pip intall -r training_requirements.txt
Create a .env file
Invite the bot to the server
Run python main.py

# To add bot to server:
1. Visit this (link)[https://discord.com/oauth2/authorize?client_id=1394383883176247386&permissions=274878024704&integration_type=0&scope=bot] in your browser
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
Image of clouds and their altitudes: Wikipedia

# Other notes:
Clouds are also pretty hard to classify, to the point that even I sometimes can't tell them apart. There's a lot of variation between them (definitely not making excuses for my inability to train a CNN), and also doesn't help that there are typically multiple clouds in a picture. I spent a LOT of unlogged time on colab trying to train it but I am pretty happy with the final model. It's not perfect, but it's some sense of direction to allow users to try and ask it about the cloud types the model thinks it is and identify the clouds themselves.

I also wound up removing cirrostratus clouds from the classifier to help it learn. (As it tended to say everything was cirrostratus)
