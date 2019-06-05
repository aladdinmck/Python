<<<<<<< HEAD
# I've created this file inorder
# to explore Scipy briefly

# Python script using Scipy 
# for image manipluation

from scipy.misc import imread, imsave, imresize

# Read a JPEG image into a numpy array 
img = imread('cat.jpg') # path of the image 
print(img.dtype, img.size)

# Tinting the image
img_tint = img * [1, 0.45, 0.3]

# Saving the tinted image
imsave('cat_tinted.jpg', img_tint) 

# Resizing the tinted image to be 300 x 300 pixels
img_tint_resize = imresize(img_tint, (300, 300))

# Saving the resized tinted image
imsave('cat_tinted_resize.jpg', img_tint_resize)
=======
# Python script using Scipy  
# for image manipulation 
  
from scipy.misc import imread, imsave, imresize 
  
# Read a JPEG image into a numpy array 
img = imread('cat.jpg') # path of the image 
print(img.dtype, img.shape) 
  
# Tinting the image 
img_tint = img * [1, 0.45, 0.3] 
  
# Saving the tinted image 
imsave('cat_tinted.jpg', img_tint) 
  
# Resizing the tinted image to be 300 x 300 pixels 
img_tint_resize = imresize(img_tint, (300, 300)) 
  
# Saving the resized tinted image 
imsave('cat_tinted_resized.jpg', img_tint_resize) 
>>>>>>> 0c931757d53680396fa67280d6b527ca93ad188b
