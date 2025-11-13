# Image Classification & Artistic Filters  
### Final Report – Artificial Intelligence Ecosystem

This project was completed following the assignment instructions for Parts 1 and 2. It includes running the MobileNetV2 classifier, implementing Grad-CAM, analyzing the heatmap, understanding and modifying image filters, creating an artistic filter, and reflecting on my experience working with AI.

---

# Part 1 – Basic Classifier & Grad-CAM

## 1. Find an Image
I selected a cat image to use for classification and Grad-CAM visualization.

## 2. Setting Up the Workspace
I followed the required setup steps by forking the repository, opening VS Code using WWSL, cloning my fork into the Ubuntu environment, opening the `Image_Classification` folder, creating and activating a Python virtual environment, and installing all dependencies from the requirements file. Everything in the setup process worked correctly.

## 3. Running the Basic Classifier
I asked the AI to explain the base classifier line-by-line using the prompt “Explain what each line of this Python program does.” Since I already have Python experience, most of the explanation aligned with what I already understood. The TensorFlow-specific parts—like why `expand_dims()` and `preprocess_input()` are needed—were the most helpful because they clarified how MobileNetV2 expects its inputs.

## 4. Top-3 Predictions
From MobileNetV2, the results were:

Top-3 Predictions for Image_Classification/cat.jpg  
1: Persian_cat (0.41)  
2: lynx (0.07)  
3: Egyptian_cat (0.06)

## 5. Implementing Grad-CAM
I asked the AI how to add Grad-CAM to my classifier. It walked me through building a gradient model, computing gradients for the predicted class, weighting the feature maps, and generating the heatmap. I integrated the Grad-CAM code into `base_classifier.py` successfully.

## 6. Understanding Grad-CAM
I asked the AI to explain the Grad-CAM algorithm, and the explanation clarified how gradients determine channel importance, why the last convolutional layer is used, how the heatmap keeps spatial relevance, why ReLU is applied, and how the heatmap gets overlaid onto the original image. This helped me fully understand the technique.

## 7. Heatmap Analysis
The heatmap showed that the model strongly focused on the cat’s eyes, nose, mouth, and the center of the face. The ears and outer head shape had moderate activation, while the body and background were largely ignored. This indicates that the classifier is paying attention to meaningful features like the eyes, snout, and overall facial structure, rather than irrelevant background details, which is expected behavior for a well-functioning model.

---

# Part 2 – Creating and Experimenting With Image Filters

## 1. Understanding the Blur Filter
I opened `basic_filter.py` and asked the AI to explain every line. The explanation made sense and matched my understanding of how the program works. The blur effect is created by first resizing the image to 128×128, which already removes detail, and then applying a Gaussian blur with radius 2, which smooths edges even more and produces a soft, low-detail output.

## 2. Designing My Own Artistic Filter
I asked the AI to modify the filter to create a new artistic effect. It generated a filter that applied color inversion, increased saturation, added sharpening, and introduced a small amount of noise. I implemented these changes in a new file called `negative_filter.py` and tested it on multiple images.

## 3. Final Artistic Filter Description
The final filter produces a high-contrast, neon-negative aesthetic. It inverts colors, boosts saturation, sharpens edges, and adds slight film grain. The combination makes normal images look stylized, vivid, and visually intense.

---

# Final Reflection – Working With AI

Working with the AI helped make the assignment much easier to navigate. It explained complex TensorFlow and Pillow functions in simple terms, provided correct Grad-CAM implementation details, and assisted in designing and tweaking the artistic filter. The explanations matched my experience level, and the iterative prompting process made experimentation quick and productive. Overall, it felt like having a tutor who could instantly clarify code and generate new ideas on demand.
