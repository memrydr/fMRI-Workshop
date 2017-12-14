#!/usr/bin/python
 
# This script will generate each subjects design.fsf, but does not run it.
# It depends on your system how will launch feat 
import os
import glob
 
# Set this to the directory all of the sub### directories live in
studydir = '/Users/saraappleton-knapp/Desktop/Scripts/FSL_tutorial_data/'
 
# Set this to the directory where you'll dump all the fsf files
# May want to make it a separate directory, because you can delete them all o
#   once Feat runs
fsfdir="%s/fsfs"%(studydir)
 
# Get all the paths!  Note, this won't do anything special to omit bad subjects
subdirs=glob.glob("%s/sub[0-9][0-9][0-9]"%(studydir))
print(subdirs)
 
for dir in list(subdirs):
  splitdir = dir.split('/')
  # YOU WILL NEED TO EDIT THIS TO GRAB sub001
#  splitdir_sub = splitdir[8]
  subnum=dir[-3:]
  print(subnum)
  #  YOU WILL ALSO NEED TO EDIT THIS TO GRAB THE PART WITH THE RUNNUM
#  ntime = os.popen('fslnvols %s/bold.nii.gz'%(dir)).read().rstrip()
  replacements = {'SUBNUM':subnum}
  with open("%s/template.fsf"%(fsfdir)) as infile: 
    with open("%s/design_sub%s.fsf"%(fsfdir, subnum), 'w') as outfile:
        for line in infile:
          # Note, since the video, I've changed "iteritems" to "items"
          # to make the following work on more versions of python
          #  (python 3 no longer has iteritems())  
          for src, target in replacements.items():
            line = line.replace(src, target)
          outfile.write(line)
          
  dir=subdirs[0]
  print(dir)