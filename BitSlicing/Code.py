{
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"},
    },
    "cells": [
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {"id": "9MAPRNQcRSU9"},
            "outputs": [],
            "source": [
                "\n",
                "import cv2\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "\n",
                "# Load the image in grayscale mode\n",
                "image = cv2.imread('/content/image1.jpeg', cv2.IMREAD_GRAYSCALE)\n",
                "\n",
                "# Check if the image is loaded successfully\n",
                "if image is None:\n",
                '    print("Error loading image.")\n',
                "else:\n",
                '    print("Image loaded successfully.")\n',
                "\n",
                "# List to store the 8 bit planes of the image\n",
                "bit_planes = []\n",
                "\n",
                "# Loop through each bit plane from 0 to 7\n",
                "for i in range(8):\n",
                "    # Initialize an empty array with the same shape as the image to store the bit plane\n",
                "    bit_plane = np.zeros_like(image)\n",
                "\n",
                "    # Extract the i-th bit plane using bitwise AND operation\n",
                "    # (1 << i) shifts 1 to the left by 'i' bits to create a mask for the i-th bit\n",
                "    bit_plane = cv2.bitwise_and(image, 1 << i)\n",
                "\n",
                "    # Convert non-zero values to 255 (white) for better visualization of the bit plane\n",
                "    bit_plane = np.where(bit_plane > 0, 255, 0).astype(np.uint8)\n",
                "\n",
                "    # Append the extracted bit plane to the list\n",
                "    bit_planes.append(bit_plane)\n",
                "\n",
                "# Create a 2x4 grid of subplots to display all 8 bit planes\n",
                "fig, axes = plt.subplots(2, 4, figsize=(20, 10))\n",
                "axes = axes.ravel()  # Flatten the 2x4 array into a 1D array for easy iteration\n",
                "\n",
                "# Loop through each bit plane and display it in the corresponding subplot\n",
                "for i in range(8):\n",
                "    axes[i].imshow(bit_planes[i], cmap='gray')\n",
                "    axes[i].set_title(f'Bit Plane {i}')  # Set the title to indicate the bit plane number\n",
                "    axes[i].axis('off')  # Hide the axis for a cleaner visualization\n",
                "\n",
                "plt.tight_layout()  # Adjust the spacing between subplots\n",
                "plt.show()  # Display the bit planes\n",
                "\n",
                "# Initialize an empty array to store the reconstructed image\n",
                "# The reconstruction will be based on the most significant bit planes (4 to 7)\n",
                "reconstructed_image = np.zeros_like(image)\n",
                "\n",
                "# Loop through bit planes 4 to 7 and add their contributions to the reconstructed image\n",
                "for i in range(4, 8):\n",
                "    # Add the weighted bit plane to the reconstructed image\n",
                "    # (1 << i) shifts the bit plane back to its original value in the pixel\n",
                "    reconstructed_image += bit_planes[i] * (1 << i)\n",
                "\n",
                "# Display the reconstructed image using only the most significant bit planes\n",
                "plt.figure(figsize=(10, 7))\n",
                "plt.imshow(reconstructed_image, cmap='gray')\n",
                "plt.title('Reconstructed Image Using Bit Planes 4 to 7')  # Set the title\n",
                "plt.axis('off')  # Hide the axis for a cleaner visualization\n",
                "plt.show()  # Display the reconstructed image",
            ],
        }
    ],
}
