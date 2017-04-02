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
        self.Input = open('test_input.txt', 'r')
    def getInput(self):
        text = self.Input.readlines()
        talkPool = []
        for line in text:
            li = line.strip('\n')
            talkPool.append(li)
        self.Input.close()
        return talkPool