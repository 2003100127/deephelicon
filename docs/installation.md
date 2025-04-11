# Installation

## Overview

We tested **DeepHelicon** on a Linux operating system, as several input feature generation tools are Linux-dependent. However, if you already have the required feature files (as shown in [example_data](./tutorial/data#Input)), the program can be run on other platforms such as Windows and macOS. Before using the software, please ensure that Python (version `>=3.11`) is installed. We highly recommend using [Anaconda](https://www.anaconda.com/), an integrated Python development environment, which simplifies package management and environment setup.

## Installing

### GitHub

Then, we can follow the step-by-step precedures for installation.

Step 1: Get the most recent version of **DeepHelicon** from GitHub (_clone it at your preferred location_), PyPI, or Conda.

```{code} shell
git clone https://github.com/2003100127/deephelicon.git
```

Step 2: Create a conda environment in your local machine.

```{code} shell
conda create --name deephelicon python=3.12

conda activate deephelicon
```

Step 3: install via pip

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
cd deephelicon

pip install .
```
:::
:::{tab-item} Log
:sync: tab2
```{code} shell
Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting biopython<2.0,>=1.85 (from deephelicon==0.0.1)
  Using cached biopython-1.85-cp312-cp312-win_amd64.whl.metadata (13 kB)
Collecting click<9.0.0,>=8.1.8 (from deephelicon==0.0.1)
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting joblib==1.4.2 (from deephelicon==0.0.1)
  Using cached joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Collecting numba<0.62.0,>=0.61.0 (from deephelicon==0.0.1)
  Downloading numba-0.61.0-cp312-cp312-win_amd64.whl.metadata (2.8 kB)
Collecting numpy==2.1.3 (from deephelicon==0.0.1)
  Using cached numpy-2.1.3-cp312-cp312-win_amd64.whl.metadata (60 kB)
Collecting pandas==2.2.3 (from deephelicon==0.0.1)
  Using cached pandas-2.2.3-cp312-cp312-win_amd64.whl.metadata (19 kB)
Collecting pyfiglet<2.0.0,>=1.0.2 (from deephelicon==0.0.1)
  Using cached pyfiglet-1.0.2-py3-none-any.whl.metadata (7.1 kB)
Collecting tensorflow==2.19 (from deephelicon==0.0.1)
  Using cached tensorflow-2.19.0-cp312-cp312-win_amd64.whl.metadata (4.1 kB)
Collecting python-dateutil>=2.8.2 (from pandas==2.2.3->deephelicon==0.0.1)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas==2.2.3->deephelicon==0.0.1)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas==2.2.3->deephelicon==0.0.1)
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting absl-py>=1.0.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached absl_py-2.2.2-py3-none-any.whl.metadata (2.6 kB)
Collecting astunparse>=1.6.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached astunparse-1.6.3-py2.py3-none-any.whl.metadata (4.4 kB)
Collecting flatbuffers>=24.3.25 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached flatbuffers-25.2.10-py2.py3-none-any.whl.metadata (875 bytes)
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached gast-0.6.0-py3-none-any.whl.metadata (1.3 kB)
Collecting google-pasta>=0.1.1 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached google_pasta-0.2.0-py3-none-any.whl.metadata (814 bytes)
Collecting libclang>=13.0.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached libclang-18.1.1-py2.py3-none-win_amd64.whl.metadata (5.3 kB)
Collecting opt-einsum>=2.3.2 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting packaging (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
Collecting protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.3 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached protobuf-5.29.4-cp310-abi3-win_amd64.whl.metadata (592 bytes)
Collecting requests<3,>=2.21.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: setuptools in d:\programming\anaconda3\envs\deephelicon\lib\site-packages (from tensorflow==2.19->deephelicon==0.0.1) (78.1.0)
Collecting six>=1.12.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting termcolor>=1.1.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached termcolor-3.0.1-py3-none-any.whl.metadata (6.1 kB)
Collecting typing-extensions>=3.6.6 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached typing_extensions-4.13.1-py3-none-any.whl.metadata (3.0 kB)
Collecting wrapt>=1.11.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached wrapt-1.17.2-cp312-cp312-win_amd64.whl.metadata (6.5 kB)
Collecting grpcio<2.0,>=1.24.3 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached grpcio-1.71.0-cp312-cp312-win_amd64.whl.metadata (4.0 kB)
Collecting tensorboard~=2.19.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached tensorboard-2.19.0-py3-none-any.whl.metadata (1.8 kB)
Collecting keras>=3.5.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached keras-3.9.2-py3-none-any.whl.metadata (6.1 kB)
Collecting h5py>=3.11.0 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached h5py-3.13.0-cp312-cp312-win_amd64.whl.metadata (2.5 kB)
Collecting ml-dtypes<1.0.0,>=0.5.1 (from tensorflow==2.19->deephelicon==0.0.1)
  Using cached ml_dtypes-0.5.1-cp312-cp312-win_amd64.whl.metadata (22 kB)
Collecting colorama (from click<9.0.0,>=8.1.8->deephelicon==0.0.1)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting llvmlite<0.45,>=0.44.0dev0 (from numba<0.62.0,>=0.61.0->deephelicon==0.0.1)
  Downloading llvmlite-0.44.0-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
Requirement already satisfied: wheel<1.0,>=0.23.0 in d:\programming\anaconda3\envs\deephelicon\lib\site-packages (from astunparse>=1.6.0->tensorflow==2.19->deephelicon==0.0.1) (0.45.1)
Collecting rich (from keras>=3.5.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached rich-14.0.0-py3-none-any.whl.metadata (18 kB)
Collecting namex (from keras>=3.5.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached namex-0.0.8-py3-none-any.whl.metadata (246 bytes)
Collecting optree (from keras>=3.5.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached optree-0.14.1-cp312-cp312-win_amd64.whl.metadata (50 kB)
Collecting charset-normalizer<4,>=2 (from requests<3,>=2.21.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached charset_normalizer-3.4.1-cp312-cp312-win_amd64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.21.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.21.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached urllib3-2.3.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests<3,>=2.21.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached certifi-2025.1.31-py3-none-any.whl.metadata (2.5 kB)
Collecting markdown>=2.6.8 (from tensorboard~=2.19.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached Markdown-3.7-py3-none-any.whl.metadata (7.0 kB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard~=2.19.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached tensorboard_data_server-0.7.2-py3-none-any.whl.metadata (1.1 kB)
Collecting werkzeug>=1.0.1 (from tensorboard~=2.19.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting MarkupSafe>=2.1.1 (from werkzeug>=1.0.1->tensorboard~=2.19.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl.metadata (4.1 kB)
Collecting markdown-it-py>=2.2.0 (from rich->keras>=3.5.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich->keras>=3.5.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached pygments-2.19.1-py3-none-any.whl.metadata (2.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->keras>=3.5.0->tensorflow==2.19->deephelicon==0.0.1)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Using cached joblib-1.4.2-py3-none-any.whl (301 kB)
Using cached numpy-2.1.3-cp312-cp312-win_amd64.whl (12.6 MB)
Using cached pandas-2.2.3-cp312-cp312-win_amd64.whl (11.5 MB)
Using cached tensorflow-2.19.0-cp312-cp312-win_amd64.whl (376.0 MB)
Using cached biopython-1.85-cp312-cp312-win_amd64.whl (2.8 MB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Downloading numba-0.61.0-cp312-cp312-win_amd64.whl (2.8 MB)
   ---------------------------------------- 2.8/2.8 MB 13.6 MB/s eta 0:00:00
Using cached pyfiglet-1.0.2-py3-none-any.whl (1.1 MB)
Using cached absl_py-2.2.2-py3-none-any.whl (135 kB)
Using cached astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Using cached flatbuffers-25.2.10-py2.py3-none-any.whl (30 kB)
Using cached gast-0.6.0-py3-none-any.whl (21 kB)
Using cached google_pasta-0.2.0-py3-none-any.whl (57 kB)
Using cached grpcio-1.71.0-cp312-cp312-win_amd64.whl (4.3 MB)
Using cached h5py-3.13.0-cp312-cp312-win_amd64.whl (3.0 MB)
Using cached keras-3.9.2-py3-none-any.whl (1.3 MB)
Using cached libclang-18.1.1-py2.py3-none-win_amd64.whl (26.4 MB)
Downloading llvmlite-0.44.0-cp312-cp312-win_amd64.whl (30.3 MB)
   ---------------------------------------- 30.3/30.3 MB 10.9 MB/s eta 0:00:00
Using cached ml_dtypes-0.5.1-cp312-cp312-win_amd64.whl (210 kB)
Using cached opt_einsum-3.4.0-py3-none-any.whl (71 kB)
Using cached protobuf-5.29.4-cp310-abi3-win_amd64.whl (434 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tensorboard-2.19.0-py3-none-any.whl (5.5 MB)
Using cached termcolor-3.0.1-py3-none-any.whl (7.2 kB)
Using cached typing_extensions-4.13.1-py3-none-any.whl (45 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Using cached wrapt-1.17.2-cp312-cp312-win_amd64.whl (38 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached packaging-24.2-py3-none-any.whl (65 kB)
Using cached certifi-2025.1.31-py3-none-any.whl (166 kB)
Using cached charset_normalizer-3.4.1-cp312-cp312-win_amd64.whl (102 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached Markdown-3.7-py3-none-any.whl (106 kB)
Using cached tensorboard_data_server-0.7.2-py3-none-any.whl (2.4 kB)
Using cached urllib3-2.3.0-py3-none-any.whl (128 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached namex-0.0.8-py3-none-any.whl (5.8 kB)
Using cached optree-0.14.1-cp312-cp312-win_amd64.whl (306 kB)
Using cached rich-14.0.0-py3-none-any.whl (243 kB)
Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl (15 kB)
Using cached pygments-2.19.1-py3-none-any.whl (1.2 MB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Building wheels for collected packages: deephelicon
  Building wheel for deephelicon (pyproject.toml) ... done
  Created wheel for deephelicon: filename=deephelicon-0.0.1-py3-none-any.whl size=43805 sha256=737164dfce4079656dc6e962546a53d8ef1d5d1a79f1718fe0b36417c4d885d6
  Stored in directory: C:\Users\jianf\AppData\Local\Temp\pip-ephem-wheel-cache-1tmt2fi6\wheels\79\7b\16\b43d9771719ae42acfe1e86d8a33d0f8e7b50801f3f0b2b0bc
Successfully built deephelicon
Installing collected packages: pytz, namex, libclang, flatbuffers, wrapt, urllib3, tzdata, typing-extensions, termcolor, tensorboard-data-server, six, pygments, pyfiglet, protobuf, packaging, opt-einsum, numpy, mdurl, MarkupSafe, markdown, llvmlite, joblib, idna, grpcio, gast, colorama, charset-normalizer, certifi, absl-py, werkzeug, requests, python-dateutil, optree, numba, ml-dtypes, markdown-it-py, h5py, google-pasta, click, biopython, astunparse, tensorboard, rich, pandas, keras, tensorflow, deephelicon
Successfully installed MarkupSafe-3.0.2 absl-py-2.2.2 astunparse-1.6.3 biopython-1.85 certifi-2025.1.31 charset-normalizer-3.4.1 click-8.1.8 colorama-0.4.6 deephelicon-0.0.1 flatbuffers-25.2.10 gast-0.6.0 google-pasta-0.2.0 grpcio-1.71.0 h5py-3.13.0 idna-3.10 joblib-1.4.2 keras-3.9.2 libclang-18.1.1 llvmlite-0.44.0 markdown-3.7 markdown-it-py-3.0.0 mdurl-0.1.2 ml-dtypes-0.5.1 namex-0.0.8 numba-0.61.0 numpy-2.1.3 opt-einsum-3.4.0 optree-0.14.1 packaging-24.2 pandas-2.2.3 protobuf-5.29.4 pyfiglet-1.0.2 pygments-2.19.1 python-dateutil-2.9.0.post0 pytz-2025.2 requests-2.32.3 rich-14.0.0 six-1.17.0 tensorboard-2.19.0 tensorboard-data-server-0.7.2 tensorflow-2.19.0 termcolor-3.0.1 typing-extensions-4.13.1 tzdata-2025.2 urllib3-2.3.0 werkzeug-3.1.3 wrapt-1.17.2
```
:::
::::

Everything should be all set before you run **DeepHelicon**.