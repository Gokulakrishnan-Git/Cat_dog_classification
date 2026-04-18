# 🐱🐶 Cat-Dog Image Classification (Deep Learning + Deployment)

## 🚀 Live Demo

👉 **Try the app here:**
🔗 https://huggingface.co/spaces/GOKULAKRISHNAN7/cat-dog-classifier

---

## 📌 Overview

This project is a deep learning-based image classification system that predicts whether an input image is a **cat or a dog**.

The model is built using a **custom Convolutional Neural Network (CNN)** implemented in PyTorch and deployed as an interactive web application using **Gradio on Hugging Face Spaces**.

---

## 🎯 Features

* ✅ Custom CNN architecture (built from scratch)
* ✅ Real-time image classification
* ✅ Confidence score output
* ✅ Interactive UI with Gradio
* ✅ Fully deployed (accessible via browser)

---

## 🧠 Model Architecture

The model is a deep CNN with the following structure:

* Convolutional layers
* ReLU activations
* MaxPooling layers
* Dropout for regularization
* Fully connected layer (binary classification)

---

## 📂 Project Structure

```bash
├── app.py                  # Gradio app for inference
├── model.py               # CNN architecture
├── best_model.pth         # Trained model weights
├── cat_dog_classify.ipynb # Training notebook
├── requirements.txt       # Dependencies
├── train/                 # Training dataset
├── test/                  # Testing dataset
```

---

## ⚙️ Installation (Run Locally)

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

Then open the Gradio link in your browser.

---

## 🖼️ Usage

1. Upload an image (cat or dog)
2. The model predicts the label
3. Confidence scores are displayed

---

## 📊 Example Output

```
Prediction: Cat  
Confidence:  
Cat: 0.87  
Dog: 0.13
```

---

## 🧪 Training Details

* Input size: 64 × 64 (grayscale)
* Loss Function: CrossEntropyLoss
* Optimizer: Adam
* Custom hyperparameter tuning

---

## 📦 Requirements

* torch
* torchvision
* gradio
* pillow

---

## 🚀 Deployment

This project is deployed using **Hugging Face Spaces** with Gradio.

👉 Live App:
https://huggingface.co/spaces/GOKULAKRISHNAN7/cat-dog-classifier





---

## 💡 Key Learnings

* Building CNN from scratch
* Model training & evaluation
* Converting ML models into deployable apps
* Using Hugging Face Spaces for deployment

---

## 🤝 Contributing

Feel free to fork this repository and improve the model or UI.

---

## 📬 Contact

If you have any suggestions or feedback, feel free to connect! gokulakrishnan6008@gmail.com


---

⭐ If you found this project useful, consider giving it a star!
