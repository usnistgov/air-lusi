# Air-LUSI Data Repository

This repository contains data on lunar irradiance and reflectance based on measurements by the air-LUSI instrument. The instrument is described in [Grantham, *et al*, 2022](https://doi.org/10.1088/1361-6501/ac5875) and is a joint NASA, NIST, USGS, University of Maryland Baltimore County, McMaster University project. The data are provided in a pre-publication state and small changes may be made as the review process progresses. 

Before use, please review:
- Any notebooks in the [examples directory](https://github.com/usnistgov/air-lusi/tree/main/example_usage). Even if you are not a notebook or Python user, this is informative and you can view the notebooks and plots within GitHub.
- The [issues page](https://github.com/usnistgov/air-lusi/issues)

Note that as of 7/17/24, the wavelength scale is "in air," due to the data product distributed by the NIST Stray Light Characterization Facility. There is an issue in the GitHub tracker and the scale will be later changed to "vacuum." The conversion is straightforward, but we'd like to distribute bandpasses with evenly spaced sampling, which means that there is a bit of reprocessing to do. 

Users of the repository should have a relatively recent python installation with the ability to use Jupyter notebooks. See the `requirements.txt` file in the root directory for required packages. 


The repository has three main folders
 - `data` contains raw netCDF files containing air-LUSI data. The files are separated by campaign, and for now only a campaign from 2022 is available.
 - `instrument_characterization` contains auxilliary instrument data (line shapes) necessary to understand the data.
 - `example_usage` contains Jupyter Notebook files that provide guidance on how to use the data.


The repository maintainers are:

John Woodward  
NIST Physical Measurement Laboratory  
Sensor Science Division  
Remote Sensing Group  
john.woodward@nist.gov  

Stephen Maxwell  
NIST Physical Measurement Laboratory  
Sensor Science Division  
Remote Sensing Group  
stephen.maxwell@nist.gov  
