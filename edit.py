import os
import sys
import fileinput

path = 'C:\\Users\\dario\\AWE.txt'
for line in fileinput.input(path, inplace=1):
    sys.stdout.write(line.replace('h4', ''))
