import os
import numpy as np
import matplotlib.pyplot as plt


def plot_simulated_lenses(num_to_display=4):
    """Loads the generated dataset from data/raw/ and displays a grid of lens images."""
    images_path = os.path.join('data', 'raw', 'lens_images.npy')
    params_path = os.path.join('data', 'raw', 'lens_params.npy')

    # 1. Check if the dataset files actually exist
    if not os.path.exists(images_path) or not os.path.exists(params_path):
        print("❌ Error: Dataset files not found. Run main.py first to generate data!")
        return

    # 2. Load the arrays
    images = np.load(images_path)
    params = np.load(params_path)

    print(f"📊 Loaded {len(images)} images for visualization.")

    # 3. Create a clean grid layout
    fig, axes = plt.subplots(1, num_to_display, figsize=(4 * num_to_display, 4))

    # Handle the edge case where we only display 1 image
    if num_to_display == 1:
        axes = [axes]

    for i in range(num_to_display):
        # Grab individual parameters for the title
        theta_E, center_x, center_y = params[i]

        # Plot the matrix heatmap
        im = axes[i].imshow(images[i], origin='lower', cmap='magma')
        axes[i].set_title(f"Lens #{i + 1}\n$\\theta_E$: {theta_E:.2f} | X: {center_x:.2f}")
        axes[i].axis('off')

    # Add a global color bar to show pixel intensity scale
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.88, 0.15, 0.02, 0.7])
    fig.colorbar(im, cax=cbar_ax, label="Intensity")

    # Save a copy to your figures directory
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/dataset_preview.png', bbox_inches='tight')
    print("🎨 Preview grid saved to figures/dataset_preview.png")

    # Show the pop-up window
    plt.show()


if __name__ == "__main__":
    plot_simulated_lenses(num_to_display=4)