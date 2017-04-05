#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:15:42 2017

@author: annakizilova
"""
import sys
from file_reader import FileReader
from talk_parser import TalkParser
from firstfit_scheduler import FirstFitScheduler

def main(argv):
    if len(argv) < 2:
        print('No argument given. Please specify name of a file with conference talks')
        return 1
    text = FileReader(argv[1]).getText()
    talkList = TalkParser(text).parseTalks()
    tracks = FirstFitScheduler(talkList).formTracks()
    for item in tracks:
        print(item)

if __name__ == "__main__":
    main(sys.argv)