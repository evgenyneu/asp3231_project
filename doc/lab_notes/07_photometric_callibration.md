# Photometric calibration


1. Pick four bright blue stars (using Aladin https://aladin.u-strasbg.fr/AladinLite/) present both in science and photometric nights: stars A, B, C, D etc.

2. Find m2 of each four stars using photometric equations from [05_data_summary.pdf](https://github.com/evgenyneu/asp3231_project/blob/master/doc/lab_notes/05_data_summary.pdf): m2_A, m2_B etc. Do this for at least three filter bands.

3. Now, in science image, find magnitudes m1 all other other stars using star A as a reference star using equation

> m1 = m2_A - 2.5 log(f1/f2_A),

where
    * m2_A is magnitude of star A found in Step 2 from photometric image.
    * f1, f2_A are measured fluxes of any star and star A in NON-photometric image.

4. Find m1 using other reference stars B, C and D. Then calculate the average magnitude m1.


## Questions

* What is considered a bright blue star?

* Our photometric and non-photometric night images are rotated, hard to locate same stars.
