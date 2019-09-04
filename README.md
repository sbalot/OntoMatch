# OntoMatch

## Introduction

This work won the award for the best project at [LDAC2019 Hackathon ](http://linkedbuildingdata.net/ldac2019/summerschool/). We extended the work by [Faria et al.](https://www.semanticscholar.org/paper/The-AgreementMakerLight-Ontology-Matching-System-Faria-Pesquita/b1b2a1db535e90b9b192c92b55a5e9e0375f2f0f) and modified their tool [AgreementMakerLight](https://github.com/AgreementMakerLight/AML-Project/releases) for this project.

Our implementation can be used to exploring the capabilities of AgreementMakerLight tool for ontology matching. We used Python scripts to automate creating different outputs by trying out different settings of [AgreementMakerLight](https://github.com/AgreementMakerLight/AML-Project/releases) to determine the best property combination for matching your domain ontology.

## Requirements and Steps

### Python libraries required

1. Python 3.7
2. RDFlib
3. Numpy
4. Itertols
5. re
6. os

### Precompiled tools required

 [AgreementMakerLight](https://github.com/AgreementMakerLight/AML-Project/releases)

### Steps

1. Clone this repo.
2. Download and unzip [AgreementMakerLight](https://github.com/AgreementMakerLight/AML-Project/releases) inside the repo such that  [AgreementMakerLight.jar](https://github.com/AgreementMakerLight/AML-Project/releases) and OntoMatch.py and Folder 'store' are in the root folder.
3. Place the ontologies to be compared in your root folder.
4. Open OntoMatch.py using VS code or similar.
5. Edit the combination of properties in the `main()` in the file `OntoMatch.py`. 
6. Run the code.
7. You would see results in `count_result` and `result` file.

### Using Knowledge Bases to improve matching
The AgreementMakerLight has options to different matching steps, the default one being "Background Knowledge Matcher". An owl file of any ontology has to be copied in the following root folder of the tool: ./store/knowledge. The, in the tool, go to Match>Custom Match>Match Options>Settings>Matching Settings, and select your loaded knowledge base prior to initiating the matching. 

