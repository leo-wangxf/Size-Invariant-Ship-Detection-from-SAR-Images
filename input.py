import rasterio

fp = r"C:\\Users\super\Data\S1A_IW_GRDH_1SDV_20191114T012623_20191114T012652_029900_036941_7320\S1A_IW_GRDH_1SDV_20191114T012623_20191114T012652_029900_036941_7320.SAFE\\measurement\s1a-iw-grd-vh-20191114t012623-20191114t012652-029900-036941-002.tiff"

# Opening the raster image

raster = rasterio.open(fp)
type(raster)