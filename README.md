# Discord_Bot
Balin Surface ChatGPT Discord Bot

Brief summary of this project prompt in your own words
- 
The project prompt was to create a working Discord bot with a specific functionality, and could be interacted with in the Discord channel.

Explanation of what you chose and why, and what “being successful” meant to you
-
Being successful meant creating a bot that is able to consistently perform its intended function, and is good to use in the channel. 

Full explanation of what your program does
-
I initially started trying to create a sports data API - bot, but after searching for a couple days for a free, current, and usable API, I could not find one (mostly the free part was the problem). So, I turned to creating a ChatGPT bot that could theoretically show past sports data, even though it is not current, as well as do many other things. 
Upon typing the start codes: /ai, /bot, or /chatgpt, and entering a prompt afterwards, the Discord Bot uses the ChatGPT API to compile a response and administer it in Discord. 
My program hinges on the "chatgpt_response" function, which is imported in from openai.py. It basically uses the davinci-003 from ChatGPT 3.5 version to extract OpenAI's response_dict dictionary, assigning it to prompt_response and printing it in Discord channel. The surface.py file was created first, and outlines how to get the bot working in Discord and recognizing (checking) text with /ai, /bot, or /chatgpt commands in them to generate a response. 

ID any “skeleton” sources that make up the bones of your code
- 
Done in surface.py and openai.py, the ChatGPT function was a "skeleton" source collaborated with Liam and the ChatGPT getting started library usage directions.

Full explanation of how your code improves upon any skeleton code
-
I am able to import the function into surface.py, and provide a usable discord bot interface using multiple commands

Any other info that will help your target audience understand your code
-
Nothing else is necessary
