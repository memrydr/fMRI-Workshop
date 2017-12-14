#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:33 2017

@author: saraappleton-knapp
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
#Do something cool
    print('Hello data in the path '+basedir)
def main():
#load in all the global variables prepro needs, right now this is just the path to the data
    basedir='/Users/sappleton-knapp/fMRI_workshop/'
    prepro(basedir) #call prepro to do cool things
    
main()
input=glob.glob('/Users/saraappleton-knapp/Documents/CHEAR/fMRI workshop/data1/sub-*/func/sub-*bart*.nii.gz')
print(input[0:10])

x=input[0]
print('my path is '+x)
y=x.split('/')
print (y)
sub=y[7]

#whatcomp=y[2]
#sub=y[5]
#print sub

sub=input[0].split('/')[7]
print(sub)

subtask=input[1].split('/')[9].split('.')[0]
#subtask=subtask.strip('.nii.gz')
print(subtask)

output=subtask+'_brain'
print(output)
os.system('bet %s %s -F'%(x, output))

basedir='/Users/saraappleton-knapp/Documents/CHEAR/fMRI workshop/data1'
path=os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')
print(path)
input=glob.glob(path)
len(input[1:5])
print(input)
#os.path.exists(basedir)

def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*.nii.gz')):
        input=item
        output_path=item.strip('.nii.gz')
        output=output_path+('_brain')
        print(output)
        subprocess.check_call("/usr/local/fsl/bin/bet '%s' '%s' -F -m"%(input, output), shell=True)
def main():
    basedir='/Users/saraappleton-knapp/Documents/CHEAR/fMRI workshop/data1'
    prepro(basedir)
main()