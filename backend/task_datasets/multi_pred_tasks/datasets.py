_DATASETS = {
    "dti":["BindingDB_Kd", "DAVIS", "KIBA"],
    "ddi": ["DrugBank", "TWOSIDES"],
    "ppi": ["HuRI"],
    "gdi": ["DisGeNET"],
    "drugres":["GDSC1", "GDSC2"],
    "drugsyn":["OncoPolyPharmacology", "DrugComb"],
    "peptidemhc":["MHC1_IEDB-IMGT_Nielsen", "MHC2_IEDB_Jensen"],
    "antibodyaff":["Protein_SAbDab"],
    "mti":["miRTarBase"],
    "catalyst":["USPTO_Catalyst"],
    "tcrepitope":["weber"],
    "trialoutcome":["TOP"],
    "proteinpeptide":["brown_mdm2_ace2_12ca5"],
    "counterfactual":["scperturb"],  # scperturb is further spit into more datasets; so this page is not templated
    "scdti":["opentargets_dti"]
}

_META = {
    "DisGeNET": [
        "disgenet",
        "DisGeNET",
        "DisGeNET is a discovery platform containing one of the largest publicly available collections of genes and variants \
            associated to human diseases. DisGeNET integrates data from expert curated repositories, GWAS catalogues, animal \
                models and the scientific literature. DisGeNET data are homogeneously annotated with controlled vocabularies and\
                    community-driven ontologies. TDC uses the curated subset from UNIPROT, CGI, ClinGen, Genomics England, CTD\
                        (human subset), PsyGeNET, and Orphanet. TDC maps disease ID to disease definition through MedGen and maps\
                            GeneID to uniprot amino acid sequence.",
        "Regression. Given the disease description and the amino acid sequence of the gene, predict their association.",
        " 52,476 gene-disease pairs, 7,399 genes, 7,095 diseases",
        ["Random Split"],
        "GDA",
        [
            [
                "[1] Piñero, Janet, et al. “The DisGeNET knowledge platform for disease genomics: 2019 update.” Nucleic acids\
                    research 48.D1 (2020): D845-D855. ",
                "https://academic.oup.com/nar/article-abstract/48/D1/D845/5611674"
            ],
            [
                "[2] Halavi, Maryam, et al. “MedGen.” The NCBI Handbook [Internet]. 2nd edition. National Center for Biotechnology\
                    Information (US), 2018.",
                "https://www.ncbi.nlm.nih.gov/books/NBK159970/?report=printable"
            ]
        ],
        "CC BY-NC-SA 4.0.",
        "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    ],
    "OncoPolyPharmacology": [
        "oncopolypharmacology",
        "OncoPolyPharmacology",
        "A large-scale oncology screen produced by Merck & Co., where each sample consists of two compounds and a cell line. The \
            dataset covers 583 distinct combinations, each tested against 39 human cancer cell lines derived from 7 different tissue\
                types. Pairwise combinations were constructed from 38 diverse anticancer drugs (14 experimental and 24 approved). \
                    The synergy score is calculated by Loewe Additivity values using the batch processing mode of Combenefit. The\
                        genomic features are from ArrayExpress database (accession number: E-MTAB-3610) and was quantile normalized\
                            and summarized with Factor Analysis for Robust Microarray Summarization (FARMS). The processed data is\
                                provided by DeepSynergy.",
        "Regression. Given the gene expression of cell lines and two SMILES strings of the drug combos, predict the drug synergy level.",
        "23,052 drug combo-cell line points, among 39 cancer cell lines and 37 drugs",
        ["Random Split", "Cold Cell Line Split"],
        "DrugSyn",
        [
            [
                "[1] O’Neil, Jennifer, et al. “An unbiased oncology compound screen to identify novel combination strategies.” \
                    Molecular cancer therapeutics 15.6 (2016): 1155-1162. ",
                "https://mct.aacrjournals.org/content/15/6/1155.short"
            ],
            [
                "[2] Preuer, Kristina, et al. “DeepSynergy: predicting anti-cancer drug synergy with Deep Learning.” Bioinformatics\
                    34.9 (2018): 1538-1546. ",
                "https://academic.oup.com/bioinformatics/article-abstract/34/9/1538/4747884"
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "DrugComb": [
        "drugcomb",
        "DrugComb",
        "This dataset contains the summarized results of drug combination screening studies for the NCI-60 cancer cell lines \
            (excluding the MDA-N cell line). A total of 129 drugs are tested across 59 cell lines resulting in a total of 297098\
                unique drug combination-cell line pairs. For each of the combination drugs, we provide its canonical SMILES string\
                    queried from PubChem. For each cell line, we include the following features downloaded from NCI’s CellMiner\
                        interface: 25,723 gene features capturing transcript expression levels averaged from five microarray \
                            platforms, 627 microRNA expression features and 3171 proteomic features that capture the abundance \
                                levels of a subset of proteins. \n \n There are two kinds of labels included in this dataset. \
                                    CSS measures\
                                    the drug combination sensitivity and is derived using relative IC50 values of compounds and \
                                        the area under their dose-response curves. The other four metrics capture the synergy \
                                            between the two drugs. Synergy is a dimensionless measure of deviation of an observed \
                                                drug combination response from the expected effect of non-interaction. Synergy is \
                                                    calculated using four different models: Bliss model, Highest Single Agent (HSA),\
                                                        Loewe additivity model and Zero Interaction Potency (ZIP).",
        "Given the chemical structural information for the combining drugs and genomic features for a particular cell line, predict\
            the drug synergy level or the drug combination sensitivity in that cell line.",
        " 129 drugs are tested across 59 cell lines resulting in a total of 297098 unique drug combination-cell line pairs.",
        ["Random Split", "Cold Cell Line Split"],
        "DrugSyn",
        [
            [
                "[1] Zagidullin, Bulat, et al. “DrugComb: an integrative cancer drug combination data portal.” Nucleic acids \
                    research 47.W1 (2019): W43-W51. ",
                "https://academic.oup.com/nar/article-abstract/47/W1/W43/5486743"
            ],
            [
                "[2] Reinhold, William C., et al. “CellMiner: a web-based suite of genomic and pharmacologic tools to explore \
                    transcript and drug patterns in the NCI-60 cell line set.” Cancer research 72.14 (2012): 3499-3511. ",
                "https://creativecommons.org/licenses/by/4.0/"
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "MHC1_IEDB-IMGT_Nielsen": [
        "mhc-class-i-iedb-imgt-nielsen-et-al",
        "MHC Class I, IEDB-IMGT, Nielsen et al.",
        "Binding of peptides to MHC class I molecules (MHC-I) is essential for antigen presentation to cytotoxic T-cells. An \
            organized datasets by NetMHCpan for MHC class I collected from IEDB and IMGT/HLA database.",
        "Regression. Given the amino acid sequence of peptide and the pseudo amino acid sequence of MHC, predict the binding \
            affinity.",
        " 185,985 pairs, 43,018 peptides and 150 MHC class 1s",
        ["Random Split"],
        "PeptideMHC",
        [
            [
                "[1] Nielsen, Morten, and Massimo Andreatta. “NetMHCpan-3.0; improved prediction of binding to MHC class I \
                    molecules integrating information from multiple receptor and peptide length datasets.” Genome medicine 8.1\
                        (2016): 1-9. ",
                "https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-016-0288-x"
            ],
            [
                "[2] Vita, Randi, et al. “The immune epitope database (IEDB): 2018 update.” Nucleic acids research 47.D1 (2019): \
                    D339-D343.",
                "http://www.iedb.org/home_v3.php"
            ],
            [
                "[3] Zeng, Haoyang, and David K. Gifford. “Quantification of uncertainty in peptide-MHC binding prediction improves\
                    high-affinity peptide Selection for therapeutic design.” Cell systems 9.2 (2019): 159-166.",
                "https://www.sciencedirect.com/science/article/pii/S240547121930153X"
            ]
        ],
        " CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "MHC2_IEDB_Jensen": [
        "mhc-class-ii-iedb-jensen-et-al",
        "MHC Class II, IEDB, Jensen et al.",
        "Major histocompatibility complex class II (MHC‐II) molecules are found on the surface of antigen‐presenting cells where\
            they present peptides derived from extracellular proteins to T helper cells. Useful to identify T‐cell epitopes. An \
                organized datasets by NetMHCIIpan for MHC class II collected from IEDB database.",
        "Regression. Given the amino acid sequence of peptide and the pseudo amino acid sequence of MHC, predict the \
            binding affinity.",
        "134,281 pairs, 17,003 peptides and 75 MHC class 2s",
        ["Random Split"],
        "PeptideMHC",
        [
            [
                "[1] Jensen, Kamilla Kjaergaard, et al. “Improved methods for predicting peptide binding affinity to MHC class\
                    II molecules.” Immunology 154.3 (2018): 394-406.",
                "https://onlinelibrary.wiley.com/doi/full/10.1111/imm.12889"
            ],
            [
                "[2] Vita, Randi, et al. “The immune epitope database (IEDB): 2018 update.” Nucleic acids research 47.D1 (2019):\
                    D339-D343.",
                "http://www.iedb.org/home_v3.php"
            ],
            [
                "[3] Zeng, Haoyang, and David K. Gifford. “Quantification of uncertainty in peptide-MHC binding prediction improves\
                    high-affinity peptide Selection for therapeutic design.” Cell systems 9.2 (2019): 159-166.",
                "https://www.sciencedirect.com/science/article/pii/S240547121930153X"
            ]
        ],
        " CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "opentargets_dti": [
        "li-michelle-et-al",
        "(Li, Michelle, et al.)",
        "To curate target information for a therapeutic area, we examine the drugs indicated for the therapeutic area of interest and\
            its descendants. The two therapeutic areas examined are rheumatoid arthritis (RA) and inflammatory bowel disease. \
                Positive examples (i.e., where the label y = 1) are proteins targeted by drugs that have at least completed phase \
                    2 of clinical trials for treating a specific therapeutic area. As such, a protein is a promising candidate if \
                        a compound that targets the protein is safe for humans and effective for treating the disease. We retain \
                            positive training examples activated in at least one cell type-specific protein interaction network. We\
                                define negative examples (i.e., where the label y = 0) as druggable proteins that do not have any \
                                    known association with the therapeutic area of interest according to Open Targets. A protein is\
                                        deemed druggable if targeted by at least one existing drug. We extract drugs and their \
                                            nominal targets from Drugbank. We retain negative training examples activated in at \
                                                least one cell type-specific protein interaction network. Note: to get the exact cell-type-specific \
                                                    data and labels used in the PINNACLE paper, please refer to the TDC.scDTI benchmark group.",
        "Classification. Given the protein and cell-context, predict whether the protein is a therapeutic target. ",
        "The final number of positive (negative) samples for RA and IBD were 152 (1,465) and 114 (1,377), respectively. In PINNACLE,\
            this dataset was augmented to include 156 cell types.",
        ["Cold Protein Split"],
        "DataLoader",
        [
            [
                "Michelle M. Li, Yepeng Huang, Marissa Sumathipala, Man Qing Liang, \
                    Alberto Valdeolivas, Ashwin N. Ananthakrishnan, Katherine Liao, \
                        Daniel Marbach and Marinka Zitnik Nature Methods 2024",
                "https://www.biorxiv.org/content/10.1101/2023.07.18.549602v1"
            ]
        ],
        " CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ]
    
}