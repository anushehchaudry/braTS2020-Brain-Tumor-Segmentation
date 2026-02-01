import os
import numpy as np


subjects = [ f.name for f in os.scandir('/content/drive/Shareddrives/cs231n_final/cs231n_baseline/BraTS2020/BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData') if f.is_dir() ]
with open('official_valid.txt', 'w') as f:
    for item in subjects:
        f.write("%s\n" % item)
