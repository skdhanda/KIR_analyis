#!/usr/bin/python
import pandas as pd
import seaborn as sns; 
sns.set(color_codes=True)
df = pd.read_csv('all_genes.tsv',sep="\t")
df1 = pd.read_csv('tmc_gene.tsv',sep="\t")
print list(df),list(df1)
merge = df.append(df1,ignore_index=True)
#print merge
pivot = merge.pivot_table(index='Population',columns='Allele',values='Gene Frequency')
#pivot.to_csv('pivot.csv')
#print pivot.count().sum()
col=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','3DP1','2DL4','3DL1','3DS1','2DL5A','2DL5B','2DS3','2DS5','2DS1','2DS4','3DL2']
col=['3DL3','2DS2','2DL2','2DL3','2DP1','2DL1','2DL4','3DL1','3DS1','2DL5','2DS3','2DS5','2DS1','2DS4','3DL2']
#merge.to_csv('merge.csv')
pivot=pivot[col].astype('float')
pivot.dropna(how='any',inplace=True)

#print pivot.columns
pivot.to_csv('pivot2_wo3DP1.csv')
#sns.set(rc={'font.size': 20, 'axes.labelsize': 20, 'legend.fontsize': 10.0, 
#    'axes.titlesize': 20, 'xtick.labelsize': 15, 'ytick.labelsize': 10})

#g = sns.clustermap(pivot)
#g.savefig("heatmap_wo3DP1.png",dpi=600)
