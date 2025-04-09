# Air-LUSI Data Repository

## Details
This repository contains data on lunar irradiance and reflectance based on measurements by the air-LUSI instrument. The instrument is described in [Grantham, *et al*, 2022](https://doi.org/10.1088/1361-6501/ac5875) and is a joint NASA, NIST, USGS, University of Maryland Baltimore County, McMaster University project. The NIST-hosted home for the data is [https://data.nist.gov/pdr/lps/ark:/88434/mds2-3397](https://data.nist.gov/pdr/lps/ark:/88434/mds2-3397). 

Before use, please review:
- Any notebooks in the [examples directory](https://github.com/usnistgov/air-lusi/tree/main/example_usage). Even if you are not a notebook or Python user, this is informative and you can view the notebooks and plots within GitHub.
- The [issues page](https://github.com/usnistgov/air-lusi/issues)


Users of the repository should have a relatively recent python installation with the ability to use Jupyter notebooks. See the `pyproject.toml` file in the root directory for required packages. 


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
Research Data and Computing Office  
stephen.maxwell@nist.gov  
