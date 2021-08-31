# Introduction to Bioinformatics
* [Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) If you have a little background knowledge of statistics, please read this book first.
*	[Coursera's machine learning course](coursera.org/learn/machine-learning) is a compulsory course for anyone interested in machine learning.
*	[RR & Bioconductor Manual Make](http://manuals.bioinformatics.ucr.edu/home/R_BioCondManual/)
sure you understand the code before starting any bioinformatics project.
*	[Use R and Bioconductor](http://manuals.bioinformatics.ucr.edu/home/ht-seq) for HT sequence analysis Make sure you understand the code before proceeding with any NGS project.
*	[ChemmineR: R’s Chemistry Toolbox](http://www.bioconductor.org/packages/devel/bioc/vignettes/ChemmineR/inst/doc/ChemmineR.html) recommends running the code before proceeding with any cheminformatics project.
*	[Practice the deep learning [PyTorch](http://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) deep learning tutorial step by step .
*	Harvard University Biomedical Data Science Open Online Training A comprehensive data science tutorial from [rafalab](http://rafalab.github.io/pages/harvardx.html) code.
*	An outstanding video tutorial on statistics by biologists from [StatQuest](https://statquest.org/videoindex/) .
*	[List of commonly used data analysis Quickly view the list of basic knowledge of data analysis](https://github.com/Bin-Chen-Lab/BigData_AI_DrugDiscovery/blob/master/data_science_cheatsheet.pdf)
*	Single-cell [RNA-Seq] analysis [osca](https://osca.bioconductor.org/introductiontion.html) , [seurat's](https://satijalab.org/seurat/vignettes.html) excellent scRNA-Seq analysis process.
# Basic thesis
## Field review articles
*	[The characteristics of cancer]: next-generation analysis to understand the basis of cancer.
*	[Tumor metastasis]: the evolutionary process from a molecular perspective to understand the basis of cancer metastasis.
*	[Cancer Genome Map Understand] the basics of cancer genomics.
*	[Cancer transcriptome analysis] at critical moments of clinical translation A review of cancer transcriptomes.
*	[Ewing's Sarcoma]: Historical Prospects, Current Technology Levels, and Future Opportunities for Targeted Therapy A review of typical cases of cancer treatment discovery.
*	[Opportunities and challenges of phenotypic drug discovery]: an industry perspective, a method for drug screening
*	10 years of biological pathway analysis: current methods and outstanding challenges This is a good summary of the development of pathway analysis methods.
*	Deep learning A review of deep learning.
*	High-performance medicine: the integration of humans and artificial intelligence. The current progress and challenges of DL application in biomedical research.
Statistical method development
*	Significance analysis of RNA microarray data Development of SAM, a popular method for differential expression analysis using microarray data.
*	limma: Linear model of matrix data The development of LIMMA, another algorithm for expression analysis using matrix data.
*	Differential expression analysis of sequence count data Development of DEseq, a method for matrix expression analysis using RNA-SEQ data.
*	Gene set enrichment analysis: A method based on known knowledge to explain the development of genome-wide expression profile GSEA is currently the most popular gene enrichment analysis method, and it is also the basis for understanding drug discovery methods.
*	Use the empirical Bayes method to adjust the batch method in matrix expression data
Correct the method of testing the difference between batch processing samples.
*	The definition of distance in a random network The definition of a scale-free network.
*	Heterogeneous information network top-k similarity search based on meta-path A machine learning method for mining heterogeneous networks.
*	MuSiC: Identifying the significance of mutations in cancer genomes The development of MuSiC, a popular method for identifying mutations.
Development and application of bioinformatics methods
*	Connecting small molecules, genes, and diseases using gene expression signatures The first paper describing methods for drug discovery.
*	Use of public gene expression data for summary discovery and preclinical indication verification The basis of our drug discovery work, and an example of writing a computational paper (from method development to experimental verification).
*	The relationship between ligand chemistry and protein pharmacology The development of SEA, a method for predicting drug-target interactions, and another great demonstration of writing computational papers.
*	Characterization of the drug-induced transcription module: repositioning and functional understanding of drugs starting from data analysis and finally verified by biological experiments
*	Cross-species regulatory network analysis determines the synergy between the genes FOXM1 and CENPF to drive prostate cancer malignancies starting from data analysis and finally verified by biological experiments
*	To clarify the mechanism of compound action through network disturbance analysis, starting from data analysis, and finally verifying through biological experiments
*	Discover the mode of action of the drug and the repositioning of the drug from the transcription reaction, starting from data analysis, and finally verifying it through biological experiments
*	[Imagenet Deep Convolutional Neural Network Classification]( http://papers.nips.cc/paper/4824-Imagenet-classification-with-deep-convolutional neural-networks.pdf) The development and popularity of Convolutional Neural Networks (CNN) Deep learning methods.
Tumor calculation analysis
*	Drug-target interaction network Network analysis of drug-target interactions.
*	The molecular map of human breast cancer comes from a typical genome analysis paper by TCGA.
*	Mutation Map and Significance of 12 Major Cancer Types A paper on pan-cancer genome analysis.
*	Comprehensive characterization of cancer molecular differences between male and female patients A paper on pan-cancer genome analysis.
*	The genetics of rheumatoid arthritis contributes to the discovery of biology and drugs. Use genes for drug discovery.
*	Tumor cell lines support predictive modeling of anticancer drug sensitivity . Articles using cell line data to discover biomarkers.
*	A time-process-based multi-cohort analysis of full-time sepsis and aseptic inflammation. A reliable diagnostic gene set . Articles using public expression data to discover biomarkers.
*	Using a multi-class Bayesian model trained on a chemical genomics database to predict the biological target of a compound . A typical machine learning paper in chemoinformatics.
*	Do molecules with similar structures have similar biological activities ? A typical data analysis paper in chemoinformatics.
##Drug discovery based on deep learning
*	Drug Design Reinforcement Learning Network Develop a reinforcement learning model to generate a target chemical library of new compounds that can be optimized for one or more characteristics.
*	Convolutional network for learning molecular feature maps Inspired by ECFP, DL-based features are designed
*	Automatic chemical design using data-driven continuous molecular representations. Use a variational autoencoder to encode and optimize compounds from the potential molecular compound space.
Shape our future
*	Single-cell RNA-seq highlights the application of heterogeneous single cells in primary glioblastoma tumors in cancer research.
*	Single-cell transcriptomics reveals the unique molecular characteristics of chronic myeloid leukemia stem cells . The application of single-cell analysis in individualized cancer treatment.
*	Brown fat remodeling induced by small molecules Use small molecules to control cell development.
*	Relevant chemosensitivity and basic gene expression mechanism explain the use of pharmacogenomics data to understand the mechanism of drug action.
*	Next-generation drug connectivity graph: L1000 platform and the first 1,000,000 data LINCS, we mainly use the data set for drug discovery.
*	Metastatic cancer integrated clinical genomics We have a lot of experience in the treatment of primary cancer, now is the time to focus our attention on metastatic cancer, most patients die of metastatic cancer.
*	Unpaired image-to-image using recurrent adversarial network uses deep learning GAN to achieve field applications.
Well-known translational drug target discovery tools and data sets
** List excellent tools/data sets for cancer drug discovery
Patient data and disease data
*	ClinicalTrials.gov finds drugs used in cancer clinical trials.
*	Cancer Today (Globocan): A data visualization tool that displays current estimates of cancer incidence, mortality, and prevalence across the country . Search for cancer incidence.
*	British Biobank and British Biobank Engine Search for public clinical/molecular data of cancer and genetic variation of liver cancer through the Stanford Biological Database engine.
*	COSMIC looks for somatic mutations in cancer.
Drug target development
*	cBioPortal . Search for molecular changes in cancer from public data sets including TCGA.
*	GTEx . Look for gene expression in normal tissues.
*	Human Protein Atlas Search for protein expression and pathology of cancer.
*	Encyclopedia of Tumor Cell Lines Look for gene expression in cancer cell lines.
*	The Achilles project searches for the necessary genes for cancer cells.
*	DepMap establishes a complete pre-clinical reference map that links tumor characteristics with tumor correlation to accelerate the development of precise treatments.
*	GEO searches for cancer's functional genomic data and requires additional computational analysis to create cancer features.
*	Enrichr searches the rich TS/Pathway/biological process/cell type gene list.
*	STRING DB visualizes protein-protein relationships.
Drug discovery
*	PubChem needs to know everything about compounds/drugs.
*	DrugBank searches for drug-target-indication.
*	SEA predicts the target of a given compound.
*	LINCS predicts drugs with liver cancer characteristics.
*	ChemMine is very useful for chemical structure enrichment analysis.
NGS analysis
*	RNASEQ Blog A large number of RNA-SEQ analysis methods/applications.
*	RPKM, FPKM and TPM
*	RNA-seq workflow: exploratory analysis and differential expression at the gene level
Python
*	Python recommends using anaconda to manage python packages
*	scikit: a popular python machine learning package
*	rdkit is a free python library for handling chemical structures.
*	PyTorch deep learning framework.
R/Bioconductor
*	ggplot one must use R to read visualization data.
*	ChemmineR: Chemoinformatics Toolkit calls R package
*	biomaRt is a powerful package for molecular data mapping id relations.
*	GEOquery downloads data from GEO.
*	cgdsr API for obtaining cBioportal data.
*	pheatmap visualized heat map.
*	[An easy way to mix multiple graphs on the same page]( http://www.sthda.com/english/articles/24-ggpubr-public--plots/81-ggplot2-Easy-Way-mix-multiple- graphs -onsamepage/)
