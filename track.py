#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:12:27 2017

@author: annakizilova
"""

class Track:
    '''
    compiles tracks from sessions, lunch and networking events
    takes:
    returns: a list of lists(tracks)
    '''
    def __init__(self, morning_session, afternoon_session):
        self.morning_session = morning_session
        self.afternoon_session = afternoon_session