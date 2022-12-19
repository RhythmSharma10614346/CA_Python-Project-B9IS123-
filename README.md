Different types of chatbots.
AI, Mental Health Chat Bot Service and General.


B9IS123 Programming for Information Systems
(B9IS123_2223_TMD1S)


Lecturers:
Paul Laird
Amit Sharma


Group Members:
Rhythm Sharma
Kailash Kamalkumar Khatwani
Tuba Tosunoglu 
Marouan Alouache



# CA_Python-Project-B9IS123-
Creating a webiste with Chatbot using python
# Decided to use Django, as it is a very helpfull framework of python. 
Learning Django from W3schools.



# Content Notes


# What are the benefits of chatbots?




Chatbots look like a cool thing to play around with.
But what is the target of chatbots? Why do companies use bot assistants instead of offering a more human customer service?
Here are some obvious benefits of using chatbots:
Faster replies. Even the fastest human need some time to write in an appropriate response. Bots can send responses in milliseconds.
24 hrs support. Bots don’t need to rest, and they never get bored. Chatbots work for free and limitless.
Better user experiences. About forty percent of customers prefer bots to other forms of customer service. While some still prefer to wait for a real person, it is important to provide a solution that delivers the best customer experiences.
More customer interactions. Chatbots increase customer engagement levels. Their reply rates are quite higher than engaging customers via email or contact forms. 
Many integrations with messaging apps. Chatbots provide multi-channel customer service and can work on many different messaging platforms meanwhile.
Conversation templates. Many chatbots have a library of many different industries.
Great return on investment for businesses. The costs of deploying a chatbot on your website or social media are insignificant. A single bot can do the work of a whole call center.
Their primary target is to facilitate human interaction.
On top of that, this new technology is becoming quite popular. Over 1.400.000 people have already used a chatbot!
This looks impressive. Are there any downsides to chatting bots, though?


# The Most popular Chatbot Types



1. Quick answer bots
It is the one that is used to interact with the end customer via a predefined knowledge base and technical abilities that can capably respond to fixed instructions only.
 
2. Natural Language Processing (NLP) Chatbots
Natural Language Processing (NLP) to depict user’s input such as text or voice to an intent. 
3. Service/Action Chatbots
In order to complete the user’s request, these types of chatbots question relevant information from the user or take a certain action
4. Social Messaging Chatbots
Social messaging chatbots are amalgamated within a social messaging platform such as Messenger, Whatsapp, Telegram, Slack, etc, allowing customers to directly communicate with the bot, similar to the way they do with their family or friends.
5. Context Enabled Chatbots
The most advanced form of conversational bots are the contextual chatbots. In order to remember the conversations that happened earlier, these types of chatbots make use of Machine Learning and Artificial Intelligence, with particular users, to learn and grow with the passage of time. Contextual chatbots learn by experience with the user. A few examples of these chatbots are Google Assistant, Siri, Alexa, etc.
6. Voice-Enabled Chatbots
These types of chatbots make personalized experiences for users. Voice enabled chatbots accept the user’s input when he/she speaks, act upon his/her request, reply to his/her queries, and perform numerous creative tasks. 

Well, if users genuinely want to solve their problems, chatbots work fine. But if someone just wants to find out how to break a chatbot and is not cooperating with AI, it is easy to confuse a bot. Your virtual assistant may fall victim to mischievous users who find provoking it funny.




# The Best User Experiences for the Best Chatbot




1. Hook Your User
The most basic chatbot user experience is to inform the user of your bot’s capabilities, so they know what to expect from it in the future.

2. When In Doubt, Be Generic
While onboarding or subscribing your users to notifications, let them know they’re in charge and can easily change their minds in the future.

3. Lead The Conversation
Bot has to take the attempt! Decide the moments in which the user starts the chat window and says hello, and take that opportunity to start a new conversation and present guidance.

4. Be Interesting
Bot should make it look like a real conversation. Don’t write  a 100-word paragraph and expect your user to read everything. Think of how would you introduce a new conversation to a friend—they want to hear the whole story. While you chat, there should be short messages and breaks. Let users to end up one paragraph when the bot “writes” the next one, and show loading speech icons on their screens as the bot “types”.

5. Make The Conversation Continuously
This method is not new, particularly among eCommerce websites and blogs. It is particularly necessary when designing chatbots, since we trust  a linear conversation and it’s all so easy for flow to be disrupted.

