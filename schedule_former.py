#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:33:43 2017

@author: annakizilova
"""

def scheduleFormer():
    '''
    displays time, when an event begins and the event's title
    in case of networking event
    displays either 4pm or 5pm, 
    depending on the end of the last talk
    '''
    talks = get_title_time()
    startTime = 540
    schedule_ms = []
    schedule_as = []
    for item in talks:
        if 0 <= startTime//60 < 12:
            Time = str((startTime)//60) + ':' + str(startTime%60) + 'AM '
            if len(str(startTime%60)) < 2:
                Time = str((startTime)//60) + ':0' + str(startTime%60) + 'AM '
            else:
                pass
        elif startTime//60 == 12:
            Time = str((startTime)//60) + ':' + str(startTime%60) + 'PM '
            if len(str(startTime%60)) < 2:
                Time = str((startTime)//60) + ':0' + str(startTime%60) + 'PM '
        else:
            Time = str((startTime//60)-12) + ':' + str(startTime%60) + 'PM '
            if len(str(startTime%60)) < 2:
                Time = str((startTime//60)-12) + ':0' + str(startTime%60) + 'PM '
        schedule.append(Time + item)
        startTime = startTime + int(talks[item])

        
    print(schedule)
    return schedule
    
def morning_session():
    duration_ms = 180
    startTime = 540
    talks = {'A World Without HackerNews 30min': '30',
 'Accounting-Driven Development 45min': '45',
 'Clojure Ate Scala (on my project) 45min': '45',
 'Common Ruby Errors 45min': '45',
 'Communicating Over Distance 60min': '60',
 'Lua for the Masses 30min': '30',
 'Overdoing it in Python 45min': '45',
 'Pair Programming vs Noise 45min': '45',
 'Programming in the Boondocks of Seattle 30min': '30',
 'Rails Magic 60min': '60',
 'Rails for Python Developers lightning': '5',
 'Ruby Errors from Mismatched Gem Versions 45min': '45',
 'Ruby on Rails Legacy App Maintenance 60min': '60',
 'Ruby on Rails: Why We Should Move On 60min': '60',
 'Ruby vs. Clojure for Back-End Development 30min': '30',
 'Sit Down and Write 30min': '30',
 'User Interface CSS in Rails Apps 30min': '30',
 'Woah 30min': '30',
 'Writing Fast Tests Against Enterprise Rails 60min': '60'}
    morning_session = []
    while duration_ms > 0:
        for talk in talks:
            if 0 <= startTime//60 < 12:
                Time = str((startTime)//60) + ':' + str(startTime%60) + 'AM '
                if len(str(startTime%60)) < 2:
                    Time = str((startTime)//60) + ':0' + str(startTime%60) + 'AM '
                else:
                    pass
                morning_session.append(Time + talk)
                duration_ms = duration_ms - int(talks[talk])
                startTime = startTime + int(talks[talk])
    if duration_ms < 0:
        morning_session.pop(-1)
        for talk in talks:
            if talk in morning_session:
                talks.pop(talk)
    if duration_ms == 0:
        pass
    return morning_session
morning_session()
            