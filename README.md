# DEG
Differential expression analysis means taking a
normalized number of readings and performing statistical 
analysis to reveal quantitative changes in 
expression levels between experimental groups.

We read the readcounts file remove unwanted columns 
then convert the data in to the matrix inorder 
to produce cpm, log values and zscore, plot heatmap

then we split into test and control and find its mean
followed by p value and log2FC convert into dataframe
taking its transpons and labelling the columns and append its gene id which we removed

then plot volcano viz. showing the genes overaly expressed

# Heatmap
    shows diffrentially expressed genes in yellow and negatively expressed genes in voilet-purple





