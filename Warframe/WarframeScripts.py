# Install python 3, duh!
# Run the command below in a cmd window to install the needed packages, without the #, duh!
# pip install bs4 requests pandas openpyxl lxml html5lib
# Run the python file with the included batch file, DUH!
try:
    # Error handling if something happens during script initialisation
    from csv import QUOTE_ALL  # Needed to export data to CSV
    from bs4 import BeautifulSoup  # Needed to parse the dynamic webpage of the Ducanator
    from requests import get  # Needed to get the webpage of the Ducanator
    from re import search  # Needed to find the json string to import into pandas
    from pandas import merge, read_csv, set_option, concat, DataFrame, read_json, read_html, ExcelWriter,option_context  # Needed to convert the json string into a usable dataframe object for manipulation
    from traceback import format_exc  # Needed for more friendly error messages.
    from openpyxl import load_workbook
    from numpy import arange
    from os import path
    from time import sleep
    from datetime import datetime
    import lxml
    import cchardet
    from json import dumps
except ModuleNotFoundError:
    print('OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!')
    print('You didn\'t install the packages like I told you to. Please run \"pip install bs4 requests pandas\" in a cmd window to install the required packages!')
    print('\033[1;31m' + format_exc())
    exit(1)

try:
    startTime = datetime.now()
    #User Variables
    csv_name = 'Prime-Relic Data.csv'
    sheet_name_relic = 'Relic_Data'
    retry_attempts = 10
    order_type = 'buy'

    # Sets the URL to scrape, because hard-coding is bad
    url_ducats = "https://warframe.market/tools/ducats"
    # Scrapes the given URL
    soup = str(BeautifulSoup(get(url_ducats).content, "lxml")).replace('\n', '')
    # Finds the needed json string for item data, previous hour data, and previous day data.
    # Slices off the first bit to make a valid json string for pandas later
    items = search('"items": (\[(?:\[??[^\[]*?\]))', soup).group(0)[9:]
    previous_hour = search('"previous_hour": (\[(?:\[??[^\[]*?\]))', soup).group(0)[17:]
    previous_day = search('"previous_day": (\[(?:\[??[^\[]*?\]))', soup).group(0)[16:]

    # Reads and sanitises the item data into a pandas dataframe
    df_items = read_json(items)
    df_items2 = read_json(items)
    df_items = df_items.drop(columns=['url_name', 'thumb'])
    df_items = df_items.reindex(columns=['id', 'item_name'])

    # Reads and sanitises the previous hour data into a pandas dataframe
    df_previous_hour = read_json(previous_hour)
    df_previous_hour = df_previous_hour.drop(columns=['id', 'plat_worth', 'median'])
    df_previous_hour = df_previous_hour.rename(columns={'item': 'id'})

    # Merges the item data and previous hour data on the id column, drops the redundant id column, then renames the column names for export
    df_previous_hour_merged = df_items.merge(df_previous_hour, how='inner', on='id')
    df_items2 = df_items2.merge(df_previous_hour, how='inner', on='id')
    df_ids = df_items2.merge(df_previous_hour, how='inner', on='id')
    patternDel = '.+ Set$'
    filter_df = df_items2['item_name'].str.contains(patternDel)
    df_items2 = df_items2[~filter_df]
    df_items2 = df_items2['url_name']
    df_items2 = DataFrame(df_items2).sort_values(by=['url_name'])
    df_items2 = df_items2.reset_index(drop=True)
    df_items2 = df_items2['url_name'].values.tolist()
    list_orders = []
    list_prepandas = []
    for count, elem1 in enumerate(df_items2):
        for x in range(1, retry_attempts):
            try:
                sleep(0.15)
                temp_json = get('https://api.warframe.market/v1/items/' + elem1 + '/orders').json()
                break
            except Exception:
                print(elem1+' Item data download failed, retrying... ' + str(retry_attempts - x - 1) + ' attempts left...', end='\r')
        for elem2 in temp_json['payload']['orders']:
            if elem2['order_type'] == order_type and elem2['user']['status'] == 'ingame':
                list_orders.append(elem2['platinum'])
        list_orders.sort()
        try:
            list_order_value = sum(list_orders[-2:])/len(list_orders[-2:])
        except ZeroDivisionError:
            list_order_value = 0
        list_prepandas.append([elem1, list_order_value])
        list_orders = []
    df_plat = merge(DataFrame(list_prepandas), df_ids, left_on=0, right_on='url_name')
    df_plat = df_plat[['item_name','ducats_x',1]]
    df_plat['ducats_per_plat'] = round(df_plat['ducats_x']/df_plat[1],2)
    df_plat = df_plat.set_axis(['Item Name','Ducats','Top Buy Order Average','Ducats per Plat'], axis=1)
    df_previous_hour_merged = df_previous_hour_merged.drop(columns=['id'])
    df_previous_hour_merged = df_previous_hour_merged.reindex(columns=['item_name', 'datetime', 'ducats_per_platinum', 'ducats', 'wa_price','ducats_per_platinum_wa', 'position_change_month', 'position_change_week', 'position_change_day', 'volume'])
    df_previous_hour_merged = df_previous_hour_merged.sort_values(by='item_name')
    df_previous_hour_merged['datetime'] = df_previous_hour_merged['datetime'].astype(str).str[:-6]
    df_previous_hour_merged = df_previous_hour_merged.drop(columns=['datetime','ducats_per_platinum','position_change_month','position_change_week','position_change_day','volume'])
    patternDel = '.+ Set$'
    filter_df = df_previous_hour_merged['item_name'].str.contains(patternDel)
    df_previous_hour_merged = df_previous_hour_merged[~filter_df]
    df_previous_hour_merged = df_previous_hour_merged.reset_index(drop=True)

    #url_relics = 'https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html'
    url_relics = 'http://web.archive.org/web/20211218105219/https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html'
    relic_data_txt_name = 'RelicData.txt'

    for x in range(0, retry_attempts):
        try:
            soup = str(BeautifulSoup(get(url_relics).content, "lxml")).replace('\n', '')
        except Exception:
            print('Relic data download failed, retrying... ' + str(retry_attempts - x - 1) + ' attempts left...', end='\r')

    parsed_relics = search('<h3 id="relicRewards">Relics:</h3><table>.*?</table>', soup).group(0)[34:].replace('th>', 'td>').replace(r'<th colspan="2">', r'<td>').replace('X Kuva', 'x Kuva')
    df_parsed_relics = read_html(parsed_relics, header=None)
    df_parsed_relics = df_parsed_relics[0].replace(to_replace=r'.+\((.+)\%\)', value=r'\1', regex=True)
    df_parsed_relics[1] = df_parsed_relics[1].astype(float)
    df_parsed_relics = df_parsed_relics.dropna(how='all').fillna(999)
    groups = df_parsed_relics.groupby(arange(len(df_parsed_relics.index)) // 7, sort=False).apply(lambda x: x.sort_values(by=1, ascending=False))
    groups[1] = ' (' + groups[1].astype(str) + '%)'
    groups = groups[0] + groups[1]
    groups = groups.replace(to_replace=r'\(999.0\%\)', value=r'', regex=True)
    templist = []
    templist2 = []
    for count, value in enumerate(groups):
        if count % 7 == 0 and count != 0:
            templist2.append(templist)
            templist = []
        templist.append(value)
    df_even_more_parsed_relics = DataFrame(templist2, columns=['Relic_Name', 'C1', 'C2', 'C3', 'U1', 'U2', 'Rare'])
    df_relic_class = df_even_more_parsed_relics['Relic_Name'].str.split().str[0]
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'Class', df_relic_class, allow_duplicates=True)
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'Type', df_even_more_parsed_relics['Relic_Name'].str.upper().str.split().str[1], allow_duplicates=True)
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'Refinement', df_even_more_parsed_relics['Relic_Name'].str.split().str[3].replace(to_replace=r'[\(\)]', value=r'', regex=True), allow_duplicates=True)
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'C1_Raw', df_even_more_parsed_relics['C1'].replace(to_replace=r' \(.+\)',value='',regex=True))
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'C2_Raw', df_even_more_parsed_relics['C2'].replace(to_replace=r' \(.+\)',value='',regex=True))
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'C3_Raw', df_even_more_parsed_relics['C3'].replace(to_replace=r' \(.+\)',value='',regex=True))
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'U1_Raw', df_even_more_parsed_relics['U1'].replace(to_replace=r' \(.+\)',value='',regex=True))
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'U2_Raw', df_even_more_parsed_relics['U2'].replace(to_replace=r' \(.+\)',value='',regex=True))
    df_even_more_parsed_relics.insert(len(df_even_more_parsed_relics.columns), 'Rare_Raw', df_even_more_parsed_relics['Rare'].replace(to_replace=r' \(.+\)',value='',regex=True))
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Systems Blueprint',value=r'Systems', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Neuroptics Blueprint',value=r'Neuroptics', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Chassis Blueprint',value=r'Chassis', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Cerebrum Blueprint',value=r'Cerebrum', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Carapace Blueprint',value=r'Carapace', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Buckle Blueprint',value=r'Buckle', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Band Blueprint',value=r'Band', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Wings Blueprint',value=r'Wings', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.replace(to_replace=r'Harness Blueprint',value=r'Harness', regex=True)
    df_even_more_parsed_relics = df_even_more_parsed_relics.drop(df_even_more_parsed_relics.loc[df_even_more_parsed_relics['Refinement'] == 'Exceptional'].index)
    df_even_more_parsed_relics = df_even_more_parsed_relics.drop(df_even_more_parsed_relics.loc[df_even_more_parsed_relics['Refinement'] == 'Flawless'].index)
    df_even_more_parsed_relics = df_even_more_parsed_relics.drop(df_even_more_parsed_relics.loc[df_even_more_parsed_relics['Refinement'] == 'Radiant'].index)
    df_even_more_parsed_relics = df_even_more_parsed_relics.drop(df_even_more_parsed_relics.loc[df_even_more_parsed_relics['Class'] == 'Requiem'].index)
    df_even_more_parsed_relics = df_even_more_parsed_relics.drop(columns=['Relic_Name','C1','C2','C3','U1','U2','Rare','Refinement'])
    
    # Export data
    print('Exporting Worksheet')
    df_even_more_parsed_relics.to_csv(csv_name, index=None, quoting=QUOTE_ALL)
    df_plat.to_csv('HourPrices.csv', index=None, quoting=QUOTE_ALL)
    print(datetime.now() - startTime)

except Exception:
    # Error handling if something happens during the main script
    print('OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!')
    print('\033[1;31m' + format_exc())
    exit(1)
