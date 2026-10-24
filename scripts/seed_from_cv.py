#!/usr/bin/env python3
"""Write the CV-backed YAML data files. Run only to regenerate those files."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "data"


def bibtex(kind, key, fields):
    lines = [f"@{kind}{{{key},"]
    for name, value in fields.items():
        if value:
            lines.append(f"  {name} = {{{value}}},")
    lines.append("}")
    return "\n".join(lines)


def publication(
    pid,
    title,
    authors,
    year,
    venue,
    kind,
    topics,
    featured=False,
    doi="",
    url="",
    detail="",
    bibtype="article",
    bib_extra=None,
):
    bare_doi = doi.removeprefix("https://doi.org/")
    fields = {
        "title": title,
        "author": authors,
        "year": str(year),
        "journal" if bibtype == "article" else "booktitle": venue,
    }
    if bibtype == "misc":
        fields = {
            "title": title,
            "author": authors,
            "year": str(year),
            "howpublished": venue,
        }
    if bibtype == "incollection":
        fields = {
            "title": title,
            "author": authors,
            "year": str(year),
            "booktitle": venue,
        }
    if bare_doi:
        fields["doi"] = bare_doi
    if url:
        fields["url"] = url
    if bib_extra:
        fields.update(bib_extra)
    return {
        "id": pid,
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue,
        "detail": detail,
        "type": kind,
        "topics": topics,
        "doi": doi,
        "url": url,
        "pdf": "",
        "code": "",
        "dataset": "",
        "featured": featured,
        "open_access": False,
        "bibtex": bibtex(bibtype, pid, fields),
    }


MA = ["materials-ai"]
XA = ["explainable-ai"]
SR = ["structural-resilience"]
SM = ["scientific-ml"]

publications = [
    publication(
        "zaki2026llamat",
        "LLaMat: A family of large language models for materials research with insights into model adaptability in continued pre-training",
        "Zaki M, Ahlawat D, Mishra V, Singh S, Bihani V, Grover H, Mishra B, Miret S, Mausam M, Krishnan NMA",
        2026,
        "Nature Machine Intelligence",
        "journal",
        MA,
        featured=True,
        detail="2026 Feb 27; 1–14",
    ),
    publication(
        "mandal2025afm-agents",
        "Evaluating large language model agents for automation of atomic force microscopy",
        "Mandal I, Soni J, Zaki M, Smedskjaer MM, Wondraczek K, Wondraczek L, Gosvami NN, Krishnan NMA",
        2025,
        "Nature Communications",
        "journal",
        MA,
        detail="2025 Oct 14; 16(1): 9104",
    ),
    publication(
        "hira2025matskraft",
        "MatSKRAFT: A framework for large-scale materials knowledge extraction from scientific tables",
        "Hira K, Zaki M, Krishnan NMA, Mausam M",
        2025,
        "arXiv preprint arXiv:2509.10448",
        "preprint",
        MA,
        url="https://arxiv.org/abs/2509.10448",
        detail="2025 Sep 12",
        bibtype="misc",
    ),
    publication(
        "zaki2025cement-chapter",
        "Artificial intelligence for information extraction from cement literature",
        "Zaki M, Bharadwaj K, Goyal R, Jayadeva J, Krishnan NMA",
        2025,
        "Binding Materials for Sustainable Construction, Woodhead Publishing",
        "chapter",
        MA,
        detail="pp. 819–832",
        bibtype="incollection",
    ),
    publication(
        "mishra2024llamat-workshop",
        "LLaMaT: Large Language Model for Materials Science",
        "Mishra V, Singh S, Zaki M, Grover HS, Miret S, Mausam, Krishnan NMA",
        2024,
        "AI4MAT Workshop, BOKU Vienna",
        "conference",
        MA,
        detail="Accepted, July 2024",
        bibtype="inproceedings",
    ),
    publication(
        "zaki2024mascqa",
        "MaScQA: Investigating Materials Science Knowledge of Large Language Models",
        "Zaki M, Jayadeva J, Mausam M, Anoop Krishnan NM",
        2024,
        "Digital Discovery",
        "journal",
        MA,
        featured=True,
        doi="https://doi.org/10.1039/D3DD00188A",
    ),
    publication(
        "zaki2023glassomics",
        "Glassomics: An omics approach toward understanding glasses through modeling, simulations, and artificial intelligence",
        "Zaki M, Jan A, Krishnan NMA, Mauro JC",
        2023,
        "MRS Bulletin",
        "journal",
        MA,
        featured=True,
        doi="https://doi.org/10.1557/s43577-023-00560-1",
    ),
    publication(
        "hira2024tetrahedron",
        "Reconstructing materials tetrahedron: Challenges in materials information extraction",
        "Hira K, Zaki M, Sheth D, Krishnan N, others",
        2024,
        "Digital Discovery, special issue on AI4MAT NeurIPS-2023",
        "journal",
        MA,
        detail="Accepted, 2024",
    ),
    publication(
        "mannan2023hardness",
        "Glass hardness: Predicting composition and load effects via symbolic reasoning-informed machine learning",
        "Mannan S, Zaki M, Bishnoi S, et al.",
        2023,
        "Acta Materialia",
        "journal",
        XA,
        doi="https://doi.org/10.1016/j.actamat.2023.119046",
        detail="255: 119046",
    ),
    publication(
        "zaki2023cementron",
        "Cementron: Machine learning the alite and belite phases in cement clinker from optical images",
        "Zaki M, Sharma S, Gurjar SK, Goyal R, Krishnan NA, others",
        2023,
        "Construction and Building Materials",
        "journal",
        MA + SR,
        featured=True,
        detail="397: 132425",
    ),
    publication(
        "gupta2023discomat",
        "DiSCoMaT: Distantly supervised composition extraction from tables in materials science articles",
        "Gupta T, Zaki M, Khatsuriya D, Hira K, Krishnan NMA, Mausam M",
        2023,
        "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
        "conference",
        MA,
        featured=True,
        doi="https://doi.org/10.18653/v1/2023.acl-long.753",
        detail="pp. 13465–13483, Toronto, Canada",
        bibtype="inproceedings",
    ),
    publication(
        "singla2023chalcogenide",
        "Accelerated design of chalcogenide glasses through interpretable machine learning for composition–property relationships",
        "Singla S, Mannan S, Zaki M, Krishnan NA",
        2023,
        "Journal of Physics: Materials",
        "journal",
        XA,
        detail="6(2): 024003",
    ),
    publication(
        "zaki2022afm-tip",
        "Interpretable Machine Learning Approach for Identifying the Tip Sharpness in Atomic Force Microscopy",
        "Zaki M, Kasimuthumaniyan S, Sahoo S, Jayadeva, Gosvami NN, Krishnan NMA",
        2022,
        "Scripta Materialia",
        "journal",
        XA,
        featured=True,
        doi="https://doi.org/10.1016/j.scriptamat.2022.114965",
        detail="221: 114965",
    ),
    publication(
        "bhattoo2023composition",
        "Understanding the compositional control on electrical, mechanical, optical, and physical properties of inorganic glasses with interpretable machine learning",
        "Bhattoo R, Bishnoi S, Zaki M, Krishnan NMA",
        2023,
        "Acta Materialia",
        "journal",
        XA,
        doi="https://doi.org/10.1016/j.actamat.2022.118439",
        detail="242: 118439",
    ),
    publication(
        "zaki2022structure-factor",
        "Natural language processing-guided meta-analysis and structure factor database extraction from glass literature",
        "Zaki M, Namireddy SR, Pittie T, et al.",
        2022,
        "Journal of Non-Crystalline Solids: X",
        "journal",
        MA,
        doi="https://doi.org/10.1016/j.nocx.2022.100103",
        detail="15: 100103",
    ),
    publication(
        "gupta2022matscibert",
        "MatSciBERT: A materials domain language model for text mining and information extraction",
        "Gupta T, Zaki M, Krishnan NMA, Mausam M",
        2022,
        "npj Computational Materials",
        "journal",
        MA,
        featured=True,
        doi="https://doi.org/10.1038/s41524-022-00784-w",
        detail="8(1): 102",
    ),
    publication(
        "zaki2022optical",
        "Interpreting the optical properties of oxide glasses with machine learning and Shapely additive explanations",
        "Zaki M, Venugopal V, Bhattoo R, et al.",
        2022,
        "Journal of the American Ceramic Society",
        "journal",
        XA,
        featured=True,
        detail="105(6): 4046–4057",
    ),
    publication(
        "lyngdoh2020csh",
        "Elucidating the constitutive relationship of calcium–silicate–hydrate gel using high throughput reactive molecular simulations and machine learning",
        "Lyngdoh GA, Li H, Zaki M, Krishnan NMA, Das S",
        2020,
        "Scientific Reports",
        "journal",
        SR + SM,
        doi="https://doi.org/10.1038/s41598-020-78368-1",
        detail="10(1): 21336",
    ),
    publication(
        "ravinder2021challenges",
        "Artificial intelligence and machine learning in glass science and technology: 21 challenges for the 21st century",
        "Ravinder, Venugopal V, Bishnoi S, … Zaki M, … et al.",
        2021,
        "International Journal of Applied Glass Science",
        "journal",
        MA,
        doi="https://doi.org/10.1111/ijag.15881",
        detail="12(3): 277–292",
    ),
    publication(
        "venugopal2021looking",
        "Looking through glass: Knowledge discovery from materials science literature using natural language processing",
        "Venugopal V, Sahoo S, Zaki M, Agarwal M, Gosvami NN, Krishnan NMA",
        2021,
        "Patterns",
        "journal",
        MA,
        featured=True,
        doi="https://doi.org/10.1016/j.patter.2021.100290",
        detail="2(7): 100290",
    ),
    publication(
        "sharma2021cost",
        "Machine learning-aided cost prediction and optimization in construction operations",
        "Sharma V, Zaki M, Jha KN, Krishnan NMA",
        2021,
        "Engineering, Construction and Architectural Management",
        "journal",
        SR,
        doi="https://doi.org/10.1108/ECAM-10-2020-0778",
    ),
    publication(
        "zaki2022processing",
        "Extracting processing and testing parameters from materials science literature for improved property prediction of glasses",
        "Zaki M, Jayadeva, Krishnan NMA",
        2022,
        "Chemical Engineering and Processing - Process Intensification",
        "journal",
        MA + XA,
        doi="https://doi.org/10.1016/j.cep.2021.108607",
        detail="180: 108607",
    ),
    publication(
        "lyngdoh2022concrete",
        "Prediction of concrete strengths enabled by missing data imputation and interpretable machine learning",
        "Lyngdoh GA, Zaki M, Krishnan NMA, Das S",
        2022,
        "Cement and Concrete Composites",
        "journal",
        XA + SR,
        doi="https://doi.org/10.1016/j.cemconcomp.2022.104414",
        detail="128: 104414",
    ),
]

awards = [
    {"year": "2026", "title": "USACM Travel and Registration grant for WCCM-ECCOMAS 2026"},
    {"year": "2026", "title": "AI4MAT-ICLR 2026 Travel Grant"},
    {
        "year": "2024",
        "title": "Best poster award in AI for materials science at the inaugural Hopkins Extreme Materials Institute conference",
    },
    {"year": "2024", "title": "3-Minute Thesis presentation award, Open House, IIT Delhi"},
    {
        "year": "2024",
        "title": "Travel, registration, and accommodation grant, 5th Indian Symposium on Machine Learning, BITS Pilani, Goa",
    },
    {
        "year": "2023",
        "title": "Travel, registration, and accommodation grant, 4th Indian Symposium on Machine Learning, IIT Bombay, Mumbai",
    },
    {
        "year": "2023",
        "title": "Travel grant from the Industrial Research and Development Unit, IIT Delhi, for presenting at the 2023 MRS Fall Conference, Boston, USA",
    },
    {"year": "2023", "title": "ACL D&I grant for attending the 61st ACL Conference, Toronto, Canada"},
    {
        "year": "2023",
        "title": "SERB International Travel Support Grant for presenting at the 2023 MRS Spring Conference, San Francisco, USA",
    },
    {"year": "2020–2024", "title": "Prime Minister’s Research Fellowship (PMRF)"},
    {
        "year": "2013–2017",
        "title": "Meritorious student scholarship award, Department of Civil Engineering, Motilal Nehru National Institute of Technology Allahabad",
    },
    {"year": "2015", "title": "Summer Research Internship, Indian Institute of Technology Mandi"},
    {"year": "2011", "title": "DST INSPIRE Internship"},
]

teaching = [
    {
        "id": "cvp441",
        "code": "CVP441",
        "title": "Structural Design and Detailing",
        "institution": "Indian Institute of Technology Delhi",
        "years": "2020–2023",
        "role": "Teaching",
        "audience": "100 students, undergraduate",
        "description": "Designing structures in STAAD Pro and drawing in AutoCAD.",
        "resources": [],
    },
    {
        "id": "cvl757",
        "code": "CVL757",
        "title": "Finite Element Methods in Structural Engineering",
        "institution": "Indian Institute of Technology Delhi",
        "years": "2021–2022",
        "role": "Teaching",
        "audience": "30 students, undergraduate, master’s, and PhD",
        "description": "Introduced Python programming assignments for finite element analysis.",
        "resources": [],
    },
    {
        "id": "mll703",
        "code": "MLL703",
        "title": "Mathematical and Computational Methods in Materials",
        "institution": "Indian Institute of Technology Delhi",
        "years": "2020–2021",
        "role": "Teaching",
        "audience": "30 students, master’s and PhD",
        "description": "Numerical differentiation and integration, with MATLAB and Python programming assignments.",
        "resources": [],
    },
    {
        "id": "ell409",
        "code": "ELL409 and ELL784",
        "title": "Introduction to Machine Learning",
        "institution": "Indian Institute of Technology Delhi",
        "years": "2020–2021",
        "role": "Teaching",
        "audience": "60 students, undergraduate (ELL409) and postgraduate (ELL784)",
        "description": "Logistic support and a hands-on session on the high performance computing cluster at IIT Delhi.",
        "resources": [],
    },
]


def talk(title, fmt=""):
    return {"title": title, "format": fmt}


conferences = [
    {
        "id": "wccm-2026",
        "order": 1,
        "year": 2026,
        "name": "17th World Congress on Computational Mechanics and 10th European Congress on Computational Methods in Applied Sciences and Engineering",
        "location": "Munich, Germany",
        "dates": "July 19–24, 2026",
        "talks": [talk("Uncertainty Quantification of Foundation Models for Scientific Machine Learning")],
    },
    {
        "id": "ai4mat-iclr-2026",
        "order": 2,
        "year": 2026,
        "name": "AI4MAT workshop at ICLR 2026",
        "location": "Rio de Janeiro, Brazil",
        "dates": "April 26, 2026",
        "talks": [talk("Materials Research Agent")],
    },
    {
        "id": "siam-uq-2026",
        "order": 3,
        "year": 2026,
        "name": "SIAM Conference on Uncertainty Quantification",
        "location": "Minneapolis, Minnesota",
        "dates": "March 22–25, 2026",
        "talks": [talk("Uncertainty quantification across the lifecycle of foundation models for scientific machine learning")],
    },
    {
        "id": "jhu-hpc-2025",
        "order": 4,
        "year": 2025,
        "name": "Inaugural High Performance Computing Symposium, Johns Hopkins University",
        "location": "Johns Hopkins University",
        "dates": "April 2, 2025",
        "talks": [talk("Automated information extraction for ceramic materials")],
    },
    {
        "id": "consec-2024",
        "order": 5,
        "year": 2024,
        "name": "10th International Conference on Concrete under Severe Conditions — Environment and Loading",
        "location": "",
        "dates": "September 25–27, 2024",
        "talks": [talk("AI Driven Information Extraction From Construction Materials Literature")],
    },
    {
        "id": "emi-2024",
        "order": 6,
        "year": 2024,
        "name": "Engineering Mechanics Institute Conference 2024",
        "location": "Chicago, Illinois, USA",
        "dates": "May 28–31, 2024",
        "talks": [talk("CEMCAT: Cementitious materials catalogue with their compositions, properties, synthesis and characterization methods, and applications")],
    },
    {
        "id": "gomd-2024",
        "order": 7,
        "year": 2024,
        "name": "Glass and Optical Materials Division Meeting (GOMD 2024)",
        "location": "Las Vegas, Nevada, USA",
        "dates": "May 19–24, 2024",
        "talks": [talk("Extracting materials tetrahedron of inorganic glasses using natural language processing")],
    },
    {
        "id": "mrs-fall-2023",
        "order": 8,
        "year": 2023,
        "name": "2023 Materials Research Society Meeting and Exhibit",
        "location": "Boston, Massachusetts, USA",
        "dates": "November 26–December 1, 2023",
        "talks": [
            talk("Large language models for materials science education and research"),
            talk("Information extraction from materials science research papers"),
        ],
    },
    {
        "id": "acl-2023",
        "order": 9,
        "year": 2023,
        "name": "61st Annual Meeting of the Association for Computational Linguistics",
        "location": "Toronto, Canada",
        "dates": "2023",
        "talks": [talk("DiSCoMaT: Distantly Supervised Composition Extraction from Tables in Materials Science Articles")],
    },
    {
        "id": "gomd-2023",
        "order": 10,
        "year": 2023,
        "name": "Glass and Optical Materials Division Meeting (GOMD 2023)",
        "location": "New Orleans, Louisiana, USA",
        "dates": "June 4–8, 2023",
        "talks": [talk("Automated extraction of glass compositions and properties from research literature", "Oral")],
    },
    {
        "id": "emi-2023",
        "order": 11,
        "year": 2023,
        "name": "Engineering Mechanics Institute Conference 2023",
        "location": "Atlanta, Georgia, USA",
        "dates": "June 6–10, 2023",
        "talks": [talk("Investigating large language models’ understanding of mechanics", "Oral")],
    },
    {
        "id": "mrs-spring-2023",
        "order": 12,
        "year": 2023,
        "name": "2023 Materials Research Society Meeting and Exhibit",
        "location": "San Francisco, California, USA",
        "dates": "April 10–14, 2023",
        "talks": [talk("Extracting materials compositions from research papers using natural language processing", "Oral")],
    },
    {
        "id": "icg-2022",
        "order": 13,
        "year": 2022,
        "name": "26th International Congress on Glass",
        "location": "Online",
        "dates": "2022",
        "talks": [
            talk("Predicting Vickers hardness of glasses as a function of processing parameters", "Oral"),
            talk("Predicting optical properties of glasses as a function of testing parameters", "Oral"),
        ],
    },
    {
        "id": "sisecam-2022",
        "order": 14,
        "year": 2022,
        "name": "Şişecam 37th International Glass Conference",
        "location": "Istanbul, Turkey",
        "dates": "2022",
        "talks": [
            talk(
                "Machine learning based predictions and explanations of glass properties as a function of composition, testing, and processing parameters",
                "Poster",
            )
        ],
    },
    {
        "id": "gomd-2022",
        "order": 15,
        "year": 2022,
        "name": "Pacific Rim Conference on Ceramic and Glass Technology, including the Glass and Optical Materials Division Meeting (GOMD 2022)",
        "location": "Online",
        "dates": "2022",
        "talks": [talk("Predicting electrical properties of glasses as a function of composition and wavelengths", "Oral")],
    },
    {
        "id": "gomd-2021",
        "order": 16,
        "year": 2021,
        "name": "Pacific Rim Conference on Ceramic and Glass Technology, including the Glass and Optical Materials Division Meeting (GOMD 2021)",
        "location": "Online",
        "dates": "2021",
        "talks": [
            talk("Predicting normal and anomalous glasses directly from the indent images using machine learning", "Oral"),
            talk("Extracting the synthesis and processing protocols from materials science literature for improved property prediction", "Oral"),
            talk("Understanding the optical properties of glasses using interpretable machine learning", "Oral"),
        ],
    },
    {
        "id": "mst-2021",
        "order": 17,
        "year": 2021,
        "name": "Materials Science and Technology 2021 (MS&T21)",
        "location": "Online",
        "dates": "2021",
        "talks": [
            talk("Elucidating compositional governance of optical properties of oxide glasses using interpretable machine learning", "Oral"),
            talk("Predicting glass behavior from optical microscopy images using interpretable machine learning", "Oral"),
        ],
    },
]

profile = {
    "name": "Mohd Zaki",
    "research_description": "Artificial Intelligence for Materials Science and Structural Engineering",
    "job_title": "Postdoctoral Researcher",
    "affiliation": "Johns Hopkins University",
    "affiliation_detail": "Hopkins Extreme Materials Institute, Baltimore, Maryland",
    "email": "mzaki4@jh.edu",
    "biography": (
        "My research develops artificial intelligence and data-driven methods to understand, "
        "discover, and design engineering materials and resilient structures. My interests span "
        "scientific language models, materials informatics, explainable machine learning, "
        "structural response prediction, earthquake engineering, and uncertainty quantification. "
        "I am particularly interested in connecting scientific knowledge, experimental data, "
        "computational models, and AI to accelerate engineering discovery."
    ),
    "site_description": (
        "Personal academic website of Mohd Zaki, postdoctoral researcher at Johns Hopkins University, "
        "working on artificial intelligence for materials science and structural engineering."
    ),
    "links": {
        "scholar": "",
        "orcid": "",
        "github": "https://github.com/zakidotai",
        "linkedin": "",
        "website": "https://web.iitd.ac.in/~cez198233",
        "website_label": "IIT Delhi",
    },
    "photo": "",
    "cv_pdf": "cv/mohd-zaki-cv.pdf",
    "cv_pdf_available": True,
}

research = [
    {
        "id": "materials-ai",
        "title": "Materials AI and Scientific Language Models",
        "summary": "Scientific language models and methods for reading, extracting, and organizing knowledge from the materials literature.",
        "url": "research/materials-ai/",
    },
    {
        "id": "explainable-ai",
        "title": "Explainable AI and Materials Informatics",
        "summary": "Interpretable models that connect composition, processing, structure, and properties of engineering materials.",
        "url": "research/explainable-ai/",
    },
    {
        "id": "structural-resilience",
        "title": "Structural Resilience and Earthquake Engineering",
        "summary": "Data-driven methods for cementitious materials, structural response, and resilient infrastructure.",
        "url": "research/structural-resilience/",
    },
    {
        "id": "scientific-ml",
        "title": "Scientific Machine Learning and Uncertainty Quantification",
        "summary": "Scientific machine learning, reproducible research software, and uncertainty in engineering models.",
        "url": "research/scientific-ml/",
    },
]

news = [
    {
        "date": "2026-02-27",
        "title": "LLaMat published in Nature Machine Intelligence",
        "description": "A family of large language models for materials research, with a study of model adaptability in continued pre-training.",
        "url": "",
    },
    {
        "date": "2025-02-01",
        "title": "Joined Johns Hopkins University as a postdoctoral researcher",
        "description": "Hopkins Extreme Materials Institute. Topic: discovering materials for extreme environments through agentic AI, with Prof. Michael D. Shields.",
        "url": "",
    },
]

education = [
    {
        "degree": "Ph.D., Structural Engineering",
        "institution": "Indian Institute of Technology Delhi",
        "years": "2019–2025",
        "detail": "CGPA 9.214/10. Department of Civil Engineering.",
        "thesis": "Machine learning and natural language processing for construction materials",
        "supervisors": "Prof. N. M. Anoop Krishnan and Prof. Jayadeva",
    },
    {
        "degree": "B.Tech., Civil Engineering",
        "institution": "Motilal Nehru National Institute of Technology Allahabad",
        "years": "2013–2017",
        "detail": "CGPA 8.57/10. Department of Civil Engineering.",
        "thesis": "",
        "supervisors": "",
    },
    {
        "degree": "Class XII (CBSE)",
        "institution": "S.S. Children Senior Secondary School, Moradabad",
        "years": "2013",
        "detail": "479/500 (95.8%).",
        "thesis": "",
        "supervisors": "",
    },
    {
        "degree": "Class X (CBSE)",
        "institution": "S.S. Children Senior Secondary School, Moradabad",
        "years": "2011",
        "detail": "CGPA 10.0/10.0.",
        "thesis": "",
        "supervisors": "",
    },
]

appointments = [
    {
        "title": "Postdoctoral Researcher",
        "organization": "Johns Hopkins University, Hopkins Extreme Materials Institute",
        "years": "February 2025–present",
        "detail": "Discovering materials for extreme environments through agentic AI. PI: Prof. Michael D. Shields.",
    }
]

service = [
    {
        "years": "2021–present",
        "text": (
            "Reviewed more than 40 research papers for Computational Materials, Journal of Physics: Materials, "
            "Journal of Non-Crystalline Solids, Journal of American Ceramics Society, Digital Discovery, and "
            "conference venues including ACL ARR, computational linguistics conferences, and the AI4MAT and "
            "AI4Science NeurIPS workshops."
        ),
    }
]

skills = [
    {"group": "Programming languages", "items": "Python, C, FORTRAN"},
    {
        "group": "Tools",
        "items": "Cursor, MATLAB, OpenSees, AutoCAD, STAAD Pro, Revit Architecture",
    },
    {"group": "Robotic platforms", "items": "Arduino, Raspberry Pi, NVIDIA Jetson Nano"},
]

impact = [
    {
        "title": "[Sample fixture] Not a real paper",
        "authors": "Sample Author",
        "year": 2024,
        "venue": "Sample Venue",
        "paper_url": "",
        "doi": "",
        "cited_work_id": "gupta2022matscibert",
        "relationship_category": "Methods Extended",
        "relationship_summary": "This unverified fixture must not appear on the public site.",
        "evidence_note": "Delete this record or replace it after manual review. Do not mark it verified.",
        "verified": False,
        "featured": False,
        "research_topics": ["materials-ai"],
    }
]


def dump(name, obj, comment):
    text = comment.rstrip() + "\n" + yaml.safe_dump(
        obj,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )
    (ROOT / name).write_text(text)


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    dump(
        "profile.yaml",
        profile,
        """# Public profile. This is the only place to edit the name, biography, affiliation, and links.
