"""
Specifics for bounding box for chosen region and Sentinel2 bands 
"""

REGION_NAME = 'Baltoro_Glacier'
BOUNDING_BOX = {
	"min_lat": 35.55,
    "max_lat": 35.78,
    "min_lon": 76.19,
    "max_lon": 76.60,
}

# Sentinel-2 bands -- RGB and NIR 
SENTINEL2_BANDS = ['B02','B03','B04','B08']

# Target resolution (meters per pixel)
TARGET_RESOLUTION = 10			# Sentinel2 default for the above bands 

# Training tile size (expressed in pixel)
TILE_SIZE = (256,256) 

