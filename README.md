# ASP3231 project for Maria and Evgenii

## Data reduction

### Reduce Bias and Dark frames

Run `code/010_bias_and_dark/Bias and Dark.ipynb` to create bias_median.fits and dark_median.fits files.

### Reduce flat frames

Run `code/020_flat`. It will create reduced flats in `data/flats/reduced` directory.

### Reduce individual science frames

Run `code/030_science_frames/science_frames.ipynb`. It will create reduced science images in `data/reduced` directory.
