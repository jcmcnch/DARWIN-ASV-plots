# DARWIN-ASV-plots

## Preamble

These are scripts for comparing and plotting phytoplankton types between the DARWIN model and ASV data generated with the 515Y/926R primer pair. At present, the comparison uses taxonomy strings that come from SILVA138 / PR2 4.12.0 with some manual curation. In the future, it will be desirable to link these functional annotations to specific sequence types (i.e. ASVs or reference full-length 16S genes) so the pipeline can be more reproducible and extensible.

The plotting uses **jupyter notebooks** to allow for interactive tweaking of plotting parameters, so it's best to install it on your local machine or use it remotely through something like a **jupyter-hub** installation.

## Setup

1. Download miniconda to your system (follow instructions [here](https://docs.conda.io/en/latest/miniconda.html#linux-installers)).

2. Install mamba into your base environment, create a new jupyter environment, activate, and install software dependencies needed for plotting and data parsing:

```
conda install -c conda-forge mamba
conda create --name jupyter-env
conda activate jupyter-env
mamba install -c conda-forge jupyterlab 
mamba install -c conda-forge seaborn
```

3. Clone the repository and enter the directory where files are stored:

```
#make a convenient place to store the repository, e.g.:
mkdir ~/github ; cd ~/github
git clone git@github.com:jcmcnch/DARWIN-ASV-plots.git
cd DARWIN-ASV-plots
```

4. Open jupyter with the command `jupyter-notebook`. This should open an interactive window in your default web browser that shows the files contained in the repository. Click on the "ipynb" file to open the interactive plotting interface. If it asks about a python3 kernel, just click "OK".

5. Test whether the plots work by clicking on one of the cells, and then pressing "CTRL-Enter" on your keyboard to run the code in that cell. It should generate a subfolder with today's date that contains plots.
