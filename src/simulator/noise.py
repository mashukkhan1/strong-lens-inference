import numpy as np

def add_cosmic_noise(clean_image, scale=1.5):
    """Adds standard Gaussian background noise to a simulated image."""
    noise = np.random.normal(loc=0, scale=scale, size=clean_image.shape)
    return clean_image + noise