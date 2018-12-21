#!/usr/bin/python
import pandas as pd
from sklearn import decomposition
import matplotlib.pyplot as plt
import sys
import numpy as np 
from matplotlib.pyplot import cm 
color=iter(cm.rainbow(np.linspace(0,1,15)))

#df = pd.read_csv('final_data_heatmap_14march.tsv',sep="\t",index_col='Population')
df = pd.read_csv('pca_input.tsv',sep="\t",index_col=['Continent','Population','Population Abbrevation'])
pca=decomposition.PCA(n_components=10)
pca.fit(df)
y=pca.transform(df)
pc1=y[:,0]
pc2=y[:,1]
fig, ax = plt.subplots()
df2=pd.DataFrame(y)
df1=df.reset_index()
col_list=list(df1)
df3=pd.concat([df1,df2],axis=1)#.toarray().tolist()
#print df3
#print list(df3)
continents=df3.Continent.unique()
#print continents
#plt.scatter(pc1,pc2)
#print y.shape
print continents
for continent in continents:
	df4=df3[df3.Continent == continent]
	print continent
	c=next(color)
	ax.scatter(df4[0],df4[1],color=c,label=continent)
	for i,row in df4.iterrows():
		
		print row,type(row),list(df4)
		plt.annotate(str(row['Population Abbrevation']),(row[0],row[1]))
		print df3['Population'].iloc[i]
#		ax.scatter(row[0],row[1],color=c,label=df3['Population'].iloc[i])	
#plt.legend(handle=list(df.index))
#lines = axes.get_lines()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#lgd=plt.legend(loc=1,ncol=4,bbox_to_anchor=(0.,0.15,1.,1.02),mode="expand",fontsize="x-small")
#lgd2=plt.legend(loc=3,ncol=4,bbox_to_anchor=(0.,0.15,1.,1.02),mode="expand",fontsize="x-small")
#ax.add_artist(lgd)
#ax.add_artist(lgd2)
#h = [plt.plot([],[], color="gray", marker="o", ms=i, ls="")[0] for i in range(1,115)]
plt.legend(loc=1,ncol=4,bbox_to_anchor=(0.,0.15,1.,1.02),mode="expand",fontsize="x-small")
#plt.legend(handles=h, labels=df3['Population'].all(),loc=(1.03,0.5))
plt.xlabel("PCA-1")
plt.ylabel("PCA-2")
#plt.bar(x[0],x[1])
#plt.show()
fig.savefig('pca_image.png', bbox_inches='tight')
