# only aggregating 2 things at a time
import cerberus
refs = [False for i in range(2)]
prev_ics = "analysis/240221_nm/cerberus/agg/ad004_hTREM2KI-WT_M_8_months_HC_6_ic.tsv"
cur_ics = "/share/crsp/lab/model-ad/share/freese/modelad_pipeline/proc_update_2/data/cerberus/ad004/hTREM2KI-WT_M_8_weeks_HC_ic.tsv"
analysis = "240221_nm" 
study = "ad004" 
genotype = "hTREM2KI-WT" 
sex = "M" 
age = "8_weeks" 
tissue = "HC" 
cerberus_run = "7"
source = "_".join([study, genotype, sex, age, tissue])
sources = ["cerberus", source]
out_ics = "analysis/240221_nm/cerberus/agg/ad004_hTREM2KI-WT_M_8_weeks_HC_7_ic.tsv"
cerberus.agg_ics([prev_ics, cur_ics],
          refs,
          sources,
          out_ics)
