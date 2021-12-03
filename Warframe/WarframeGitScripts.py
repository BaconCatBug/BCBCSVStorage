from datetime import datetime
from os import system

now = datetime.now()
now = str(now.year) +'-'+ f"{now.month:02d}" +'-'+ f"{now.day:02d}"
# print(now)

# print('python WarframeScripts.py')
system('python WarframeScripts.py')
#print ('WarframeCSVtoTSV.py')
system('python WarframeCSVtoTSV.py')
# print('git add *')
system('git add *')
# print("git commit -m 'now'")
system('git commit -m "' + now + '"')
# print('git push')
system('git push')