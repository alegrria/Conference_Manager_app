#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:12:27 2017

@author: annakizilova
"""

class Track:
    '''
    takes: lest of lists(sessions)
    returns: a list of lists(tracks)
    '''
    def __init__(self, morning_session, afternoon_session, number):
        self.morning_session = morning_session
        self.afternoon_session = afternoon_session
        self.number = number
        
    def __str__(self):
        result = 'Track ' + str(self.number) + ":\n"
        for talk in self.morning_session:
            result += talk + "\n"
        for talk in self.afternoon_session:
            result += talk + "\n"
        return result