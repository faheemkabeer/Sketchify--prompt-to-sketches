from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import os
import uuid
import random
import traceback
import torch

from PIL import Image

from diffusers import (
    StableDiffusionInpaintPipeline,
    DPMSolverMultistepScheduler,
    AutoencoderKL
)

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FRONTEND_FOLDER = os.path.abspath(
    os.path.join(BASE_DIR, "..", "frontend")
)

OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

BASE_MODEL_PATH = r"C:\Users\FAHEEM\Desktop\sketchify\backend\models\MyBack_SD1.5_Realistic_Vision_inpainting_VAE_V5.1.safetensors"

LORA_PATH = r"C:\Users\FAHEEM\Desktop\sketchify\backend\models\trained model sketches v1-000006.safetensors"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================================================
# FLASK
# ==========================================================

app = Flask(
    __name__,
    static_folder=FRONTEND_FOLDER,
    static_url_path=""
)

CORS(app)

# ==========================================================
# DEVICE
# ==========================================================

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

print(f"🚀 Using device: {device}")

# ==========================================================
# LOAD MODEL
# ==========================================================

print("📦 Loading inpainting model...")

pipe = StableDiffusionInpaintPipeline.from_single_file(
    BASE_MODEL_PATH,
    torch_dtype=dtype,
    safety_checker=None
)

print("📦 Loading VAE...")

pipe.vae = AutoencoderKL.from_pretrained(
    "stabilityai/sd-vae-ft-mse",
    torch_dtype=dtype
)

pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    pipe.scheduler.config,
    algorithm_type="dpmsolver++"
)

pipe = pipe.to(device)

try:
    pipe.enable_xformers_memory_efficient_attention()
    print("✅ xformers enabled")
except Exception as e:
    print("⚠️ xformers not available")
    print(e)

pipe.enable_attention_slicing()
pipe.enable_vae_slicing()

print("📦 Loading LoRA...")
pipe.load_lora_weights(LORA_PATH)

pipe.safety_checker = lambda images, clip_input: (
    images,
    [False] * len(images)
)

print("✅ Model Ready")

# ==========================================================
# ROUTES
# ==========================================================

@app.route("/")
def home():
    return send_from_directory(
        FRONTEND_FOLDER,
        "index.html"
    )

@app.route("/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({
                "success": False,
                "error": "Prompt is empty"
            })

        prompt = "abhi_sketch_style, " + user_prompt

        negative_prompt = (
            "low quality, blurry, distorted face, bad anatomy, "
            "cartoon, anime, 3d render, watermark, text, "
            "duplicate, extra fingers, extra limbs, cropped, "
            "deformed, ugly, poorly drawn"
        )

        generator = torch.Generator(
            device=device
        ).manual_seed(
            random.randint(1, 999999)
        )

        print(f"\n🎨 Generating...")
        print(f"Prompt: {prompt}")

        init_image = Image.new(
            "RGB",
            (768, 768),
            color="white"
        )

        mask_image = Image.new(
            "RGB",
            (768, 768),
            color="white"
        )

        if device == "cuda":
            with torch.autocast("cuda"):
                result = pipe(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    image=init_image,
                    mask_image=mask_image,
                    num_inference_steps=30,
                    guidance_scale=7,
                    generator=generator
                )
        else:
            result = pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                image=init_image,
                mask_image=mask_image,
                num_inference_steps=30,
                guidance_scale=7,
                generator=generator
            )

        if len(result.images) == 0:
            return jsonify({
                "success": False,
                "error": "No image generated"
            })

        image = result.images[0]

        filename = f"{uuid.uuid4()}.png"

        save_path = os.path.join(
            OUTPUT_FOLDER,
            filename
        )

        image.save(save_path)

        print(f"✅ Saved: {save_path}")

        return jsonify({
            "success": True,
            "image_url": f"/image/{filename}"
        })

    except Exception as e:

        traceback.print_exc()

        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/image/<filename>")
def get_image(filename):

    return send_from_directory(
        OUTPUT_FOLDER,
        filename
    )

# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )