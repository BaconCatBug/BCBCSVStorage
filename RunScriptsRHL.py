from datetime import datetime
from os import system

now = datetime.now()
now = str(now.year) +'-'+ str(now.month) +'-'+ str(now.day)
# print('FFRK_Relic_Data_Format')
system('python3 FFRK_Relic_Data_Format.py')
# print('FFRK_Soul_Break_etc_Data_Format')
system('python3 FFRK_Soul_Break_etc_Data_Format.py')
# print('git add *.csv')
system('git add *')
# print("git commit -m 'now'")
system('git commit -m "' + now + '"')
# print('git push')
system('git push')
