#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:35:26 2023

@author: andrewwynn
"""

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate



class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError



class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def is_phrase_in(self, text):
        text = text.lower()
        text_split = re.split('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ ]', text)
        
        for element in text_split[:]:
            if element == "":
                text_split.remove(element)
        
        text_minus_punct = " ".join(text_split)
        if self.phrase in text_minus_punct:
            phrase_ind = text_minus_punct.index(self.phrase)
            phrase_ind += len(self.phrase)
            
            try:
                if text_minus_punct[phrase_ind] == " ":
                    return True
                else:
                    return False
            #If exception is raised, then last character in the phrase is the last letter in the text
            except:
                return True

        else:
            return False


class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def evaluate(self, NewsStory):
        return self.is_phrase_in(NewsStory.title)

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def evaluate(self, NewsStory):
        return self.is_phrase_in(NewsStory.get_description())

class TimeTrigger(Trigger):
    def __init__(self, DateTime):
        datetimeObject = datetime.strptime(DateTime, "%d %b %Y %H:%M:%S")
        datetimeObject = datetimeObject.replace(tzinfo=pytz.timezone("EST"))
        self.DateTime = datetimeObject



class BeforeTrigger(TimeTrigger):
    def __init__(self, DateTime):
        TimeTrigger.__init__(self, DateTime)
        
    def evaluate(self, NewsStory):
        
        if NewsStory.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.DateTime:
            return True
        else:
            return False
        
        
class AfterTrigger(TimeTrigger):
    def __init__(self, DateTime):
        TimeTrigger.__init__(self, DateTime)
    
    def evaluate(self, NewsStory):
        if NewsStory.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.DateTime:
            return True
        else:
            return False


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    
    def evaluate(self, NewsStory):
        return not self.trigger.evaluate(NewsStory)
    
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, NewsStory):
        if self.trigger1.evaluate(NewsStory) and self.trigger2.evaluate(NewsStory):
            return True
        else:
            return False
        
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, NewsStory):
        if self.trigger1.evaluate(NewsStory) or self.trigger2.evaluate(NewsStory):
            return True
        else:
            return False
        

        
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    triggerStories = []
    
    for NewsStory in stories:
        for trigger in triggerlist:
            if trigger.evaluate(NewsStory):
                triggerStories.append(NewsStory)
    
    return triggerStories



def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    #Dictionary maps from trigger names to trigger objects
    triggers_dict = {}
    #List of trigger objects specified by the trigger configuration file
    triggers_list = []
    for line in lines:
        line_split = line.split(",")
        
        if line_split[1] == "TITLE":
            triggers_dict[line_split[0]] = TitleTrigger(line_split[2])
        
        elif line_split[1] == "DESCRIPTION":
            triggers_dict[line_split[0]] = DescriptionTrigger(line_split[2])
        
        elif line_split[1] == "NOT":
            triggers_dict[line_split[0]] = NotTrigger(triggers_dict.getline_split[2])
        
        elif line_split[1] == "AND":
            triggers_dict[line_split[0]] = AndTrigger(triggers_dict.get(line_split[2]), triggers_dict.get(line_split[3]))
        
        elif line_split[1] == "OR":
            triggers_dict[line_split[0]] = OrTrigger(triggers_dict.get(line_split[2]), triggers_dict.get(line_split[3]))
        
        elif line_split[1] == "AFTER":
            triggers_dict[line_split[0]] = AfterTrigger(line_split[2])
        
        elif line_split[1] == "BEFORE":
            triggers_dict[line_split[0]] = BeforeTrigger(line_split[2])
        
        
        elif line_split[0] == "ADD":
            for i in line_split[1:]:
                triggers_list.append(triggers_dict.get(i))
                
        
    return triggers_list

stories = []
x = NewsStory('', '', "something somethingnew york city", '', datetime.now())
y =  NewsStory('', '', "asfd New York City asfdasdfasdf", '', datetime.now())
z = NewsStory('', "something somethingnew york city", '', '', datetime.now())

stories.append(x)
stories.append(y)
stories.append(z)
print(stories)

triggerlist = read_trigger_config('triggers.txt')
print(triggerlist)

for trigger in triggerlist:
    print(filter_stories(stories, triggerlist))
    



'''guid = "123"
title = "Election of donald trump and joe biden"
description = "Donald Trump and Joe Biden"
link = "www.google.com"
pubdate = "10 Feb 2015 17:00:09"
datetimeObject = datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")
#datetimeObject = datetimeObject.replace(tzinfo=pytz.timezone("EST"))

story = NewsStory(guid, title, description, link, datetimeObject)
print(story.pubdate)


x = AfterTrigger("4 Oct 2016 17:00:10")
print(x.evaluate(story))

NotTriggerObject = NotTrigger(x)
print(NotTriggerObject.evaluate(story))


'''