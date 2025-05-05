import {

    HomeDemo1TokenIcon1,

    HomeDemo1TeamImg1,
    // HomeDemo1TeamImg2,
    // HomeDemo1TeamImg3,
    // HomeDemo1TeamImg4,
    
    HomeDemo1Partners1,
    HomeDemo1Partners2,
    // HomeDemo1Partners3,
    // HomeDemo1Partners4,
    // HomeDemo1Partners5,
    // HomeDemo1Partners6,
    // HomeDemo1Partners7,
    // HomeDemo1Partners8,
    // HomeDemo1Partners9,
    // HomeDemo1Partners10,
    // HomeDemo1Partners11,
    // HomeDemo1Partners12,

    HomeDemo1BlogImg1,
    HomeDemo1BlogImg2,
    HomeDemo1BlogImg3

} from '../../utils/allImgs'

export const VerticalSocial = [
    {nameIco:'fa-brands fa-x-twitter', link:'https://x.com/ProjectTDC'},
    {nameIco:'fa-brands fa-github', link:'https://github.com/mims-harvard/TDC'},
    {nameIco:'fa-brands fa-discord', link:'https://discord.gg/6zdHZ3tT'},
    {nameIco:'fa-brands fa-slack', link:'https://join.slack.com/t/pytdc/shared_invite/zt-x0ujg5v6-zwtQZt83fhRdgrYjXRFz5g'},
    {nameIco:'fa-brands fa-youtube', link:'https://www.youtube.com/watch?v=ZuCOhEZtaOw&pp=ygUfeml0bmlrIHRoZXJhcGV1dGljIGRhdGEgY29tbW9ucw%3D%3D'},
    {nameIco:'fa-solid fa-face-smile', link:'https://huggingface.co/tdc'},
    {nameIco:'fa-solid fa-file-pdf', link:'https://zitniklab.hms.harvard.edu/publications/papers/TDC-neurips21-main.pdf'} 
]

export const SingleCoolFact = [
    {
        img:HomeDemo1BlogImg1,
        link:'https://www.events.westernu.ca/events/schulich-medicine-dentistry/2024-11/western-bioinformatics-nov14.html',
        title:'Western Bioinformatics Conference'
    },
    {
        img:HomeDemo1BlogImg1,
        link:'https://western-bioinfo.github.io/seminars/alejandro-velez-arce',
        title:'Medical Bioinformatics@Western'
    },
]

export const service_single_content = [
    {
        title:'TDC.scDTI',
        content: 'Single-cell drug-target nomination (identification). The goal is to train a model for predicting the probability that a protein is a candidate therapeutic target in a specific cell type.',
        link:'https://tdcommons.ai/multi_pred_tasks/scdti'
    },
    {
        title:'TDC.PerturbOutcome',
        content:'We define a task for predicting responses in gene expression of single cells to chemical and genetic perturbations, aiming to measure model generalization across cell lines and perturbation types.',
        link:'https://tdcommons.ai/multi_pred_tasks/counterfactual'
    },
    {
        title:'TDC.ProteinPeptide',
        content:"Capturing the dynamic nature of protein-peptide interactions requires advanced sampling techniques and computational resources, making the prediction of binding affinities more complex (Antes et al., 2014). We provide benchmarks integrating newly discovered peptides to test ML models on their ability to generalize to cutting-edge peptidomimetics.",
        link:'https://tdcommons.ai/multi_pred_tasks/proteinpeptide'
    },
    {
        title:'TDC.TCREpitope',
        content:" T-cells are an integral part of the adaptive immune system, whose survival, proliferation, activation and function are all governed by the interaction of their T-cell receptor (TCR) with immunogenic peptides (epitopes). This new task aims to predict the binding affinity given a pair of TCR sequence and epitope sequence. The models are, at very least, expected to generalize to unseen TCRs. But the main challenge of this dataset is to generalize to samples where both epitope and TCR are unseen.",
        link: 'https://tdcommons.ai/multi_pred_tasks/tcrepitope'
    },
    {
        title: "TDC.TrialOutcome",
        content: "Clinical trial outcome prediction is a machine learning task that aims to forecast the outcome of clinical trials, such as the approval rate of a drug or treatment. It utilizes various clinical trial features, including the drug's molecular structure, disease code representing the medical condition, and eligibility criteria that specify participant selection criteria. Machine learning models for clinical trial outcome prediction are expected to demonstrate robust generalization to novel drug molecular structures and rare diseases. The ability to generalize well to diverse and evolving conditions is crucial for the models to be adaptable and effectively contribute to the field of clinical trials.",
        link: 'https://tdcommons.ai/multi_pred_tasks/trialoutcome'
    },
    {
        title:'TDC.SBDD',
        content:'Structure-based Drug Design is to generate diverse, novel molecules that have high binding affinity to protein pockets (3D structures) and desirable chemical properties. These properties are measured by oracle functions. A machine learning task first learns the molecular characteristics given specific protein pockets from a large set of protein-ligand pair data. Then, from the learned conditional distribution, we can sample novel candidates.',
        link:'https://tdcommons.ai/multi_pred_tasks/sbdd'
    }

]

