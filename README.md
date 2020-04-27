# ASP3231 project for Maria and Evgenii

## Setup

Follow [setup instructions](setup.md) if you run this code for the first time.

## Running the code

To run the project code, do the following steps in the specified order:

1. [Reduce Bias and Dark frames](code/010_bias_and_dark)


### Reduce flat frames

Run `code/020_flat`. It will create reduced flats in `data/flats/reduced` directory.

### Reduce individual science frames

Run `code/030_science_frames/science_frames.ipynb`. It will create reduced science images in `data/reduced` directory.
