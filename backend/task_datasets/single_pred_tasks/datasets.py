_DATASETS = {
    "tox": ["hERG", "hERG_Karim", "AMES", "DILI", "Skin Reaction", "LD50_Zhu", "Carcinogens_Lagunin", "ToxCast", "Tox21", "ClinTox"],
    "hts": ["HIV", "SARSCoV2_3CLPro_Diamond", "SARSCoV2_Vitro_Touret", "Orexin1 Receptor", "M1 Muscarinic Receptor Agonists", 
            "M1 Muscarinic Receptor Antagonists", "Potassium Ion Channel Kir2.1", "KCNQ2 Potassium Channel", "Cav3 T-type Calcium Channels", 
            "Choline Transporter", "Serine/Threonine Kinase 33", "Tyrosyl-DNA Phosphodiesterase"],
    "qm": ["QM7b", "QM8", "QM9"],
    "yields": ["Buchwald-Hartwig", "USPTO"],
    "epitope": ["IEDB_Jespersen", "PDB_Jespersen"],
    "develop": ["TAP", "SAbDab_Chen"],
    "CRISPROutcome": ["Leenay"],
}

_META = {
    "LD50_Zhu": [
        "acute-toxicity-ld50", # id
        "Acute Toxicity LD50", # full name
        "Acute toxicity LD50 measures the most conservative \
            dose that can lead to lethal adverse effects. The higher the dose, the more lethal of a drug. \
                This dataset is kindly provided by the authors of [1].", # dataset description
        "Regression. Given a drug SMILES string, predict its acute toxicity.",  # Task Description
        " 7,385 drugs. ", # dataset statistics
        ["Random Split", "Scaffold Split"], # split types
        "Tox", # class name
        [
            [
                "[1] Zhu, Hao, et al. “Quantitative structure− activity relationship modeling of rat acute toxicity \
                by oral exposure.” Chemical research in toxicology 22.12 (2009): 1913-1921. ",
                "https://pubs.acs.org/doi/abs/10.1021/tx900189p?casa_token=vfBbuxuUCqEAAAAA:YAcI0r4Z3rtlRYP_\
                    l5H8OlTfdUh3DVlO6ws_h1NkhpaXH3-NrdI2-s5ghWWJbxfPQw-KhQIAwMi1Di3v"   
            ],  # reference, reference link
        ], # references
        "CC BY 4.0.", # license
        "https://creativecommons.org/licenses/by/4.0/", # license link
    ],
    "hERG": [
        "herg-blockers",
        "hERG blockers",
        "Human ether-à-go-go related gene (hERG) is crucial for the coordination of the heart's beating. Thus, if \
            a drug blocks the hERG, it could lead to severe adverse effects. Therefore, reliable prediction of hERG \
                liability in the early stages of drug design is quite important to reduce the risk of cardiotoxicity-related \
                    attritions in the later development stages. ",
        "Binary classification. Given a drug SMILES string, predict whether it blocks (1) or not blocks (0).",
        "648 drugs.",
        ["Random Split", "Scaffold Split"],
        "Tox",
        [
            [
                "[1] Wang, Shuangquan, et al. “ADMET evaluation in drug discovery. 16. Predicting hERG blockers by combining \
                multiple pharmacophores and machine learning approaches.” Molecular Pharmaceutics 13.8 (2016): 2855-2866.",
                "https://pubs.acs.org/doi/abs/10.1021/acs.molpharmaceut.6b00471?casa_token=YszQx1sl0QgAAAAA:lIztZjmLzi3CPjnYh4lVFe3FAjOKF12N9IwBxjV4wiGw6S6QbpnegfgHEjwPzbgmpW-Bk9VvY9RLAsVo"
            ],
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/",
    ],
    "hERG_Karim": [
        "herg-karim-et-al",
        "hERG Karim et al.",
        "A integrated Ether-a-go-go-related gene (hERG) dataset consisting of molecular structures\
            labelled as hERG (<10uM) and non-hERG (>=10uM) blockers in the form of SMILES strings was obtained from the\
                DeepHIT, the BindingDB database, ChEMBL bioactivity database, and other literature.",
        "Binary classification. Given a drug SMILES string, predict whether it blocks (1, <10uM) or not blocks (0, >=10uM).",
        "13,445 drugs. ",
        ["Random Split", "Scaffold Split"], 
        "Tox",
        [
            [
                "[1] Karim, A., et al. CardioTox net: a robust predictor for hERG channel blockade based on deep learning \
                meta-feature ensembles. J Cheminform 13, 60 (2021).",
                "https://doi.org/10.1186/s13321-021-00541-z"   
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "AMES": [
        "ames-mutagenicity",
        "AMES Mutagenicity",
        "Mutagenicity means the ability of a drug to induce genetic alterations. Drugs that can cause damage to\
            the DNA can result in cell death or other severe adverse effects. Nowadays, the most widely used assay for\
                testing the mutagenicity of compounds is the Ames experiment which was invented by a professor named Ames.\
                    The Ames test is a short-term bacterial reverse mutation assay detecting a large number of compounds which\
                        can induce genetic damage and frameshift mutations. The dataset is aggregated from four papers",
        "Binary classification. Given a drug SMILES string, predict whether it is mutagenic (1) or not mutagenic (0).",
        "7,255 drugs.",
        ["Random Split", "Scaffold Split"], 
        "Tox",
        [
            [
                "[1] Xu, Congying, et al. “In silico prediction of chemical Ames mutagenicity.” Journal of chemical information \
                and modeling 52.11 (2012): 2840-2847.",
                "https://pubs.acs.org/doi/abs/10.1021/ci300400a?casa_token=A86ksblef0kAAAAA:2kLxP4j2NOigeBsSqUb8C9ThZLVBR_\
                    Ztc8gJg_HhyLCRtZF-MfMMyq4bIwhMlH0MyJXZuWkFXXrGqiMR"  
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "DILI": [
        "dili-drug-induced-liver-injury",
        "DILI (Drug Induced Liver Injury)",
        "Drug-induced liver injury (DILI) is fatal liver disease caused by drugs and it has been the single most frequent cause\
            of safety-related drug marketing withdrawals for the past 50 years (e.g. iproniazid, ticrynafen, benoxaprofen).\
                This dataset is aggregated from U.S. FDA’s National Center for Toxicological Research. ",
        "Binary classification. Given a drug SMILES string, predict whether it can cause liver injury (1) or not (0).",
        "475 drugs",
        ["Random Split", "Scaffold Split"],
        "Tox",
        [
            [
                "[1] Xu, Youjun, et al. “Deep learning for drug-induced liver injury.” Journal of chemical information and \
                modeling 55.10 (2015): 2085-2093. ",
                "https://pubs.acs.org/doi/abs/10.1021/acs.jcim.5b00238" 
            ],
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "Skin Reaction": [
        "skin-reaction",
        "Skin Reaction",
        "Repetitive exposure to a chemical agent can induce an immune reaction in inherently susceptible individuals \
            that leads to skin sensitization. The dataset used in this study was retrieved from the ICCVAM (Interagency \
                Coordinating Committee on the Validation of Alternative Methods) report on the rLLNA.",
        "Binary classification. Given a drug SMILES string, predict whether it can cause skin reaction (1) or not (0). ",
        "404 drugs.",
        ["Random Split", "Scaffold Split"],
        "Tox", 
        [
            [
                "[1] Alves, Vinicius M., et al. “Predicting chemically-induced skin reactions. Part I: QSAR models\
                of skin sensitization and their application to identify potentially hazardous compounds.” Toxicology\
                    and applied pharmacology 284.2 (2015): 262-272. ",
                "https://www.sciencedirect.com/science/article/pii/S0041008X14004529?casa_token=gMz283g8Tj0AAAAA:\
                    DNKlQvZC2fUfMNz4vbqB7WEQGSDMpibtoST_G8vhZ7I4GK950VKxrLTK3jBrSlYKH5flC4sJ6O4"
                
            ],
            [
                "[2] The reduced murine local lymph node assay: an alternative test method using fewer animals to assess\
                the allergic contact dermatitis potential of chemicals and products. ",
                "https://ntp.niehs.nih.gov/whatwestudy/niceatm/test-method-evaluations/immunotoxicity/llna/index.html"
            ],
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/" 
    ],
    "Carcinogens_Lagunin": [
        "carcinogens",
        "Carcinogens",
        "A carcinogen is any substance, radionuclide, or radiation that promotes carcinogenesis, the formation of cancer.\
            This may be due to the ability to damage the genome or to the disruption of cellular metabolic processes.",
        "Binary classification. Given a drug SMILES string, predict whether it can cause carcinogen.",
        "278 drugs.",
        ["Random Split", "Scaffold Split"],
        "Tox",
        [
            [
                "[1] Lagunin, Alexey, et al. “Computer‐aided prediction of rodent carcinogenicity by PASS and CISOC‐PSCT.”\
                QSAR & Combinatorial Science 28.8 (2009): 806-810. ",
                "https://onlinelibrary.wiley.com/doi/abs/10.1002/qsar.200860192?casa_token=NR55Na01l8gAAAAA:603Kr5drd\
                    -EIWlXFQVJpnpEm05-GxMBwVeBJiORBah8IIsPt1yvy8UNdADagv1ty8SlPvX4XF4r7QpWK" 
            ],
            [
                "[2] Cheng, Feixiong, et al. “admetSAR: a comprehensive source and free tool for assessment of chemical\
                ADMET properties.” (2012): 3099-3105.",
                "https://pubs.acs.org/doi/abs/10.1021/ci300367a?casa_token=9fEKYcMw5zoAAAAA:ZDPZ-e-M9RulemgBjAPNkSn\
                    WXlVCcPzkxNK9bX40Abz9o24NpitsXY0tizgDL5ekPiNtEPFSeOwwUTHG"
            ],
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "ClinTox": [
        "clintox",
        "ClinTox",
        "The ClinTox dataset includes drugs that have failed clinical trials for toxicity reasons and also drugs\
            that are associated with successful trials.",
        "Binary classification. Given a drug SMILES string, predict the clinical toxicity. ",
        "1,484 drugs. ",
        ["Random Split", "Scaffold Split"],
        "Tox",
        [
            [
                "[1] Gayvert, Kaitlyn M., Neel S. Madhukar, and Olivier Elemento. “A data-driven approach to predicting \
                successes and failures of clinical trials.” Cell chemical biology 23.10 (2016): 1294-1301.",
                "https://pubmed.ncbi.nlm.nih.gov/27642066/"
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "SARSCoV2_Vitro_Touret": [
        "sars-cov-2-in-vitro-touret-et-al",
        "SARSCoV2 Vitro Touret",
        "An in-vitro screen of the Prestwick chemical library composed of 1,480 approved drugs in an \
            infected cell-based assay. From MIT AiCures. ",
        "Binary classification. Given a drug SMILES string, predict its activity against SARSCoV2.",
        "1,480 drugs. ",
        ["Random Split", "Scaffold Split"],
        "HTS",
        [
            [
                "[1] Touret, F., Gilles, M., Barral, K. et al. In vitro screening of a FDA approved \
                    chemical library reveals potential inhibitors of SARS-CoV-2 replication. Sci Rep 10, 13093 (2020).",
                "https://www.nature.com/articles/s41598-020-70143-6"
            ],
            [
                "[2] MIT AI Cures.",
                "https://www.aicures.mit.edu/data"
            ],
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "SARSCoV2_3CLPro_Diamond": [
        "sars-cov-2-3cl-protease-diamond",
        "SARS-CoV-2 3CL Protease, Diamond.",
        "A large XChem crystallographic fragment screen against SARS-CoV-2 main protease at high resolution. From MIT AiCures.",
        "Binary classification. Given a drug SMILES string, predict its activity against SARSCoV2 3CL Protease",
        "879 drugs. ",
        ["Random Split", "Scaffold Split"],
        "HTS",
        [
            [
                "[1] Diamond Light Source ",
                "https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem.html"
            ],
            [
                "[2] MIT AI Cures.",
                "https://www.aicures.mit.edu/data"
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "HIV": [
        "hiv",
        "HIV",
        " The HIV dataset was introduced by the Drug Therapeutics Program (DTP) AIDS Antiviral Screen, which tested \
            the ability to inhibit HIV replication for over 40,000 compounds. From MoleculeNet.",
        "Binary classification. Given a drug SMILES string, predict its activity against HIV virus.",
        "41,127 drugs. ",
        ["Random Split", "Scaffold Split"],
        "HTS",
        [
            [
                "[1] AIDS Antiviral Screen Data. ",
                "https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data"
            ],
            [
                "[2] Wu, Zhenqin, et al. “MoleculeNet: a benchmark for molecular machine learning.” Chemical science 9.2 (2018): 513-530.",
                "https://pubs.rsc.org/--/content/articlehtml/2018/sc/c7sc02664a"
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "Buchwald-Hartwig": [
        "buchwald-hartwig",
        "Buchwald-Hartwig",
        "Ahneman et al. performed high-throughput experiments on Pd-catalysed Buchwald–Hartwig C-N cross coupling reactions, \
            measuring the yields for each reaction.",
        "Given reactant and product set X, predict the yields Y.",
        "55,370 reactions.",
        ["Random Split"],
        "Yields",
        [
            [
                "[1] Sandfort et al. “A structure-based platform for predicting chemical reactivity.” Chem (2020). ",
                "https://www.sciencedirect.com/science/article/pii/S2451929420300851"
            ],
            [
                "[2] Ahneman et al. “Predicting reaction performance in C–N cross-coupling using machine learning.” Science \
                    360.6385 (2018): 186-190. ",
                "https://science.sciencemag.org/content/360/6385/186.abstract?casa_token=Y1YYm8zLW4YAAAAA:U2B1Mqw-wjgZuqf2jd5e\
                    DUSmOCHm9dKMIqrMR5aGs4Js6eCwXV4gGPvA95wgqF-Gf6UjomO9FaAFeJQ",
            ],
            [
                "[3] Schwaller, Philippe, et al. “Prediction of Chemical Reaction Yields using Deep Learning.” (2020). ChemRxiv.",
                "https://chemrxiv.org/ndownloader/files/25011413"
            ],
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "USPTO": [
        "uspto",
        "USPTO",
        "TDC parses the yields outcome from the full USPTO (United States Patent and Trademark Office) dataset.",
        "Given reactant and product set X, predict the yields Y.",
        "853,638 reactions.",
        ["Random Split"],
        "Yields",
        [
            [
                "[1] Lowe, Daniel Mark. Extraction of chemical structures and reactions from the literature. Diss. \
                    University of Cambridge, 2012. ",
                "https://aspace.repository.cam.ac.uk/handle/1810/244727"
            ]
        ],
        "CC0",
        "https://creativecommons.org/share-your-work/public-domain/cc0/"
    ],
    "IEDB_Jespersen" : [
        "iedb-jespersen-et-al",
        "IEDB, Jespersen et al.",
        "Epitope prediction is to predict the active region in the antigen. This dataset is from Bepipred, which curates a \
            dataset from IEDB. It collects B-cell epitopes and non-epitope amino acids determined from crystal structures.",
        "Token-level classification. Given an amino acid sequence, predict amino acid token that is active in binding, i.e. X is\
            amino acid sequence, Y is a list of indices for the active positions in X.",
        "3,159 antigens.",
        ["Random Split"],
        "Epitope",
        [
            [
                "[1] Vita, Randi, et al. “The immune epitope database (IEDB): 2018 update.” Nucleic acids research 47.D1 (2019):\
                    D339-D343.",
                "https://academic.oup.com/nar/article-abstract/47/D1/D339/5144151"
            ],
            [
                "[2] Jespersen, Martin Closter, et al. “BepiPred-2.0: improving sequence-based B-cell epitope prediction using \
                    conformational epitopes.” Nucleic acids research 45.W1 (2017): W24-W29.",
                "https://pubmed.ncbi.nlm.nih.gov/28472356/"
            ]
        ],
        "CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ],
    "PDB_Jespersen": [
        "pdb-jespersen-et-al",
        "PDB, Jespersen et al.",
        "Epitope prediction is to predict the active region in the antigen. This dataset is from Bepipred, which curates a dataset\
            from PDB. It collects B-cell epitopes and non-epitope amino acids determined from crystal structures.",
        "Token-level classification. Given the antigen's amino acid sequence, predict amino acid token that is active in binding, \
            i.e. X is an amino acid sequence, Y is a list of indices for the active tokens in X.",
        "447 antigens.",
        ["Random Split"],
        "Epitope",
        [
            [
                "[1] Jespersen, Martin Closter, et al. “BepiPred-2.0: improving sequence-based B-cell epitope prediction using \
                    conformational epitopes.” Nucleic acids research 45.W1 (2017): W24-W29.",
                "https://pubmed.ncbi.nlm.nih.gov/28472356/"
            ],
            [
                "[2] Berman, Helen M., et al. “The protein data bank.” Nucleic acids research 28.1 (2000): 235-242. ",
                "https://academic.oup.com/nar/article-abstract/28/1/235/2384399"
            ]
        ],
        " CC BY 4.0.",
        "https://creativecommons.org/licenses/by/4.0/"
    ]
    
}