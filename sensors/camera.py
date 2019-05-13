from io import BytesIO
from time import sleep

import picamera
from imageio import imwrite
from numpy import array
from PIL import Image


class Camera:
    def convert_image(self, img_array, threshold: int, mean: int):
        """Convert image into a binary representation of black/white."""
        arr = (img_array > threshold).mean(1)
        arr = arr > mean
        return arr

    def take_picture(self):
        """Take a picture with the default Pi camera."""
        stream = BytesIO()

        with picamera.PiCamera() as camera:
            camera.resolution = (640, 360)
            camera.framerate = 24
            sleep(2)
            camera.capture(stream, format="png")
            stream.seek(0)

        image = Image.open(stream).convert("L")
        arr = array(image)
        return arr

    def write_picture(self, name: str, image):
        """Write a picture to a file."""
        imwrite(name, image)

    def write_binary_picture(self, image, name: str, height: int):
        """Create and write a binary (black/white only) image."""
        out = Image.new("1", (height, 1))
        pixels = out.load()
        for (i, x) in enumerate(image):
            pixels[i, 0] = 1 if x else 0
        out.save(name)


c = Camera()
image = c.take_picture()
c.write_picture("pi.png", image)
c.write_binary_picture(c.convert_image(image, 80, 0.5), "stripe.png", 360)

oldImage = Image.open("Original.png")
oldImage = oldImage.convert("L")
oldImage = array(oldImage)
c.write_picture("Original2.png", oldImage)
c.write_binary_picture(c.convert_image(oldImage, 80, 0.5), "stripeOld.png", 360)
