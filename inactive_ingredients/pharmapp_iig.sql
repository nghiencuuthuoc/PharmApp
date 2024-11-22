-- SCHEMA: pharmapp

-- DROP SCHEMA IF EXISTS pharmapp ;

CREATE SCHEMA IF NOT EXISTS pharmapp
    AUTHORIZATION sagerx


-----------------
-- Table: pharmapp.nadac

-- DROP TABLE IF EXISTS pharmapp.nadac;

CREATE TABLE IF NOT EXISTS pharmapp.nadac
(
    ndc_description text COLLATE pg_catalog."default",
    ndc character varying(11) COLLATE pg_catalog."default",
    nadac_per_unit numeric(12,5),
    effective_date date,
    pricing_unit text COLLATE pg_catalog."default",
    pharmacy_type_indicator text COLLATE pg_catalog."default",
    otc text COLLATE pg_catalog."default",
    explanation_code text COLLATE pg_catalog."default",
    classifiation_for_rate_setting text COLLATE pg_catalog."default",
    corresponding_generic_drug_nadac_per_unit text COLLATE pg_catalog."default",
    corresponding_generic_drug_effective_date date,
    as_of_date date
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS pharmapp.nadac
    OWNER to sagerx;

-----------
CREATE TABLE IF NOT EXISTS pharmapp.iig
(
INGREDIENT_NAME text COLLATE pg_catalog."default",
ROUTE text COLLATE pg_catalog."default",
DOSAGE_FORM text COLLATE pg_catalog."default",
CAS_NUMBER text COLLATE pg_catalog."default",
UNII text COLLATE pg_catalog."default",
POTENCY_AMOUNT numeric(12,5),
POTENCY_UNIT text COLLATE pg_catalog."default",
MAXIMUM_DAILY_EXPOSURE numeric(12,5),
MAXIMUM_DAILY_EXPOSURE_UNIT text COLLATE pg_catalog."default",
RECORD_UPDATED text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS pharmapp.nadac
    OWNER to sagerx;

-----------
COPY pharmapp.iig
FROM 'IIR_OCOMM.csv' 
DELIMITER ',' 
CSV HEADER;


----------
