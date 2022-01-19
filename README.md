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

## Extending this framework to new datasets, using existing classifications

The point of these scripts is to allow us to make ecologically or model-relvant annotations of taxonomy and/or ASV sequence types (probably both will be needed in the end). To this end, I've written up a couple of very basic python scripts to automate this.

### Input for scripts

One of the following:

1. A TSV file with the first column representing the taxonomy string of interest, and several columns afterwards that indicate some ecologically-relevant parameters and references (this format is ad-hoc at the moment and can be changed or added to as we see fit). For examples, check the directory `model-classification/plain-taxonomy/`.

2. A TSV file with the first column representing the ASV hashes of the organisms you've classified manually. For an example of this, read on.

How to use these python scripts:

First off, make sure you're in an environment with `python3` installed (the `jupyter-env` specified above should work well).

A) Using just taxonomy:

```
scripts/classify-using-prev-data-plain-taxonomy-input.py model-classification/plain-taxonomy/GA03-classifications-based-on-GP13.tsv example-data/210420_GA03_proportions_reordered.tsv > 210420_GA03_proportions_reordered.model-classifications.tsv
``` 

This takes the taxonomy information contained in the file in the `model-classification/plain-taxonomy/` folder and appends this information to the ASV table you specify as input, creating an amended ASV table with those new columns added in between the `taxonomy` column and the ASV counts (i.e. the file `210420_GA03_proportions_reordered.model-classifications.tsv`).

B) Using the ASV hashes (which has clear advantages since we could make a truly customized taxonomy for misclassified "corner cases", e.g. some cyanobacteria that might be incorrectly classified by `qiime2`):

First, let's make a ASV directory from the output file we just created:

```
cut -f 1-5 210420_GA03_proportions_reordered.model-classifications.tsv > model-classification/GA03-GP13_classifications.tsv 
```

Now the idea would be to use this classification (or the previous taxonomy-only one) for new cruise data. If you want to use the data you just produced, you just need to run the other script, e.g.:

```
scripts/classify-using-prev-data.py model-classification/GA03-GP13_classifications.tsv <your new table>.tsv > annotated.tsv
```

At this stage you'll have a table that follows the custom taxonomic annotations (either from just taxonomy strings or ASV hashes).

The next steps I haven't automated at all. I just did it in excel to generate the data used in the folder `plot-input`.
