# Computer Vision Utilities

This is an attempt to put together a collection of resources and scripts I put together while working on various 
Computer Vision projects, hope they can help you save your time if you come across tasks these resources can handle.

## Setup

In Terminal

```
git clone https://github.com/r3stl355/cv-utils.git
cd cv-utils
```

I often use Conda environments for my projects but you may have other preferences. Here is an example of setting up
a Conda environment to test the scripts (install Anaconda or Miniconda first).
```
conda create -n cv-utils python=3.7
conda activate cv-utils
pip install -r requirements.txt
```

## Running Jupyter Notebooks

Most of the resources here are implemented as Jupyter Notebooks, with others being just loose script files.

Run a Jupyter server and check the Notebook(s) of interest in the Jupyter instance that opens in your browser (if it
does not launch automatically, just copy/paste the URL shown in the Terminal to your browser address bar)
```
jupyter notebook
```

## Build an RecordIO file from dataset in Pascal VOC format

Check out `voc_2_rec.ipynb` Notebook for details. 

## Shuffle and split an `.lst` file into `train` and `val` files

Script is using fixed split of 90/10, adjust as needed to fit your needs within the script or extend the script to 
accept more parameters. Third parameter determines the shuffle tool to use, e.g. `gshuf` on Mac OS installed as part
of `coreutils`
```
source split_train_val.sh data/voc_like_sample test.lst gshuf
```