# Shift images

* Change directory:

```
cd code/040_shift
```

* Open [shift.ipynb](shift.ipynb) notebook in Jupyter:

```
jupyter notebook science_frames.ipynb
```
* Run all code by selecting `Kernel > Restart & Run All` menu.

* The program will create reduced science images in [data/reduced](data/reduced) directory.

## Shift check video

The following video shows shifted images from March 9 archive:

[https://youtu.be/Z9XV4Pqw8lE](https://youtu.be/Z9XV4Pqw8lE)


### Using shifting settings

We used the `shift` function to shift the images:

```Python
shifted = shift(image, yx_shift, order=0, mode='constant', cval=np.median(image))
```

The difference between `order=0` and `order=1` parameter values are shown on Fig. 1 and 2.

![Shifting with order=0](https://github.com/evgenyneu/asp3231_project/raw/master/code/040_shift/images/shifting_order_0.gif)

Figure 1: Shifting the images using `order=0` setting. We can see that image is simply translated by integer number of pixels, so the brightness of pixels is not changed. This is the setting that we ended up using, because we don't want shifting to affect pixel values.


![Shifting with order=1](https://github.com/evgenyneu/asp3231_project/raw/master/code/040_shift/images/shifting_order_1.gif)

Figure 2: Shifting the images using `order=1` setting. This setting allows to shift the image by non-integer number of pixels and uses spline interpolation of order 1 to calculate the pixel value. You can see that this results in changes in pixel values, this is not ideal.
