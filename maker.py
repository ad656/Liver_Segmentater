import meshlib.mrmeshpy as mr
import os
from PIL import Image

# Open the TIF file
#image = Image.open('c:/Users/allan/Downloads/tiffs/f_2396.nii_slice_1.tif')

# Display the image
#image.show()


settings = mr.LoadingTiffSettings()

settings.dir = "tiffs"
settings.voxelSize = mr.Vector3f(1,1,7)

volume = mr.loadTiffDir(settings)
iso = 27.0
mesh = mr.gridToMesh(volume, iso)

mr.saveMesh(mesh, ("8379.stl"))