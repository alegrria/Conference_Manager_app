#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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