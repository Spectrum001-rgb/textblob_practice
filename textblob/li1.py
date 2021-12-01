                                                                                        #textblob

from textblob import TextBlob
from textblob import Word

#text sentiment

tetimonial=TextBlob("get lost ok bye lets meet tommorow")

print(tetimonial.sentiment)

#words and Lemmatization
print(tetimonial.words)

print(tetimonial.words[-1].pluralize())   #pluralizes the word 

w=Word("octopi")
print(w.lemmatize())