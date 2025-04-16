import imageio.v3 as iio

filenames = ['example1.png', 'example2.png', 'example3.png'] # change/add the filenames as needed.
images = []

# the images must be in the same directory as this script
# the images must be in the same format (e.g. png, jpg, etc.)
# the images must be in the same size (e.g. 640x480, 800x600, etc.)

for filename in filenames:
    images.append(iio.imread(filename)) 

iio.imwrite('output.gif', images, duration = 0.5, loop=0)