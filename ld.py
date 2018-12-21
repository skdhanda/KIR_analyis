#!/usr/bin/python
from __future__ import division
import pandas as pd
import sys,os
import matplotlib.pyplot as plt
import numpy as np
#col_list=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5A','2DL5B','2DS3','2DS5','2DS1','2DS4','3DL2']
col_list=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5','2DS3','2DS5','2DS1','2DS4','3DL2']

data_file=pd.read_csv('../gene_frequency_data_14march_2018.tsv',sep="\t")

data_file2=data_file[col_list]
gene_freq = data_file2.notnull().sum()/len(data_file2)

rows=[]
for col1 in col_list:
	for col2 in col_list:
		x11=len(data_file2[(data_file2[col1]=='P') & (data_file2[col2]=='P')])/len(data_file2)
		x12=len(data_file2[(data_file2[col1]=='P') & (data_file2[col2]!='P')])/len(data_file2)
		x21=len(data_file2[(data_file2[col1]!='P') & (data_file2[col2]=='P')])/len(data_file2)
		x22=len(data_file2[(data_file2[col1]!='P') & (data_file2[col2]!='P')])/len(data_file2)
		p1=len(data_file2[(data_file2[col1]=='P')])/len(data_file2)  # & (data_file2[col2]=='P')])/len(data_file2),2)
		p2=len(data_file2[(data_file2[col1]!='P')])/len(data_file2)  # & (data_file2[col2]!='P')])/len(data_file2),2)
		q1=len(data_file2[(data_file2[col2]=='P')])/len(data_file2)  # & (data_file2[col2]=='P')])/len(data_file2),2)
		q2=len(data_file2[(data_file2[col2]!='P')])/len(data_file2)  # & (data_file2[col2]!='P')])/len(data_file2),2)
		d=x11-p1*q1
		if d <0:
			dmin=max(-p1*q1,-p2*q2)
			ld=d/dmin
			dmax=None
		elif d>=0:
			dmax=min(p1*q2,p2*q1)
			ld=d/dmax
			dmin=None
		r2=(d**2)/(p1*p2*q1*q2)
		pvalue=r2*len(data_file2)
		row=[col1,col2,x11,x12,x21,x22,p1,p2,q1,q2,d,dmin,dmax,ld,pvalue]
		rows.append(row)
		#df = df.append([col1,col2,x11,x12,x21,x22,p1,p2,q1,q2,d,dmin,dmax,ld],ignore_index=True)
df=pd.DataFrame(rows,columns=['Gene1','Gene2','x11','x12','x21','x22','p1','p2','q1','q2','d','dmin','dmax','ld','pvalue'])
df.to_csv("ld_raw_14march.csv",index=False)
df_pivot=df.pivot_table(index='Gene1',columns='Gene2',values=['ld','pvalue']).round(3).transpose()
#print df_pivot
df1= df_pivot.groupby(level=[1,0]).sum()

df1.to_csv('ld_14march.csv')
