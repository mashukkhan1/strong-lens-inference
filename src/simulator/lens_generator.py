import numpy as np
from lenstronomy.LensModel.lens_model import LensModel
from lenstronomy.LightModel.light_model import LightModel
from lenstronomy.Data.pixel_grid import PixelGrid
from lenstronomy.Data.psf import PSF
from lenstronomy.ImSim.image_model import ImageModel


def setup_image_model(num_pix=64, delta_pix=0.08):
    """Initializes the core physics simulators for lenstronomy."""
    kwargs_grid = {
        'nx': num_pix, 'ny': num_pix,
        'transform_pix2angle': np.array([[delta_pix, 0], [0, delta_pix]]),
        'ra_at_xy_0': -(num_pix * delta_pix) / 2.0,
        'dec_at_xy_0': -(num_pix * delta_pix) / 2.0
    }
    pixel_grid = PixelGrid(**kwargs_grid)
    psf_class = PSF(psf_type='NONE')

    lens_model = LensModel(lens_model_list=['SIS'])
    source_light_model = LightModel(light_model_list=['SERSIC'])

    return ImageModel(data_class=pixel_grid, psf_class=psf_class,
                      lens_model_class=lens_model, source_model_class=source_light_model)


def simulate_single_lens(image_model, theta_E, center_x, center_y):
    """Generates a clean warped cosmic image given specific parameters."""
    kwargs_lens = [{'theta_E': theta_E, 'center_x': 0.0, 'center_y': 0.0}]
    kwargs_source = [{'amp': 200, 'R_sersic': 0.15, 'n_sersic': 1, 'center_x': center_x, 'center_y': center_y}]

    return image_model.image(kwargs_lens=kwargs_lens, kwargs_source=kwargs_source)