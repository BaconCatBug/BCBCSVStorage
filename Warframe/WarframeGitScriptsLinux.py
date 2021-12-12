from datetime import datetime
from os import system

start_time = datetime.now() 
now = datetime.now()
now = str(now.year) +'-'+ f"{now.month:02d}" +'-'+ f"{now.day:02d}"
# print(now)

# print('python WarframeScripts.py')
system('python3 WarframeScripts.py')
#print ('WarframeCSVtoTSV.py')
system('python3 WarframeCSVtoTSV.py')
# print('git add *')
system('git add *')
# print("git commit -m 'now'")
system('git commit -m "' + now + '"')
# print('git push')
system('git push')
end_time = datetime.now()
with open("execution.log", "w") as text_file:
    text_file.write('Duration: {}'.format(end_time - start_time))
