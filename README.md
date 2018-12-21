# KIR_analyis
Analysis of KIR genes/alleles 

##Linkage Disequilbirium 
The idea was derived from
http://pbgworks.org/sites/pbgworks.org/files/measuresoflinkagedisequilibrium-111119214123-phpapp01_0.pdf
http://csg.sph.umich.edu/abecasis/class/666.03.pdf


Linkage disequilibrium in following steps:
1. Calculate the gene pair (i.e. gene A and gene B) phenotype frequency with following equations

	x11 = number of individuals where both the genes are present /sample size

	x12 = number of individuals where gene A is present and gene B is absent/ sample size

	x21 = number of individuals where gene A is absent and gene B is present/ sample size

	x22 = number of individuals where both genes are absent / sample size

2. Calculate individual gene frequencies 

	p1 = x11 + x12

	p2 = x21 + x22

	q1 = x11 + x21

	q2 = x12 + x22

3. Calculate the standard measure of linkage disequilibrium 

	D = x11 - p1*q1

	If D = 0, there is no linkage disequilibrium. 


3.1. for D  ≥  0 

	D’ = D/Dmax

	Dmax = smaller value between (p1*q2) and )p2*q1)


3.2. for D < 0

	D’ =  D/Dmin

	Dmin is the larger value between  (–p1*q1) and (–p2*q2). 

4. Calculating the correlation between pair of genes

	r2 (r square)= D*D/(p1*p2*q1*q2)


The value of D' and r2 are reported as final analysis, where r2=0 means genes have no linkage, r2=1 means genes have complete linkage disequilibrium. 


5. Significance of chi square and degree of freedom table 

https://www.medcalc.org/manual/chi-square-table.php

The degree of freedom was selected and therefore value 6.64 was used as threshold for significance at 0.01
derived from (http://pbgworks.org/sites/pbgworks.org/files/measuresoflinkagedisequilibrium-111119214123-phpapp01_0.pdf)
