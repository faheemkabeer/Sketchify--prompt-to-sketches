# Sketchify--prompt-to-sketches
# ✏️ Sketchify

Transform text prompts into realistic black-and-white pencil sketches using Stable Diffusion and a custom-trained LoRA model.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-green)
![PyTorch](https://img.shields.io/badge/PyTorch-AI-red)
![License](https://img.shields.io/badge/License-Apache%202.0-orange)



## 📌 Overview

Sketchify is an AI-powered sketch generation application that converts simple text descriptions into detailed monochrome pencil sketches.

The project uses:

* Stable Diffusion
* Custom LoRA Fine-Tuning
* Flask Backend
* Web-based User Interface
* GPU Acceleration (CUDA)

Users can generate portraits, landscapes, architecture sketches, fantasy illustrations, cityscapes, and creative artwork from text prompts.



## ✨ Features

* 🎨 Text-to-Sketch Generation
* ✏️ Pencil Sketch Style
* 🖤 Black & White Monochrome Output
* 🤖 Custom Trained LoRA Model
* ⚡ Fast GPU Inference
* 🌐 Browser-Based Interface
* 📥 Download Generated Sketches
* 📱 Responsive UI



## 🖼️ Sample Outputs

### Portrait Sketch

![Portrait](./sample1.png)

### Architecture Sketch

![Architecture](./sample2.png)

### Landscape Sketch

![Landscape](./sample3.png)



## 🏗️ Project Structure

text
Sketchify/
│
├── backend/
│   ├── app.py
│   ├── models/
│   ├── outputs/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
├── requirements.txt
├── README.md
└── LICENSE




## 🚀 Installation

### Clone Repository

bash
git clone https://github.com/yourusername/Sketchify.git
cd Sketchify


### Create Environment

bash
python -m venv sketchify_env


Activate Environment

Windows:

bash
sketchify_env\Scripts\activate


Linux/Mac:

bash
source sketchify_env/bin/activate


### Install Dependencies

bash
pip install -r requirements.txt




## 🤖 Model Setup

Place your files inside:

text
backend/models/


Required files:

text
MyBack_SD1.5_Realistic_Vision_inpainting_VAE_V5.1.safetensors

trained_model_sketches_v1.safetensors




## ▶️ Running the Application

Navigate to backend:

bash
cd backend


Run Flask:

bash
python app.py


Open browser:

text
http://127.0.0.1:5000




## 💡 Example Prompts

### Portrait

text
beautiful young woman smiling, long wavy hair, expressive eyes


### Architecture

text
modern luxury villa with garden


### Nature

text
large tree beside a river during sunset


### Horror

text
terrifying horror man with glowing eyes and sinister smile


### Romance

text
young couple holding hands and smiling


### City Life

text
night city life in Ernakulam, busy streets and city lights




## ⚙️ Tech Stack

| Technology | Purpose          |
| ---------- | ---------------- |
| Python     | Backend          |
| Flask      | Web Server       |
| PyTorch    | Deep Learning    |
| Diffusers  | Stable Diffusion |
| LoRA       | Fine-Tuning      |
| HTML/CSS   | Frontend         |
| JavaScript | Frontend Logic   |



## 🎯 Use Cases

* Portrait Sketches
* Character Design
* Architecture Concepts
* Storybook Illustrations
* Fantasy Art
* Landscape Sketches
* Educational Art Generation



## 🔮 Future Improvements

* Image-to-Sketch Conversion
* Multiple Sketch Styles
* High Resolution Output
* User Gallery
* Cloud Deployment
* Mobile Application



## 📄 License

Licensed under the Apache License 2.0.

See the LICENSE file for details.

-
## 👨‍💻 Author

**Faheem Kabeer**

Artificial Intelligence & Data Science Student

MES College of Engineering Kuttippuram

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
