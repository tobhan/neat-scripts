#! /usr/bin/python

# Uses the string returned from filename.py to create a folder that Plex can index.
# 
# Accepts a string as an argument and uses that as the source directory
# The destination directory is created using the foldername() function from filename.py

import os, sys, shutil
# Import function from filename.py
from filename import foldername
folderarg = sys.argv[1]

# Destination for file copy
path = '/var/db/plexdata/Plex\ Media\ Server/Movies/' + foldername(folderarg)
print(path)

# Try to copy files in folder to destination, return errors.
try:
    shutil.copytree(folderarg, path)

except shutil.Error as e:
    print('Directory not copied. Error: %s' % e)

except OSError as e:
    print('Directory not copied. Error: %s' % e)
