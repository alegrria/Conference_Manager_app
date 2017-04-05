#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:55:08 2017

@author: annakizilova
"""
from track import Track

class FirstFitScheduler:
    '''
    uses first fit algorithm for compiling sessions 
    takes: a set of talks and their durations
    returns: a list of sets (sessions)
    '''
    def __init__(self, talkList):
        self.talkList = talkList

    def formTracks(self):
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
                    startTime = startTime + int(self.talkList[talk])
                session.append('12:00PM Lunch')
            else:
                startTime = 780
                for index, talk in enumerate(session): 
                    Time = str((startTime//60)-12) + ':' + str(startTime%60) + 'PM '
                    if len(str(startTime%60)) < 2:
                        Time = str((startTime//60)-12) + ':0' + str(startTime%60) + 'PM '
                    else:
                        pass
                    session[index] = Time + talk
                    startTime = startTime + int(self.talkList[talk])
                if startTime <= 960:
                    session.append('4:00PM Networking Event')
                elif startTime > 960:
                    session.append('5:00PM Networking Event')
                    
        tracks = []
        for i in range(0, len(sessions), 2):
            tracks.append(Track(sessions[i], sessions[i+1], i//2 + 1))
        return tracks
                        