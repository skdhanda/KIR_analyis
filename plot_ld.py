import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
from PIL import Image
sns.set(style="white")
genes=['2DL1','2DL2','2DL3','2DL5','2DP1','2DS1','2DS2','2DS3','2DS4','2DS5','3DL1','3DS1']
# Generate a large random dataset
df_in = pd.read_csv('ld_raw_24june.csv')
df = df_in[df_in['Gene1'].isin(genes)]
df = df[df['Gene2'].isin(genes)]
df['p value']=np.where(df['p value'] <= 0.01,0.01,0)
df['association'].replace({'Positive':1,'Negative':-1},inplace=True)
df['ld coefficient']=df['ld coefficient']*df['association']
df_ld=df.pivot_table(index='Gene1',columns='Gene2',values='ld coefficient').round(3).transpose()
df_pval=df.pivot_table(index='Gene1',columns='Gene2',values='p value').round(3).transpose()
#del df_pval.index.name
#del df_ld.index.name
#del df_ld.columns.name
#del df_pval.columns.name

# Generate a mask for the upper triangle
mask = np.zeros_like(df_ld, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(25, 25))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10,n=2, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
#sns.heatmap(df_pval, mask=mask,cmap=cmap, center=0, annot=df_ld, annot_kws={"size": 24,"rotation":-45}, square=True, linewidths=1.5, cbar_kws={"shrink": .5,"use_gridspec":False,"location":"bottom"})
#cbar = ax.collections[0].colorbar
#cbar.set_ticks([0, 0.01])
#cbar.set_ticklabels(["Non significant", "Significant"])

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(df_pval, mask=mask,cmap=cmap, center=0, annot=df_ld, annot_kws={"size": 25,"rotation":-45}, square=True, linewidths=1.5, cbar=False)
plt.axis('off')
for i in range(len(df_pval)):
 ax.text(i+(0.25),i+0.25,df_pval.index[i], ha='left',va='baseline',rotation=-45,fontsize='30')
plt.savefig("ld_plot_raw.png",dpi=300)

### Rotate the image 45 degree to make haploview image
im = Image.open("ld_plot_raw.png")
out = im.rotate(45, expand=True,fillcolor='white')
out.save("ld_plot_final.png")
