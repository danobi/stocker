#!/usr/bin/python
import stocker
import os.path
import yql

#This function assumes that filename is valid and not currently in use
def export_csv(filename,data):
    myfile = open(filename,'a')
    for i in range(0,len(data)):
        myfile.write('\n' + data[i])
    myfile.close()
