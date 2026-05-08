"""
This module provides a blur function that performs a simple blur on an image by
averaging a pixel with its immediate neighbors.  It also includes a small
program to load an image, blur it, and save the blurred version.  The
implementation follows the algorithm described in Chapter 8 of *Fundamentals of
Python* slides【348052005562421†L964-L999】.  A pixel is replaced by the average
of itself and its left, right, top and bottom neighbors.  Edges are left
untouched to avoid indexing outside the image bounds.
"""

from functools import reduce
from image_lib import Image


def blur(image):
    """Build and return a new blurred copy of the argument image.

    The blur algorithm computes the average of the color components of a pixel
    and its four immediate neighbors (left, right, top, bottom).  This
    implementation is adapted from the pseudocode in the textbook slides【348052005562421†L964-L999】.
    A new image is returned; the original image is not modified.

    :param image: An Image object representing the original picture.
    :return: A new Image object containing the blurred version.
    """
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)

    # Clone the original so we can write to the result without affecting the input.
    new = image.clone()
    width = image.getWidth()
    height = image.getHeight()

    # Skip the edges (y=0 and y=height‑1, x=0 and x=width‑1) because they don't
    # have neighbors on all sides.
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Gather the current pixel and its four neighbors
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)
            sums = reduce(tripleSum, [oldP, left, right, top, bottom])
            averages = tuple(map(lambda val: val // 5, sums))
            new.setPixel(x, y, averages)
    return new


def main():
    # Load the original image.  The GIF file must exist in the same directory
    # as this script.  We specify just the filename so that Image finds it
    # relative to this file's location.
    my_image = Image("smokey.gif")
    # Apply the blur algorithm
    blurred = blur(my_image)
    # Save the blurred image as a PNG to support more colors.  The filename is
    # chosen to indicate the image has been blurred.
    blurred_filename = "smokey_blurred.png"
    blurred.save(blurred_filename)
    # Optionally display both images for visual verification.  Comment out
    # display calls when running automated tests.
    # my_image.draw()
    # blurred.draw()


if __name__ == "__main__":
    main()