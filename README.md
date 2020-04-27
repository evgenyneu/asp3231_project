# ASP3231 project for Maria and Evgenii

## Setup

Download the project

```
git clone https://github.com/evgenyneu/asp3231_project.git
```

## Data reduction


1. [Reduce Bias and Dark frames](code/010_bias_and_dark)


### Reduce flat frames

Run `code/020_flat`. It will create reduced flats in `data/flats/reduced` directory.

### Reduce individual science frames

Run `code/030_science_frames/science_frames.ipynb`. It will create reduced science images in `data/reduced` directory.
