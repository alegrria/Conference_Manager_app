#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:06:16 2017

@author: annakizilova
"""

talks = {'Ruby on Rails: Why We Should Move On 60min': '60', 'Ruby Errors from Mismatched Gem Versions 45min': '45', 'Woah 30min': '30', 'Sit Down and Write 30min': '30', 'Communicating Over Distance 60min': '60', 'Rails Magic 60min': '60', 'Rails for Python Developers lightning': '5', 'Programming in the Boondocks of Seattle 30min': '30', 'Common Ruby Errors 45min': '45', 'User Interface CSS in Rails Apps 30min': '30', 'A World Without HackerNews 30min': '30', 'Lua for the Masses 30min': '30', 'Clojure Ate Scala (on my project) 45min': '45', 'Ruby vs. Clojure for Back-End Development 30min': '30', 'Pair Programming vs Noise 45min': '45', 'Overdoing it in Python 45min': '45', 'Ruby on Rails Legacy App Maintenance 60min': '60', 'Accounting-Driven Development 45min': '45', 'Writing Fast Tests Against Enterprise Rails 60min': '60'}
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
print(sessions)