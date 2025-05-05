_GROUPS = [
    ["admet_group", # url
     "ADMET Group", # dropdown label
     "ADMET Benchmark Group"], # title
    ["drugcombo_group", "DrugCombo Group", "Drug Combination Benchmark Group"],
    ["docking_group", "Docking Group", "Docking Molecule Generation Benchmark Group"],
    ["dti_dg_group", "DTI DG Group", "Drug-Target Interaction Domain Generalization Benchmark Group"],
    ["scdti_group", "Single-cell DTI Group", "Single-cell Drug-Target Interaction Benchmark Group"],
    ["proteinpeptide_group", "Protein-Peptide Binding Affinity Group", "Protein-Peptide Interaction Benchmark Group (+TCR-Epitope)"],
    ["counterfactual_group", "Counterfactual Prediction Group", "PerturbOutcome Prediction Benchmark Group"],
    ["clinical_trial", "Clinical Trial Outcome Prediction", "TrialOutcome Prediction Benchmark Group"]
]

_GROUP_MEMBERSHIP = {
    "admet_group": [
        "Caco2_Wang",
        "Bioavailability_Ma",
        "Lipophilicity_AstraZeneca",
        "Solubility_AqSolDB",
        "HIA_Hou",
        "Pgp_Broccatelli",
        "BBB_Martins",
        "PPBR_AZ",
        "VDss_Lombardo",
        "CYP2C9_Veith",
        "CYP2D6_Veith",
        "CYP3A4_Veith",
        "CYP2C9_Substrate_CarbonMangels",
        "CYP2D6_Substrate_CarbonMangels",
        "CYP3A4_Substrate_CarbonMangels",
        "Half_Life_Obach",
        "Clearance_Hepatocyte_AZ",
        "Clearance_Microsome_AZ",
        "LD50_Zhu",
        "hERG",
        "AMES",
        "DILI"
    ],
    "drugcombo_group": [
        "DrugComb_CSS",
        "DrugComb_HSA",
        "DrugComb_Loewe",
        "DrugComb_Bliss",
        "DrugComb_ZIP"
    ],
    "docking_group": [
        "DRD3",
    ],
    "dti_dg_group": [
        "BindingDB_Patent",
    ],
    "scdti_group": [
        "opentargets_dti_ra",
        "opentargets_dti_ibd",
    ],
    "proteinpeptide_group": [
        "brown_mdm2_ace2_12ca5",
        "tchard_na",
        "tchard_rn",
    ],
    "counterfactual_group": [
        "scperturb_drug_SrivatsanTrapnell2020_sciplex2",
    ],
    "clinical_trial": [
        "TOP",
    ],
}