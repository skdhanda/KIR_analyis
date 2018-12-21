#!/usr/bin/python
from __future__ import division
import pandas as pd
import sys
import matplotlib.pyplot as plt

df=pd.read_csv('tmh_data2.tsv',sep="\t")

lig_list_res=[]
df.rename(columns={"A3/A11":"A3/A11_present",'Bw4':'Bw4_present'},inplace=True)
ligand_list=['A3/A11_present', 'Bw4_present', 'Bw4_absent', 'C1_Present', 'C2_Present', 'C1C1_present', 'C1C2_present', 'C2C2_present', 'A3/A11_present_3DL2_present', 'Bw4_present_3DL1_present', 'C1_present_2DL2_present', 'C1_present_2DL3_present', 'C1_present_2DS2_present', 'C2_present_2DL1_present', 'C2_present_2DS1_present']
def colplot(df,ligand_list,figname,tsvname):
  full_dic=[]
  for lig in ligand_list:
        df[lig].fillna('NA',inplace=True)
	nuniq= df[lig].unique()
	each_dict={'Ligand':lig}
	for uniq in nuniq:
		each_dict[uniq]=df[df[lig]==uniq].shape[0]
	full_dic.append(each_dict)
  df_full=pd.DataFrame(full_dic)
  df_full.rename(columns={1:'Present',0:'Absent'},inplace=True)
  df_full['Frequency']=100*df_full['Present']/(df_full['Present']+df_full['Absent'])
  df_full['Ligand']=df_full['Ligand'].str.replace('Present','Pos')
  df_full['Ligand']=df_full['Ligand'].str.replace('present','Pos')
  df_full['Ligand']=df_full['Ligand'].str.replace('absent','Neg')
  df_full.plot(kind='bar',x='Ligand', y='Frequency',legend=None)
  plt.ylabel('Frequency (%)')
  plt.tight_layout()
  plt.savefig(figname,dpi=300)
  df_full.to_csv(tsvname,sep="\t",index=False)
  return df_full
colplot(df,ligand_list,'lig_freq.png','ligand_freq.tsv')
small_list=['Bw4_present','C1_Present', 'C2_Present', 'C1C1_present', 'C1C2_present', 'C2C2_present']
colplot(df,small_list,'lig_req.png','ligand_req.tsv')
