
### 2024/12/18
Repository locked to air-LUSI team only access during review for official data release with no use restrictions.  
Added DOI to NetCDF file. 

### 2024/10/11
Calibration report issued. See pdf in documentation directory.

### 2024/9/30
Re-ran code, now considered beta version. Approval for wide-release imminent. Matches calibration report. 

### 2024/8/10
- wavelength scale now entirely in vacuum.
- LSFs/SRFs regridded on vacuum scale at denser grid to match TSIS/HSRS-2 grid adopted by LSICS. The pipeline code at NIST uses in-air for historical reasons, and the data are converted in post processing.
- A few additional sources of Type B errors were added. See Issue [https://github.com/usnistgov/air-lusi/issues/1].
