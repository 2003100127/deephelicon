# Prediction

## Overview

You need to decompress the `example_data.zip` file in your preferred folder, e.g., `deephelicon/`.

:::{caution} Model declaration
We primarily use models in Tensorflow `2x` to perform predictions.
:::

## Multi-stage deep learning

DeepHelicon is a multi-stage, iterative deep learning framework for residue-residue contact prediction. We first perform stage-1 prediction.

### Stage-1 prediction

We define several parameters required for running DeepHelicon at stage 1. 

```{code} python
params_s1 = {
    'prot_name': '2wsc',
    'prot_chain': '2',
    'fasta_fp': '../../data/deephelicon/example_data/',
    'fc_fp': '../../data/deephelicon/example_data/',
    'gdca_fp': '../../data/deephelicon/example_data/',
    'cp_fp': '../../data/deephelicon/example_data/',
    'plmc_fp': '../../data/deephelicon/example_data/',
    'plmc_param_fp': '../../data/deephelicon/example_data/',
    'sv_fp_feature': '../../data/deephelicon/',
    'sv_suffix_feature': '.fs1',
    'model_frozen_fpn': '../../data/deephelicon/model/tf2/frozen_graph/s1.pb',
    'batch_size': 100,
    'seq_sep_inferior': 4,
    'sv_fp_pred': '../../data/deephelicon/',
    'sv_suffix_pred': '.s1',
}
```

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deephelicon

