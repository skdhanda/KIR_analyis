#!/usr/bin/python
from __future__ import division
import pandas as pd
import sys

df=pd.read_csv('tmh_data2.tsv',sep="\t")
print list(df)
total=df.shape[0]
allele='2DL3' #'2DL2'  #'2DL1' #'3DL1'
ligand='C1 Present' #'C1 Present' #'C2 Present' #'Bw4'
allele=sys.argv[1]
ligand=sys.argv[2]

df[allele].fillna('A',inplace=True)
df[allele].replace('p','P',inplace=True)
print df[allele].unique()
print df[ligand].unique()
allele_pos= df[(df[allele].str.contains('P'))].shape[0]
ligand_pos= df[df[ligand] == 1].shape[0]
#) & (df[ligand] == 1)].shape[0]
#print df[['ID',allele, ligand,]]
ligand_pos_allele_pos= df[(df[allele] == 'P') & (df[ligand] == 1)].shape[0]
ligand_pos_allele_neg= df[(df[allele] == 'A') & (df[ligand] == 1)].shape[0]
ligand_neg_allele_neg= df[(df[allele] == 'A') & (df[ligand] == 0)].shape[0]
ligand_neg_allele_pos= df[(df[allele] == 'P') & (df[ligand] == 0)].shape[0]
data_missing=df[(df[ligand].isnull())].shape[0]
total_present=total-data_missing

print allele,ligand,allele_pos,ligand_pos,ligand_pos_allele_pos,ligand_neg_allele_pos,ligand_pos_allele_neg,ligand_neg_allele_neg,total,total_present,data_missing,total-total_present-data_missing
print allele,ligand,100*ligand_pos_allele_pos/total_present,100*ligand_neg_allele_pos/total_present,100*ligand_pos_allele_neg/total_present,100*ligand_neg_allele_neg/total_present,data_missing
'''
for ind, rows in df.iterrows():
  if rows[ligand] == rows['ligand absent']:
     print ind,rows
  else:
     print "okay"
'''