export const timelineInfo = [
    {
        timelineClass:"block block-right mt-30",
        title:'TDC.TCREpitope Introduced',
        date_from:'Feb 19th, 2022',
        date_to:'June 19th, 2024',
        content:'TDC has a new task on TCR-Epitope Binding prediction (Thanks to Anna and Jannis)! We enhanced the task by consolidating TCHard and PanPep datasets and further ran benchmarks for numerous SoTA models in our publications.'
    },
    {
        timelineClass:"block block-left",
        title:'Introduction of TDC-2 Resource model and TDC.PrimeKG',
        date_from:'July 27,2022',
        date_to:'Sep 24th, 2024',
        content:'Piloted by the introduction of the PrimeKG API to TDC, the TDC Resource module became the data model for the later introduction of TDC\'s API-first architecture. Enhancements have been implemented for the PrimeKG API since.'
    },
    {
        timelineClass:"block block-right mt-30",
        title:'TDC.SBDD introduced',
        date_from:'November 3rd, 2022',
        date_to:'June 19th, 2024',
        content:'TDC has a new task on structure-based drug design SBDD with four datasets PDBBind, DUD-E, scPDB. To support evaluation of SBDD tasks, we also include two evaluation metrics (RMSD, Kabsch-RMSD) that compare distances between two structures.'
    },
    {
        timelineClass:"block block-left mt-30",
        title:'TDC Huggingface Model Hub released using DeepPurpose framework',
        date_from:'April 17th, 2023',
        date_to:'June 19th, 2024',
        content:'We\'re excited to announce the release of a new interface tdc_hf_interface that allows users to easily access and leverage pre-trained models hosted at HuggingFace on TDC datasets and tasks. In this first batch, we\'ve released nine pre-trained models from DeepPurpose that cover three popular ADMET datasets in the Commons.'
    },
    {
        timelineClass:"block block-right mt-30",
        title:'TDC.TrialOutcome introduced',
        date_from:'July 10th, 2023',
        date_to:'June 19th 2024',
        content:'TDC has a new exciting task on clinical trial outcome prediction (Thanks to Tianfan)! The release features the TOP dataset. TOP consists of 17,538 clinical trials with 13,880 small-molecule drugs and 5,335 diseases.'
    },
    {
        timelineClass:"block block-left mt-30",
        title:'TDC.ProteinPeptide and API-first architecture introduced',
        date_from:'March 22nd, 2024',
        date_to:'June 19th 2024',
        content:'TDC introduced the new protein-peptide binding affinity task along with the Ye X et al. dataset (thanks to Joseph Brown!). Affinity selection-mass spectrometry data of discovered ligands against single biomolecular targets (MDM2, ACE2, 12ca5) from the Pentelute Lab of MIT This dataset contains affinity selection-mass spectrometry data of discovered ligands against single biomolecular targets. Furthermore, the architecture of TDC was redesigned using the model-view-controller design pattern to enable multimodal dataviews, with this dataset serving as the pilot API-first dataset.'
    },
    {
        timelineClass:"block block-right mt-30",
        title:'TDC.PerturbOutcome introduced',
        date_from:'April 5th, 2024',
        date_to:'June 19th 2024',
        content:'TDC introduced the new single-cell genetic and chemical perturbation response prediction tasks along with the scPerturb datasets.'
    },
    {
        timelineClass:"block block-left mt-30",
        title:'TDC-2 Multimodal Single-cell Retrieval API introduced',
        date_from:'April 18th, 2024',
        date_to:'June 19th 2024',
        content:'TDC-2 introduces over 1,000 multimodal datasets, spanning approximately 85 million cells and pre-calculated foundation model embeddings from 5 state-of-the-art single-cell models via CZ CELLxGENE Census. The resource is integrated into the TDC API-first dataset model to enable retrieval of multimodal dataviews for diverse single-cell therapeutic AI tasks.'
    },
    {
        timelineClass:"block block-right mt-30",
        title:'TDC.scDTI introduced',
        date_from:'April 26th, 2024',
        date_to:'June 19th 2024',
        content:'TDC-2 introduced the first-of-its-kind single-cell drug target nomination task. The release features a high-quality curated dataset from OpenTargets (thanks Michelle Li!).'
    },
    {
        timelineClass:"block block-left mt-30",
        title:'Alpha release of TDC-2, along with single-cell therapeutics AI benchmarks, is presented to MoML2024 at Mila',
        date_from:'June 19th, 2024',
        date_to:'June 22nd 2024',
        content:'TDC-2 was released along with its pre-print in biorxiv and spotlight accepted to the Molecular Machine Learning Conference at Mila. Our poster featured single-cell therapeutics AI tasks and benchmarks, the API-first dataset, and the multimodal single-cell retrieval API.'
    },
    {
        timelineClass:"block block-right mt-30",
        title:'TDC-2 Model Server is alpha released',
        date_from:'October 19th, 2024',
        date_to:'November 11th 2024',
        content:'TDC-2 released the alpha version of the Model Server, open source inference serving software that streamlines AI inferencing for single-cell foundation models across modalities, piloted by an inference pipeline for Geneformer. It is a first-of-its-kind release.'
    },
    {
        timelineClass:"block block-left mt-30",
        title:'TDC-2 is published and presented at NeurIPS and other venues',
        date_from:'November 14th, 2024',
        date_to:'December 15th 2024',
        content:'The TDC-2 manuscript, "Signals in the Cells: Multimodal and Contextualized Machine Learning Foundations for Therapeutics.", was spotlight at NeurIPS AIDrugX 2024. TDC-2 was presented at the Western Bioinformatics Seminar Series and a new poster was presented at AIDrugX. The new poster introduced the TDC-2 model server for the first time.'
    },
    {
        timelineClass:"block block-right mt-30",
        title:'TDC-2 beta release',
        date_from:'TBD',
        date_to:'TBD',
        content:'COMING SOON'
    },
]

