# This script is an example of writing a logfile when an error occurs
import traceback

try:
    raise Exception('This is the error message.')
except:
     errorFile = open('errorInfo.txt', 'w')
     errorFile.write(traceback.format_exc())
     errorFile.close()
     print('The traceback info was written to errorInfo.txt.')