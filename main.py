import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.filters import sobel

# Read image
image = plt.imread("./images/deer.jpg")

# Convert image to grayscale
gray_image = color.rgb2gray(image)

# Apply edge detection filters
sobel_image = sobel(gray_image)

# Save image
plt.imsave("./images/deer_edges.jpg", sobel_image, cmap = "gray")

# Plot images
def plot_image_grid(images, titles, color_maps):
    figure = plt.figure()
    height = len(images)
    width = len(images[0])
    for r in range(height):
        for c in range(width):
            plot = figure.add_subplot(height, width, r * width + c + 1)
            if color_maps[r][c]:
                plot.imshow(images[r][c], cmap = color_maps[r][c])
            else:
                plot.imshow(images[r][c])
            plot.title.set_text(titles[r][c])
    plt.show()

plot_image_grid([[image, sobel_image]], [["Original Image", "Sobel Edge Detection"]], [[None, "gray"]])
    

