import os
import shutil
import numpy as np

source1 = "/content/drive/Shareddrives/cs231n_final/cs231n_baseline/BraTS2020/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData"
dest11 = "/content/drive/Shareddrives/cs231n_final/cs231n_baseline/BraTS2020/BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData"
files = os.listdir(source1)

for f in files:
    if np.random.rand(1) < 0.2:
        shutil.move(source1 + '/'+ f, dest11 + '/'+ f)