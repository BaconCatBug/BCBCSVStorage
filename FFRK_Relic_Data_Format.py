# coding=utf-8
from csv import QUOTE_ALL
from numpy import where, ceil
from pandas import read_csv, to_numeric, concat
# Initialisation

# print('Format Start')
google_sheet_id = '1f8OJIQhpycljDQ8QNDk_va1GJ1u7RVoMaNjFcHH0LKk'
sheet_id_RL = '1623354916'
sheet_id_HA = '559973931'
url = 'https://docs.google.com/spreadsheets/d/' + \
    google_sheet_id + '/export?format=csv&gid=' + sheet_id_RL
    
url2 = 'https://docs.google.com/spreadsheets/d/' + \
    google_sheet_id + '/export?format=csv&gid=' + sheet_id_HA

df_import_relics = read_csv(url, dtype=str)
df_import_ha = read_csv(url2, dtype=str)
df_import_ha.rename(columns={'Fixed Passive Effects':'Effect'}, inplace=True)
df_import_ha.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" | "," | "], regex=True, inplace=True)
df_import = concat([df_import_relics, df_import_ha], axis=0, ignore_index=True)
# Maps
correctedTypeMap = {'Dagger': '1 ', 'Sword': '1 ', 'Katana': '1 ', 'Axe': '1 ', 'Hammer': '1 ', 'Spear': '1 ',
                    'Fist': '1 ', 'Rod': '1 ', 'Staff': '1 ', 'Bow': '1', 'Instrument': '1', 'Whip': '1',
                    'Thrown': '1', 'Book': '1', 'Gun': '1', 'Blitzball': '1', 'Hairpin': '1', 'Gun-Arm': '1',
                    'Gambling Gear': '1', 'Doll': '1', 'Shield': '2', 'Hat': '2', 'Helm': '2',
                    'Light Armor': '2', 'Heavy Armor': '2', 'Robe': '2', 'Bracer': '2', 'Accessory': '3'}

correctedTypeMap2 = {'Dagger': 'Weapon', 'Sword': 'Weapon', 'Katana': 'Weapon', 'Axe': 'Weapon',
                     'Hammer': 'Weapon', 'Spear': 'Weapon', 'Fist': 'Weapon', 'Rod': 'Weapon',
                     'Staff': 'Weapon', 'Bow': 'Weapon', 'Instrument': 'Weapon', 'Whip': 'Weapon',
                     'Thrown': 'Weapon', 'Book': 'Weapon', 'Gun': 'Weapon', 'Blitzball': 'Weapon',
                     'Hairpin': 'Weapon', 'Gun-Arm': 'Weapon', 'Gambling Gear': 'Weapon', 'Doll': 'Weapon',
                     'Shield': 'Armor', 'Hat': 'Armor', 'Helm': 'Armor', 'Light Armor': 'Armor',
                     'Heavy Armor': 'Armor', 'Robe': 'Armor', 'Bracer': 'Armor', 'Accessory': 'Accessory'}

correctedCategoryMap = {'Dagger': '1 ', 'Sword': '2 ', 'Katana': '3 ', 'Axe': '4 ', 'Hammer': '5 ', 'Spear': '6 ',
                        'Fist': '7 ', 'Rod': '8 ', 'Staff': '9 ', 'Bow': '10', 'Instrument': '11', 'Whip': '12',
                        'Thrown': '13', 'Book': '14', 'Gun': '15', 'Blitzball': '16', 'Hairpin': '17', 'Gun-Arm': '18',
                        'Gambling Gear': '19', 'Doll': '20', 'Shield': '21', 'Hat': '22', 'Helm': '23',
                        'Light Armor': '24', 'Heavy Armor': '25', 'Robe': '26', 'Bracer': '27', 'Accessory': '28'}

correctedRealmMap = {'Core': '0', 'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'VII': '7',
                     'VIII': '8', 'IX': '9', 'X': '10', 'XI': '11', 'XII': '12', 'XIII': '13', 'XIV': '14', 'XV': '15',
                     'FFT': '50', 'KH': '70', 'Type-0': '60', 'Beyond': '90', '-': '99'}

correctedRarityMap = {'S': '100', '8': '8', '7': '7',
                      '6': '6', '5': '5', '4': '4', '3': '3', '2': '2', '1': '1'}