export const ServiceBlock = [
    {
        classIco:"icon ti-mobile",
        title:"Powerfull Mobile and Online App"
    },
    {
        classIco:"icon ti-widget",
        title:"Brings more Transparency and Speed"
    },
    {
        classIco:"icon ti-settings",
        title:"Special for Multiple Use Capabilities"
    },
]

export const SocialListIco = [
    {icoName:"fa fa-facebook-square"},
    {icoName:"fa fa-twitter-square"},
    {icoName:"fa fa-github-square"},
    {icoName:"fa fa-instagram"},
    {icoName:"fa fa-medium"}
]

export const FQAInfo = [
    {
        text:'What are the objectives of this token?',
        ID:'Q1'
    },
    {
        text:'What is Token Sale and pre-sale?',
        ID:'Q2'
    },
    {
        text:'What is the pre-sale start date?',
        ID:'Q3'
    },
    {
        text:'how may I take part in pre-sale?',
        ID:'Q4'
    },
]

export const DocElementTitle = [
    {
        title:'NeurIPS\'24 AIDrugX Spotlight Paper',
        link:'https://openreview.net/pdf?id=kL8dlYp6IM'
    },
    {
        title:'NeurIPS\'24 AIDrugX Poster',
        link:'https://drive.google.com/file/d/1plypydZCaegbgxyCl-xehFxSgwX6e8So/view?usp=sharing'
    },
    {
        title:'Western Bioinformatics Seminar Slides',
        link:'https://drive.google.com/file/d/197Zay3tu0F-MJw_orf0QRWyyhkwN6lqC/view?usp=sharing'
    },
    {
        title:'MoML\'24 Conference @ Mila Poster',
        link:'https://drive.google.com/file/d/1LYdITeFY5iX07zyXPGVEjMpYjuHMrneS/view?usp=sharing'
    },
    {
        title:'Nature Chemical Biology 2022',
        link:'https://www.nature.com/articles/s41589-022-01131-2'
    },
    {
        title:'NeurIPS 2021',
        link:'https://openreview.net/pdf?id=8nvgnORnoWr'
    }
]

