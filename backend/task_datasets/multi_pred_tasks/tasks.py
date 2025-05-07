_TASKS = [
    ["dti", "DTI", "Drug-Target Interaction"],
    ["ddi", "DDI", "Drug-Drug Interaction"],
    ["ppi", "PPI", "Protein-Protein Interaction"],
    ["gdi", "GDA", "Gene-Disease Association"],
    ["drugres", "DrugRes", "Drug Response Prediction"],
    ["drugsyn", "DrugSyn", "Drug Synergy Prediction"],
    ["peptidemhc", "PeptideMHC", "Peptide-MHC Binding"],
    ["antibodyaff", "AntibodyAFF", "Antibody-Antigen Affinity"],
    ["mti", "MTI", "miRNA-Target Interaction"],
    ["catalyst", "Catalyst", "Catalyst Prediction"],
    ["tcrepitope", "TCREpitopeBinding", "TCR-Epitope Binding"],
    ["trialoutcome", "TrialOutcome", "Clinical Trial Outcome Prediction"],
    ["proteinpeptide", "ProteinPeptide", "Protein-Peptide Interaction"],
    ["counterfactual", "PerturbOutcome", "Counterfactual Prediction"],
    ["scdti", "scDTI", "Single-cell Drug-Target Interaction"]
]

