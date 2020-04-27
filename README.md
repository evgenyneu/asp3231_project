# ASP3231 project by Maria and Evgenii

## Setup

Follow [setup instructions](setup.md) if you run this code for the first time.

## Running the code

To run the project code, do the following steps in the specified order:

1. Reduce Bias and Dark frames: [code/010_bias_and_dark](code/010_bias_and_dark)

1. Reduce Flat frames: [code/020_flat](code/020_flat).

1. Reduce individual science frames: [code/030_science_frames](code/030_science_frames).


### Reduce individual science frames

Run `code/030_science_frames/science_frames.ipynb`. It will create reduced science images in `data/reduced` directory.
