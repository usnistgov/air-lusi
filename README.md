# Air-LUSI Data Repository

## Updates

### 2024/12/18
Repository locked to air-LUSI team only access during review for official data release with no use restrictions. 

### 2024/10/11
Calibration report issued. See pdf in documentation directory.

### 2024/9/30
Re-ran code, now considered beta version. Approval for wide-release imminent. Matches calibration report. 

### 2024/8/10
- wavelength scale now entirely in vacuum.
- LSFs/SRFs regridded on vacuum scale at denser grid to match TSIS/HSRS-2 grid adopted by LSICS. The pipeline code at NIST uses in-air for historical reasons, and the data are converted in post processing.
- A few additional sources of Type B errors were added. See Issue [https://github.com/usnistgov/air-lusi/issues/1].

## Details
This repository contains data on lunar irradiance and reflectance based on measurements by the air-LUSI instrument. The instrument is described in [Grantham, *et al*, 2022](https://doi.org/10.1088/1361-6501/ac5875) and is a joint NASA, NIST, USGS, University of Maryland Baltimore County, McMaster University project. The data are provided in a pre-publication state and small changes may be made as the review process progresses. 

Before use, please review:
- Any notebooks in the [examples directory](https://github.com/usnistgov/air-lusi/tree/main/example_usage). Even if you are not a notebook or Python user, this is informative and you can view the notebooks and plots within GitHub.
- The [issues page](https://github.com/usnistgov/air-lusi/issues)


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
