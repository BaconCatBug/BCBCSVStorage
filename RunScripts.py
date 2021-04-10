from datetime import datetime
from os import system

now = datetime.now()
now = str(now.year) +'-'+ f"{now.month:02d}" +'-'+ f"{now.day:02d}"
# print(now)

# print('FFRK_Relic_Data_Format')
#system('python FFRK_Relic_Data_Format.py')
# print('FFRK_Soul_Break_etc_Data_Format')
#system('python FFRK_Soul_Break_etc_Data_Format.py')
# print('git add *')
system('git add *')
# print("git commit -m 'now'")
system('git commit -m "' + now + '"')
# print('git push')
system('git push')
