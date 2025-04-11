# Data

## Input

### External tools

Protein sequences are only needed for running DeepHelicon, and are also used to generate a list of intermediate files before running DeepHelicon, as shown in [Table 1](#tbl:external-tool).

:::{note} Fasta
:class: dropdown
Protein sequences in [the Fasta format](https://en.wikipedia.org/wiki/FASTA_format) are required. The file extension must be `.fasta` for recognition of the software.
:::

:::{table} External tools for generating intermediate files before running DeepHelicon.
:label: tbl:external-tool
:align: center

|                              Tool                              |     Role     |                Function                 |                     Source                     |
|:--------------------------------------------------------------:|:------------:|:---------------------------------------:|:----------------------------------------------:|
|       [HHblits](https://github.com/soedinglab/hh-suite)        |    Input     | generating multiple sequence alignments |      <https://doi.org/10.1038/nmeth.1818>      |
|        [CCMPred](https://github.com/soedinglab/CCMpred)        |    Input     |      predictor of residue contacts      | <https://doi.org/10.1093/bioinformatics/btu500> |
|        [plmDCA](https://github.com/debbiemarkslab/plmc)        |    Input     |      predictor of residue contacts      | <https://doi.org/10.1103/PhysRevE.87.012707> |
|  [Gaussian DCA](https://github.com/carlobaldassi/GaussDCA.jl)  |    Input     |      predictor of residue contacts      | <https://doi.org/10.1371/journal.pone.0092721> |
| [Freecontact](https://rostlab.org/owiki/index.php/FreeContact) |    Input     |      predictor of residue contacts      |   <https://doi.org/10.1186/1471-2105-15-85>    |
|          [TMHMM](https://services.healthtech.dtu.dk/software.php)           |    Input     |  predictor of transmembrane topologies  |  <https://doi.org/10.1006/jmbi.2000.4315>   |
|      [Uniclust30 database](https://uniclust.mmseqs.com/)       | Intermediate |            sequence database            |     <https://doi.org/10.1093/nar/gkw1081>      |

:::

:::{tip}
`troll.sh` is used to generate multiple sequence alignments, transmembrane topologies, and all of evolutionary coupling features including [EVfold](https://doi.org/10.1371/journal.pone.0028766) (generated using [FreeContact](https://doi.org/10.1186/1471-2105-15-85)), [Gaussian DCA](https://doi.org/10.1371/journal.pone.0092721), [CCMPred](https://doi.org/10.1093/bioinformatics/btu500), and [plmDCA](https://doi.org/10.1103/PhysRevE.87.012707).
:::

## Output files

DeepHelicon can return an output file with the suffix of `.s1` (stage 1), `.s2i1` (stage 2), `.s2i2` (stage 2), `.s2i3` (stage 2), `.s2i4` (stage 2) or `.deephelicon` depending on different models used at different stages.

This predictor returns predictions of inter-helical residue contacts in tansmembrane proteins. If non-transmembrane segment or <1 transmembrane segment is detected, the programe will not return final results. However, you can still utilise the intermediate results at stage 1 and 2 as stated in the paper @Sun2020deephelicon. Considering <1 helix detection by inside transmembrane topology predictor, we will consider extending our module to generate a file including entire results in the future work. DeepHelicon outputs results in two formats.

### Deephelicon-format

Prediction results of interaction sites in tansmembrane proteins consist of [5 columns](#tbl:deephelicon-output-format).

:::{table} DeepHelicon output format.
:label: tbl:deephelicon-output-format
:align: center

| Position 1 | Residue 1 | Position 2 | Residue 2 | Probability |
|:----------:|:---------:|:----------:|:---------:|:-----------:|
|     1      |     S     |     6      |     L     | 0.14790976  |
|     1      |     S     |     7      |     R     | 0.041100707 |
|     1      |     S     |     8      |     W     | 0.04841847  |
|    ...     |   ...     |    ...     |   ...     |    ...      |
|    170     |     F     |    176     |     K     | 0.05994133  |
|    171     |     A     |    176     |     K     | 0.07471807  |

:::

### CASP14 format

[CASP14](https://predictioncenter.org/casp14/index.cgi?page=format#RR) output has [3 columns](#tbl:casp14-output-format): positions of residue pairs and their contact probabilities.

:::{table} DeepHelicon output format.
:label: tbl:casp14-output-format
:align: center

| Position 1 | Position 2 | Probability |
|:----------:|:----------:|:-----------:|
|     1      |     6      |    .148     |
|     1      |     7      |    .041     |
|     1      |     8      |    .048     |
|    ...     |    ...     |     ...     |
|    170     |    176     |    .060     |
|    171     |    176     |    .075     |

:::

## Example data

Users can download some example data and check an assortment of input files.

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deephelicon

deephelicon.predict.download_data(
    url='https://github.com/2003100127/deephelicon/releases/download/example_data/example_data.zip',
    sv_fpn='../../data/deephelicon/example_data.zip',
)
```
:::
:::{tab-item} Output
:sync: tab2
```{code} shell
 ____                  _   _      _ _                 
|  _ \  ___  ___ _ __ | | | | ___| (_) ___ ___  _ __  
| | | |/ _ \/ _ \ '_ \| |_| |/ _ \ | |/ __/ _ \| '_ \ 
| |_| |  __/  __/ |_) |  _  |  __/ | | (_| (_) | | | |
|____/ \___|\___| .__/|_| |_|\___|_|_|\___\___/|_| |_|
                |_|                                   

06/04/2025 04:45:18 logger: =>Downloading starts...
06/04/2025 04:45:20 logger: =>downloaded.
```
:::
::::

