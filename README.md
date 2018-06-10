# Seam Carving for Content-Aware Image Resizing

## Summary
Resizing the image using seam-carving technique.  

## Implementation
Seam Carving is a technique that allows for content-aware image resizing for both reduction and expansion of an image. By repeatedly carving out or inserting seams in one direction, it is possible to change the aspect ratio of the image. A seam is an optimal path in an image (ideally one which has the lowest energy). We have used the dual gradient image energy function in order to calculate the energy values for pixels. The selection and order of seams protects the content of the image, thus causing minimum distortion. Optimal seam identification is done using dynamic programming.

## Results

Resized image after running 100 iterations on the image.

### Before
![SeamCarving1](https://github.com/anish03/image-seam-carving/blob/master/TestImages/dolphinstretch2.png)

### After
![SeamCarving2](https://github.com/anish03/image-seam-carving/blob/master/TestImages/test.png)


## Contributors

* Neeraj Kulkarni - [xOmega](https://github.com/xOmega)

* Anish Narkhede - [anish03](https://github.com/anish03)

## References

http://graphics.cs.cmu.edu/courses/15-463/2007_fall/hw/proj2/imret.pdf

