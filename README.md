# DeepPano
Image segmentation for dental panoramic radiographs. 

Segmentation is based on UNet architecture, which has proved effective in medical image segmentation, requiring few images for training while ensuring good quality of segmentation (see https://arxiv.org/abs/1505.04597). 

Implementation is done using Keras library, based on Tensorflow backend.

First milestone is segmentation of metallic amalgams. If successful, further milestones will include tooth decay detection.

All training/test data are panoramic radiographs of my family members which is why I did not include them in this repo.
