from PIL import Image, ImageOps, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import os

def apply_custom_filter(image_path, output_path="filtered_image.png"):
    try:
        img = Image.open(image_path).convert("RGB")
        img = img.resize((128, 128))

        # --- NEW FIXED PARAMETERS ---
        NEGATIVE = True
        SATURATION = 1.8     # increased color intensity
        SHARPNESS = 1.5      # stronger edges
        NOISE_LEVEL = 0.05   # subtle film grain
        # ----------------------------

        # Apply negative
        if NEGATIVE:
            img = ImageOps.invert(img)

        # Saturation adjustment
        img = ImageEnhance.Color(img).enhance(SATURATION)

        # Sharpness adjustment
        img = ImageEnhance.Sharpness(img).enhance(SHARPNESS)

        # Noise addition
        if NOISE_LEVEL > 0:
            arr = np.array(img, dtype=np.float32)
            noise = np.random.randn(*arr.shape) * (NOISE_LEVEL * 255)
            arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
            img = Image.fromarray(arr)

        # Display & save
        plt.imshow(img)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()

        print(f"Processed image saved as '{output_path}'.")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    print("Custom Filter Processor (type 'exit' to quit)\n")

    while True:
        image_path = input("Enter image filename: ").strip()

        if image_path.lower() == "exit":
            print("Goodbye!")
            break

        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        base, ext = os.path.splitext(image_path)
        output_file = f"{base}_filtered{ext}"

        apply_custom_filter(image_path, output_file)
