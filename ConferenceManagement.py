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
class FileReader:
    '''
    reads an input file  
    returns a list of strings (talk titles)
    '''
    def __init__(self, fileName):
        self.fileName = fileName
        
    def getText(self):
        try:
            text = open(self.fileName)
            lines = text.readlines()
            talkPool = []
            for line in lines:
                li = line.strip('\n')
                talkPool.append(li)
            return talkPool
        finally:
            text.close()
        
        
        
class TalkParser:
    '''
    displays title of a talk and its duration
    takes: list of strings 
    returns: a set with title of a talk and its duration in minutes
    '''
    def __init__(self, talkPool):
        self.talkPool = talkPool
        
    def parseTalks(self):
        talkList = {}
        texts = self.talkPool
        for i in texts:
            l = ''.join(item for item in i if item in '0123456789')
            if not l:
                l = '5'
            else:
                l = l
            talkList[i] = l
        return talkList    
        
        
class FirstFitScheduler:
    '''
    uses first fit algorithm for compiling sessions 
    takes: a set of talks and their durations
    returns: a list of sets (sessions)
    '''
    def __init__(self, talkList):
        self.talkList = talkList

    def formSessions(self):
        sessions = []
        for talk in self.talkList:
            sessionFound = False
            talkLength = int(self.talkList[talk])
            for index, session in enumerate(sessions):
                if index%2==1:
                    sessionLength = 240
                    size = sum(int(self.talkList[talk]) for talk in session)
                else:
                    sessionLength = 180
                    size = sum(int(self.talkList[talk]) for talk in session)
                if talkLength <= (sessionLength - size):
                    sessions[index].append(talk)            
                    sessionFound = True
                    break
            if sessionFound == False:
                sessions.append([talk])
        return sessions
     
        def scheduleSessions(self):
            sessions = formSessions()
            for index, session in enumerate(sessions):
                if index%2 == 0:
                    startTime = 540
                    for index, talk in enumerate(session):
                        Time = str((startTime)//60) + ':' + str(startTime%60) + 'AM '
                        if len(str(startTime%60)) < 2:
                            Time = str((startTime)//60) + ':0' + str(startTime%60) + 'AM '
                        else:
                            pass
                        session[index] = Time + talk
                        startTime = startTime + int(talkList[talk])
                else:
                    startTime = 780
                    for index, talk in enumerate(session): 
                        Time = str((startTime//60)-12) + ':' + str(startTime%60) + 'PM '
                        if len(str(startTime%60)) < 2:
                            Time = str((startTime//60)-12) + ':0' + str(startTime%60) + 'PM '
                        else:
                            pass
                        session[index] = Time + talk
                        startTime = startTime + int(talkList[talk])
            return sessions
                        
                
        
class Tracker:
    '''
    compiles tracks from sessions, lunch and networking events
    takes:
    returns: a list of lists(tracks)
    '''
    def __init__(self, sessions, talkPool):
        self.sessions = sessions
        self.talkPool = talkpool
        
    def makeTracks(self):
        lunch = '12:00PM Lunch'
        tracks = []
        for index, session in enumerate(self.sessions):
            track = []
            index = 0
            for talk in session:
                startTime = 540
                if 0 <= startTime//60 < 12:
                    Time = str((startTime)//60) + ':' + str(startTime%60) + 'AM '
                if len(str(startTime%60)) < 2:
                    Time = str((startTime)//60) + ':0' + str(startTime%60) + 'AM '
                else:
                    pass
                track.append(Time + talk)
                startTime = startTime + int(talkpool[talk])
            
            
            
       
        
        
        
def main(args):
    text = InputReader(argv[0])
    durations = Parser(text)
    tracks = FirstFitScheduler(durations)
    for(t in tracks) print(t.string)
    