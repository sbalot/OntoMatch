# OntoMatch

## Introduction

This work won the award for the best project at [LDAC2019 Hackathon ] (http://linkedbuildingdata.net/ldac2019/summerschool/). We extended the work by [Faria et al.] (https://www.semanticscholar.org/paper/The-AgreementMakerLight-Ontology-Matching-System-Faria-Pesquita/b1b2a1db535e90b9b192c92b55a5e9e0375f2f0f) and modified their tool [AgreementMakerLight](https://github.com/AgreementMakerLight/AML-Project/releases) for this project.

Our implementation can be used to exploring the capabilities of AgreementMakerLight tool for ontology matching. We used Python scripts to automate creating different outputs by trying out different settings of [AgreementMakerLight](https://github.com/AgreementMakerLight/AML-Project/releases) to determine the best property combination for matching your domain ontology.

## Requirements and Steps

###Python libraries required

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
3. Place the otologies to be compared in your root folder.
4. Open Matchresults_method2.py using VS code or similar.
5. Edit the following in `OntoMatch.py` to include your ontologies instead of `BOT.owl` and `DogOntW.owl`. This should be exact file names of ontologies you have placed in root folder.
    ~~~~ 
    os.system('java -jar ./AgreementMakerLight.jar -s BOT.owl -t DogOntW.owl -o alignment.rdf -m')
    ~~~~
6. Edit the combination of properties in the `main()` 
7. Run the code.
8. You would see results in `count_result` and `result` file.
