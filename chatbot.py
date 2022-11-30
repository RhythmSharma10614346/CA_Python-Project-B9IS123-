import random

#Each question is able to be answered in many type of way. Better user experience
name = "Tesla Dbs Bot" 
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
        TeslaDbs_message = random.choice(response[messageContent])
    else: 
        TeslaDbs_message = random.choice(response["default"])
    return TeslaDbs_message