------------------------------------------------------------
Fast Response Database, v.1.3, 2023-02-15
------------------------------------------------------------

Database on the pharmacokinetics, adverse events, drug-drug 
interactions and sourcing of ~4.5k FDA approved, previously 
approved, OTC approved or investigationsl non-biological 
drugs.

Prepared by Rancho BioSciences for NCATS

------------------------------------------------------------

Contents:

frdbmeta-data_model.tsv
	data model (description of DB fields)
	
frdbmeta-data_dictionary.tsv 
	data dictionary (values for dictionary-controlled DB 
	fields)

frdbmeta-units.tsv 
	dictionary of units of measurements, relationships to 
	standard units, and conversion factors between them 
	
frdbmeta-units_factors.tsv
	dictionary of conversion factors between units and 
	standard units
	
frdbmeta-targets.tsv 
	DDI targets and their ChEMBL and UNIPROT ids 
	
frdbmeta-about.tsv
	description of columns in frdbmeta-about.tsv and
	frdbmeta-data_dictionary.tsv
	
frdb-drugs.tsv
	data on drug names and UNIIs
	
frdb-pk.tsv
	data on drug pharmacokinetics

frdb-toxicity.tsv
	metadata on toxicity (includes information about study
	population, drug administration route, and 
	co-administered drugs)

frdb-adverseevents.tsv
	adverse events

frdb-ddi.tsv
	drug-drug interactions

frdb-sourcing.tsv
	information about sourcing (contains links to vendors)