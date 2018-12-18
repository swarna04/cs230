# Deep Visual Semantic Embedding Models for Mobile

*Author: Swarna Saraf*

## Requirements

This project uses fastai 1.0.33 which sits on top of PyTorch 1.0. See Developer Install instructions [here](https://github.com/fastai/fastai/blob/master/README.md#installation).

```
git clone https://github.com/fastai/fastai
cd fastai
tools/run-after-git-clone
pip install -e ".[dev]"
```

Note: fastai v1 currently supports Linux only, and requires PyTorch v1 and Python 3.6 or later.

## Task

The project implements a deep visual-semantic model based on Squeezenet 1.1 architecture and trained with fastText word vectors. The model takes in image input and outputs a 300-D image feature vector. Using nmslib, an efficient cross-platform similarity search, the output feature vector is used for (1) Image To Image: Searching similar Images in model predictions, (2) Image to Text: Predicting Label for an image based on nearest fastText word vector for the label in the dataset (3) Text to Image: Predicting nearest image for an input text label based on nearest image feature vector in model predictions to the fastText word vector for the given label (zero shot).

![Visual-Semantic Embedding Model for Mobile](https://raw.githubusercontent.com/swarna04/cs230/master/images/model_diagram.jpg)

## Download the AWA2 dataset

AWA2, a benchmark dataset for transfer learning algorithms such as zero-shot learning, is used for this project. It consists of 37322 images for 50 animal categories. The images in the dataset are in JPEG format. The dataset (~13 GB) can be downloaded from [here](https://cvml.ist.ac.at/AwA2/).

Here is the structure of the data:
```
path/
    JPEGImages\
        antelope\
            antelope_10001.jpg
            antelope_10002.jpg
            ...
        bobcat\
            bobcat_10001.jpg
            bobcat_10002.jpg
            ...
        .
        .
        .
        ...
    classes.txt
    trainclasses.txt
    testclasses.txt 
```

**classes.txt** contains names of all the 50 animal categories, one per line.
**trainclasses.txt** contains names of 40 animal categories (one per line) to be used for training/ validation.
**testclasses** contains names of 10 animal categories (one per line) to be used for zero-shot tests.

The images are named following `{label}_{id}.jpg` where the label is in `classes.txt`.
Train/valid sets: 30,337 images in the 40 train classes are split 90:10 to create train and valid sets. 
Test set: 6985 images belonging to 10 separate classes are set aside purely for zero-shot tests.

Once the data is downloaded, scripts `copy_awa2.py` and `move_awa2.py` , available in utils folder, are used to move the data into `train` folder and then carve out a `valid` folder based on provided percentage split. The same script can be used to create a test folder with test images. The input parameters for the script need to be updated in the script itself (top section) . For running the scipts, use python command below:

```bash
python [copy_awa2.py | move_awa2.py]
```
Note: A subset of the dataset, `data_samples.zip`, is provided in the repository for reference.

## Code

Jupyter notebook `VisualSemanticModels_Squeezenet1_1.ipynb` contains the code for:
1. Data Augmentation (applying pixel and coordinate transforms to data)
2. Hyperparameter Search
3. Model Training
4. Displaying the results
3. Error Analysis (Stage 1: Confusion Matrix, heatmaps. Stage 2: PCA Analysis)
4. Zero shot tests

**Model training** is performed in two stages:

- Stage 1: A CNN model for multi-classification task is trained for accuracy. Cross entropy loss is used in this stage.
- Stage 2: A visual-semantic model is trained (by throwing away the softmax layers used in Stage 1) to output a 300-D image feature vector. Cosine similarity loss, between image feature vector (300-D model output) and fastText word vector representation for true image label, is used in this second stage.

Note: Models from Stage-1 and Stage-2 training phases for Squeezenet 1.1 (and baseline Resnet34) are provided in the repo as `models.zip`


## Resources

- [Fastai documentation](https://docs.fast.ai/)
- [fastText word vectors](https://fasttext.cc/docs/en/english-vectors.html)
- [PyTorch vision models](https://pytorch.org/docs/stable/torchvision/models.html)
- [NMSLIB](https://github.com/nmslib/nmslib)