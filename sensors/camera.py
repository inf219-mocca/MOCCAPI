from io import BytesIO
from time import sleep

import picamera
from imageio import imwrite
from numpy import array
from PIL import Image


def write_binary_picture(image, name: str, height: int):
    """Create and write a binary (black/white only) image."""
    out = Image.new("1", (height, 1))
    pixels = out.load()
    for (i, x) in enumerate(image):
        pixels[i, 0] = 1 if x else 0
    out.save(name)


def write_picture(name: str, image):
    """Write a picture to a file."""
    imwrite(name, image)


def take_picture(width: int, height: int):
    """Take a picture with the default Pi camera."""
    stream = BytesIO()

    with picamera.PiCamera() as camera:
        camera.resolution = (width, height)
        camera.framerate = 24
        sleep(2)
        camera.capture(stream, format="png")
        stream.seek(0)

    image = Image.open(stream).convert("L")
    arr = array(image)
    return arr


def convert_image(img_array, threshold: int, mean: float):
    """Convert image into a binary representation of black/white."""
    arr = (img_array > threshold).mean(1)
    arr = arr > mean
    return arr
