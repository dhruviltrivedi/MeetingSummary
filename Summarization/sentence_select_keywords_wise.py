# -*- coding: utf-8 -*-
"""Sentence_Select_Keywords_Wise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11rmGzx0TYACxTjGcj88TD5vnFYyTAzoH
"""

import pandas as pd

from google.colab import drive
drive.mount("/content/drive")

#Reading the data from csv file
df = pd.read_csv("/content/drive/My Drive/MeetingSummary/simpsons_dataset.csv")
print(df)

type(df.spoken_words[0])

len(df)

#Checking for blank rows
df.isnull().sum()

#Droping blank rows
df.dropna(inplace=True)

len(df)

df.reset_index(inplace=True)
df.drop(['index'], axis=1)

df.isnull().sum()

#Considering first 3600 values only
#This is not needed in the actual system
test_df = df.iloc[:3600]
test_df

#Merging all statements and dialogues
text = ' '.join(df["spoken_words"])
text

#Creating an abbreviation dictionary
abbreviation_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",
                         
                           "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",

                           "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",

                           "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would",

                           "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",

                           "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam",

                           "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have",

                           "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock",

                           "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",

                           "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",

                           "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",

                           "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",

                           "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have",

                           "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",

                           "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",

                           "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",

                           "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",

                           "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",

                           "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",

                           "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",

                           "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",

                           "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",

                           "you're": "you are", "you've": "you have"}

#Cleaning text by updating the abbreviations
cleaned_text = text
cleaned_text = ' '.join([abbreviation_mapping[t] if t in abbreviation_mapping else t for t in cleaned_text.split(" ")]) 
cleaned_text

#Creating a list of crucial words
crucial_keywords = ['discussed', 'discussing', 
                    'decided',
                    'suggested', 'supported', 'support', 'suggest', 
                    'agreed', 'accepted', 'approved', 'agree', 'accept', 'approve', 
                    'accomplish', 'accomplished', 'achieve', 'achieved', 'achievement', 'credit', 'goal', 'goals', 
                    'argued', 'argue', 
                    'informed', 'noted', 'pointed out', 
                    'observed', 'observe', 
                    'reminded', 'remind', 
                    'question', 'questioned', 
                    'reject', 'rejected', 
                    'brought up',
                    'reported', 'report', 
                    'recommended', 'recommend'
                    'explained',  'explain', 'explanation', 
                    'emphasised', 'emphasis', 
                    'stressed',
                    'complained',
                    'added',
                    'summarised', 'summarise', 'summarized', 'summarize', 
                    'extremely',
                    'so yeah', 'so yes', 'yup',  
                    'accomplish', 'accomplished', 
                    'agenda',
                    'task', 'tasks', 
                    'assign', 'assigned',
                    'definately', 
                    'valuable', 
                    'ballot', 'poll', 'vote', 'voted', 
                    'brainstorm', 'brainstorming', 
                    'clarify', 'clarification', 'verify', 'verification', 
                    'collaborate',
                    'commence', 
                    'comment', 'statement', 'qoute',
                    'confidential', 
                    'deadline', 
                    'guest speaker', 'cheif speaker', 'primary speaker',
                    'implement', 
                    'mandatory',
                    'objectives',
                    'participant', 'participants', 'participated', 
                    'strategy', 'strategize', 'strategic', 
                    'commitment', 'commit', 
                    ]
print(len(crucial_keywords))
crucial_keywords

#Splitting the whole transcript into individual sentences and storing them in a list
sentence_list = cleaned_text.split('. ')
for i in range(len(sentence_list)):
  sentence_list[i] += '.'
sentence_list

len(sentence_list)

#Printing the sentences with those specific crucial keywords included in them
is_important = False
counter = 0
for i in sentence_list:
  is_important = False
  words = i.split(' ')
  for j in range(len(words)-1):
    if (words[j].casefold() in crucial_keywords):
      is_important = True
    elif (words[j+1].casefold() in crucial_keywords):
      is_important = True
    elif ((words[j].casefold() + ' ' + words[j+1].casefold()) in crucial_keywords):
      is_important = True
  if (is_important == True):
    print(i)
    counter += 1
print(counter)