#!/usr/bin/python

import pandas as pd
import sys,os
import matplotlib.pyplot as plt

#col_list=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5A','2DL5B','2DS3','2DS5','2DS1','2DS4','3DL2']
#col_list=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5','2DS3','2DS5','2DS1','2DS4','3DL2']

col_list=['3DL1','2DL1','2DL3','2DS4','2DL2','2DL5','3DS1','2DS1','2DS2','2DS3','2DS5','2DL4','3DL2','3DL3','2DP1','3DP1']
data_file=pd.read_csv('gene_frequency_sept02_18.tsv',sep="\t")

data_file2=data_file[col_list]
#data_file2=data_file.filter(like="allele")
gene_freq = data_file2.notnull().sum()/len(data_file2)
gene_freq.plot.bar(color='black')
plt.xlabel('Genes')
plt.ylabel('Frequency')
plt.savefig('Gene_frequency_02sept.png',dpi=600,bbox_inches='tight')
#print gene_freq
gene_freq=gene_freq.append(data_file2.notnull().sum())
print gene_freq