6. Aim The Right Audience
The  point is that you have to  know your users first⁠⁠⁠. If you don’t aim the right audience, you can end up providing content your users are not interested in, or using language that may be too formal.
If you aim the right audience, you will know how to solve one problem in the best way possible.




# Django follows MVT design pattern (model view template)
Model = gets data from database
View = takes http requests as arguments
Template = .html files to describe the layout
# starting talkative chatbot 
# how to create a chatbot?


## Django version 4.1.4, using settings 'mysite.settings'
## Starting development server at http://127.0.0.1:8000/
# username admin
# password admin

#Introduction
A Chatbot project is created for helping people about mental health. When we designed this project, two points are considered most: User friendly interface and natural language chatbot! These features make everything easy for people who have hoped for some help from us!!
3 different chatbot types are modeled. Smart Chatbot, AI Chatbot and Chatty. 


Smart Chatbot
This chatbot is designed for giving people general information about mental health. 
Since we had chosen a very sensitive topic, we thought it would be good to enlighten people before the service we would give. Thus, they can understand why they need this service and what they would have from this website with scientific aspects.

This chatbot receives some inputs from users. And it researches these inputs in a txt file which is given by us, with some special techniques which we modeled.

AI Chatbot 
This chatbot is a software program for simulating intelligent conversations with human using rules or artificial intelligence. Users interact with the chatbot via conversational interface through written text. In this design, the most significant thing is being natural and keeping conversation going. Unlike smart chat bot, talkative bot should give some advice to users and ask questions in the meantime. 
Conversation begins with shared reference. We point to objects in the world so that we and our conversational partner know that we are talking about the same things.


Backend

Technical Details:

Logic of researching keywords in text file 
How can chatbot scan a text properly and can find some keywords? At this point, thinking as a machine is a must!
A chatbot needs to understand everything word by word or sentence by sentence. As we researched, nltk framework is found suitable for text processing. 


