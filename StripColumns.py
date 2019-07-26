# coding=utf-8

import pandas as pd
df=pd.read_csv("C:\\Users\\BaconCatBug\\Google Drive\\FFRK\\Enlir\\Abilities.csv")
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.to_csv('Abilities.csv', index = False)

df=pd.read_csv("C:\\Users\\BaconCatBug\\Google Drive\\FFRK\\Enlir\\Commands.csv")
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.to_csv('Commands.csv', index = False)

df=pd.read_csv("C:\\Users\\BaconCatBug\\Google Drive\\FFRK\\Enlir\\Magicite.csv")
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.to_csv('Magicite.csv', index = False)

df=pd.read_csv("C:\\Users\\BaconCatBug\\Google Drive\\FFRK\\Enlir\\Relics.csv")
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.to_csv('Relics.csv', index = False)

df=pd.read_csv("C:\\Users\\BaconCatBug\\Google Drive\\FFRK\\Enlir\\SoulBreaks.csv")
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.to_csv('SoulBreaks.csv', index = False)