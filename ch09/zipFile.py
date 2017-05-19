import zipfile,os

os.chdir('C:\\Users\\tyarboro\\Documents\\scripts\\testfolder') # change directory to example.zip

exampleZip = zipfile.ZipFile('example.zip')

exampleZip.namelist()