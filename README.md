# OBservational astronomy project

This is a project Maria Funcich and I did in Observational Astronomy ASP 3231 unit in Monash university. In this project we were given images of NGC 3201 globular cluster (Fig. 1) made using Monash eleven inch telescope. Our goal was to reduce the images, calculate magnitudes of the stars, plot color-magnitude diagrams and estimate the distance to the cluster, as well as its age. This work was only possible because of the help from our teachers: Vaishali Parkash, Madhooshi Senarath, Michael Brown and Duncan Galloway. 

![False color image of NGC 3201 globular cluster](https://raw.githubusercontent.com/evgenyneu/asp3231_project/master/code/090_color_image/images/spaceshit.jpg)

Figure 1: False color image of NGC 3201 globular cluster, as viewed from a cockpit of an imperial combat vessel. The cockpit image is from [pngguru.com](https://www.pngguru.com/free-transparent-background-png-clipart-nprbv) web site.

## Setup

Follow [setup instructions](setup.md) if you run this code for the first time.

## Running the code

Follow this steps to run the project code:

1. Reduce Bias and Dark frames: [code/010_bias_and_dark](code/010_bias_and_dark)

1. Reduce Flat frames: [code/020_flat](code/020_flat).

1. Reduce individual science frames: [code/030_science_frames](code/030_science_frames).

1. Shift individual science frames: [code/040_shift](code/040_shift).

1. Scale and combine science frames: [code/050_scaling_and_combining](code/050_scaling_and_combining).

1. Calculate magnitudes: [code/060_find_magnitudes](code/060_find_magnitudes).

1. Verify magnitudes: [code/065_verify_magnitudes](code/065_verify_magnitudes).

1. Find age/distance by fitting Girardi isochrones (Evgenii): [code/070_fit_isochrones](code/070_fit_isochrones).

1. Find age/distance by fitting Girardi isochrones (Maria): [code/080_science](code/080_science).

1. Make color image of the galaxy: [code/090_color_image](code/090_color_image).


## The unlicense

This work is in [public domain](https://github.com/evgenyneu/tarpan/blob/master/LICENSE).
