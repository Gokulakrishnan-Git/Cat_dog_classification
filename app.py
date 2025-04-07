




# #cd Cat_dog_classification
# # Run the server using: uvicorn app:app --reload



# import torch
# from fastapi import FastAPI, UploadFile, File
# from torchvision import transforms
# from PIL import Image
# import io

# # Import the model from your Jupyter Notebook
# from model import DeepCNN  # Replace 'your_notebook' with the actual notebook name

# # Initialize FastAPI
# app = FastAPI()

# IMG_SIZE = 64  # Image size used for training

# # Load the model
# best_model = DeepCNN(num_layers=5, hidden_size=173, dropout_rate=0.2693923833702318)  # Ensure this class is correctly defined in your Jupyter Notebook
# best_model.load_state_dict(torch.load("best_model.pth", map_location=torch.device('cpu')))
# best_model.eval()  # Set model to evaluation mode

# # Define image transformations (must match training)
# transform = transforms.Compose([
#     transforms.Resize((IMG_SIZE, IMG_SIZE)),  # Resize to match model input size
#     transforms.ToTensor(),
# ])

# app = FastAPI()

# @app.post("/predict/")
# async def predict(file: UploadFile = File(...)):
#     try:
#         # Read the image
#         image = Image.open(io.BytesIO(await file.read())).convert("L")  # Convert to grayscale
#         image = transform(image).unsqueeze(0)  # Add batch dimension
        
#         # Perform prediction
#         with torch.no_grad():
#             output = best_model(image)
#             prediction = torch.argmax(output, dim=1).item()
        
#         # Convert prediction to label
#         label = "Cat" if prediction == 0 else "Dog"
#         return {"prediction": label, "confidence_scores": output.softmax(dim=1).tolist()}  # Get probability scores
    
#     except Exception as e:
#         return {"error": str(e)}

# @app.get("/")
# def home():
#     return {"message": "Cat-Dog Classification API is running!"}

import torch
from torchvision import transforms
from PIL import Image
import gradio as gr
import io

# Import the model
from model import DeepCNN  

IMG_SIZE = 64  # Image size used for training

# Load the trained model
best_model = DeepCNN(num_layers=5, hidden_size=173, dropout_rate=0.2693923833702318)
best_model.load_state_dict(torch.load("best_model.pth", map_location=torch.device("cpu")))
best_model.eval()

# Define image transformations (must match training)
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),  
    transforms.ToTensor(),
])

def predict(image):
    image = image.convert("L")  # Convert to grayscale
    image = transform(image).unsqueeze(0)  # Add batch dimension
    
    with torch.no_grad():
        output = best_model(image)
        prediction = torch.argmax(output, dim=1).item()
        confidence_scores = output.softmax(dim=1).squeeze().tolist()  # Convert to list
    
    # Convert confidence scores to dictionary format for Gradio
    labels = ["Cat", "Dog"]
    confidence_dict = {labels[i]: confidence_scores[i] for i in range(len(labels))}
    
    label = labels[prediction]  # Get predicted label
    
    return label, confidence_dict  # Gradio `Label` expects a dictionary for confidence


# Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),  
    outputs=[gr.Text(), gr.Label(num_top_classes=2)],  
    title="🐱🐶 Cat-Dog Classification",
    description="Upload an image to classify it as a Cat or Dog!",
)

# Launch app
interface.launch()

