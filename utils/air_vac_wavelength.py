import numpy as np


def n_air(l: float) -> float:
    """Edlen's formula from https://iopscience.iop.org/article/10.1088/0026-1394/2/2/002/pdf

    Parameters
    ----------
    l : float
        wavelength in nm

    Returns
    -------
    float
        index of refraction in air
    """
    sigma = 1 / (1e-3 * l)
    a = 8342.13
    b = 2406030
    c = 15997
    d = a + b * (130 - sigma**2) ** -1 + c * (38.9 - sigma**2) ** -1
    n = 1e-8 * d + 1
    return n


wlvac = np.linspace(200, 1150, 10000)
wlair = wlvac / n_air(wlvac)

vac2air = lambda x: x / n_air(x)
air2vac = lambda x: np.interp(x, wlair, wlvac)
