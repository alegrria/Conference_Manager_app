#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:50:47 2017

@author: annakizilova
"""

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