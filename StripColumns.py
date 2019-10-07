# coding=utf-8
import csv
import pandas as pd

df = pd.read_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Abilities.csv", dtype=str)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
export_csv = df.to_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Abilities.csv", index=None, header=True,
                        quoting=csv.QUOTE_ALL)

df = pd.read_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Commands.csv", dtype=str)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
export_csv = df.to_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Commands.csv", index=None, header=True,
                        quoting=csv.QUOTE_ALL)

df = pd.read_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\LegendMateria.csv", dtype=str)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
export_csv = df.to_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\LegendMateria.csv", index=None, header=True,
                        quoting=csv.QUOTE_ALL)

df = pd.read_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Magicite.csv", dtype=str)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
export_csv = df.to_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Magicite.csv", index=None, header=True,
                        quoting=csv.QUOTE_ALL)

df = pd.read_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Relics.csv", dtype=str)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
export_csv = df.to_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\Relics.csv", index=None, header=True,
                        quoting=csv.QUOTE_ALL)

df = pd.read_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\SoulBreaks.csv", dtype=str)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
export_csv = df.to_csv(r"C:\Users\BaconCatBug\Documents\GitHub\BCBCSVStorage\SoulBreaks.csv", index=None, header=True,
                        quoting=csv.QUOTE_ALL)