#!/usr/bin/python
import pandas as pd
import seaborn as sns; 
import numpy as np
sns.set(color_codes=True)
#df = pd.read_csv('final_data_heatmap_14march.tsv',sep="\t",index_col='Population', encoding='utf-8')
df = pd.read_csv('pivot2_wo3DP1.csv',index_col='Population', encoding='utf-8')
pop=pd.read_csv('selected_pop.tsv',sep="\t");
df.columns.rename('Allele',inplace=True)
df2=pd.merge(df,pop,right_on='Population',left_index=True,how='left')
import sys
df2=df2[df2.Number.isnull()==False]
df2.drop('Number',axis=1,inplace=True)
df2=df2.set_index('Population')
#col=['2DL1','2DL2','2DL3','2DL4','2DP1','2DS1','2DS2','2DS3','2DS4','2DS5','3DL1','3DL2','3DL3','3DP1','3DS1']
df3 = df2.astype('float')
#print df1.isnull()
#df1.to_csv("testing_data.csv")
#print df[pd.isnull(df).any(axis=1)]
df3.dropna(how='any',inplace=True)
df3.columns.rename('Genes',inplace=True)
for cols in list(df3):
	print cols
	df3[cols]=df[cols].apply(np.int64)
#print df.columns
print df3
sns.set(rc={'font.size': 20, 'axes.labelsize': 20, 'legend.fontsize': 20.0, 
    'axes.titlesize': 20, 'xtick.labelsize': 15, 'ytick.labelsize': 20})
g = sns.clustermap(df3,figsize=(15,25),annot=True, fmt="d")
#g.set_xticklabels(g.get_xticklabels(), rotation=90)
g.savefig("final_sel_pop_heatmap_wo3DP1_test.png",dpi=300)
