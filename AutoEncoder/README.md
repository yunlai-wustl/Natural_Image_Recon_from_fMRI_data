# ssfmri2im

----------
## Basic usage:
1. Download "Generic Object Decoding" dataset (by Kamitani Lab)
```
http://brainliner.jp/data/brainliner/Generic_Object_Decoding
```

2. Download the images used in the experiment
```
http://image-net.org/download
```
For me it was easiest to download the relevant winds

more instructions here:
```
https://github.com/KamitaniLab/GenericObjectDecoding
```
3. Change Paths in config_file.py to match your file locations, specifically:
   - imagenet_wind_dir - point to the Imagenet image directory
   - external_images_dir - external iamges to be used in training, we use the Imagenet(2011) validation images
   - kamitani_data_mat - mat file containing the fMRI activations
4. Run run file, this will do the following:
   - create a NPZ file with the images used in the experiment.
   - Train an Encoder model and save it's weights
   - Train the full model and save the reconstructed images

example output: \
<img src="./collage.jpeg" width="250" height="250">






