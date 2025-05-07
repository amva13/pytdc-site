_LEADERBOARDS = {
    "Caco2_Wang": [
        "old", # old or new format (incl dataset description)
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr", # increasing or descending order
        [
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.276
            ],
            [
                "BaseBoosting", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "365,713", 0.285
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.287
            ],
            [
                "MolMapNet-D", "Shen Wan Xiang", "wanxiang.shen@u.nus.edu", "https://github.com/shenwanxiang/bidd-molmap/tree\
                    /master/misc/tdc_leaderboard_submission/Caco2_Wang-MolMapNet-D.ipynb", 
                    "https://www.nature.com/articles/s42256-021-00301-6", "407,617", 0.287
            ],
            [
                "XGBoost", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/blob/main/submission.ipynb", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "12", 0.289
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies", 
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.297
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons", 
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.321
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "12.6M", 0.322
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.330
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu","https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.335
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.341
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.344
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.393
            ]
        ], # meta info: model, contact_name, contact_email, GH, repo, .. other .., value to rank by
        [
            [
                0.276,
                0.005
            ],
            [
                0.285,
                0.005
            ],
            [
                0.287,
                0.005
            ],
            [
                0.287,
                0.005
            ],
            [
                0.289,
                0.011
            ],
            [
                0.297,
                0.008
            ],
            [
                0.321,
                0.005
            ],
            [
                0.322,
                0.026
            ],
            [
                0.330,
                0.024
            ],
            [
                0.335,
                0.033
            ],
            [
                0.341,
                0.004
            ],
            [
                0.344,
                0.015
            ],
            [
                0.393,
                0.024
            ],
        ], # metrics (val, std)
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Caco2_Wang ", "cm/s", "906", "Regression", "MAE", "Scaffold"]
    ],
    "Bioavailability_Ma": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC"],
        "desc",
        [
            [
                "HistGradientBoostingClassifier (DeepMol)", "DeepMol Team", "jcapels96@gmail.com", 
                "https://github.com/BioSystemsUM/deepmol_case_studies", "https://doi.org/10.1101/2024.05.27.595849",
                "N/A", 0.753
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.748
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.746
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.742
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.730
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.715
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.706
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.672
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.671
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", 
                "https://github.com/chemprop/chemprop", "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A",
                0.667
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.632
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.632
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies", 
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.617
            ],
        ],
        [
            [
                0.753,
                0
            ],
            [
                0.748,
                0.033
            ],
            [
                0.746,
                0.030
            ],
            [
                0.742,
                0.010
            ],
            [
                0.730,
                0.010
            ],
            [
                0.715,
                0.011
            ],
            [
                0.706,
                0.031
            ],
            [
                0.672,
                0.021
            ],
            [
                0.671,
                0.026
            ],
            [
                0.667,
                0.068
            ],
            [
                0.632,
                0.036
            ],
            [
                0.617,
                0.009
            ],
            [
                0.613,
                0.015
            ],
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Bioavailability_Ma" , "%", "640", "Binary", "AUROC", "Scaffold"],
    ],
    "Lipophilicity_AstraZeneca": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.460
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.467
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.470
            ],
            [
                "BaseBoosting KyQVZ6b2", "David Huang", "david@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/tree/main", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6350b9d186473a47d31a8492", "N/A", 0.479
            ],
            [
                "CMPNN", "Devansh Amin", "devanshamin97@gmail.com", "https://github.com/devanshamin/LitGNN", 
                "https://www.ijcai.org/Proceedings/2020/392", "3.0 M", 0.515
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.525
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.535
            ],
            [
                "StackingRegressor (DeepMol)", "DeepMol Team", "jcapels96@gmail.com", 
                "https://github.com/BioSystemsUM/deepmol_case_studies", "https://doi.org/10.1101/2024.05.27.595849",
                "N/A", 0.538
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.539
            ],
            [
                "GCN", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1609.02907",
                "191,810", 0.541
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.547
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.563
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.572
            ],
        ],
        [
            [
                0.460,
                0.006
            ],
            [
                0.467,
                0.006
            ],
            [
                0.470,
                0.009
            ],
            [
                0.479,
                0.007
            ],
            [
                0.515,
                0.038
            ],
            [
                0.525,
                0.003
            ],
            [
                0.535,
                0.012
            ],
            [
                0.538,
                0.001
            ],
            [
                0.539,
                0.002
            ],
            [
                0.541,
                0.011
            ],
            [
                0.547,
                0.024
            ],
            [
                0.563,
                0.023
            ],
            [
                0.572,
                0.007
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Lipophilicity_AstraZeneca", "log-ratio", "4,200", "Regression", "MAE", "Scaffold"]
    ],
    "Solubility_AqSolDB": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE" ],
        "incr",
        [
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.725
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.761
            ],
            [
                "DeepMol (AutoML) ", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.775
            ],
            [
                "AttentiveFP ", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.776
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.789
            ],
            [
                " MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.792
            ],
            [
                "CMPNN", "Devansh Amin", "devanshamin97@gmail.com", "https://github.com/devanshamin/LitGNN", 
                "https://www.ijcai.org/Proceedings/2020/392", "3.0 M", 0.796
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.827
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons", 
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.828
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.829
            ]
            
        ],
        [
            [
                0.725,
                0.011
            ],
            [
                0.761,
                0.025
            ],
            [
                0.775,
                0.006
            ],
            [
                0.776,
                0.008
            ],
            [
                0.789,
                0.003
            ],
            [
                0.792,
                0.002
            ],
            [
                0.796,
                0.038
            ],
            [
                0.827,
                0.047
            ],
            [
                0.828,
                0.002
            ],
            [
                0.829,
                0.022
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Solubility_AqSolDB ", "log mol/L", "9,982", "Regression", "MAE", "Scaffold"]
    ],
    "HIA_Hou": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC" ],
        "desc",
        [
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.990
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.989
            ],
            [
                "RFStacker", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/blob/main/submission.ipynb", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "1,858,225", 0.988
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.986
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "1.6M", 0.984
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.981
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.981
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.978
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.975
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.974
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", "https://doi.org/10.1093/bioinformatics/btaa1005",
                "633,409", 0.972
            ]
        ],
        [
            [
                0.990,
                0.002
            ],
            [
                0.989,
                0.001
            ],
            [
                0.988,
                0.002
            ],
            [
                0.986,
                0.000
            ],
            [
                0.984,
                0.004
            ],
            [
                0.981,
                0.009
            ],
            [
                0.981,
                0.002
            ],
            [
                0.978,
                0.006
            ],
            [
                0.975,
                0.004
            ],
            [
                0.974,
                0.007
            ],
            [
                0.972,
                0.008
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.HIA_Hou ", "%", "578", "Binary", "AUROC", "Scaffold"]
    ],
    "Pgp_Broccatelli": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC" ],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.938
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.935
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "1.6M", 0.931
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.930
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.929
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.929
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", 
                "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.928
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.923
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.922
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", "https://doi.org/10.1093/bioinformatics/btaa1005",
                "633,409", 0.918
            ],
            [
                "CNN (DeepPurpose)", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "226,625", 0.908
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.902
            ],
        ],
        [
            [
                0.938,
                0.002
            ],
            [
                0.935,
                0.006
            ],
            [
                0.931,
                0.003
            ],
            [
                0.930,
                0.002
            ],
            [
                0.929,
                0.010
            ],
            [
                0.929,
                0.006
            ],
            [
                0.928,
                0.008
            ],
            [
                0.923,
                0.005
            ],
            [
                0.922,
                0.0
            ],
            [
                0.918,
                0.007
            ],
            [
                0.908,
                0.012
            ],
            [
                0.902,
                0.020
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Pgp_Broccatelli ", "%", "1,212", "Binary", "AUROC", "Scaffold"]
    ],
    "BBB_Martins": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC" ],
        "desc",
        [
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.920
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.916
            ],
            [
                "Lantern RADR Ensemble", "Rick Fontenot", "rick@lanternpharma.com", "https://github.com/lanternpharma/tdc-bbb-martins",
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "N/A", 0.915
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.913
            ],
            [
                "Lantern RADR Deep Neural Network", "Rick Fontenot", "rick@lanternpharma.com", 
                "https://github.com/lanternpharma/tdc-bbb-martins", 
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "N/A", 0.912
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark",
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.910
            ],
            [
                "Lantern RADR Random Forest", "Rick Fontenot", "rick@lanternpharma.com", 
                "https://github.com/lanternpharma/tdc-bbb-martins", 
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "319", 0.908
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.908
            ],
            [
                "Lantern RADR SVM", "Rick Fontenot", "rick@lanternpharma.com", "https://github.com/lanternpharma/tdc-bbb-martins",
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "241", 0.905
            ],
            [
                "Lantern RADR Logistic Regression", "Rick Fontenot", "rick@lanternpharma.com", 
                "https://github.com/lanternpharma/tdc-bbb-martins", 
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf","456", 0.903
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC",
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.901
            ],
        ],
        [
            [
                0.920,
                0.006
            ],
            [
                0.916,
                0.001
            ],
            [
                0.915,
                0.002
            ],
            [
                0.913,
                0.001
            ],
            [
                0.912,
                0.003
            ],
            [
                0.910,
                0.024
            ],
            [
                0.908,
                0.002
            ],
            [
                0.908,
                0.010
            ],
            [
                0.905,
                0.007
            ],
            [
                0.903,
                0.002
            ],
            [
                0.901,
                0.007
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.BBB_Martins ", "%", "1,975", "Binary", "AUROC", "Scaffold"]
    ],
    "PPBR_AZ": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "26.0M", 7.505
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 7.526
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 7.660
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 7.788
            ],
            [
                "BaseBoosting KyQVZ6b2", "David Huang", "david@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/tree/main", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6350b9d186473a47d31a8492", "N/A", 7.914
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 7.99
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 8.288
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 8.680
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons",
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 9.185
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 9.292
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://pubmed.ncbi.nlm.nih.gov/31408336/",
                "300,806", 9.373
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 9.445
            ]
        ],
        [
            [
                7.505,
                0.073
            ],
            [
                7.526,
                0.106
            ],
            [
                7.660,
                0.058
            ],
            [
                7.788,
                0.210
            ],
            [
                7.914,
                0.096
            ],
            [
                7.99,
                0.104
            ],
            [
                8.288,
                0.173
            ],
            [
                8.680,
                0.262
            ],
            [
                9.185,
                0.000
            ],
            [
                9.292,
                0.384
            ],
            [
                9.373,
                0.335
            ],
            [
                9.445,
                0.224
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.PPBR_AZ ", "%", "1,797", "Regression", "MAE", "Scaffold"]
    ],
    "VDss_Lombardo": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "Spearman"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.713
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.707
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "26.0M", 0.662
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.628
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons",
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.627
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.609
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.582
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.561
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.559
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.497
            ],
            [
                "Morgan + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "1,477,185", 0.493
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.491
            ],
        ],
        [
            [
                0.713,
                0.007
            ],
            [
                0.707,
                0.009
            ],
            [
                0.662,
                0.013
            ],
            [
                0.628,
                0.023
            ],
            [
                0.627,
                0.010
            ],
            [
                0.609,
                0.014
            ],
            [
                0.582,
                0.031
            ],
            [
                0.561,
                0.025
            ],
            [
                0.559,
                0.019
            ],
            [
                0.497,
                0.011
            ],
            [
                0.493,
                0.011
            ],
            [
                0.491,
                0.046
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.VDss_Lombardo ", "L/kg", "1,130", "Regression", "Spearman", "Scaffold"]
    ],
    "CYP2C9_Veith": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.859
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.839
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.829
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.788
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark",
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.786
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.783
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.777
            ],
            [
                "ColorRefinement + Weighted Ensemble LGBM", "Parker Burchett", "parkerburchett@gmail.com", 
                "https://github.com/parkerburchett/TDC-DeepLearning/blob/main/modeling/CYP%20Weighted%20Model.ipynb",
                "https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/No%20paper", "68", 0.767
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.758
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.754
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.751
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.749
            ],
        ],
        [
            [
                0.859,
                0.001
            ],
            [
                0.839,
                0.003
            ],
            [
                0.829,
                0.003
            ],
            [
                0.788,
                0.005
            ],
            [
                0.786,
                0.004
            ],
            [
                0.783,
                0.002
            ],
            [
                0.777,
                0.003
            ],
            [
                0.767,
                0.003
            ],
            [
                0.758,
                0.002
            ],
            [
                0.754,
                0.002
            ],
            [
                0.751,
                0.006
            ],
            [
                0.749,
                0.004
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.CYP2C9_Veith ", "%", "12,092", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP2D6_Veith": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.790
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.739
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.723
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://doi.org/10.1101/2024.05.27.595849",
                "2,067,053", 0.721
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "26.0M", 0.704
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.685
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.673
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.664
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.649
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://pubmed.ncbi.nlm.nih.gov/31408336/",
                "300,806", 0.646
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.644
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://ieeexplore.ieee.org/document/9412489",
                "480,193", 0.627
            ],
        ],
        [
            [
                0.790,
                0.001
            ],
            [
                0.739,
                0.005
            ],
            [
                0.723,
                0.003
            ],
            [
                0.721,
                0.009
            ],
            [
                0.704,
                0.003
            ],
            [
                0.685,
                0.000
            ],
            [
                0.673,
                0.007
            ],
            [
                0.664,
                0.012
            ],
            [
                0.649,
                0.016
            ],
            [
                0.646,
                0.014
            ],
            [
                0.644,
                0.085
            ],
            [
                0.627,
                0.009
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.CYP2D6_Veith ", "%", "13,130", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP3A4_Veith": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.916
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.904
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.902
            ],
            [
                "MapLight", "Jim Notwell", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.881
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "26.0M", 0.878
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.876
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.875
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.862
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.855
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://pubmed.ncbi.nlm.nih.gov/31408336/",
                "300,806", 0.851
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.849
            ],
        ],
        [
            [
                0.916,
                0.000
            ],
            [
                0.904,
                0.002
            ],
            [
                0.902,
                0.002
            ],
            [
                0.881,
                0.001
            ],
            [
                0.878,
                0.003
            ],
            [
                0.876,
                0.003
            ],
            [
                0.875,
                0.002
            ],
            [
                0.862,
                0.003
            ],
            [
                0.855,
                0.004
            ],
            [
                0.851,
                0.006
            ],
            [
                0.849,
                0.004
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.CYP3A4_Veith ", "%", "12,328", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP2C9_Substrate_CarbonMangels": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.441
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.437
            ],
            [
                "Random Forest", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "9", 0.437
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf",
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.433
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.417
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.417
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.415
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "26.0M", 0.414
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.400
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.392
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.382
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.381
            ]
        ],
        [
            [
                0.441,
                0.033
            ],
            [
                0.437,
                0.008
            ],
            [
                0.437,
                0.022
            ],
            [
                0.433,
                0.017
            ],
            [
                0.417,
                0.010
            ],
            [
                0.417,
                0.005
            ],
            [
                0.415,
                0.008
            ],
            [
                0.414,
                0.027
            ],
            [
                0.400,
                0.008
            ],
            [
                0.392,
                0.026
            ],
            [
                0.382,
                0.019
            ],
            [
                0.381,
                0.045
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.CYP2C9_Substrate_CarbonMangels ", "%", "666", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP2D6_Substrate_CarbonMangels": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "1.6M", 0.739
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.736
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.731
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.720
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.713
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.704
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.704
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.686
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.685
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.677
            ],
            [
                "Morgan + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "1,477,185", 0.671
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.632
            ]
        ],
        [
            [
                0.739,
                0.024
            ],
            [
                0.736,
                0.024
            ],
            [
                0.731,
                0.037
            ],
            [
                0.720,
                0.002
            ],
            [
                0.713,
                0.009
            ],
            [
                0.704,
                0.015
            ],
            [
                0.686,
                0.031
            ],
            [
                0.685,
                0.029
            ],
            [
                0.677,
                0.047
            ],
            [
                0.671,
                0.066
            ],
            [
                0.632,
                0.037
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.CYP2D6_Substrate_CarbonMangels ", "%", "664", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP3A4_Substrate_CarbonMangels": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC"],
        "desc",
        [
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.667
            ],
            [
                "CNN (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "226,625", 0.662
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.665
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "52.0M", 0.654
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.650
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.647
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.640
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.639
            ],
            [
                "Morgan + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "1,477,185", 0.633
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.630
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.629
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.619
            ]
        ],
        [
            [
                0.667,
                0.019
            ],
            [
                0.662,
                0.031
            ],
            [
                0.655,
                0.003
            ],
            [
                0.654,
                0.022
            ],
            [
                0.650,
                0.006
            ],
            [
                0.647,
                0.008
            ],
            [
                0.640,
                0.016
            ],
            [
                0.639,
                0.012
            ],
            [
                0.633,
                0.013
            ],
            [
                0.630,
                0.008
            ],
            [
                0.629,
                0.027
            ],
            [
                0.619,
                0.030
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.CYP3A4_Substrate_CarbonMangels ", "%", "667", "Binary", "AUROC", "Scaffold"]
    ],
    "Half_Life_Obach": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "Spearman"],
        "desc",
        [
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.576
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.562
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.557
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "6.5M", 0.551
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.547
            ],
            [
                "Voting Regressor (KNN, SVM)", "Euclia", "euclia@euclia.io", "https://tdcommons.ai/benchmark/admet_group/16halflife/",
                "https://tdcommons.ai/benchmark/admet_group/16halflife/", "5", 0.544
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.485
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons",
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.438
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC",
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.392
            ],
            [
                "Morgan + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet",
                "https://doi.org/10.1093/bioinformatics/btaa1005", "1,477,185", 0.329
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.265
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.239
            ]
        ],
        [
            [
                0.576,
                0.025
            ],
            [
                0.562,
                0.008
            ],
            [
                0.557,
                0.034
            ],
            [
                0.551,
                0.020
            ],
            [
                0.547,
                0.032
            ],
            [
                0.544,
                0.034
            ],
            [
                0.485,
                0.039
            ],
            [
                0.438,
                0.011
            ],
            [
                0.392,
                0.065
            ],
            [
                0.329,
                0.083
            ],
            [
                0.265,
                0.032
            ],
            [
                0.239,
                0.019
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Half_Life_Obach ", "hr", "667", "Regression", "Spearman", "Scaffold"]   
    ],
    "Clearance_Hepatocyte_AZ": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "Spearman"],
        "desc",
        [
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.536
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.498
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "1.6M", 0.495
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.466
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons",
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.440
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.440
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.439
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.431
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop",
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.430
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", "https://github.com/euclia/public-models",
                "50", 0.424
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.413
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.401
            ]
        ],
        [
            [
                0.536,
                0.020
            ],
            [
                0.498,
                0.009
            ],
            [
                0.495,
                0.030
            ],
            [
                0.466,
                0.012
            ],
            [
                0.440,
                0.003
            ],
            [
                0.440,
                0.011
            ],
            [
                0.439,
                0.026
            ],
            [
                0.431,
                0.006
            ],
            [
                0.430,
                0.021
            ],
            [
                0.424,
                0.008
            ],
            [
                0.413,
                0.028
            ],
            [
                0.401,
                0.037
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Clearance_Hepatocyte_AZ ", "uL.min-1.(10^6 cells)-1", "1,020", "Regression", "Spearman", "Scaffold"]
    ],
    "Clearance_Microsome_AZ": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "Spearman"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.630
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.626
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.625
            ],
            [
                "RFStacker", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/blob/main/submission.ipynb",
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "1,858,225", 0.625
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "3.2M", 0.611
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.599
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC",
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.597
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet",
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.586
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.585
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.578
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.572
            ]
        ],
        [
            [
                0.630,
                0.010
            ],
            [
                0.626,
                0.008
            ],
            [
                0.625,
                0.012
            ],
            [
                0.625,
                0.002
            ],
            [
                0.611,
                0.016
            ],
            [
                0.599,
                0.025
            ],
            [
                0.597,
                0.025
            ],
            [
                0.586,
                0.014
            ],
            [
                0.585,
                0.034
            ],
            [
                0.578,
                0.007
            ],
            [
                0.572,
                0.010
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.Clearance_Microsome_AZ ", "mL.min-1.g-1", "1,102", "Regression", "Spearman", "Scaffold"]
    ],
    "LD50_Zhu": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.541
            ],
            [
                "BaseBoosting KyQVZ6b2", "David Huang", "david@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/tree/main",
                "https://chemrxiv.org/engage/chemrxiv/article-details/6350b9d186473a47d31a8492", "N/A", 0.552
            ],
            [
                "MACCS keys + autoML", "Alexander Scarlat", "ascarlat@mitre.org", "https://github.com/scarlat1/AcuteToxicityLD50",
                "https://tdcommons.ai/benchmark/admet_group/19ld50/NaN", "N/A", 0.588
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237",
                "N/A", 0.606
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.614
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.621
            ],
            [
                "QuGIN", "Shuai Shi", "310284598@qq.com", "https://github.com/NumnumM/QuGIN.git", "https://arxiv.org/pdf/1810.00826.pdf",
                "1,797,506", 0.622
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.625
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.630
            ],
            [
                "CMPNN", "Devansh Amin", "devanshamin97@gmail.com", "https://github.com/devanshamin/LitGNN", "https://www.ijcai.org/Proceedings/2020/392",
                "3.0M", 0.631
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.633
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons", "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1",
                "N/A", 0.636
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", "https://github.com/euclia/public-models",
                "50", 0.646
            ]
        ],
        [
            [
                0.541,
                0.015
            ],
            [
                0.552,
                0.009
            ],
            [
                0.588,
                0.005
            ],
            [
                0.606,
                0.024
            ],
            [
                0.614,
                0.004
            ],
            [
                0.621,
                0.003
            ],
            [
                0.622,
                0.015
            ],
            [
                0.625,
                0.022
            ],
            [
                0.630,
                0.012
            ],
            [
                0.631,
                0.021
            ],
            [
                0.633,
                0.003
            ],
            [
                0.636,
                0.001
            ],
            [
                0.646,
                0.011
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.LD50_Zhu ", "log(1/(mol/kg))", "7,385", "Regression", "MAE", "Scaffold"]
    ],
    "hERG": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.880
            ],
            [
                "CFA", "Nan Jiang",  "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.875
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf",
                "1,103,000", 0.874
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.871
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.856
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13.0M", 0.848
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet",
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.841
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237",
                "N/A", 0.840
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.825
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.778
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.756
            ],
            [
                "ContextPred", "Kexin Huang", "kexinhuang@hsph.harvard.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet",
                "https://doi.org/10.1093/bioinformatics/btaa1005", "2,067,053", 0.756
            ]
        ],
        [
            [
                0.880,
                0.002
            ],
            [
                0.875,
                0.014
            ],
            [
                0.874,
                0.014
            ],
            [
                0.871,
                0.004
            ],
            [
                0.856,
                0.009
            ],
            [
                0.848,
                0.009
            ],
            [
                0.841,
                0.020
            ],
            [
                0.840,
                0.007
            ],
            [
                0.825,
                0.007
            ],
            [
                0.778,
                0.046
            ],
            [
                0.763,
                0.015
            ],
            [
                0.756,
                0.023
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.hERG ", "%", "648", "Binary", "AUROC", "Scaffold"]
    ],
    "AMES": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC"],
        "desc",
        [
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark",
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.871
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.869
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.868
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "6.5M", 0.854
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.852
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237",
                "N/A", 0.850
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.847
            ],
            [
                "CMPNN", "Devansh Amin", "devanshamin97@gmail.com", "https://github.com/devanshamin/LitGNN", "https://www.ijcai.org/Proceedings/2020/392",
                "3.0M", 0.843
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237",
                "N/A", 0.842
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.842
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.837
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.823
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet",
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.823
            ]
        ],
        [
            [
                0.871,
                0.002
            ],
            [
                0.869,
                0.002
            ],
            [
                0.868,
                0.002
            ],
            [
                0.854,
                0.007
            ],
            [
                0.852,
                0.005
            ],
            [
                0.850,
                0.004
            ],
            [
                0.847,
                0.007
            ],
            [
                0.843,
                0.009
            ],
            [
                0.842,
                0.014
            ],
            [
                0.842,
                0.008
            ],
            [
                0.837,
                0.009
            ],
            [
                0.823,
                0.006
            ],
            [
                0.823,
                0.011
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.AMES ", "%", "7,255", "Binary", "AUROC", "Scaffold"]
    ],
    "DILI": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC"],
        "desc",
        [
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.925
            ],
            [
                "ChemFM", "Feiyang Cai", "feiyang@clemson.edu", "https://github.com/TheLuoFengLab/ChemFM/tree/master/finetuning/property_prediction",
                "https://arxiv.org/abs/2410.21422", "13M", 0.920
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.919
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.919
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.917
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.909
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.899
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.887
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.887
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.886
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.885
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet",
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.875
            ]
        ],
        [
            [
                0.925,
                0.005
            ],
            [
                0.920,
                0.012
            ],
            [
                0.919,
                0.014
            ],
            [
                0.919,
                0.008
            ],
            [
                0.917,
                0.005
            ],
            [
                0.909,
                0.011
            ],
            [
                0.899,
                0.008
            ],
            [
                0.887,
                0.006
            ],
            [
                0.887,
                0.011
            ],
            [
                0.886,
                0.015
            ],
            [
                0.885,
                0.014
            ],
            [
                0.875,
                0.019
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.DILI ", "%", "475", "Binary", "AUROC", "Scaffold"]
    ],
    "DrugComb_HSA": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "MLP", "Yusuf Roohani", "yroohani@stanford.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/multi_pred/drugcombo",
                "https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2509-3", "7,141,297", 4.453
            ],
        ],
        [
            [
                4.453,
                0.002
            ]
        ],
        ["Label", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.DrugComb_HSA", "297,098", "Regression", "MAE", "Combination"],
    ],
    "DrugComb_Loewe": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "MLP", "Yusuf Roohani", "yroohani@stanford.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/multi_pred/drugcombo",
                "https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2509-3", "7,141,297", 9.184
            ],
        ],
        [
            [
                9.184,
                0.001
            ],
        ],
        ["Label", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.DrugComb_Loewe", "297,098", "Regression", "MAE", "Combination"],
    ],
    "DrugComb_Bliss": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "MLP", "Yusuf Roohani", "yroohani@stanford","https://github.com/mims-harvard/TDC/tree/master/examples/multi_pred/drugcombo",
                "https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2509-3", "7,141,297", 4.560 
            ],
        ],
        [
            [
                4.560,
                0.000
            ],
        ],
        ["Label", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.DrugComb_Bliss", "297,098", "Regression", "MAE", "Combination"],
    ],
    "DrugComb_ZIP": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "MLP", "Yusuf Roohani", "yroohani@stanford","https://github.com/mims-harvard/TDC/tree/master/examples/multi_pred/drugcombo",
                "https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2509-3", "7,141,297", 4.027  
            ],
        ],
        [
            [
                4.027,
                0.003
            ],
        ],
        ["Label", "Size", "Task", "Metric", "Dataset Split"],
        ["tdc_ml.DrugComb_ZIP", "297,098", "Regression", "MAE", "Combination"],
        
    ],
    "BindingDB_Patent": [
        "new",
        ["Rank", "Model", "Contact", "Link", "PCC"],
        "desc",
        [
            [
                "IM-DTI", "Shasha Tao", " taoshasha@wust.edu.cn", "https://github.com/kuku-tss/IM-DTI-", 
                "https://github.com/kuku-tss/IM-dti/blob/master/Integrated%20Model%20for%20Drug%E2%80%93Target%20Interaction%20Prediction%20Using%20Multiple%20Protein%20Language%20Embeddings.pdf", 0.596
            ],
            [
                "Otter-Knowledge-Ensemble", "Hoang Thanh Lam", "t.l.hoang@ie.ibm.com", "https://github.com/IBM/otter-knowledge", 
                "https://arxiv.org/abs/2306.12802", 0.588
            ],
            [
                "OrangeBalls-ProtBertMorgan", "Samuel Sledzieski", "samsl@mit.edu", "https://github.com/samsledje/MLSB2021_PLM_DTI/blob/main/train_plm_dti-TDC-DG.py",
                "https://www.mlsb.io/papers_2021/MLSB2021_Adapting_protein_language_models.pdf", 0.538
            ],
            [
                "MMD", "Kexin", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.433
            ],
            [
                "CORAL", "Kexin", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.432
            ],
            [
                "ERM", "Kexin", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.427
            ],
            [
                "MTL", "Kexin", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.425
            ],
            [
                "GroupDRO", "Kexin", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.384
            ],
            [
                "AndMASK", "Kexin","kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.288
            ],
            [
                "IRM", "Kexin", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/multi_pred/dti_dg",
                "https://arxiv.org/abs/2007.01434", 0.284
            ],
        ],
        [
            [
                0.596,
                0.000
            ],
            [
                0.588,
                0.002
            ],
            [
                0.538,
                0.008
            ],
            [
                0.433,
                0.010
            ],
            [
                0.432,
                0.010
            ],
            [
                0.427,
                0.012
            ],
            [
                0.425,
                0.010
            ],
            [
                0.384,
                0.006
            ],
            [
                0.288,
                0.019
            ],
            [
                0.284,
                0.021
            ]
        ],
        [],
        [],
    ],
    "opentargets_dti_ra": [
        "new",
        ["Rank", "Model", "Contact", "Link", "APR@5 Top 20 CT"],
        "desc",
        [
            [
                "PINNACLE", "Alejandro Velez-Arce", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/mims-harvard/PINNACLE",
                "https://www.biorxiv.org/content/10.1101/2023.07.18.549602v2", 0.913
            ],
        ],
        [
            [
                0.913,
                0.059
            ],
        ],
        [],
        [],
    ],
    "opentargets_dti_ibd": [
        "new",
        ["Rank", "Model", "Contact", "Link", "APR@5 Top 20 CT"],
        "desc",
        [
            [
                "PINNACLE", "Michelle Li", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/mims-harvard/PINNACLE",
                "https://www.biorxiv.org/content/10.1101/2023.07.18.549602v2", 0.873
            ],
        ],
        [
            [
                0.873,
                0.069
            ],
        ],
        [],
        [],
    ],
    "brown_mdm2_ace2_12ca5": [
        "new",
        ["Rank", "Model", "Contact", "Link", "X"],
        "desc",
        [
            [
                "TO BE ANNOUNCED", "Alejandro Velez-Arce", "alejandro_velez-arce@hms.harvard.edu", "", "", 0
            ],
        ],
        [
            [
                "classified",
                "classified",
            ],
        ],
        [],
        [],
    ],
    "tchard_na": [
        "new",
        ["Rank", "Model", "Contact", "Link", "AUPRC"],
        "desc",
        [
            [
                "MIX-TPI", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/Wolverinerine/MIX-TPI",
                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10423027/", 0.995
            ],
            [
                "NET-TCR2", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/mnielLab/NetTCR-2.0",
                "https://www.nature.com/articles/s42003-021-02610-3", 0.985
            ],
            [
                "TEINet", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/jiangdada1221/TEINet",
                "https://www.biorxiv.org/content/10.1101/2022.10.20.513029v1", 0.981
            ],
            [
                "AVIB-TCR", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/nec-research/vibtcr",
                "https://pubmed.ncbi.nlm.nih.gov/36571499/", 0.949
            ],
            [
                "TITAN", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/PaccMann/TITAN",
                "https://pubmed.ncbi.nlm.nih.gov/34252922/", 0.661
            ],
            [
                "PanPep", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/bm2-lab/PanPep",
                "https://www.nature.com/articles/s42256-023-00619-3", 0.499
            ],
        ],
        [
            [
                0.995,
                0.001
            ],
            [
                0.985,
                0.005
            ],
            [
                0.981,
                0.006
            ],
            [
                0.949,
                0.023
            ],
            [
                0.661,
                0.040
            ],
            [
                0.499,
                0.031
            ],
        ],
        [],
        [],
    ],
    "tchard_rn": [
        "new",
        ["Rank", "Model", "Contact", "Link", "AUPRC"],
        "desc",
        [
            [
                "AVIB-TCR", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/nec-research/vibtcr",
                "https://pubmed.ncbi.nlm.nih.gov/36571499/", 0.605
            ],
            [
                "MIX-TPI", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/Wolverinerine/MIX-TPI",
                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10423027/", 0.597
            ],
            [
                "TEINet", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/jiangdada1221/TEINet",
                "https://www.biorxiv.org/content/10.1101/2022.10.20.513029v1", 0.581
            ],
            [
                "PanPep", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/bm2-lab/PanPep",
                "https://www.nature.com/articles/s42256-023-00619-3", 0.579
            ],
            [
                "NET-TCR2", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/mnielLab/NetTCR-2.0",
                "https://www.nature.com/articles/s42003-021-02610-3", 0.554
            ],
            [
                "TITAN", "Xiang Lin", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/PaccMann/TITAN",
                "https://pubmed.ncbi.nlm.nih.gov/34252922/", 0.523
            ],
        ],
        [
            [
                0.605,
                0.044
            ],
            [
                0.597,
                0.049
            ],
            [
                0.581,
                0.043
            ],
            [
                0.579,
                0.040
            ],
            [
                0.554,
                0.075
            ],
            [
                0.523,
                0.055
            ],
        ],
        [],
        [],
    ],
    "TOP": [
        "new",
        ["Rank", "Model", "Contact", "Link", "Indication Level AUPRC"],
        "desc",
        [
            [
                "HINT", "Tianfan Fu", "alejandro_velez-arce@hms.harvard.edu", "https://github.com/futianfan/clinical-trial-outcome-prediction",
                "https://www.sciencedirect.com/science/article/pii/S2666389922000186", 0.703
            ],
        ],
        [
            [
                0.703,
                "undefined",
            ],
        ],
        [],
        [],
    ],
}
