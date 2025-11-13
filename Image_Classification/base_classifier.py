import tensorflow as tf
tf.get_logger().setLevel('ERROR')

import numpy as np
import cv2

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model


# Load pretrained ImageNet model
base_model = MobileNetV2(weights="imagenet")
LAST_CONV_LAYER_NAME = "Conv_1"


def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    """
    Generates a Grad-CAM heatmap for the given image batch.
    img_array: preprocessed image batch of shape (1, 224, 224, 3)
    """
    # Model that maps input -> (last conv outputs, predictions)
    grad_model = Model(
        inputs=model.inputs,
        outputs=[model.get_layer(last_conv_layer_name).output, model.output]
    )

    # Record operations for automatic differentiation
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    # Gradient of class score wrt conv feature maps
    grads = tape.gradient(class_channel, conv_outputs)

    # Global average pooling of gradients over spatial dimensions
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # Weighted sum of feature maps
    conv_outputs = conv_outputs[0]  # (H, W, C)
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # ReLU + normalize to [0, 1]
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()


def overlay_heatmap(img_path, heatmap, alpha=0.4, colormap=cv2.COLORMAP_JET):
    """
    Overlays a colored heatmap on top of the original image.
    """
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Could not read image at '{img_path}'")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize heatmap to match original image size
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)

    heatmap_color = cv2.applyColorMap(heatmap, colormap)

    # Blend heatmap with original image
    overlay = heatmap_color * alpha + img
    overlay = np.uint8(overlay)
    return overlay


def classify_image_with_gradcam(image_path, top=3):
    try:
        # Load and preprocess image
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = base_model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=top)[0]

        # Grad-CAM for the top predicted class (index 0)
        top_class_index = np.argmax(predictions[0])
        heatmap = make_gradcam_heatmap(
            img_array, base_model, LAST_CONV_LAYER_NAME, pred_index=top_class_index
        )

        # Overlay heatmap on original image
        overlay = overlay_heatmap(image_path, heatmap)

        # Save overlay image next to original
        out_path = image_path.rsplit(".", 1)[0] + "_gradcam.jpg"
        cv2.imwrite(out_path, cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR))

        # Print predictions
        print(f"\nTop-{top} Predictions for {image_path}")
        for i, (_, label, score) in enumerate(decoded_predictions):
            print(f"  {i + 1}: {label} ({score:.2f})")

        print(f"GradCAM overlay saved to: {out_path}")

    except Exception as e:
        print(f"Error processing '{image_path}': {e}")


if __name__ == "__main__":
    print("Image Classifier with Grad-CAM (type 'exit' to quit)\n")
    while True:
        image_path = input("Enter image filename: ").strip()
        if image_path.lower() == "exit":
            print("Goodbye!")
            break
        classify_image_with_gradcam(image_path)
