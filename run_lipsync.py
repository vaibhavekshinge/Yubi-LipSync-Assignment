import os
from gtts import gTTS

# Step 1: Generate Audio
text = """Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit 
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which 
needs to be paid by 31st December 2024. 
Missing this payment could lead to two significant consequences: 
First, a late fee will be added to your outstanding balance. 
Second, your credit score will be negatively impacted, which may affect your future borrowing 
ability. 
Make your payment by clicking the link here... Pay through UPI or bank transfer. Thank you!"""

tts = gTTS(text, lang="en", tld="co.in")  
tts.save("input_audio.wav")
print("Audio generated: input_audio.wav")

# Step 2: Run Wav2Lip
os.system("python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face input_image.jpg --audio input_audio.wav --outfile output.mp4")

print("Lip-Synced Video Generated: output.mp4")
