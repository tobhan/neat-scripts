#! /usr/bin/python

# Takes a string of the following format:
#
#   folder.of.stuff.2008
#
# And returns a string using a naming convention that Plex can read properly:
#
#   folder of stuff
#
# Splits a string using '.' as delimiter, searches for numbers and returns
# every item with a lower index than the number in the range.
#
# The string return from this function is then used in plexfolder.py, where the folder is created.

plexfoldername = []
numberindex = 0
import re, sys
def foldername(filefolder):
    #
    split = filefolder.split('.')
    regex = re.compile(r'\d+')
    numbers = regex.findall(filefolder)
    for number in numbers:
        if 1960 <= int(number) <= 2018:
            numberindex = split.index(number)
    
    for string in split:
        if split.index(string) < numberindex:
            plexfoldername.append(string)
    return ' '.join(plexfoldername)
