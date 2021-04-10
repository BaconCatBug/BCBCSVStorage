# coding=utf-8
from csv import QUOTE_ALL
from pandas import read_csv
from time import sleep

google_sheet_id = '1f8OJIQhpycljDQ8QNDk_va1GJ1u7RVoMaNjFcHH0LKk'
# Soul Breaks

sheet_gid_SB = "344457459"
sheet_gid_CM = "1373487754"
sheet_gid_AB = "1933803309" 
sheet_gid_MG = "195881060"
sheet_gid_LM = "1881349203"
sheet_gid_LB = "258757653"
sheet_gid_SY = "13552509"
sheet_gid_other = "2001933731"
sheet_gid_status = "1899148923"


url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_AB
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Type","Target","Formula","Multiplier","Element","Time","Effects","Auto Target","SB","Max","ID"]]
df_export = selected_columns.copy()
df_export.to_csv('Abilities_Processed.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_CM
df_import = read_csv(url, dtype=str)
df_import["Element"].replace({"-":"NE"},inplace=True)
selected_columns = df_import[["Character","Source","Img","Name","Type","Target","Formula","Multiplier","Element","Time","Effects","Counter","Auto Target","SB","School","Name (JP)","ID"]]
df_export = selected_columns.copy()
df_export.to_csv('Commands.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_LM
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["ID","Character","Name","Effect"]]
df_export = selected_columns.copy()
df_export.to_csv('LegendMateria.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_MG
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Passive 1","Passive 2","Passive 3","Magicite Ultra Skill","Type","Auto Target","Multiplier","Time","Effects","Formula","ID"]]
df_export = selected_columns.copy()
df_export.to_csv('Magicite_Processed.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_SB
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Realm","Character","Img","Name","Tier","Type","Target","Formula","Multiplier","Element","Time","Effects","Counter","Auto Target","Points","Mastery Bonus","Honing Effects","Relic","Name (JP)","ID"]]
df_export = selected_columns.copy()
df_export.to_csv('SoulBreaks.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_LB
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Realm","Character","Name","Tier","Type","Target","Formula","Multiplier","Element","Time","Effects","Counter","Auto Target","Minimum LB Points","Limit Break Bonus","Mastery Bonus","Relic","Name (JP)","ID"]]
df_export = selected_columns.copy()
df_export.drop(df_import.tail(16).index, inplace = True) 
df_export.to_csv('LimitBreaks.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_SY
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Character","Source","Name","Synchro Ability Slot","Synchro Condition","Type","Target","Formula","Multiplier","Element","Time","Effects","Counter","Auto Target","SB","School","Name (JP)","ID","Synchro Condition ID"]]
df_export = selected_columns.copy()
df_export.to_csv('SyncCommands.csv', index=None, header=True, quoting=QUOTE_ALL)

#"""
sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_other
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Source","Name","Type","Target","Formula","Multiplier","Element","Time","Effects","Counter","Auto Target","SB","School","ID"]]
df_export = selected_columns.copy()
df_export.to_csv('Other.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_status
df_import = read_csv(url, dtype=str)
selected_columns = df_import[["Common Name","Effects","Default Duration","MND Modifier","Exclusive Status","ID"]]
df_export = selected_columns.copy()
df_export.to_csv('Status.csv', index=None, header=True, quoting=QUOTE_ALL)
#"""
