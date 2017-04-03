#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:20:42 2017

@author: annakizilova


You are planning a big programming conference and have received many proposals 
which have passed the initial screen process but you're 
having trouble fitting them into the time constraints of the day -- 
there are so many possibilities! So you write a program to do it for you.
The conference has multiple tracks each of which has a morning and afternoon session.
Each session contains multiple talks.
Morning sessions begin at 9am and must finish by 12 noon, for lunch.
Afternoon sessions begin at 1pm and must finish in time for the networking event.
The networking event can start no earlier than 4:00 and no later than 5:00.
No talk title has numbers in it.
All talk lengths are either in minutes (not hours) or lightning (5 minutes).
Presenters will be very punctual; there needs to be no gap between sessions.
 
Note that depending on how you choose to complete this problem, your solution 
may give a different ordering 
or combination of talks into tracks. This is acceptable; 
you don’t need to exactly duplicate the sample output given here.
"""
class GetInput:
    '''
    reads an input file  
    returns a list of strings (talk titles)
    '''
    def __init__(self):
        self.Input = open('test_input.txt')
    def getInput(self):
        text = self.Input.readlines()
        talkPool = []
        for line in text:
            li = line.strip('\n')
            talkPool.append(li)
        self.Input.close()
        return talkPool
        
        
class getTitleTime:
    '''
    displays title of a talk and its duration
    takes: list of strings 
    returns: a set with title of a talk and its duration in minutes
    '''
    def __init__(self):
        self.talkPool = GetInput()
    def get_title_time(self):
        talkList = {}
        texts = self.talkPool.getInput()
        for i in texts:
            l = ''.join(item for item in i if item in '0123456789')
            if not l:
                l = '5'
            else:
                l = l
            talkList[i] = l
        return talkList    
        
        
class Sessions:
    '''
    uses first fit algorithm for compiling sessions and makes a dictionary of session lengths
    takes: a set of talks and their durations
    returns: a list of sets (sessions) and a dictionary wth session index:duration pairs
    '''
    def __init__(self):
        self.talkList = getTitleTime()
        self.session_length = {}
    def sessionFormer(self):
        talks = self.talkList.get_title_time()
        sessions = []
        for talk in talks:
            sessionFound = False
            talkLength = int(talks[talk])
            for index, session in enumerate(sessions):
                if index%2==1:
                    sessionLength = 240
                    size = sum(int(talks[talk]) for talk in session)
                else:
                    sessionLength = 180
                    size = sum(int(talks[talk]) for talk in session)
                if talkLength <= (sessionLength - size):
                    sessions[index].add(talk)            
                    sessionFound = True
                    break
            if sessionFound == False:
                sessions.append({talk})
        return sessions
     
    def sessionLength(self):
        talks = self.talkList.get_title_time()
        sessionsPool = Sessions()
        for index, session in enumerate(sessionsPool.sessionFormer()):
            length = sum(int(talks[talk]) for talk in session)
            self.session_length[index] = length
        return self.session_length