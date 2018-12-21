#!/usr/bin/python

import pandas as pd
import sys,os
import matplotlib.pyplot as plt

col_list=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5A','2DL5B','2DS3','2DS5','2DS1','2DS4','3DL2']

#col_list=['2DS4','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5A','2DL5B','2DS3','2DS5','2DS1','2DS4','3DL2']

data_file=pd.read_csv('gene_frequency_sept02_18.tsv',sep="\t")

#data_file2=data_file.filter(like="allele")
#df=data_file2.apply(pd.value_counts)
#print df
#sys.exit()
#data_file2.fillna('Not present',inplace=True)
#gene_freq = data_file2.notnull().sum()/len(data_file2)
#cols=list(data_file2)
#print cols
df=[]
for col in col_list:
	df11=data_file.filter(like=col+"_allele")
	if col+'_allele2' not in list(df11):
		df11.loc[:,col+"_allele2"]=df11[col+"_allele1"]
	else:
		df11[col+"_allele2"].fillna(df11[col+"_allele1"],inplace=True)	
	df11.dropna(how='all',inplace=True)
	alleles=pd.unique(df11.values.ravel())
	all_count=len(df11)*2
	#print alleles
	for allele in alleles:
		al_count=len(df11[df11[col+"_allele1"]==allele]) + len(df11[df11[col+"_allele2"]==allele])
		df.append([col,allele,al_count,all_count,round(al_count/float(all_count),2)])
#print allele_freq

headers=['Gene','Allele','Count','Total','Frequency']
df_new=pd.DataFrame(df,columns=headers)
df_pivot=pd.pivot_table(df_new,index='Gene',columns='Allele',values='Frequency',aggfunc="sum")
#print df_pivot
#print(df_new)
#print df.round(2)
#sys.exit()
df_pivot.to_csv('allele_frequency.cvs')
df_pivot.plot.bar(stacked=True,colormap="jet")
plt.xlabel('Genes')
plt.ylabel('Frequency of each allele')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('allele_frequency_15sept.png',dpi=600,bbox_inches='tight')

#plt.show()
#print gene_freq
#print data_file2.notnull().sum()
