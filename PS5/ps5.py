# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re

#If you get recursion error when running code, this is a GUI problem and can be fixed by 
# restarting Spyder - Andrew

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

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


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
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
          

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def evaluate(self, NewsStory):
        return self.is_phrase_in(NewsStory.get_title())
        

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def evaluate(self, NewsStory):
        return self.is_phrase_in(NewsStory.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, DateTime):
        datetimeObject = datetime.strptime(DateTime, "%d %b %Y %H:%M:%S")
        datetimeObject = datetimeObject.replace(tzinfo=pytz.timezone("EST"))
        self.DateTime = datetimeObject
        
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6

class BeforeTrigger(TimeTrigger):
    def __init__(self, DateTime):
        TimeTrigger.__init__(self, DateTime)
        
    def evaluate(self, NewsStory):
        return NewsStory.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.DateTime
        
        
        
class AfterTrigger(TimeTrigger):
    def __init__(self, DateTime):
        TimeTrigger.__init__(self, DateTime)
    
    def evaluate(self, NewsStory):
        return NewsStory.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.DateTime


# COMPOSITE TRIGGERS

# Problem 7

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    
    def evaluate(self, NewsStory):
        return not self.trigger.evaluate(NewsStory)

# Problem 8

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, NewsStory):
        if self.trigger1.evaluate(NewsStory) and self.trigger2.evaluate(NewsStory):
            return True
        else:
            return False

# Problem 9

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, NewsStory):
        if self.trigger1.evaluate(NewsStory) or self.trigger2.evaluate(NewsStory):
            return True
        else:
            return False


#======================
# Filtering
#======================

# Problem 10
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
        

#======================
# User-Specified Triggers
#======================
# Problem 11
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
            triggers_dict[line_split[0]] = NotTrigger(triggers_dict.get(line_split[2]))
        
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
        


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        
        triggerlist = [t1, t4]

        # Problem 11
        # After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers2.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # I COMMENTED OUT THE LINE BELOW AS YAHOO'S RSS FEED NO LONGER INCLUDES DESCRIPTIONS
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