synergyMap = {'3': 15, '5': 20, '10': 30, '15': 40, '20': 50, '25': 60, '30': 70, '35': 80, '40': 90,
              '45': 100, '50': 110, '55': 120}

# Stuff
df_base = df_import[['ID']]
df_base = df_base.rename(columns={'ID': 'ID_Zero'})
df_base['Brar'] = df_import[['Brar']].fillna(0)
df_base['Blvl'] = df_import[['Blv']].fillna(0)
df_base['Batk'] = df_import[['Batk']].fillna(0)
df_base['Bdef'] = df_import[['Bdef']].fillna(0)
df_base['Bmag'] = df_import[['Bmag']].fillna(0)
df_base['Bres'] = df_import[['Bres']].fillna(0)
df_base['Bmnd'] = df_import[['Bmnd']].fillna(0)
df_base['Bacc'] = df_import[['Bacc']].fillna(0)
df_base['Beva'] = df_import[['Beva']].fillna(0)
df_base['Mrar'] = df_import[['Mrar']].fillna(0)
df_base['Mlvl'] = df_import[['Mlv']].fillna(0)
df_base['Matk'] = df_import[['Matk']].fillna(0)
df_base['Mdef'] = df_import[['Mdef']].fillna(0)
df_base['Mmag'] = df_import[['Mmag']].fillna(0)
df_base['Mres'] = df_import[['Mres']].fillna(0)
df_base['Mmnd'] = df_import[['Mmnd']].fillna(0)
df_base['Macc'] = df_import[['Macc']].fillna(0)
df_base['Meva'] = df_import[['Meva']].fillna(0)
df_base['GL'] = df_import[['GL']].fillna(0)
df_base = df_base.drop(
    df_base[(df_base.ID_Zero == '21030005') & (df_base.GL == "x")].index)
df_base = df_base.drop(
    df_base[(df_base.ID_Zero == '22051070') & (df_base.GL == "x")].index)
df_base = df_base.drop('GL', 1)


df_base['ID'] = df_import[['ID']] + '0'
# df_base['Name'] = ''
df_base['Name'] = df_import[['Name']]
df_base['Realm'] = df_import[['Realm']]
df_base['Rarity'] = df_base['Brar'].map(correctedRarityMap)
df_base['BaseRarity'] = df_base['Brar'].map(correctedRarityMap)
df_base['Type'] = df_import['Type'].map(correctedTypeMap2)
df_base['Category'] = df_import[['Type']]

df_base['Level'] = df_base['Blvl']
df_base['Atk'] = df_base['Batk']
df_base['Def'] = df_base['Bdef']
df_base['Mag'] = df_base['Bmag']
df_base['Res'] = df_base['Bres']
df_base['Mnd'] = df_base['Bmnd']
df_base['Acc'] = df_base['Bacc']
df_base['Eva'] = df_base['Beva']
df_base['Effect'] = ''
df_base['Character'] = ''
df_base['SoulBreak'] = ''
df_base['LegendMateria'] = ''
df_base['Synergy'] = 'No'
df_base['CorrectedType'] = df_base['Category'].map(correctedTypeMap)
df_base['CorrectedCategory'] = df_base['Category'].map(correctedCategoryMap)
df_base['CorrectedRealm'] = df_base['Realm'].map(correctedRealmMap)
df_base['Realm'] = where(
    ((to_numeric(df_base['Rarity'])) == 100) & (
        to_numeric(df_base['CorrectedRealm']) == 99), 'Artifact',
    df_base['Realm'])
df_base['CorrectedRealm'] = where(
    ((to_numeric(df_base['Rarity'])) == 100) & (
        to_numeric(df_base['CorrectedRealm']) == 99), '100',
    df_base['CorrectedRealm'])

df_base['Level'] = where(to_numeric(df_base['Rarity']) == 1 & (to_numeric(df_base['CorrectedType']) != 3), '3',
                         df_base['Level'])
df_base['Level'] = where(
    (to_numeric(df_base['CorrectedType']) == 3), '1', df_base['Level'])
df_base['Level'] = where((to_numeric(df_base['Rarity']) > 1) & (to_numeric(df_base['Rarity']) < 10) & (
    to_numeric(df_base['CorrectedType']) != 3), (to_numeric(df_base['Rarity']) - 1) * 5, df_base['Level'])