# Leave a link blank to hide it. photo is a path under static/, for example images/portrait.jpg.
# scholar and orcid are blank until a verified URL is added.
# The CV also lists mohdzaki1995@gmail.com; the public site shows the institutional address only.
""",
    )
    dump(
        "research.yaml",
        research,
        "# Research directions. url is a site path without a leading slash.\n",
    )
    dump(
        "publications.yaml",
        publications,
        """# Publications transcribed from 003_zaki_cv_20260904.pdf.
# Empty doi, url, pdf, code, and dataset fields were not given on the CV. Do not invent them.
# Set open_access: true only when the version is legally shareable.
# featured: true places the paper in the homepage selection.
# topics: materials-ai, explainable-ai, structural-resilience, scientific-ml.
""",
    )
    dump("awards.yaml", awards, "# Awards transcribed from the CV. Shown on the homepage and the CV page.\n")
    dump(
        "teaching.yaml",
        teaching,
        """# Courses transcribed from the CV. The teaching block names IIT Delhi.
# role is "Teaching" because the CV does not state instructor or assistant.
# resources can list notes or slides, for example:
#   - label: Notes
#     url: https://example.org/notes
""",
    )
    dump(
        "conferences.yaml",
        conferences,
        """# Talks transcribed from the CV. order 1 is the newest.
