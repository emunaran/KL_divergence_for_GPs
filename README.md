# Gaussian Process KL Divergence Calculator

This repository contains a utility for calculating the Kullback-Leibler (KL) divergence over the distribution of functions represented by Gaussian Processes (GPs). The `kl_divergence_gps` module provides a function `discrete_kl_for_gps` for this purpose. This utility can be particularly useful in Bayesian optimization, probabilistic modeling, and various machine learning tasks where understanding the divergence between distributions is important.

## Installation
To use this utility, follow these steps:
1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. You can then import the `discrete_kl_for_gps` function from `kl_divergence_gps` module and use it in your Python code.

## Usage
Here's an example of how to use the `discrete_kl_for_gps` function:
```python
from kl_divergence_gps import discrete_kl_for_gps

def main():
    gps_means = [(3.2, 3.1), (3.6, 2.4), (3.5, 4.1), (2.2, 2.5)]
    gps_stds = [(1.2, 1.4), (0.5, 0.7), (1.8, 1.9), (1.3, 1.35)]

    kl_divergence = discrete_kl_for_gps(mus_list=gps_means, sigmas_list=gps_stds, upper_limit=10, lower_limit=10)
    print(kl_divergence)

if __name__ == '__main__':
    main()
```
In this example, `gps_means` and `gps_stds` are lists of tuples representing the means and standard deviations of Gaussian Processes respectively. `upper_limit` and `lower_limit` define the upper and lower limits of the calculation range. The function `discrete_kl_for_gps` returns the KL divergence over the specified range.

## Contributing
Contributions to this repository are welcome. If you have any suggestions, bug fixes, or feature implementations, please feel free to open an issue or submit a pull request.

## Contact
For any questions or concerns, you can contact the repository owner [Ran Emuna](https://www.linkedin.com/in/ran-emuna-ba902579/).

## Acknowledgments
This utility is inspired by the need for efficient computation of KL divergence over Gaussian Processes, used in the papers ["Deep Reinforcement Learning for Human-Like Driving Policies in Collision Avoidance Tasks of Self-Driving Cars"](https://arxiv.org/abs/2006.04218) and ["Example-guided learning of stochastic human driving policies using deep reinforcement learning"](https://link.springer.com/article/10.1007/s00521-022-07947-2), concerning with probabilistic modeling, and deep reinforcement learning.

Thank you for using this utility! We hope it proves helpful in your projects and research endeavors.
