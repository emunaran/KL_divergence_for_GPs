import numpy as np
from scipy.stats import norm
from utils.utils import kl_divergence_discrete


def discrete_kl_for_gps(mus_list: list, sigmas_list: list, upper_limit: float, lower_limit: float, sample_step: float = 0.001) -> float:

    """

    this function calculating Kullback-Leibler (KL) divergence of two Gaussian processes (GPs) based their computed
    means and standard deviations

    :param mus_list: list of means tuples computed by the GP
    :param sigmas_list: list of std tuples computed by GP
    :param upper_limit: the upper limit of the random sampling
    :param lower_limit: the lower limit of the random sampling
    :param sample_step: the sample step size of the random sampling
    :return: KL divergence score
    """
    x = np.arange(-lower_limit, upper_limit, sample_step)
    kl_scores = []
    for mus, sigmas in zip(mus_list, sigmas_list):
        # sampling from the first GP
        p = norm.pdf(x, mus[0], sigmas[0])
        # sampling from the second GP
        q = norm.pdf(x, mus[1], sigmas[1])
        # insert the KL score to a list
        kl_scores.append(kl_divergence_discrete(p, q))

    # averaging over all the KL scores to get the final KL score of the two GPs
    score = np.mean(kl_scores)

    return score
