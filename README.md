### Introduction
This project reproduced the base model of the paper ["Context-adaptive Entropy Model for End-to-end Optimized Image Compression"](https://arxiv.org/abs/1809.10452).

#####Team Name : HeySiri

## Installation

This project can only run on Linux and Mac OS, not on Windows, because the tensorflow compression package cannot be installed in the Windows environment.

Python  > 3.6

Run the below command to install the tensorflow package

```$xslt
pip install tensorflow==1.15
```

Run the below command to install the tensorflow-compression package
```$xslt
pip install tensorflow_compression
```


### Training model

```$xslt
python model.py --verbose train --train_glob="pictures/*.jpg"
```

### compress/decompress an image
If you want to compress or decompress an image, the simplest way is to run test.py

Or 


```
python model.py --checkpoint_dir train compress  pictures/image4.jpg compressed.tfci

```

```$xslt
python model.py decompress compressed.tfci reconstruction.png

```