Why nltk 
Nltk is a platform for working with natural language process, it provides many libraries that we can use classification, tokenization, stemming, tagging, parsing, and semantic reasoning (https://www.nltk.org/) 


What we used from nltk:
•	wordnet  dictionary: wordnet helps us to read our corpus. We used the wordnet dictionary for the lemmatization process. It is important to understand what lemmatization and stemming are and why we needed it. Lemmatization takes the context and converts the word to its meaningful base form. That is called Lemma. Stemming is a process that stems or removes last few characters from a word, often leading to incorrect meanings and spelling. (https://www.analyticsvidhya.com/blog/2022/06/stemming-vs-lemmatization-in-nlp-must-know-differences/)
•	punct dictionary: Punct  helps for dividing text into a list of sentences or a list of words so that our curpos can readable easier by chatbot. 
sent_tokenize: Used for convert text to the list of sentences.
word_tokenize: Used for convert text to the list of words.


What is TfIdfVectorizer
This is an algorithm for meaningful prediction. It is important to understand what Tf and Idf are. 
Tf: is for term frequency(How many times all the words each individual word is repeated in the corpus) 
Idf: is for inverse document frequency(how rare is the occurence of the word in the corpus)
TfIdfVectorizer helps to count words into the cursor and finds how rare the word is in the cursor, giving the chatbot an idea about the importance of the word or sentence.


Endpoint
In this project, it is necessary sending-receiving data between chat bot and users. Chat bot needs to get the user's response and post response by giving rules.
Ajax is used for these data communication between server and html pages. Ajax dependency is added in base.html so that we can use jquery and read some data from html. 



How ajax works: 
Browser:Create and XmlHttpRequest >> Send Http request >> Server: Create a response and send data back to the browser>> Browser:Update page content


Frontend
During this project, We considered how we can focus on python chatbot techniques more and less spending time with website. After we researched many different frontend solutions, we decided to use Django, which provides us with the fastest solution when we create a website.


Website is created with Django and bootstrap is implemented for designing navbar. A simple, user-friendly website design is modeled so that users can benefit from chatbot service fastest.


Website consists of 4 different pages that are home page, about us, smart chatbot and talkative chatbot.


About Pages And Technical Details


Home page: Home page contains information about types of chatbots and it is created using bootstrap5 from the documentation site with help of w3schools.

AI Bot and Smart chatbot page: Ready html and css template is found for chat box design and implemented in project. Source code is shared in references. We removed some features and also added some new features. It is turned out to suitable form for this project. Both pages use the same chat box template. These pages are extended from the base.html page. 


Base page and ajax usage


-Other pages are extended from base.html and use the <head> elements from base.
-Navbar code is used from base.html.
-Ajax added in base.html. Ajax has been told in the ‘Endpoint’ section in detail.


Technologies Used:
Python
Django
HTML
CSS
Bootstrap
JS
JSON

Liberaries and dependencies used:
Numpy
NLTK
Scikit-Learn
Tersorflow
pip


Individual Contribution:

#[Kailash Kamalkumar Khatwani]
In the beginning, when we received our CA, we all were nervous regarding which topic to choose. With time, me and my group partners Ms. Rhythm sharma and Ms. Tuba Tosunoglu started working together on project after deciding the topic and I feel happy that we easily understood each other ideas and point of views and successfully completed this CA. After deciding the project, it was necessary that we distribute our roles in the overall project puzzle. 

I took the responsibilities of creating Talkative AI chatbot. I trained the chatbot so that it could understand words and answer accordingly. The chatbox was then later integrated to HTML page. I helped my teammates in minimizing the errors.

#[Tuba Tosunoglu]
I have designed chatbot name Smart Bot and GUI. By using Python, HTML, CSS, Bootstrap and Jquery. Throughput the project I helped Rhythm Creating Website with Django.
This Smartchatbot is designed for giving people general information about mental health. This is very sensitive topic and we thought it would be good to enlighten people before the service we would give. This chatbot receives some inputs from users. And it researches these inputs in a txt file which is given by us (whatismetalhealth.txt) How can chatbot scan a text properly and can find some keywords? At this point, thinking as 
a machine is a must! A chatbot needs to understand everything word by word or sentence by sentence. We used, nltk framework  for text processing. 


#[Rhythm Sharma]
I have started searching for ideas and end up choosing this, a website about chatbots and also with chatbots using python, therefor I have used Django for initializing the project and end up creating single page for the webiste with html, css and bootstrap. Tuba helped me with Django. We have three different chatbots mentioned in navigation bar on the website. I have created Chatty by using python and html. Also helped tuba in Smart chatbot.



Bibliography
MIT, docs CC BY 3.0. ,Navbar, Available at: 
https://getbootstrap.com/docs/5.2/components/navbar/ 
Build your own chatbot using Python | Python Tutorial for Beginners in 2022 | Great Learning, Available at:
https://www.youtube.com/watch?v=c_gXrw1RoKo

What Is Mental Health? Available at:
https://www.mentalhealth.gov/basics/what-is-mental-health 
2022, NLTK Project, 3   Processing Raw Text, Available at:
w.nltk.org/book_1ed/ch03.html


2022, NLTK Project, Installing NLTK Data, Available at:
https://www.nltk.org/data.html

2022, NLTK Project , Sample usage for tokenize, Available at:
https://www.nltk.org/howto/tokenize.html

2022, NLTK Project , Sample usage for wordnet, Available at:
https://www.nltk.org/howto/wordnet.html

2013 - 2022 Great Learning. All rights reserved, Available at:
https://www.mygreatlearning.com/academy?ambassador_code=GLYT_DES_c_gXrw1RoKo&utm_source=GLYT&utm_campaign=GLYT_DES_c_gXrw1RoKo


2022 Machine Learning Mastery. All Rights Reserved. , A Gentle Introduction to the Bag-of-Words Model, Available at:
https://machinelearningmastery.com/gentle-introduction-bag-words-model/


2022 Section, Creating ChatBot Using Natural Language Processing in Python, Available at:
https://www.section.io/engineering-education/creating-chatbot-using-natural-language-processing-in-python/ 

BBBootstrap.com, Bootstrap 4 Simple chat application, Available at:
https://bbbootstrap.com/snippets/simple-chat-application-57631463

Copyright 2013-2022 Analytics Vidhya. Stemming vs Lemmatization in NLP: Must-Know Differences, Available at:
https://www.analyticsvidhya.com/blog/2022/06/stemming-vs-lemmatization-in-nlp-must-know-differences/

TF-IDF Vectorizer scikit-learn, Available at:
https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a

1999-2022 by Refsnes Data. All Rights Reserved., What is AJAX?, Available at:
https://www.w3schools.com/whatis/whatis_ajax.asp











