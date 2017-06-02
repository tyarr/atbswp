#! python3
# Write a webpage to a file

import requests

# request to get the file
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# check status to ensure it was successful in pulling
res.raise_for_status()
# create the file in binary mode 
playFile = open('RomeoAndJuliet.txt', 'wb')
# inter_content method returns chunks of the content on each iteration through the loop
for chunk in res.iter_content(100000):
        playFile.write(chunk)
# close the created file
playFile.close()