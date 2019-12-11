# coding=utf-8
from csv import QUOTE_ALL
from numpy import where, ceil
from pandas import read_csv, to_numeric, concat

google_sheet_id = '1f8OJIQhpycljDQ8QNDk_va1GJ1u7RVoMaNjFcHH0LKk'
# Soul Breaks

sheet_gid_SB= "344457459"
sheet_gid_effects = "1899148923"


url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_SB
df_sb = read_csv(url, dtype=str)
df_sb.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)
df_sb.drop(df_import.columns[len(df_import.columns)-1], axis=1, inplace=True)

url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=csv&gid=' + sheet_gid_effects
df_effects = read_csv(url, dtype=str)
df_sb.to_csv('SoulBreaks.csv', index=None, header=True, quoting=QUOTE_ALL)
