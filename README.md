# 🐱🐶 Cat-Dog Image Classification (Deep Learning + Gradio)

## 🚀 Overview

This project is a deep learning-based image classification system that predicts whether an input image is a **cat or a dog**.

The model is built using a **custom Convolutional Neural Network (CNN)** implemented in PyTorch and deployed using an interactive **Gradio web interface**.

---

## 🎯 Features

* ✅ Custom-built CNN architecture (not pretrained)
* ✅ Image preprocessing pipeline
* ✅ Confidence score output for predictions
* ✅ Interactive UI using Gradio
* ✅ Lightweight and fast inference

---

## 🧠 Model Architecture

The model is a deep CNN with the following characteristics:

* Multiple convolutional layers
* ReLU activation
* MaxPooling layers
* Dropout for regularization
* Fully connected output layer (binary classification)

---

## 📂 Project Structure

```
├── app.py                  # Gradio app for inference
├── model.py               # CNN architecture
├── best_model.pth         # Trained model weights
├── cat_dog_classify.ipynb # Training notebook
├── requirements.txt       # Dependencies
├── train/                 # Training dataset
├── test/                  # Testing dataset
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cat-dog-classification.git
cd cat-dog-classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

After running, open the local Gradio link in your browser.

---

## 🖼️ Usage

1. Upload an image (cat or dog)
2. The model predicts the label
3. Confidence scores are displayed

---

## 📊 Example Output

```
Prediction: Dog  
Confidence:  
Dog: 0.92  
Cat: 0.08
```

---

## 🧪 Training Details

* Input image size: 64x64 (grayscale)
* Loss Function: CrossEntropyLoss
* Optimizer: Adam
* Hyperparameters tuned manually

---

## 📦 Requirements

See `requirements.txt`:

* torch
* torchvision
* gradio
* pillow

---

## 🚀 Future Improvements

* 🔹 Deploy on Hugging Face Spaces
* 🔹 Add GPU support
* 🔹 Improve accuracy with data augmentation
* 🔹 Use pretrained models (ResNet, EfficientNet)
* 🔹 Add REST API (FastAPI version)

---

## 💡 Learnings

* Building CNN from scratch
* Model training and evaluation
* Converting research code into a deployable app
* Creating interactive ML applications

---

## 🤝 Contributing

Feel free to fork this repo and improve the model or UI.

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!

---

⭐ If you like this project, consider giving it a star!
