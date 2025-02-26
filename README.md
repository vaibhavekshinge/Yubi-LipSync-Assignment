# 🎭 Wav2Lip Lip-Sync Model Implementation  

This repository contains the implementation of the **Wav2Lip** model for accurate lip-syncing of an input image with speech. The model is based on the open-source **Wav2Lip** repository and has been set up to generate lip-synced videos using a provided script and input image.

---

## 🚀 **Project Overview**
This project takes:
- **An input image** of a person.
- **A text script**, which is converted to speech using `gTTS` (Google Text-to-Speech).
- **A trained Wav2Lip model**, which generates a video of the input image lip-syncing to the generated speech.

---

## 🛠 **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/vaibhavekshinge/Yubi-LipSync-Assignment.git
cd Yubi-LipSync-Assignment
2️⃣ Set Up a Virtual Environment (Recommended)
conda create --name lipsync_env python=3.8
conda activate lipsync_env
If using venv instead of Conda:
python -m venv lipsync_env
source lipsync_env/bin/activate  # Mac/Linux
lipsync_env\Scripts\activate  # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Download Pre-trained Models
Wav2Lip GAN model:
Download Here
Move wav2lip_gan.pth to the checkpoints/ folder.

Face Detection Model (SFD):
Download Here
Move s3fd.pth to face_detection/detection/sfd/

FFmpeg: Required for video processing

Download FFmpeg
Extract it and add ffmpeg/bin to your system PATH.
🎬 How to Run the Model
1️⃣ Generate Lip-Synced Video
Run the script:
python run_lipsync.py
Alternatively, run manually:
python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face input_image.jpg --audio input_audio.wav --outfile output.mp4
2️⃣ Expected Output
output.mp4 → The generated lip-synced video.
🛠 Troubleshooting
1️⃣ If FFmpeg is not found
Make sure FFmpeg is installed and added to PATH.
Run:
ffmpeg -version
If not found, reinstall from FFmpeg Official Site.
2️⃣ If wav2lip_gan.pth is missing
Manually download from Google Drive.
Move it to checkpoints/.
3️⃣ If s3fd.pth is missing
Download from this link.
Move it to face_detection/detection/sfd/.
4️⃣ If NumPy error occurs
If you see "module 'numpy' has no attribute 'long'", downgrade NumPy:
pip install numpy==1.23.5 --force-reinstall
📝 Project Files
run_lipsync.py → Automates text-to-speech and lip-syncing.
inference.py → Runs Wav2Lip model on given inputs.
requirements.txt → Required dependencies.
checkpoints/ → Folder for pre-trained models.
📜 Acknowledgments
Wav2Lip Paper:
"A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild" (ACM MM 2020)
Original Repo: https://github.com/Rudrabha/Wav2Lip
Authors: Prajwal, Rudrabha, Vinay P. Namboodiri, C.V. Jawahar
📌 License
This project is for academic and research purposes only. Commercial use is strictly prohibited.

🎯 Future Improvements
✅ Allow real-time lip-syncing
✅ Improve TTS quality using advanced models
✅ Enhance face-swapping features

📧 Contact
For any questions, feel free to reach out!

🔹 GitHub: @vaibhavekshinge
🔹 Email: vaibhavekshinge18@gmail.com
---
