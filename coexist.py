#!/usr/bin/python
from __future__ import division
import pandas as pd
import sys

df=pd.read_csv('tmh_data2.tsv',sep="\t")
alleles=['2DL2','2DL3','2DS2','2DL1','2DS1','3DL1','3DS1']
for allele in alleles:
 df[allele].fillna('A',inplace=True)
 df[allele].replace('p','P',inplace=True)
ligands=['C1_Present','C2_Present','Bw4']
print list(df)
yesno=['P','A']
for one in yesno:
  for allele in alleles:
    for ligand in ligands:
      ligand_pos= df[df[ligand] == 1].shape[0]
      num=df[(df[allele] == one) & (df[ligand] == 1)].shape[0]
      print ligand,allele+'_'+one,num,100*num/ligand_pos,ligand_pos

sys.exit()
### C1 ###
ligand='C1_Present'
ligand_pos= df[df[ligand] == 1].shape[0]
print ligand_pos
for one in yesno:
 for two in yesno:
  for three in yesno:
     num=df[(df['2DL2'] == one) & (df['2DL3'] == two) & (df['2DS2'] == three) & (df[ligand] == 1)].shape[0]
     print ligand,'2DL2_'+one+'/2DL3_'+two+'/2DS2_'+three,num,100*num/ligand_pos,ligand_pos

### C2 ###
ligand='C2_Present'
ligand_pos= df[df[ligand] == 1].shape[0]
print ligand_pos
for one in yesno:
 for two in yesno:
     num=df[(df['2DL1'] == one) & (df['2DS1'] == two) & (df[ligand] == 1)].shape[0]
     print ligand,'2DL1_'+one+'/2DS1_'+two,num,100*num/ligand_pos,ligand_pos

### Bw4 ###

ligand='Bw4'
ligand_pos= df[df[ligand] == 1].shape[0]
print ligand_pos
for one in yesno:
 for two in yesno:
     num=df[(df['3DL1'] == one) & (df['3DS1'] == two) & (df[ligand] == 1)].shape[0]
     print ligand,'3DL1_'+one+'/3DS1_'+two,num,100*num/ligand_pos,ligand_pos
