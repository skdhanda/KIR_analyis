#!/usr/bin/python
import pandas as pd

df=pd.read_csv('../gene_frequency_data_19feb_2018.tsv',sep="\t")

df_allele=df.filter(like="allele")
cols=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5A','2DL5B','2DS3','2DS5','2DS1','2DS4','3DL2']
#print list(df_allele)
df_genes=df[cols]
df_genes.replace('p','P',inplace=True)
df_genes.replace('P',1,inplace=True)
df_genes.fillna(0,inplace=True)
for col in df_genes:
	df_allele=df.filter(like=col+"_allele")
	if len(list(df_allele))>1:
		for allele in df_allele:
			print col,allele,df_allele[allele].unique()
