import os
import time

source=['"D:\\--python\\Day 4"']

targer_dir='D:\\--python\\backup2'

if not os.path.exists(targer_dir):
    os.mkdir(targer_dir)

today=targer_dir+os.sep+time.strftime('%Y%d%m')
now=time.strftime('%H%M%S')

targer=today+os.sep+now+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully creaded directory',today)

zip_command='zip -r {0} {1}'.format(targer,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command)==0:
    print('Successful backup to',targer)
else:
    print('Backup FAILED')