# a lot of non-template pages due to big differences from standard format. will only include templated pages here.
_DESC = {
    "gdi": [
        "gene-disease-association-prediction-task-overview",
        "Gene-Disease Association Prediction Task Overview",
        "Many diseases are driven by genes aberrations. Gene-disease associations (GDA) quantify the relation among a pair of gene\
            and disease. The GDA is usually constructed as a network where we can probe the gene-disease mechanisms by taking into\
                account multiple genes and diseases factors. This task is to predict the association of any gene and disease from\
                    both a biochemical modeling and network edge classification perspectives.",
        " A high association between a gene and disease could hint at a potential therapeutics target for the disease. Thus, to fill\
            in the vastly incomplete GDA using machine learning accurately could bring numerous therapeutic opportunities.",
        "Extrapolating to unseen gene and disease pairs with accurate association prediction.",
        "Any therapeutics.",
        "Basic biomedical research, target discovery."
    ],
    "drugsyn": [
        "drug-synergy-prediction-task-overview",
        "Drug Synergy Prediction Task Overview",
        "Synergy is a dimensionless measure of deviation of an observed drug combination response from the expected effect of\
            non-interaction. Synergy can be calculated using different models such as the Bliss model, Highest Single Agent (HSA),\
                Loewe additivity model and Zero Interaction Potency (ZIP). Another relevant metric is CSS which measures the drug\
                    combination sensitivity and is derived using relative IC50 values of compounds and the area under their dose-\
                        response curves.",
        "Drug combination therapy offers enormous potential for expanding the use of existing drugs and in improving their efficacy.\
            For instance, the simultaneous modulation of multiple targets can address the common mechanisms of drug resistance in\
                the treatment of cancers. However, experimentally exploring the entire space of possible drug combinations is not\
                    a feasible task. Computational models that can predict the therapeutic potential of drug combinations can thus\
                        be immensely valuable in guiding this exploration.",
        "It is important for model predictions to be able to adapt to varying underlying biology as captured through different cell\
            lines drawn from multiple tissues of origin. Dosage is also an important factor that can impact model generalizability.",
        " Small-molecule.",
        "Activity."
    ],
    "peptidemhc": [
        "peptide-mhc-binding-prediction-task-overview",
        "Peptide-MHC Binding Prediction Task Overview",
        " In the human body, T cells monitor the existing peptides and trigger an immune response if the peptide is foreign. To \
            decide whether or not if the peptide is not foreign, it must bound to a major histocompatibility complex (MHC) molecule.\
                Therefore, predicting peptide-MHC binding affinity is pivotal for determining immunogenicity. There are two classes\
                    of MHC molecules: MHC Class I and MHC Class II. They are closely related in overall structure but differ in their\
                        subunit composition. This task is to predict the binding affinity between the peptide and the pseudo \
                            sequence in contact with the peptide representing MHC molecules.",
        "Identifying the peptide that can bind to MHC can allow us to engineer peptides-based therapeutics such vaccines and \
            cancer-specific peptides. ",
        "The models are expected to be generalized to unseen peptide-MHC pairs.",
        "Immunotherapy.",
        "Activity - peptide design."
    ],
    "antibodyaff": [
        "antibody-antigen-affinity-prediction-task-overview",
        "Antibody-antigen Affinity Prediction Task Overview",
        "Antibodies recognize pathogen antigens and destroy them. The activity is measured by their binding affinities. This task\
            is to predict the affinity from the amino acid sequences of both antigen and antibodies. ",
        "Compared to small-molecule drugs, antibodies have numerous ideal properties such as minimal adverse effect and also can\
            bind to many \"undruggable\" targets due to different biochemical mechanisms. Besides, a reliable affinity predictor can\
                help accelerate the antibody development processes by reducing the amount of wet-lab experiments.",
        "The models are expected to extrapolate to unseen classes of antigen and antibody pairs.",
        "Antibody, immunotherapy.",
        "Activity"
    ],
    "trialoutcome": [
        "clinical-trial-outcome-prediction-task-overview",
        "Clinical Trial Outcome Prediction Task Overview",
        "Clinical trial outcome prediction is a machine learning task that aims to forecast the outcome of clinical trials, such\
            as the approval rate of a drug or treatment. It utilizes various clinical trial features, including the drug's molecular\
                structure, disease code representing the medical condition, and eligibility criteria that specify participant\
                    selection criteria. This task is formulated as a binary classification problem, where the machine learning \
                        model predicts whether a clinical trial will have a positive or negative outcome.",
        "Clinical trial is the most time and cost-consuming step in the drug discovery process. Optimizing and designing trials with\
            machine learning could drastically lead to the speedup of delivery of life-saving therapeutics to patients. Particularly,\
                they can effectively alert potential fallouts of trials to practitioners by pointing out potential risks,\
                    optimizing safety monitoring protocols and ensuring participant well-being. They can also assist in identifying\
                        suitable patient populations, optimizing sample sizes, refining inclusion and exclusion criteria, and\
                            selecting appropriate endpoints and outcome measures.",
        "Machine learning models for clinical trial outcome prediction are expected to demonstrate robust generalization to novel\
            drug molecular structures and rare diseases. This capability enhances the versatility and applicability of machine\
                learning in clinical research, supporting advancements in personalized medicine and treatment discovery. The ability\
                    to generalize well to diverse and evolving conditions is crucial for the models to be adaptable and effectively\
                        contribute to the field of clinical trials.",
        "All pipelines require clinical trials.",
        "Clinical trial."
    ],
    "counterfactual": [
        "counterfactual-prediction-task-overview",
        "Counterfactual Prediction Task Overview",
        "We define a task for predicting responses in gene expression of single cells to chemical and genetic perturbations,\
            aiming to measure model generalization across cell lines and perturbation types. Understanding cellular responses to\
                genetic perturbation is central to numerous biomedical applications, from identifying genetic interactions involved\
                    in cancer to developing methods for regenerative medicine. Furthermore, counterfactual prediction of drug-based\
                        perturbations at single-cell resolution enables cell-type specific drugs and treatments, facilitating\
                            precision medicine. The predictive, non-generative task is then formalized as a function of a cell, with\
                                corresponding attributes such as cell line, disease, and tissue, and a perturbation, such as a drug\
                                    type or a CRISPR-based perturbation, which outputs a count for gene expression of the cell after\
                                        the input perturbation.",
        "Machine learning has significantly advanced the ability to predict how single cells respond to various chemical and genetic\
            perturbations. This capability is crucial for understanding cellular behaviors and developing new therapeutic strategies.\
                Machine learning models have revolutionized the prediction of gene expression responses in single cells to chemical\
                    and genetic perturbations by enhancing predictive accuracy, handling dose dependencies, managing complex\
                        perturbations, and optimizing experimental designs. These advancements enable more efficient and accurate\
                            exploration of cellular responses, facilitating drug discovery and the development of personalized \
                                medicine.",
        "We measure model generalization across seen and unseen perturbations and across seen and unseen cell lines.",
        "Drug Repurposing, Predicting Adverse Drug Reactions, Biopharmaceuticals",
        " Target discovery, Phenotypic Screening."
    ],
    "scdti": [
        "single-cell-drug-target-nomination-identification-task-overview",
        "Single-cell Drug-Target Nomination (Identification) Task Overview",
        " PyTDC introduces tdc_ml.scDTI task. The goal is to train a model for predicting the probability that a protein is a candidate\
            therapeutic target in a specific cell type. The model learns an estimator for a function of a protein target and a \
                cell-type-specific biological context as input, and the model is tasked to predict the probability the candidate \
                    protein is a therapeutic target in that cell type.",
        "Single-cell data have enabled the study of gene expression and function at the level of individual cells across healthy\
            and disease states. To facilitate biological discoveries using single-cell data, machine-learning models have been \
                developed to capture the complex, cell-type-specific behavior of genes. In addition to providing the single-cell\
                    measurements and foundation models, PyTDC supports the development of contextual AI models to nominate \
                        therapeutic targets in a cell type-specific manner.",
        "Models are expected to have strong performance on cell-context-specific evaluation metrics across different sets of \
            disease-specific proteins and cells. ",
        "Small-molecule.",
        "Nomination / Identification."
    ]
    
}