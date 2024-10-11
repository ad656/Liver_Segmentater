import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load the NIfTI file
file_path = 'path_to_your_file.nii'
img = nib.load(file_path)

# Get the data from the NIfTI file
data = img.get_fdata()

# Display the middle slice of the 3D image (you can adjust this as needed)
slice_index = data.shape[2] // 2  # Middle slice index
slice_data = data[:, :, slice_index]

# Plot the slice
plt.imshow(slice_data.T, cmap='gray', origin='lower')
plt.title(f'Slice {slice_index}')
plt.axis('off')
plt.show()
