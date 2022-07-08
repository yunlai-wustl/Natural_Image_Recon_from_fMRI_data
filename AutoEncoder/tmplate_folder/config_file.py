
import os
import glob
GPU_ID = "0"

#####################  PATHS  ######################################
imagenet_dir = "/scratch/c.yunlai/fMRI_recon/ssfmri2im-master/image_net/"
imagenet_wind_dir = os.path.join(imagenet_dir,"wind/")
external_images_dir =  os.path.join(imagenet_dir,"validation_IMG/")

project_dir = "/scratch/c.yunlai/fMRI_recon/ssfmri2im-master"
images_npz = os.path.join(project_dir,"data/images_112.npz")
kamitani_data_format = True
kamitani_data_mat = glob.glob("KamitaniData/*.mat")
kamitani_data_mat =kamitani_data_mat[0]
caffenet_models_weights = os.path.join(project_dir,"Models/imagenet-caffe-ref.mat")
results  = "results/"


encoder_weights = "Models/encoder.hdf5"
retrain_encoder = False
decoder_weights = None

encoder_tenosrboard_logs = None
decoder_tenosrboard_logs = None


#####################  pretrained mat conv net weights (alexnet)  ######################################

DOWNLOAD_LINK = 'http://www.vlfeat.org/matconvnet/models/imagenet-caffe-ref.mat'
FILENAME = 'imagenet-caffe-ref.mat'
EXPECTED_BYTES = 228031200

##################### PARAMS ######################################

image_size = 112
