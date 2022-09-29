library(pheatmap)
#library(edgeR)
library(edgeCorr)
library(ggplot2)

#Reading an input cancer data file
data =  read.csv("C:/Users/GUNJAN/OneDrive/Desktop/GSE202434.csv"
                      , sep="," ,header=T , row.names = 1)

#count per metrics
cpm=data
for(i in 1:ncol(data)){
  cpm[,i]=(data[,i]/sum(data[,i]))*1000000
}

#cal a log of cpm
logcpm=log2(cpm+1)

summary(logcpm)

# z score
library(matrixStats)
zscore = (logcpm - rowMeans(logcpm))/rowSds(as.matrix(logcpm))[row(logcpm)]
zscore[is.na(zscore)]=0

#Calculate variance using log 
v =apply(logcpm , 1 , var)
v = sort(v,decreasing = T)
viw = v[1:50]
pmat = zscore[names(viw),]

#Create a heatmap
library(ComplexHeatmap)
Heatmap(pmat)

#to id-genes vir. differential in tumor vs control samples

mat=matrix(NA,ncol=4,nrow = nrow(logcpm))
rownames(mat)=rownames(logcpm)
colnames(mat)=c('meanTumor','meanControl','pvalue','log2FC')

for(i in 1:nrow(logcpm)){
  vector1 = as.numeric(logcpm[i, 1:7])
  
  vector2 = as.numeric(logcpm[i, 8:11])
  
  res=t.test(vector1, vector2, paired = F, alternative = "two.sided")
  mat[i,1]=res$estimate[[1]]
  mat[i,2]=res$estimate[[2]]
  mat[i,3]=res$p.value
  mat[i,4]=mat[i,1]-mat[i,2]
  
}

mat=as.data.frame(mat)
num=which(is.nan(mat$pvalue))
mat[num,'pvalue']=1

library(EnhancedVolcano)
EnhancedVolcano(mat,lab = rownames(mat),x = 'log2FC' ,y ='pvalue')



