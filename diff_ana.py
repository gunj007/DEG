#data preprocessing libraries 
import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
import seaborn as sns

#import data file
data=pd.read_csv("GSE205432_NormalizedCounts.csv")
gene_id=data['ensembl_gene_id']
print(data,data.columns)

data.drop(['description','external_gene_name'],axis=1,inplace=True)

#convertinng to numpy array (matrix)
try:
    cpm=[]
    for i in range(1,len(data)):
            colsum=data.iloc[:,i].sum()

            c1=(data.iloc[:,i]/colsum)*10**6
            cpm.append(c1)
    
except:
    print("ignore error")
print(cpm)
cpm=np.array(cpm)
print(cpm)
logv=np.log2(cpm +1)
print(logv)
print("Minimum value:",logv[0].min(),"\nMaximmum value:",logv[0].max())
import scipy.stats as st
zscr= st.zscore(logv)
print(zscr,zscr.shape) 
'''
import matplotlib.pyplot as  plt
plt.figure(figsize=(20,20))
ax=sns.heatmap(zscr[0:20,0:20],xticklabels=gene_id[0:20], yticklabels='auto',annot=False,cmap='gnuplot')
ax.set_xticklabels(ax.get_xticklabels(), fontsize = 7)
ax.set_yticklabels(ax.get_yticklabels(), rotation = 0, fontsize = 7)
plt.show()
'''
#splitting data into treated untreated array 
vec1= cpm[[1,3,5,7,9,11]]
print("sssssss:",vec1)
vec2=cpm[[2,4,6,8,10]]
print("vvvvvv:",vec2)

meanUntreated=np.mean(vec1,axis=0)
print("mean:",meanUntreated)
meanOsteogenesis=np.mean(vec2,axis=0)
print("meanc:",meanOsteogenesis)
#hypothesis
from scipy.stats import ttest_ind
pvalue=ttest_ind(vec1,vec2).pvalue
print(pvalue,"p")
log2FC=meanUntreated-meanOsteogenesis
print("log:",log2FC)
result=np.stack((meanUntreated,meanOsteogenesis,log2FC,pvalue),axis=0)
print("r:",result)
r=pd.DataFrame(result)
r=r.T
r.columns=["meanUntreated","meanOsteogenesis","log2FC","pvalue"]
r['gene_id']=gene_id
r["gene_id"] = r.gene_id.shift(-1)
col_1=r.pop('gene_id')
r.insert(0,'gene_id',col_1)
r.dropna(axis=0,inplace=True)
r['pvalue']=r['pvalue'].fillna(1)
print("df:",r)
#volcanoplot
from bioinfokit import analys, visuz
visuz.GeneExpression.volcano(r, lfc='log2FC', pv='pvalue',plotlegend=True, legendpos='upper right', 
    legendanchor=(1.46,1),show=True)