deephelicon.predict.rrcontact_stage1(
    prot_name=params_s1['prot_name'],
    prot_chain=params_s1['prot_chain'],
    fasta_fp=params_s1['fasta_fp'],
    fc_fp=params_s1['fc_fp'],
    gdca_fp=params_s1['gdca_fp'],
    cp_fp=params_s1['cp_fp'],
    plmc_fp=params_s1['plmc_fp'],
    plmc_param_fp=params_s1['plmc_param_fp'],
    sv_fp_feature=params_s1['sv_fp_feature'],
    sv_suffix_feature=params_s1['sv_suffix_feature'],
    model_frozen_fpn=params_s1['model_frozen_fpn'],
    sv_fp_pred=params_s1['sv_fp_pred'],
    sv_suffix_pred=params_s1['sv_suffix_pred'],
    seq_sep_inferior=params_s1['seq_sep_inferior'],
    batch_size=100,
    verbose=True,
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

06/04/2025 06:47:54 logger: ===>Protein: 2wsc chain: 2
06/04/2025 06:47:54 logger: ======>Features are being assembled...
06/04/2025 06:48:09 logger: ======>Finished assembling features.
06/04/2025 06:48:13 logger: ===>The model (../../data/deephelicon/model/tf2/frozen_graph/s1.pb) with frozen graphs converted from tensorflow 1.15.2 is being read...
06/04/2025 06:48:14 logger: ===>The model is read in, with
06/04/2025 06:48:17 logger: ======>Predicted probabilities of residue-residue contacts:
         0  1    2  3            4
0        1  S    6  L   0.14790976
1        1  S    7  R   0.04110071
2        1  S    8  W   0.04841851
3        1  S    9  N  0.094341405
4        1  S   10  V   0.09740046
...    ... ..  ... ..          ...
14701  169  I  175  P   0.05739517
14702  169  I  176  K  0.035921443
14703  170  F  175  P   0.14955024
14704  170  F  176  K   0.05994134
14705  171  A  176  K    0.0747181

[14706 rows x 5 columns]
06/04/2025 06:48:17 logger: ======>Predictions are saved to ../../data/deephelicon/2wsc2.s1
```
:::
::::

Alternatively, it can run in shell. For usage, please type

```{code} shell
deephelicon_s1 -h
```

It shows the usage of different parameters.

```{code} shell
-pn, --prot_name              Protein name identifier (e.g., "5w1h")
-pc, --prot_chain             Protein chain identifier (e.g., "A")
-fa, --fasta_fp               Path to the FASTA file containing the protein sequence
-fcfp, --fc_fp                Path to the FreeContact feature file
-gdcafp, --gdca_fp            Path to the Gaussian DCA feature file
-cpfp, --cp_fp                Path to the CCMPred feature file
-plmcfp, --plmc_fp            Path to the PLMC coupling score file
-plmcparamfp, --plmc_param_fp Path to the PLMC parameter file
-sv_fp_f, --sv_fp_feature     Path to save the generated input features for the model (default: ./)
-sv_suf_f, --sv_suffix_feature    Suffix name for the saved feature file (e.g., ".fs1", default: .fs1)
-m, --model_frozen_fpn        Path to the frozen model (.pb) file for prediction
-sv_fp_p, --sv_fp_pred        Path to save the model prediction outputs (default: ./)
-sv_suf_p, --sv_suffix_pred   Suffix name for the saved prediction file (e.g., ".s1", default: .s1)
-ss_inf, --seq_sep_inferior   Sequence separation inferior limit (default: 4)
-bs, --batch_size             Batch size used during prediction (default: 100)
-vb, --verbose                Whether to print detailed logs during processing (default: True)
```

You can run it using the following code.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deephelicon_s1 -pn 2wsc -pc 2 -fa ./data/deephelicon/example_data/ -fcfp ./data/deephelicon/example_data/ -gdcafp ./data/deephelicon/example_data/ -cpfp ./data/deephelicon/example_data/ -plmcfp ./data/deephelicon/example_data/ -plmcparamfp ./data/deephelicon/example_data/ -sv_fp_f ./data/deephelicon/ -sv_suf_f .fs1 -m ./data/deephelicon/model/tf2/frozen_graph/s1.pb -sv_fp_p ./data/deephelicon/ -ss_inf 4 -sv_suf_p .s1 -bs 100
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

06/04/2025 06:27:59 logger: ===>Protein: 2wsc chain: 2
06/04/2025 06:27:59 logger: ======>Features are being assembled...
06/04/2025 06:28:12 logger: ======>Finished assembling features.
06/04/2025 06:28:13 logger: ===>The model (./data/deephelicon/model/tf2/frozen_graph/s1.pb) with frozen graphs converted from tensorflow 1.15.2 is being read...
06/04/2025 06:28:14 logger: ===>The model is read in, with
06/04/2025 06:28:17 logger: ======>Predicted probabilities of residue-residue contacts:
         0  1    2  3            4
0        1  S    6  L   0.14790976
1        1  S    7  R   0.04110071
2        1  S    8  W   0.04841851
3        1  S    9  N  0.094341405
4        1  S   10  V   0.09740046
...    ... ..  ... ..          ...
14701  169  I  175  P   0.05739517
14702  169  I  176  K  0.035921443
14703  170  F  175  P   0.14955024
14704  170  F  176  K   0.05994134
14705  171  A  176  K    0.0747181

[14706 rows x 5 columns]
06/04/2025 06:28:17 logger: ======>Predictions are saved to ./data/deephelicon/2wsc2.s1
```
:::
::::


### Stage-2 prediction

We define several parameters required for running DeepHelicon at stage 1. 

```{code} python
params_s2i1 = {
    'prot_name': '2wsc',
    'prot_chain': '2',
    'fasta_fp': '../../data/deephelicon/example_data/',
    'dhc_fp': '../../data/deephelicon/',
    'dhc_suffix': '.s1',
    'sv_fp_feature': '../../data/deephelicon/',
    'sv_suffix_feature': '.fs2i1',
    'model_frozen_fpn': '../../data/deephelicon/model/tf2/frozen_graph/s2i1.pb',
    'batch_size': 100,
    'seq_sep_inferior': 5,
    'sv_fp_pred': '../../data/deephelicon/',
    'sv_suffix_pred': '.s2i1',
}
```

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deephelicon

deephelicon.predict.rrcontact_stage2(
    prot_name=params_s2i1['prot_name'],
    prot_chain=params_s2i1['prot_chain'],
    fasta_fp=params_s2i1['fasta_fp'],
    dhc_fp=params_s2i1['dhc_fp'],
    dhc_suffix=params_s2i1['dhc_suffix'],
    sv_fp_feature=params_s2i1['sv_fp_feature'],
    sv_suffix_feature=params_s2i1['sv_suffix_feature'],
    model_frozen_fpn=params_s2i1['model_frozen_fpn'],
    sv_fp_pred=params_s2i1['sv_fp_pred'],
    sv_suffix_pred=params_s2i1['sv_suffix_pred'],
    seq_sep_inferior=params_s2i1['seq_sep_inferior'],
    batch_size=params_s2i1['batch_size'],
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

06/04/2025 06:51:30 logger: ===>Protein: 2wsc chain: 2
06/04/2025 06:51:30 logger: ======>Features are being assembled...
06/04/2025 06:51:36 logger: ======>Finished assembling features.
06/04/2025 06:51:41 logger: ===>The model is read in, with
06/04/2025 06:51:54 logger: ======>Predicted probabilities of residue-residue contacts:
         0  1    2  3            4
0        1  S    7  R  0.026603505
1        1  S    8  W  0.020400615
2        1  S    9  N   0.05953682
3        1  S   10  V   0.04256576
4        1  S   11  Q  0.024525106
...    ... ..  ... ..          ...
14530  168  T  175  P   0.05999833
14531  168  T  176  K   0.06331837
14532  169  I  175  P    0.1027374
14533  169  I  176  K   0.08090736
14534  170  F  176  K   0.14991933

[14535 rows x 5 columns]
06/04/2025 06:51:54 logger: ======>Predictions are saved to ../../data/deephelicon/2wsc2.s2i1
```
:::
::::


In shell, for usage, please type

```{code} shell
deephelicon_s2 -h
```

It shows the usage of different parameters.

```{code} shell
-pn, --prot_name              Protein name identifier (e.g., "5w1h")
-pc, --prot_chain             Protein chain identifier (e.g., "A")
-fa, --fasta_fp               Path to the FASTA file containing the protein sequence
-dhcfp, --dhc_fp              Path to save a residue-residue contact file
-dhc_suf, --dhc_suffix        Suffix name for the saved residue-residue contact prediction file
                            (e.g., ".s1" or ".s2i1")
-sv_fp_f, --sv_fp_feature     Path to save the generated structural feature file for the model
                            (default: "./")
-sv_suf_f, --sv_suffix_feature
                            Suffix name for the saved structural feature file
                            (e.g., ".s2i2", default: ".fs2i1")
-m, --model_frozen_fpn        Path to the frozen model (.pb file) used for prediction
-sv_fp_p, --sv_fp_pred        Path to save the model prediction output (default: "./")
-sv_suf_p, --sv_suffix_pred   Suffix name for the saved prediction file
                            (e.g., "_pred.csv", default: ".s2i1")
-ss_inf, --seq_sep_inferior   Inferior threshold for sequence separation filtering
                            (residue pairs partitioned less than this number will be ignored, default: 5)
-bs, --batch_size             Batch size used during model inference (default: 100)
-vb, --verbose                Whether to print detailed logs during processing (default: True)
```

You can run it using the following code.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deephelicon_s2 -pn 2wsc -pc 2 -fa ./data/deephelicon/example_data/ -dhcfp ./data/deephelicon/ -dhc_suf .s1 -sv_fp_f ./data/deephelicon/ -sv_suf_f .fs2i1 -m ./data/deephelicon/model/tf2/frozen_graph/s2i1.pb -sv_fp_p ./data/deephelicon/ -sv_suf_p .s2i1 -ss_inf 5 -bs 100
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

06/04/2025 06:56:36 logger: ===>Protein: 2wsc chain: 2
06/04/2025 06:56:36 logger: ======>Features are being assembled...
06/04/2025 06:56:41 logger: ======>Finished assembling features.
06/04/2025 06:56:44 logger: ===>The model (./data/deephelicon/model/tf2/frozen_graph/s2i1.pb) with frozen graphs converted 
from tensorflow 1.15.2 is being read...
06/04/2025 06:56:45 logger: ===>The model is read in, with
06/04/2025 06:56:57 logger: ======>Predicted probabilities of residue-residue contacts:
         0  1    2  3            4
0        1  S    7  R  0.026603505
1        1  S    8  W  0.020400615
2        1  S    9  N   0.05953682
3        1  S   10  V   0.04256576
4        1  S   11  Q  0.024525106
...    ... ..  ... ..          ...
14530  168  T  175  P   0.05999833
14531  168  T  176  K   0.06331837
14532  169  I  175  P    0.1027374
14533  169  I  176  K   0.08090736
14534  170  F  176  K   0.14991933

[14535 rows x 5 columns]
06/04/2025 06:56:57 logger: ======>Predictions are saved to ./data/deephelicon/2wsc2.s2i1
```
:::
::::


### Formatting

DeepHelicon offers results in 2 formats, `CASP14` for the CASP14 prediction format and `Normal` for the DeepHelicon format.

:::{seealso}
Please see [data format](./data#Deephelicon-format).
:::

```{code} python
params_reformat = {
    'prot_name': '2wsc',
    'prot_chain': '2',
    'file_paths': '../../data/deephelicon/;../../data/deephelicon/',
    'file_suffixs': '.s2i3;.s2i4',
    'file_ids': '1;2',
    'tmhmm_fp': '../../data/deephelicon/example_data/',
    'sv_fp': '../../data/deephelicon/',
    'format_rr': 'CASP14',
}
```

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deephelicon

deephelicon.predict.reformat(
    prot_name=params_reformat['prot_name'],
    prot_chain=params_reformat['prot_chain'],
    file_paths=params_reformat['file_paths'],
    file_suffixs=params_reformat['file_suffixs'],
    file_ids=params_reformat['file_ids'],
    tmhmm_fp=params_reformat['tmhmm_fp'],
    sv_fp=params_reformat['sv_fp'],
    format_rr=params_reformat['format_rr'],
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

06/04/2025 07:03:27 logger: ===>Protein: 2wsc chain: 2
06/04/2025 07:03:27 logger: ======>Reformatting...
06/04/2025 07:03:32 logger: dataframe: 
      contact_id_1  contact_id_2     0
0               24           142  .984
1               27           142   .98
2               24           139  .975
3               20           139  .974
4               23           139  .966
...            ...           ...   ...
2295            22           176  .005
2296            18           176  .004
2297            16           176  .004
2298            19           176  .004
2299            20           176  .004

[2300 rows x 3 columns]
```
:::
::::

Please type the following command for usage in shell.

```{code} shell
deephelicon_fmt -h
```

```{code} shell
-pn, --prot_name    Protein name identifier (e.g., "5w1h")
-pc, --prot_chain   Protein chain identifier (e.g., "A")
-fps, --file_paths  Python dict of input file paths. The files are produced by DeepHelicon at stage 1 and stage 2.
-fss, --file_suffixs    Python dict of corresponding suffixes for each of the input files (file_paths)
-fids, --file_ids   IDs of input files
-tmhmm, --tmhmm_fp  Path to the TMHMM prediction file for transmembrane region annotation
-sv_fp, --sv_fp Path to save the merged or processed feature file (e.g., .s1, s2i1, s2i2, etc.) (default: ./)
-fmt, --format_rr   Format of the output file for residue-residue contact predictions. The default is "Normal", but "CASP14" is also supported.
-vb, --verbose  Whether to print detailed logs during processing (default: True)
```

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
deephelicon_fmt -pn 2wsc -pc 2 -fps ./data/deephelicon/;./data/deephelicon/ -fss .s2i3;.s2i4 -fids 1;2 -tmhmm ./data/deephelicon/example_data/ -sv_fp ./data/deephelicon/ -fmt Normal
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

06/04/2025 07:23:14 logger: ===>Protein: 2wsc chain: 2
06/04/2025 07:23:14 logger: ======>Reformatting...
06/04/2025 07:23:20 logger: dataframe:
     contact_id_1 aa_1 contact_id_2 aa_2         0
0              13    E           77    D  0.023345
1              13    E           78    I  0.025411
2              13    E           79    L  0.012803
3              13    E           80    N  0.010236
4              13    E           81    P  0.010737
...           ...  ...          ...  ...       ...
2295           35    K          172    A  0.006253
2296           35    K          173    F  0.005909
2297           35    K          174    T  0.005519
2298           35    K          175    P  0.005504
2299           35    K          176    K  0.004724

[2300 rows x 5 columns]
```
:::
::::