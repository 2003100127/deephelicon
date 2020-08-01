# DeepHelicon
![](https://img.shields.io/badge/DeepHelicon-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released_date-Feb_2020-green.svg)

###### tags: `transmembrane protein` `residue contact predictor` `inter-helical contacts` `v1.0`

## Overview
DeepHelicon is a predictor for accurately predicting inter-helical residue contacts in transmembrane proteins. This repository provides a standalone package of DeepHelicon.

## System Requirement
    
The software is only allowed to be run on a Linux operation system. Please be sure of python (version>3.5) installed before using. We highly recommend a package [Anaconda](https://www.anaconda.com/distribution/), an integrated development environment of python, which eases the use and management of python packages.

## Installation
    
1. **install the dependencies and specify where their executables are**.
    * [HHblits](https://github.com/soedinglab/hh-suite) - generating multiple sequence alignments
    * [CCMpred](https://github.com/soedinglab/CCMpred) - predictor of residue contacts
    * [Gaussian DCA](https://github.com/carlobaldassi/GaussDCA.jl) - predictor of residue contacts
    * [Freecontact](https://rostlab.org/owiki/index.php/FreeContact) - predictor of residue contacts
    * [plmDCA](https://github.com/debbiemarkslab/plmc) - predictor of residue contacts
    * [TMHMM2.0](https://services.healthtech.dtu.dk/software.php) - predictor of transmembrane segments
    * [EVcouplings](https://github.com/debbiemarkslab/EVcouplings) - python interface used for predicting protein structure, function and mutations using evolutionary sequence covariation
    * [Uniprot database](http://wwwuser.gwdg.de/~compbiol/data/hhsuite/databases/hhsuite_dbs/old-releases/) - a curated protein sequence database for hhblits
    
    > **_NOTE_**
    
    1. Download either the recommended Uniprot database, or other database curated for HHblits and make it work with hhblits.
    2. Download and specify the path of EVcouplings package in src/Plmc_dhc_rs.py. Please do not rename this package.
    3. Please add the paths of the above executable programs to `src/troll.sh`.


2. **install DeepHelicon**

    * To download a released package of DeepHelicon stable version, click [`here`](https://github.com/2003100127/deephelicon/releases).
    
    * To download all prediction models of DeepHelicon click [`here`](https://github.com/2003100127/deephelicon/releases).
    

    * To obtain the latest version of DeepHelicon, do
    ```
    git clone https://github.com/2003100127/deeptmcon.git
    ```

3. **install python dependencies**
    
    ```    
	pip install -r requirements.txt
	```

## Usage

1. part 1 of feature generation via **`src/troll.sh`**

    * description
        troll.sh is used to generate transmembrane topologies and most of evolutionary coupling features, including CCMpred, EVfold, plmDCA.
        
    * name format of a FASTA file
        Note, the FASTA file you are providing should have the suffix '.fasta'. For example, a whole FASTA file name can be '2wsc2.fasta' or a CASP name 'T1024.fasta'.

    * shell commands
        * general
        ```
        ./troll.sh -n NAME -c CHAIN -i /INPUT/PATH/
        ```
        * example
        ```
        ./troll.sh -n 2wsc -c 2 -i ./input/
        ```
    * parameters
	    * required
        ```
        -n --name -> protein name.
        -i --input -> input path.
        ```
        
        * optional
        ```
        -c --chain -> chain name. Chain name of a FASTA file. For example, '2'. This can be empty if you prefer a name of the input FASTA file like '2wsc2' or a CASP name 'T1024'.
        ```

2. part 1 of feature generation via **`src/gdca.julia`**
    
    * description
        
        gdca.julia is used to generate Gaussian DCA file. You'd better run it cf. https://github.com/carlobaldassi/GaussDCA.jl.
        
3. prediction via **`run_deephelicon.py`**
    
    * description
        
        If you have the feature files shown in the `input/` directory, you can skip over steps 1-2 to step 3. We tested this step in a rigorous way. Be sure of every feature file already in the `input/` or your preferred input file path. Before start, an available `EVcouplings` tool must be configured with our program properly. Finally, it works easily like this. 
    
	* python commands
	    * general
	    ```
        python run_deephelicon.py -n NAME -c CHAIN -i /YOUR/input/PATH/ -o /YOUR/OUTPUT/PATH/ -f FORMAT
        ```
	    * example
        ```
        python run_deephelicon.py -n 2wsc -c 2 -i ./input/ -o ./output/ -f 'Normal'
        ```
	* parameters
	    * required
        ```
        -n --name -> protein name.
        -i --input -> input path.
        -o --output --> prediction results.
        -f --format --> Format of a output file, 'Normal' or 'CASP14'.
        ```
        
        * optional

        ```
        -c --chain -> chain name. Chain name of a FASTA file. For example, '2'. This can be empty if you prefer a name of the input FASTA file like '2wsc2' or a CASP name 'T1024'.
        ```
        * see detail
        ```
        python run_deephelicon.py -h
        ```

2. description of an output file

	* format
	  This predictor returns predictions of inter-helical residue contacts in tansmembrane proteins. If non-transmembrane segment or <1 transmembrane segment is detected, the programe will not return final results. However, you can still utilize the intermediate results at stage 1 and 2 as stated in the paper. Considering <1 helix detection by inside transmembrane topology predictor, we will consider extending our module to generate a file including entire results in the future work. The DeepHelicon provides two formats of output file illustrated by the two examples below (see one file format of a output file `./output/2wsc2.deephelicon`).
      
    * example in 'Normal' format
	  
      ![](https://i.imgur.com/lCPvY1n.png)
      
    * example in 'CASP14' format

        see [CASP14 format](https://predictioncenter.org/casp14/index.cgi?page=format#RR)

## How to cite
Sun, J., Frishman, D. (2020). DeepHelicon: accurate prediction of inter-helical residue contacts in transmembrane proteins by residual neural networks. ***J. Struct. Biol.***, vol. 212. 107574. doi:[10.1016/j.jsb.2020.107574](https://doi.org/10.1016/j.jsb.2020.107574)

## Contact
If you have any problem in using it, please feel free to contact
> jianfeng.sunmt{[({at})]}gmail.com
> jianfeng.sun{[({at})]}tum.de