# dates are the dates printed on the CV. They are not labeled completed or upcoming.
# format is set only when the CV says Oral or Poster.
""",
    )
    dump(
        "news.yaml",
        news,
        "# News taken from dated CV facts. Add new entries at the top. date is YYYY-MM-DD. url is optional.\n",
    )
    dump("education.yaml", education, "# Education transcribed from the CV.\n")
    dump("appointments.yaml", appointments, "# Appointments transcribed from the CV.\n")
    dump("service.yaml", service, "# Professional service transcribed from the CV.\n")
    dump("skills.yaml", skills, "# Skills transcribed from the CV.\n")
    dump(
        "software.yaml",
        [],
        """# Verified software and datasets only. Do not add a repository that has not been checked.
# - name: Example
#   description: One sentence.
#   github: https://github.com/org/repo
#   documentation: ""
#   paper: ""
#   dataset: ""
#   topics: [materials-ai]
#   verified: true
""",
    )
    dump(
        "collaborators.yaml",
        [],
        """# Verified collaborators only. Coauthors are not added from the publication list.
# - name: Example Person
#   affiliation: Example University
#   area: Materials AI
#   url: https://example.org
#   photo: ""
#   projects: []
#   topics: [materials-ai]
#   verified: true
""",
    )
    dump(
        "impact.yaml",
        impact,
        """# Research impact. The public site shows records with verified: true only.
# A citation is not enough. Write relationship_summary after reading the paper.
# relationship_category must be one of:
#   Methods Extended, Applications, Follow-up Research,
#   Independent Validation, Dataset or Software Reuse
# cited_work_id must match an id in publications.yaml.
# Candidate records from OpenAlex, Semantic Scholar, or Crossref stay verified: false
# until they are reviewed. Do not scrape Google Scholar.
""",
    )


if __name__ == "__main__":
    main()
