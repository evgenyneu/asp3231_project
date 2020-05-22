# ASP3231 project by Maria and Evgenii

## Setup

Follow [setup instructions](setup.md) if you run this code for the first time.

## Running the code

To run the project code, do the following steps in the specified order:

1. Reduce Bias and Dark frames: [code/010_bias_and_dark](code/010_bias_and_dark)

1. Reduce Flat frames: [code/020_flat](code/020_flat).

1. Reduce individual science frames: [code/030_science_frames](code/030_science_frames).

1. Shift individual science frames: [code/040_shift](code/040_shift).

1. Scale and combine science frames: [code/050_scaling_and_combining](code/050_scaling_and_combining).

1. Calculate magnitudes: [code/060_find_magnitudes](code/060_find_magnitudes).

1. Find age/distance by fitting Girardi isochrones (Evgenii): [code/070_fit_isochrones](code/070_fit_isochrones).

1. Find age/distance by fitting Girardi isochrones (Maria): [code/080_science](code/080_science).

1. Make color image of the galaxy: [code/090_color_image](code/090_color_image).


## The unlicense

This work is in [public domain](https://github.com/evgenyneu/tarpan/blob/master/LICENSE).
