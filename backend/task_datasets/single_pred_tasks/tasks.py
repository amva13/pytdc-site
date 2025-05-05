_TASKS = [
    ["adme", "ADME", "Pharmaco-kinetics"],
    ["tox", "Tox", "Toxicity"],
    ["hts", "HTS", "High-Throughput Screening"],
    ["qm", "QM", "Quantum Mechanics"],
    ["yields", "Yields", "Reaction Yields Prediction"],
    ["epitope", "Epitope", "Epitope Prediction"],
    ["develop", "Develop", "Developability Prediction"],
    ["CRISPROutcome", "CRISPROutcome", "CRISPR Repair Prediction"],
]

_DESC = {
    "tox": [
        "toxicity-prediction-task-overview",  # id
        "Toxicity Prediction Task Overview",  # title
        "Majority of the drugs have some extents of toxicity to the human organisms. This learning task aims to \
            predict accurately various types of toxicity of a drug molecule towards human organisms. ", # description
        "Toxicity is one of the primary causes of compound attrition. Study shows that approximately 70%% of all \
            toxicity-related attrition occurs preclinically (i.e., in cells, animals) while they are strongly predictive of \
                toxicities in humans. This suggests that an early but accurate prediction of toxicity can significantly reduce \
                    the compound attribution and boost the likelihood of being marketed. ",  # impact
        "Similar to the ADME prediction, as the drug structures of interest evolve over time, toxicity prediction requires a \
            model to generalize to a set of novel drugs with small structural similarity to the existing drug set.",  # generalization
        "Small-molecule.",  # product
        "Efficacy and safety - lead development and optimization.",  # pipeline
    ],
    "hts": [
        "high-throughput-screening-prediction-task-overview",
        "High-throughput Screening Prediction Task Overview",
        "High-throughput screening (HTS) is the rapid automated testing of thousands to millions of samples for biological \
            activity at the model organism, cellular, pathway, or molecular level. The assay readout can vary from target \
                binding affinity to fluorescence microscopy of cells treated with drug. HTS can be applied to different kinds \
                    of therapeutics however most available data is from testing of small-molecule libraries. In this task, a \
                        machine learning model is asked to predict the experimental assay values given a small-molecule compound \
                            structure.",
        "High throughput screening is a critical component of small-molecule drug discovery in both industrial and academic \
            research settings. Increasingly more complex assays are now being automated to gain biological insights on compound \
                activity at a large scale. However, there are still limitations on the time and cost for screening a large library \
                    that limit experimental throughput. Machine learning models that can predict experimental outcomes can alleviate \
                        these effects and save many times and costs by looking at a larger chemical space and narrowing down a \
                            small set of highly likely candidates for further smaller-scale HTS.",
        "The model should be able to generalize over structurally diverse drugs. It is also important for methods to generalize \
            across cell lines. Drug dosage and measurement time points are also very important factors in determining the efficacy \
                of the drug.",
        "Small-molecule.",
        "Activity - hit identification. "
    ],
    "qm": [
        "quantum-mechanics-modeling-task-overview",
        "Quantum Mechanics Modeling Task Overview",
        "The motion of molecules and protein targets can be described accurately with quantum theory, i.e., Quantum Mechanics (QM).\
            However, ab initio quantum calculation of many-body system suffers from large computational overhead that is \
                impractical for most applications. Various approximations have been applied to solve energy from electronic \
                    structure but all of them have a trade-off between accuracy and computational speed. Machine learning models \
                        raise a hope to break this bottleneck by leveraging the knowledge of existing chemical data. This task aims \
                            to predict the QM results given a drug's structural information.",
        "A well-trained model can describe the potential energy surface accurately and quickly, so that more accurate and longer \
            simulation of molecular systems are possible. The result of simulation can reveal the biological processes in molecular \
                level and help study the function of protein targets and drug molecules.",
        "A machine learning model trained on a set of QM calculations require to extrapolate to unseen or structurally diverse set \
            of compounds.",
        "Small-molecule. ",
        "Activity - lead development."
    ],
    "yields": [
        "reaction-yields-prediction-task-overview",
        "Reaction Yields Prediction Task Overview",
        "Vast majority of small-molecule drugs are synthesized through chemical reactions. Many factors during reactions could \
            lead to suboptimal reactants-products conversion rate, i.e. yields. Formally, it is defined as the percentage of the \
                reactants successfully converted to the target product. This learning task aims to predict the yield of a given \
                    single chemical reaction.",
        "To maximize the synthesis efficiency of interested products, an accurate prediction of the reaction yield could help \
            chemists to plan ahead and switch to alternate reaction routes, by which avoiding investing hours and materials in \
                wet-lab experiments and reducing the number of attempts.",
        " The models are expected to extrapolate to unseen reactions with diverse chemical structures and reaction types. ",
        "Small-molecule. ",
        "Manufacturing - Synthesis planning."
    ],
    "epitope": [
        "epitope-prediction-task-overview",
        "Epitope Prediction Task Overview",
        "An epitope, also known as antigenic determinant, is the region of a pathogen that can be recognized by antibody and cause \
            adaptive immune response. This task is to classify the active and non-active sites from the antigen protein sequences.",
        "Identifying the potential epitope is of primary importance in many clinical and biotechnologies, such as vaccine design \
            and antibody development, and for our general understanding of the immune system.",
        "The models are expected to be generalized to unseen pathogens antigens amino acid sequences with diverse set of structures\
            and functions.",
        "Immunotherapy.",
        "Target discovery. "
    ],
    "develop": [
        "antibody-developibility-prediction-task-overview",
        "Antibody Developability Prediction Task Overview",
        " Immunogenicity, instability, self-association, high viscosity, polyspecificity, or poor expression can all preclude \
            an antibody from becoming a therapeutic. Early identification of these negative characteristics is essential. This task \
                is to predict the developability from the amino acid sequences.",
        " A fast and reliable developability predictor can accelerate the antibody development by reducing wet-lab experiments. They\
            can also alert the chemists to foresee potential efficacy and safety concerns and provide signals for modifications.\
                Previous works have devised accurate developability index based on 3D structures of antibody. However, 3D information\
                    are expensive to acquire. A machine learning that can calculate developability based on sequence information is \
                        thus highly ideal. ",
        "The model is expected to be generalized to unseen classes of antibodies with various structural and functional \
            characteristics.",
        "Antibody. ",
        "Efficacy and safety."
    ],
    "CRISPROutcome": [
        "crispr-repair-outcome-prediction-task-overview",
        "CRISPR Repair Outcome Prediction Task Overview",
        "CRISPR-Cas9 is a gene editing technology that allows targeted deletion or modification of specific regions of the DNA\
            within an organism. This is achieved through designing a guide RNA sequence that binds upstream of the target site \
                which is then cleaved through a Cas9-mediated double stranded DNA break. The cell responds by employing DNA repair \
                    mechanisms (such as non-homologous end joining) that result in heterogeneous outcomes including gene insertion\
                        or deletion mutations (indels) of varying lengths and frequencies. This task aims to predict the repair \
                            outcome given a DNA sequence.",
        "Gene editing offers a powerful new avenue of research for tackling intractable illnesses that are infeasible to treat using\
            conventional approaches. For example, the FDA recently approved engineering of T-cells using gene editing to treat \
                patients with acute lymphoblastic leukemia. However, since many human genetic variants associated with disease \
                    arise from insertions and deletions, it is critical to be able to better predict gene editing outcomes to ensure\
                        efficacy and avoid unwanted pathogenic mutations.",
        "The distribution of Cas9-mediated editing products at a given target site is reproducible and dependent on local sequence \
            context. Thus, it is expected that repair outcomes predicted using well-trained models should be able to generalize \
                across cell lines and reagent delivery methods.",
        "Cell and gene therapy.",
        "Efficacy and safety."
    ]
    
}