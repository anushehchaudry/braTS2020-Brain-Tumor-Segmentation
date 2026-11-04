# 3D Brain Tumor Segmentation on BraTS 2020

**Segmenting gliomas in multimodal MRI: a 3D U-Net baseline compared with a 3D Attention U-Net and a transformer model.**

Paper: [Automatic Brain Tumor Segmentation: Exploring Beyond U-Net](https://anushehchaudry.com/papers/brain-tumor-segmentation.pdf)

Each BraTS case is a 3D brain MRI with four modalities: T1, T1-contrast, T2, and FLAIR. The task is to label every voxel as one of three nested tumor regions:

- **WT, whole tumor:** everything abnormal.
- **TC, tumor core.**
- **ET, enhancing tumor:** the smallest and hardest region.

## Results (Dice score)

| Model | Whole tumor | Tumor core | Enhancing tumor |
|---|---|---|---|
| 3D U-Net | 0.870 | 0.782 | 0.745 |
| 3D Attention U-Net | **0.881** | **0.786** | **0.796** |
| DubTransBTS (transformer) | 0.635 | 0.592 | 0.569 |

The attention U-Net improved on the baseline in every region, most of all on the enhancing tumor. The transformer model struggled to capture tumor detail.

## What's here

| Notebook | What it does |
|---|---|
| `Baseline.ipynb` | 3D U-Net pipeline: data loading, light augmentation (horizontal flips, brightness/contrast), training, and per-region Dice and Jaccard scores. |
| `scratch.ipynb` | 3D Attention U-Net experiments. |
| `BiTr_Unet.ipynb`, `TrAtUNET.ipynb` | Transformer-based experiments. |
| `cs231n_baseline/` | Data preparation for the baseline. |

## Running it

The notebooks run on Google Colab with a GPU, or on any CUDA machine with PyTorch.

1. Request the **BraTS 2020** dataset from the [official challenge page](https://www.med.upenn.edu/cbica/brats2020/data.html). The dataset is not redistributed here.
2. Update the data paths in the first cell of each notebook.
3. Run the notebook top to bottom.

## Credits

This repository includes copies of two open-source projects for comparison. Credit belongs to their authors:

- `BiTr-Unet-main/`: **BiTr-Unet: a CNN-Transformer Combined Network for MRI Brain Tumor Segmentation** (Q. Jia & H. Shu, BrainLes 2021), [arXiv:2109.12271](https://arxiv.org/abs/2109.12271). See its LICENSE.
- `Multiclass-Segmentation-BraTS2020-main/`: an open-source BraTS 2020 multiclass segmentation project (Attention Res-UNet and UNETR notebooks). See its README.

Dataset: Menze et al., *The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)*, IEEE TMI 2015; Bakas et al., *Nature Scientific Data* 2017; Bakas et al., arXiv:1811.02629.
