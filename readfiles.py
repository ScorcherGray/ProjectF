import sys
from os import listdir, walk
from os.path import isfile, join
import sqlite3
import glob

if __name__ == '__main__':
    args = sys.argv

directory = args[1]

onlyfiles = [f for f in listdir(directory) if isfile(join(directory,f))]

directories = [d for d in walk(directory) if d not in onlyfiles]
    