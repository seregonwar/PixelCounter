from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# enter the address of the image here
image_path = 'img path'
image = Image.open(image_path)

# Convert image to black and white
image_bw = image.convert('1')  # Convert to black and white

# Convert image to numpy array
image_array = np.array(image_bw)

# Counting the number of black pixels
hole_count = np.sum(image_array == 0)  # Count black pixels (0)

print("Number of holes (black pixels):", hole_count)

# Show the image in black and white
plt.imshow(image_bw, cmap='gray')
plt.title('Immagine in bianco e nero')
plt.axis('on')  # axis switch set on/off
plt.show()
