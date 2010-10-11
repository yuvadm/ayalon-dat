
# 1. pre-condition : work by year, all files deployed on file system
# 2. un-gzip all files (by default, into same directory, overriding .gz files)
# 3. rename all TCSC files to TCSC.dmp (prepare for imp)
# 4. for each TCSC.dmp file:
#   4.1. call imp on each single file (guaranteed to be < ~300MB)
#   4.2. for each table (need to create hard-coded list)
#       4.2.1. SELECT * FROM table
#       4.2.2. save aside, or throw into new db
#   4.3. dump all tables (make room for next iteration)


import os
import sys
import subprocess

RAW_DATA_BASE_DIR = "/base/dir/location" # update this

def importYear(year):
    yearDir = os.path.join(RAW_DATA_BASE_DIR, str(year))
    print yearDir
    
importYear(2005)


