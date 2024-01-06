#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:08:48 2023

@author: andrewwynn
"""

import string
import re

txt = "purplecowpurplecowpurplecow"
phrase = "purple cow"
txt = txt.lower()


text_split = re.split('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ ]', txt)
print(text_split)

for element in text_split[:]:
    if element == "":
        text_split.remove(element)
    
    
print(text_split)

text_minus_punct = " ".join(text_split)
print(text_minus_punct)

if phrase in text_minus_punct:
    phrase_ind = text_minus_punct.index(phrase)
    print(phrase_ind)
    phrase_ind += len(phrase)
    print(phrase_ind)
    
    try:
        if text_minus_punct[phrase_ind] == " ":
            print("Whitespace after W")
            print("yes")
        else:
            print("No whitespace after W")
            print("no")
    #If exception is raised, then last character in the phrase is the last letter in the text
    except:
        print("W is last character")
        print("yes")

else:
    print("no")

   