#!/usr/bin/python3
# backupToZip.py - Copies an entire folder and its contents into a zip
# whose filename increments

import zipfile,os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number = number+1
    print('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')

    for folderName,subfilename,filenames in os.walk(folder):
        print('Adding files in %s...'%(folderName))
        backupZip.write(folderName)
        for filename in filenames:
            newBase / os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.startswith('.zip'):
                continue
            backupZip.write(os.path.join(folderName,filename))
    backupZip.close()
    print('Done')
