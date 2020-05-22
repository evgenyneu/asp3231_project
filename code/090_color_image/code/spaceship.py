# Import the libraries
import numpy as np
import astropy
import ccdproc
from ccdproc import CCDData, Combiner
from astropy import units as u
from astropy.stats import sigma_clipped_stats
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from photutils import centroid_com, centroid_1dg, centroid_2dg
from photutils import CircularAperture
from photutils import aperture_photometry
from photutils import DAOStarFinder
from scipy.ndimage import shift


# Open the image
image = CCDData.read("NGC_3201_V_median_60.0s.fits")
mean, median, std = sigma_clipped_stats(image.data, sigma=3.0, maxiters=5)

# Locate the stars
daofind = DAOStarFinder(fwhm=10.0, threshold=5.*std)
sources = daofind(image.data - median)

# Create apertures at star positions
positions = (sources['xcentroid'], sources['ycentroid'])
apertures = CircularAperture(positions, r=20.0)

# Measure fluxes
phot_table = aperture_photometry(image.data - median, apertures)
