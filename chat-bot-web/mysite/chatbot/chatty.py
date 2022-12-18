import random

#Each question is able to be answered in many type of way. Better user experience
name = "Chatty Bot" 
weather = "sunny" 
mood = "happy"
response = { 
"what's your name?": [ 
"Everybody calls me {0}".format(name), 
"I usually go by {0}".format(name), 
"My name is {0}".format(name) ],
"what's today's weather?": [ 
"The weather is {0}".format(weather), 
"It's {0} today".format(weather)], 
"how are you?": [ 
"I am feeling {0}".format(mood), 
"{0}! How about you?".format(mood), 
"I am {0}! How about yourself?".format(mood), ],
"": [ 
"Hey! Are you there?", 
"What do you mean by these?", 
 ],
"default": [
"This is a default message"] }

#can choose any response
def res(messageContent):
    if messageContent in response: 
        chattybot_message = random.choice(response[messageContent])
    else: 
        chattybot_message = random.choice(response["default"])
    return chattybot_message

    #if there something different in user question from what we give chatbot, chatbot should understand what the real question is

def real(userText):

    if "name" in userText:

        ytext = "what's your name?"

    elif "monsoon" in userText:

        ytext = "what's today's weather?"

    elif "how are" in userText:

        ytext = "how are you?"

    else:

        ytext = ""

    return ytext