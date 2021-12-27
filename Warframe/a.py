from csv import QUOTE_ALL  # Needed to export data to CSV
from bs4 import BeautifulSoup  # Needed to parse the dynamic webpage of the Ducanator
from requests import get  # Needed to get the webpage of the Ducanator
from re import search  # Needed to find the json string to import into pandas
from pandas import merge, read_csv, set_option, concat, DataFrame, read_json, read_html, ExcelWriter, \
    option_context, json_normalize # Needed to convert the json string into a usable dataframe object for manipulation
from traceback import format_exc  # Needed for more friendly error messages.
from openpyxl import load_workbook
from numpy import arange
from os import path
from time import sleep
from datetime import datetime
import lxml
import cchardet
from json import dumps, loads

url_relics = 'https://drops.warframestat.us/data/builds/d2f04a78f07d250cbb3537aaa20535a0.json'
retry_attempts = 10

for x in range(0, retry_attempts):
    try:
        url = get(url_relics)
    except Exception:
        print('Relic data download failed, retrying... ' + str(retry_attempts - x - 1) + ' attempts left...', end='\r')

text = url.text
data = loads(text)
data = data['relics']
templist = []
templist2 = []
mergelist = []

df_nested_list = json_normalize(data, record_path=['rewards'],meta=['tier','relicName','state'])
patternDel = 'Intact'
filter_df = df_nested_list['state'].str.contains(patternDel)
df_nested_list = df_nested_list[filter_df]
patternDel = 'Requiem'
filter_df = df_nested_list['tier'].str.contains(patternDel)
df_nested_list = df_nested_list[~filter_df]
df_nested_list = df_nested_list.sort_values(by=['tier','relicName','chance'], ascending=[True,True,False])
df_nested_list = df_nested_list[['tier','relicName','itemName','chance']].reset_index(drop=True)
df_nested_list = df_nested_list.values.tolist()

templist = []
templist2 = []
for count, elem in enumerate(df_nested_list):
    if (count+1) % 6 == 0 and count !=0:
        templist.append(elem[2])
        templist.append(elem[0])
        templist.append(elem[1])
        templist2.append(templist)
        templist = []
    else:
        templist.append(elem[2])

df_relics = DataFrame(templist2, columns=['C1','C2','C3','U1','U2','Rare','Class','Type'])
df_relics = df_relics[['Class','Type','C1','C2','C3','U1','U2','Rare']]

df_relics = df_relics.replace(to_replace=r'Systems Blueprint', value=r'Systems', regex=True)
df_relics = df_relics.replace(to_replace=r'Neuroptics Blueprint', value=r'Neuroptics', regex=True)
df_relics = df_relics.replace(to_replace=r'Chassis Blueprint', value=r'Chassis', regex=True)
df_relics = df_relics.replace(to_replace=r'Cerebrum Blueprint', value=r'Cerebrum', regex=True)
df_relics = df_relics.replace(to_replace=r'Carapace Blueprint', value=r'Carapace', regex=True)
df_relics = df_relics.replace(to_replace=r'Buckle Blueprint', value=r'Buckle', regex=True)
df_relics = df_relics.replace(to_replace=r'Band Blueprint', value=r'Band', regex=True)
df_relics = df_relics.replace(to_replace=r'Wings Blueprint', value=r'Wings', regex=True)
df_relics = df_relics.replace(to_replace=r'Harness Blueprint', value=r'Harness', regex=True)


df_relics.to_csv('Prime-Relic Data.csv', index=None, quoting=QUOTE_ALL)
