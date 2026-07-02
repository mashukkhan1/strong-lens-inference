import numpy as np


def sample_priors(num_samples=100):
    """Samples random physical configurations for the lenses (Prior Distribution)."""
    # Einstein radius: how massive/heavy the foreground galaxy is
    theta_E = np.random.uniform(0.6, 1.8, num_samples)

    # Background galaxy offset positions relative to center
    center_x = np.random.uniform(-0.2, 0.2, num_samples)
    center_y = np.random.uniform(-0.2, 0.2, num_samples)

    # Pack them as rows of parameters: Shape (num_samples, 3)
    return np.column_stack((theta_E, center_x, center_y))