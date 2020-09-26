import numpy as np


def kl_divergence_discrete(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))
