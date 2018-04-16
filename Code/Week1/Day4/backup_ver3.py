import os
import time


source=['"C:\\Users\\Karlo\\Desktop\\New folder"']

target_dir='C:\\Users\\Karlo\\Desktop\\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)


target=target_dir+'nameofzip'+'.zip'



zip_command='zip -r {0} {1}'.format(target,' '.join(source))

print('Zip commant is:',zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successfully backup to',target)
else:
    print('Backup FAILED')