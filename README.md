# DEG
Differential expression analysis means taking a
normalized number of readings and performing statistical 
analysis to reveal quantitative changes in 
expression levels between experimental groups.

   Dataset :  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205432
             GSE205432_NormalizedCounts.xlsx
             
             RNF4-RGMb axis is required for osteogenic differentiation and cancer cell survival
             To determine a potential transcriptional role for RNF4 in OD, and to identify RNF4-regulated, secreted factors we performed RNA-seq analysis.
             We compared the changes in gene signature of scrambled Scr-control hBMSCs to that of hBMSCs where RNF4 was knocked-down using shRNF4 upon OD
             
 Here, dataset contains ![image](https://user-images.githubusercontent.com/110597928/198849778-7388e98d-d3ea-4593-95ec-68f6d39a533c.png)


We read the readcounts file remove unwanted columns 
then convert the data in to the matrix inorder 
to produce cpm, log values and zscore, plot heatmap

then we split into test and control and find its mean
followed by p value and log2FC convert into dataframe ![image](https://user-images.githubusercontent.com/110597928/198849881-683c6ff1-6ef9-464c-9caa-f50f6004da01.png)

taking its transpons and labelling the columns and append its gene id which we removed

# Heatmap
![image](https://user-images.githubusercontent.com/110597928/198849497-b05692c9-2b7d-45af-a80a-d143519a4a6a.png)

    shows genes positively expressed in 'scrambled_untreated_2'(yellow) and negatively expressed more genes in siRNAaRNF4_7d_of_osteogenesis_1 (voilet-purple) 

then plot volcano viz. showing the genes overaly expressed:
Highly expressed upregulated genes (green) and Highly expressed downregulated genes (red)
![image](https://user-images.githubusercontent.com/110597928/198850226-dcfc407b-cb13-4c8e-927d-70f749c75a32.png)




