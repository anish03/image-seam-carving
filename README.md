# Content-Aware Image Resizing using Seam Carving

## What is Seam Carving?

Seam carving is a technique that allows for content-aware image resizing for both reduction and expansion of an image. By repeatedly carving out or inserting seams in one direction, it is possible to change the aspect ratio of the image. A seam is an optimal path in an image (ideally one which has the lowest energy). We have used the dual gradient image energy function in order to calculate the energy values for pixels. The selection and order of seams protects the content of the image, thus causing minimum distortion. Optimal seam identification is done using dynamic programming.

## Implementation

* Used dual-gradient energy function to calculate the energy for each pixel in the image.
```python
import math

delta_x(x,y) ** 2 = R_x(x,y) ** 2 + G_x(x,y) ** 2 + B_x(x,y) ** 2
delta_y(x,y) ** 2 = R_y(x,y) ** 2 + G_y(x,y) ** 2 + B_y(x,y) ** 2

energy_value(x,y) = math.sqrt((delta_x(x,y) ** 2 + (delta_y(x,y) ** 2))
```
* Used dynamic programming to identify the seam (a connected path of low energy pixels) and then deleted the seam.
* Implemented seam-carving for both, vertical and horizontal image resizing.

![seam-carving](https://github.com/anish03/image-seam-carving/blob/master/Paper/seam.png)

## How to use

### Clone Repository
```
git clone https://github.com/anish03/image-seam-carving.git
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run
```
python seam_drawing.py

```


## Contributors

* Neeraj Kulkarni - [xOmega](https://github.com/xOmega)

* Anish Narkhede - [anish03](https://github.com/anish03)

## References

http://graphics.cs.cmu.edu/courses/15-463/2007_fall/hw/proj2/imret.pdf

