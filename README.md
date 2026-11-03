# 3D Brain Tumor Segmentation on BraTS 2020

**Segmenting gliomas in multimodal MRI: a 3D U-Net baseline compared with CNN–Transformer hybrids.**

Each BraTS case is a 3D brain MRI with four modalities: T1, T1-contrast, T2, and FLAIR. The task is to label every voxel as one of three nested tumor regions:

- **WT, whole tumor:** everything abnormal.
- **TC, tumor core.**
- **ET, enhancing tumor:** the smallest and hardest region.

## What's here

| Notebook | What it does |
|---|---|
| `Baseline.ipynb` | Full 3D U-Net pipeline. Builds a train/validation/test split (232 / 37 / 100 cases), applies 3D data augmentation, trains the model, and reports **per-case Dice and Jaccard scores for WT, TC, and ET**. |
| `BiTr_Unet.ipynb` | Adapts **BiTr-UNet** (a CNN encoder with a Transformer bottleneck) to BraTS 2020 data. |
| `TrAtUNET.ipynb` | Experiments with a Transformer + attention U-Net variant. |
| `cs231n_baseline/` | Data preparation for the baseline. |

## Evaluation

The models are scored with **Dice** and **Jaccard (IoU)** for each tumor region. These are the standard BraTS overlap metrics, and per-region scores show where a model struggles. Whole tumor is usually segmented well. Enhancing tumor is the region where architectures differ most.

## Running it

The notebooks run on Google Colab with a GPU, or on any CUDA machine with PyTorch.

1. Request the **BraTS 2020** dataset from the [official challenge page](https://www.med.upenn.edu/cbica/brats2020/data.html). The dataset is not redistributed here, apart from one validation sample.
2. Update the data paths in the first cell of each notebook.
3. Run the notebook top to bottom.

## Credits

This repository includes copies of two open-source projects for comparison. Credit belongs to their authors:

- `BiTr-Unet-main/`: **BiTr-Unet: a CNN-Transformer Combined Network for MRI Brain Tumor Segmentation** (Q. Jia & H. Shu, BrainLes 2021), [arXiv:2109.12271](https://arxiv.org/abs/2109.12271). See its LICENSE.
- `Multiclass-Segmentation-BraTS2020-main/`: an open-source BraTS 2020 multiclass segmentation project (Attention Res-UNet and UNETR notebooks). See its README.

Dataset: Menze et al., *The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)*, IEEE TMI 2015; Bakas et al., *Nature Scientific Data* 2017; Bakas et al., arXiv:1811.02629.
