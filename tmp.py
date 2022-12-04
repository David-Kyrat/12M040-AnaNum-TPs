import numpy as np
from numpy import float64, ndarray, poly1d
from scipy.special import legendre
from typing import Any


def doR(x, f):
    y = x
    f(y)
    return y


k = 6
(((x := np.zeros(k))[-2]) = 0)
x

