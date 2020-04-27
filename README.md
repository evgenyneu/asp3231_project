# ASP3231 project for Maria and Evgenii

## Setup

* Download the project

```
git clone https://github.com/evgenyneu/asp3231_project.git
```

* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

* Create a Conda environment.

```
conda create --name obsastro2020 python=3.7
```

* Activate the environment:

```
conda activate obsastro2020
```

* Install Python libraries listed in `requirements.txt` file:

```
pip install -r requirements.txt
```

## Cleaning up

When you finished running the code, stop Jupyter with <Ctrl-C> and remove the Conda environment:

```
conda deactivate
conda env remove -n obsastro2020
```

## Data reduction


1. [Reduce Bias and Dark frames](code/010_bias_and_dark)


### Reduce flat frames

Run `code/020_flat`. It will create reduced flats in `data/flats/reduced` directory.

### Reduce individual science frames

Run `code/030_science_frames/science_frames.ipynb`. It will create reduced science images in `data/reduced` directory.
