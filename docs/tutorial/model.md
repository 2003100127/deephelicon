# Model

## Tensorflow `2.19`
Download DeepHelicon's models.

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deephelicon

deephelicon.predict.download_data(
    url='https://github.com/2003100127/deephelicon/releases/download/model/model.zip',
    sv_fpn='../../data/deephelicon/model.zip',
)
```
:::
:::{tab-item} Output
:sync: tab2
```{code} python
 ____                  _   _      _ _                 
|  _ \  ___  ___ _ __ | | | | ___| (_) ___ ___  _ __  
| | | |/ _ \/ _ \ '_ \| |_| |/ _ \ | |/ __/ _ \| '_ \ 
| |_| |  __/  __/ |_) |  _  |  __/ | | (_| (_) | | | |
|____/ \___|\___| .__/|_| |_|\___|_|_|\___\___/|_| |_|
                |_|                                   

06/04/2025 04:47:09 logger: =>Downloading starts...
06/04/2025 04:47:15 logger: =>downloaded.
```
:::
::::

You can download the models in shell.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deephelicon_download -u https://github.com/2003100127/deephelicon/releases/download/model/model.zip -o ./data/deephelicon/model.zip
```
:::
:::{tab-item} Output
:sync: tab2
```{code} python
 ____                  _   _      _ _
|  _ \  ___  ___ _ __ | | | | ___| (_) ___ ___  _ __
| | | |/ _ \/ _ \ '_ \| |_| |/ _ \ | |/ __/ _ \| '_ \
| |_| |  __/  __/ |_) |  _  |  __/ | | (_| (_) | | | |
|____/ \___|\___| .__/|_| |_|\___|_|_|\___\___/|_| |_|
                |_|

06/04/2025 04:50:19 logger: =>Downloading starts...
06/04/2025 04:50:24 logger: =>downloaded.
```
:::
::::

The models were obtained from multi-stage deep learning processes. In addition, we preserved models trained using tensorflow `1x`.