df_base['Atk'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Batk']) + (
        to_numeric(df_base['Matk']) - to_numeric(df_base['Batk'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Atk'])

df_base['Def'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Bdef']) + (
        to_numeric(df_base['Mdef']) - to_numeric(df_base['Bdef'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Def'])

df_base['Mag'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Bmag']) + (
        to_numeric(df_base['Mmag']) - to_numeric(df_base['Bmag'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Mag'])

df_base['Res'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Bres']) + (
        to_numeric(df_base['Mres']) - to_numeric(df_base['Bres'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Res'])

df_base['Mnd'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Bmnd']) + (
        to_numeric(df_base['Mmnd']) - to_numeric(df_base['Bmnd'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Mnd'])

df_base['Acc'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Bacc']) + (
        to_numeric(df_base['Macc']) - to_numeric(df_base['Bacc'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Acc'])

df_base['Eva'] = where((to_numeric(df_base['Rarity']) < 101) & (
    to_numeric(df_base['CorrectedType']) != 3), ceil((to_numeric(df_base['Beva']) + (
        to_numeric(df_base['Meva']) - to_numeric(df_base['Beva'])) / ((to_numeric(df_base['Mlvl']) - 1) / (
            to_numeric(df_base['Level']) - 1)))), df_base['Eva'])

df_base['Effect'] = df_import[['Effect']]
df_base['Character'] = df_import[['Character']]
df_base['SoulBreak'] = df_import[['Soul Break']]
df_base['LegendMateria'] = df_import[['Legend Materia']]

#################################################
df_plus = df_base.copy()
df_plus['ID'] = df_plus['ID_Zero'] + '1'
# Name
# Realm
df_plus['Rarity'] = where(to_numeric(df_plus['CorrectedType']) != 3, to_numeric(df_plus['Rarity']) + 1,
                          df_plus['Rarity'])
# Base Rarity
# Type
# Category
df_plus['Level'] = where(to_numeric(df_plus['Rarity']) == 1 & (to_numeric(df_plus['CorrectedType']) != 3), '3',
                         df_plus['Level'])
df_plus['Level'] = where((to_numeric(df_plus['Rarity']) > 1) & (to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), (to_numeric(df_plus['Rarity']) - 1) * 5, df_plus['Level'])

df_plus['Atk'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Batk']) + (
        to_numeric(df_plus['Matk']) - to_numeric(df_plus['Batk'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Atk'])

df_plus['Def'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Bdef']) + (
        to_numeric(df_plus['Mdef']) - to_numeric(df_plus['Bdef'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Def'])

df_plus['Mag'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Bmag']) + (
        to_numeric(df_plus['Mmag']) - to_numeric(df_plus['Bmag'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Mag'])

df_plus['Res'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Bres']) + (
        to_numeric(df_plus['Mres']) - to_numeric(df_plus['Bres'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Res'])

df_plus['Mnd'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Bmnd']) + (
        to_numeric(df_plus['Mmnd']) - to_numeric(df_plus['Bmnd'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Mnd'])

df_plus['Acc'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Bacc']) + (
        to_numeric(df_plus['Macc']) - to_numeric(df_plus['Bacc'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Acc'])

df_plus['Eva'] = where((to_numeric(df_plus['Rarity']) < 10) & (
    to_numeric(df_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus['Beva']) + (
        to_numeric(df_plus['Meva']) - to_numeric(df_plus['Beva'])) / ((to_numeric(df_plus['Mlvl']) - 1) / (
            to_numeric(df_plus['Level']) - 1)))), df_plus['Eva'])

df_plus.drop(df_plus[to_numeric(df_plus.BaseRarity) > 99].index, inplace=True)
df_plus.drop(df_plus[to_numeric(df_plus.CorrectedType)
                     == 3].index, inplace=True)
##########################################
df_plus_plus = df_base.copy()
df_plus_plus['ID'] = df_plus_plus['ID_Zero'] + '2'
# Name
# Realm
df_plus_plus['Rarity'] = where(to_numeric(df_plus_plus['CorrectedType']) != 3,
                               to_numeric(df_plus_plus['Rarity']) + 2, df_plus_plus['Rarity'])
# Base Rarity
# Type
# Category
df_plus_plus['Level'] = where(
    to_numeric(df_plus_plus['Rarity']) == 1 & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), '3',
    df_plus_plus['Level'])
df_plus_plus['Level'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), (to_numeric(df_plus_plus['Rarity']) - 1) * 5,
    df_plus_plus['Level'])

df_plus_plus['Atk'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Batk']) + (
            to_numeric(df_plus_plus['Matk']) - to_numeric(df_plus_plus['Batk'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Atk'])

df_plus_plus['Def'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Bdef']) + (
            to_numeric(df_plus_plus['Mdef']) - to_numeric(df_plus_plus['Bdef'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Def'])

df_plus_plus['Mag'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Bmag']) + (
            to_numeric(df_plus_plus['Mmag']) - to_numeric(df_plus_plus['Bmag'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Mag'])

df_plus_plus['Res'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Bres']) + (
            to_numeric(df_plus_plus['Mres']) - to_numeric(df_plus_plus['Bres'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Res'])

df_plus_plus['Mnd'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Bmnd']) + (
            to_numeric(df_plus_plus['Mmnd']) - to_numeric(df_plus_plus['Bmnd'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Mnd'])

df_plus_plus['Acc'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Bacc']) + (
            to_numeric(df_plus_plus['Macc']) - to_numeric(df_plus_plus['Bacc'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Acc'])

df_plus_plus['Eva'] = where(
    (to_numeric(df_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus['CorrectedType']) != 3), ceil((to_numeric(df_plus_plus['Beva']) + (
            to_numeric(df_plus_plus['Meva']) - to_numeric(df_plus_plus['Beva'])) / ((to_numeric(
                df_plus_plus['Mlvl']) - 1) / (to_numeric(df_plus_plus['Level']) - 1)))), df_plus_plus['Eva'])

df_plus_plus.drop(df_plus_plus[to_numeric(
    df_plus_plus.BaseRarity) > 99].index, inplace=True)
df_plus_plus.drop(df_plus_plus[to_numeric(
    df_plus_plus.CorrectedType) == 3].index, inplace=True)
##########################################
df_plus_plus_plus = df_base.copy()
df_plus_plus_plus['ID'] = df_plus_plus_plus['ID_Zero'] + '3'
# Name
# Realm
df_plus_plus_plus['Rarity'] = where(to_numeric(df_plus_plus_plus['CorrectedType']) != 3,
                                    to_numeric(df_plus_plus_plus['Rarity']) + 3, df_plus_plus_plus['Rarity'])
# Base Rarity
# Type
# Category
df_plus_plus_plus['Level'] = where(
    to_numeric(df_plus_plus_plus['Rarity']) == 1 & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), '3',
    df_plus_plus_plus['Level'])
df_plus_plus_plus['Level'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3),
    (to_numeric(df_plus_plus_plus['Rarity']) - 1) * 5, df_plus_plus_plus['Level'])

df_plus_plus_plus['Atk'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Batk']) + (to_numeric(df_plus_plus_plus['Matk']) - to_numeric(
                df_plus_plus_plus['Batk'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Atk'])

df_plus_plus_plus['Def'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Bdef']) + (to_numeric(df_plus_plus_plus['Mdef']) - to_numeric(
                df_plus_plus_plus['Bdef'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Def'])

df_plus_plus_plus['Mag'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Bmag']) + (to_numeric(df_plus_plus_plus['Mmag']) - to_numeric(
                df_plus_plus_plus['Bmag'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Mag'])

df_plus_plus_plus['Res'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Bres']) + (to_numeric(df_plus_plus_plus['Mres']) - to_numeric(
                df_plus_plus_plus['Bres'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Res'])

df_plus_plus_plus['Mnd'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Bmnd']) + (to_numeric(df_plus_plus_plus['Mmnd']) - to_numeric(
                df_plus_plus_plus['Bmnd'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Mnd'])

df_plus_plus_plus['Acc'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Bacc']) + (to_numeric(df_plus_plus_plus['Macc']) - to_numeric(
                df_plus_plus_plus['Bacc'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Acc'])

df_plus_plus_plus['Eva'] = where(
    (to_numeric(df_plus_plus_plus['Rarity']) > 1) & (to_numeric(df_plus_plus_plus['Rarity']) < 10) & (
        to_numeric(df_plus_plus_plus['CorrectedType']) != 3), ceil((to_numeric(
            df_plus_plus_plus['Beva']) + (to_numeric(df_plus_plus_plus['Meva']) - to_numeric(
                df_plus_plus_plus['Beva'])) / ((to_numeric(df_plus_plus_plus['Mlvl']) - 1) / (
                    to_numeric(df_plus_plus_plus['Level']) - 1)))), df_plus_plus_plus['Eva'])

df_plus_plus_plus.drop(df_plus_plus_plus[to_numeric(
    df_plus_plus_plus.BaseRarity) > 5].index, inplace=True)
df_plus_plus_plus.drop(df_plus_plus_plus[to_numeric(
    df_plus_plus_plus.CorrectedType) == 3].index, inplace=True)

df_base = df_base.append(df_plus)
df_base = df_base.append(df_plus_plus)
df_base = df_base.append(df_plus_plus_plus)
##########################################
df_synergy = df_base.copy()
df_synergy['Synergy'] = 'Yes'
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 50, '160', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 45, '145', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 40, '130', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 35, '115', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 30, '100', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 25, '85', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 20, '70', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 15, '55', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 10, '40', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 5, '25', df_synergy['Level'])
df_synergy['Level'] = where(to_numeric(
    df_synergy['Level']) == 3, '18', df_synergy['Level'])

df_synergy['Atk'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Batk']) + (
        to_numeric(df_synergy['Matk']) - to_numeric(df_synergy['Batk'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Atk'])

df_synergy['Atk'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Atk']) * 1.5), df_synergy['Atk'])

df_synergy['Def'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Bdef']) + (
        to_numeric(df_synergy['Mdef']) - to_numeric(df_synergy['Bdef'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Def'])

df_synergy['Def'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Def']) * 1.5), df_synergy['Def'])

df_synergy['Mag'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Bmag']) + (
        to_numeric(df_synergy['Mmag']) - to_numeric(df_synergy['Bmag'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Mag'])

df_synergy['Mag'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Mag']) * 1.5), df_synergy['Mag'])

df_synergy['Res'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Bres']) + (
        to_numeric(df_synergy['Mres']) - to_numeric(df_synergy['Bres'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Res'])

df_synergy['Res'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Res']) * 1.5), df_synergy['Res'])

df_synergy['Mnd'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Bmnd']) + (
        to_numeric(df_synergy['Mmnd']) - to_numeric(df_synergy['Bmnd'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Mnd'])

df_synergy['Mnd'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Mnd']) * 1.5), df_synergy['Mnd'])

df_synergy['Acc'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Bacc']) + (
        to_numeric(df_synergy['Macc']) - to_numeric(df_synergy['Bacc'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Acc'])

df_synergy['Acc'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Acc']) * 1.5), df_synergy['Acc'])

df_synergy['Eva'] = where((to_numeric(df_synergy['Rarity']) < 101) & (
    to_numeric(df_synergy['CorrectedType']) != 3), ceil((to_numeric(df_synergy['Beva']) + (
        to_numeric(df_synergy['Meva']) - to_numeric(df_synergy['Beva'])) / ((to_numeric(
            df_synergy['Mlvl']) - 1) / (to_numeric(df_synergy['Level']) - 1)))), df_synergy['Eva'])

df_synergy['Eva'] = where((to_numeric(df_synergy['CorrectedType']) == 3),
                          ceil(to_numeric(df_synergy['Eva']) * 1.5), df_synergy['Eva'])

##########################################

df_base.drop(df_base.columns[range(19)], axis=1, inplace=True)
df_base.drop('Name', axis=1, inplace=True)
df_base = df_base.sort_values(by=['ID'])

df_synergy.drop(df_synergy.columns[range(19)], axis=1, inplace=True)
df_synergy.drop('Name', axis=1, inplace=True)
df_synergy = df_synergy.sort_values(by=['ID'])
df_base = concat([df_base, df_synergy], axis=1)
#df_base.to_csv('Relics_Processed_Base.csv', index=None, header=True, quoting=QUOTE_ALL)
df_base.to_csv('Relics_Processed.csv', index=None,
               header=True, quoting=QUOTE_ALL)
#df_synergy.to_csv('Relics_Processed_Synergy.csv', index=None, header=True, quoting=QUOTE_ALL)

print('Format End')
