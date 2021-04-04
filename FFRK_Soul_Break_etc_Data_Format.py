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
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.to_csv('Abilities.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_CM
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import["Element"].replace({"-":"NE"},inplace=True)
df_import.to_csv('Commands.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_LM
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.to_csv('LegendMateria.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_MG
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.to_csv('Magicite.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_SB
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.to_csv('SoulBreaks.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_LB
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop('Img', axis=1, inplace=True)
df_import.drop(df_import.tail(16).index, inplace = True) 
df_import.to_csv('LimitBreaks.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_other
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[2], axis=1, inplace=True)
df_import.to_csv('Other.csv', index=None, header=True, quoting=QUOTE_ALL)

sleep(1)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_status
df_import = read_csv(url, dtype=str)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_import.to_csv('Status.csv', index=None, header=True, quoting=QUOTE_ALL)
