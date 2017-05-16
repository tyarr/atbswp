#! python3

# Project: Renaming Files with American-Style Dates to European-Style Dates
# Script that searches all the filenames in the current working directory for American style dates
# When one is found, it renames the file with the month and day swapped to make it European-style

import re, os, shutil

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('C:\\Users\\tyarboro\\Documents\\scripts\\testfolder'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.