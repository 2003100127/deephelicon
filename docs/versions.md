# Versions

## Change

::::{grid} 2 2 2 2

|  Version  |                                  Date                                   |
|:---------:|:-----------------------------------------------------------------------:|
| 2020-2024 | ![](https://img.shields.io/badge/past_released-February._2020-red.svg)  |
|  `0.0.1`  | ![](https://img.shields.io/badge/latest_released-April._2025-green.svg) |

::::

## Before `0.0.1`

The version of **DeepHelicon** released in 2020 can only be run on the Tensorflow `1x` platform.

### Inference

```{code} shell
python run_deephelicon.py -n 2wsc -c 2 -i ./input/ -o ./output/ -f 'Normal'
```

```{code} shell
-n --name -> protein name.
-i --input -> input path.
-o --output --> prediction results.
-f --format --> Format of a output file, 'Normal' or 'CASP14'.
```