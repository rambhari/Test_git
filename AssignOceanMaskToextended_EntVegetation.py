"""
        This program is aimed to prepare the boundary condition for changing the land use land cover or the anthropogenic experiments for Nile River basin.

        - Ram Singh
"""
import cdms2, vcs, cdutil, genutil, xmgrace, MV2, os, time
import EzTemplate
#
cdms2.setNetcdfShuffleFlag(0)
cdms2.setNetcdfDeflateFlag(0)
cdms2.setNetcdfDeflateLevelFlag(0)
# Specifying the parent input file path
#
Veg_PFT_ID = ['drought_br', 'ever_nd_late', 'decid_nd', 'ever_br_early', 'c3_grass_per', 'cold_br_late', 'bare_bright', 'c3_grass_ann', 'bare_dark', 'arid_shrub', 'cold_br_early', 'c3_grass_arct', 'ever_br_late', 'crops_herb', 'ever_nd_early', 'cold_shrub', 'c4_grass', 'crops_woody']
#
InputFile_Home_Path = '/discover/nobackup/projects/giss/prod_input_files/'
##GISS_VegetationFile = 'V144x90_EntMM16_lc_max_trimmed_scaled_nocrops.ext.nc'
GISS_VegetationFile ='V144x90_EntMM16_height_trimmed_scaled_ext.nc'
Veg_fin = cdms2.open(InputFile_Home_Path + GISS_VegetationFile)
TOPOFile = 'Z2HX2fromZ1QX1N.BS1.nc'
GIC_Maskfin = cdms2.open(InputFile_Home_Path +TOPOFile)
mvar=GIC_Maskfin('focean')
mvar = MV2.masked_where(mvar==1.0, mvar)
GISSOceanMask = MV2.getmask(mvar)
#
Output_HomePath = '/discover/nobackup/rsingh7/GISS_Vegetation_Data/GISSEntVegtn_Masked/'
#
##OutFile = 'V144x90_EntMM16_lc_max_trimmed_scaled_nocrops.ext_Masked.nc'
OutFile = 'V144x90_EntMM16_height_trimmed_scaled_ext_Masked.nc'
#
if not os.path.isdir(Output_HomePath): os.makedirs(Output_HomePath)
#
out_f = cdms2.open(Output_HomePath+OutFile, 'w')
#
for var in Veg_PFT_ID:
	#
	VegTn = Veg_fin('hgt_'+var)
	#
	VegTn.mask = GISSOceanMask
	#
	out_f.write(VegTn)
	#
#
out_f.close()
