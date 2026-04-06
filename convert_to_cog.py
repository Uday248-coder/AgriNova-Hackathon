from rio_cogeo.cogeo import cog_translate
from rio_cogeo.profiles import cog_profiles
import os

# paths change karna
ORTHO_INPUT  = r"C:\path\to\orthomosaic.tif"
DEM_INPUT    = r"C:\path\to\digital elevation model.tif"

ORTHO_OUTPUT = r"C:\path\to\orthomosaic_cog.tif"
DEM_OUTPUT   = r"C:\path\to\dem_cog.tif"

profile = cog_profiles.get("deflate")

print("Converting orthomosaic...")
cog_translate(ORTHO_INPUT, ORTHO_OUTPUT, profile, in_memory=False, quiet=False)
print("Done: orthomosaic_cog.tif")

print("Converting DEM...")
cog_translate(DEM_INPUT, DEM_OUTPUT, profile, in_memory=False, quiet=False)
print("Done: dem_cog.tif")