export const TokenText = [
    {
        text:'Lorem ipsum dolor sit amet, conse ctetur elit',
        img:HomeDemo1TokenIcon1
    },
    {
        text:'Sed quis accumsan nisi Ut ut felis',
        img:HomeDemo1TokenIcon1
    },
    {
        text:'felis congue nisl hendrerit commodo',
        img:HomeDemo1TokenIcon1
    },
    {
        text:'arch nemo sequi rem saepe ad quasi ullam.',
        img:HomeDemo1TokenIcon1
    },
]

export const MissionData = [
    {
        icoName:"ti-shine",
        title:"Quality"
    },
    {
        icoName:"ti-ruler-pencil",
        title:"Creativity"
    },
    {
        icoName:"ti-heart",
        title:"Reliability"
    },
]

export const TeamMember = [
    {
        img:HomeDemo1TeamImg1,
        title:'Alex V',
        text:'Founder, CEO'
    },
    // {
    //     img:HomeDemo1TeamImg2,
    //     title:'Ajoy Das',
    //     text:'Business Development'
    // },
    // {
    //     img:HomeDemo1TeamImg3,
    //     title:'Afroza Mou',
    //     text:'UX/UI Designer'
    // },
    // {
    //     img:HomeDemo1TeamImg4,
    //     title:'Lim Sarah',
    //     text:'Head of Marketing'
    // },
    // {
    //     img:HomeDemo1TeamImg1,
    //     title:'Sunny khan',
    //     text:'Executive Officer'
    // },
    // {
    //     img:HomeDemo1TeamImg2,
    //     title:'Ajoy Das',
    //     text:'Business Development'
    // },
    // {
    //     img:HomeDemo1TeamImg3,
    //     title:'Afroza Mou',
    //     text:'UX/UI Designer'
    // },
    // {
    //     img:HomeDemo1TeamImg4,
    //     title:'Lim Sarah',
    //     text:'Head of Marketing'
    // },
]

export const PartnersData = [
    {img:HomeDemo1Partners1, link:"https://aplusventures.io/"},
    {img:HomeDemo1Partners2, link:"https://discord.gg/ZJ67MtXag4"},
    // {img:HomeDemo1Partners3},
    // {img:HomeDemo1Partners4},
    // {img:HomeDemo1Partners5},
    // {img:HomeDemo1Partners6},
    // {img:HomeDemo1Partners7},
    // {img:HomeDemo1Partners8},
    // {img:HomeDemo1Partners9},
    // {img:HomeDemo1Partners10},
    // {img:HomeDemo1Partners11},
    // {img:HomeDemo1Partners12}
]

export const BlogPost = [
    {img:HomeDemo1BlogImg1},
    {img:HomeDemo1BlogImg2},
    {img:HomeDemo1BlogImg3}
]
