from kl_divergence_gps import discrete_kl_for_gps


def main():
    gps_means = [(3.2, 3.1), (3.6, 2.4), (3.5, 4.1), (2.2, 2.5)]
    gps_stds = [(1.2, 1.4), (0.5, 0.7), (1.8, 1.9), (1.3, 1.35)]

    print(discrete_kl_for_gps(mus_list=gps_means, sigmas_list=gps_stds, upper_limit=10, lower_limit=10))


if __name__ == '__main__':
    main()
