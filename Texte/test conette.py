import os
import csv
from tqdm import tqdm
from conette import CoNeTTEConfig, CoNeTTEModel
import torch
import torchaudio

AUDIO_DIR = "Audio"
OUTPUT_CSV = "descriptions.csv"
TARGET_SR = 32000  # fréquence d’échantillonnage recommandée

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Utilisation de : {device}")

config = CoNeTTEConfig.from_pretrained("Labbeti/conette")
model = CoNeTTEModel.from_pretrained("Labbeti/conette", config = config)
model.to(device)
model.eval()

audio_files = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(".wav")] #on s'assure de ne prendre que des wav

with open(OUTPUT_CSV, mode = "w", newline = "", encoding = "utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "description"])

    for file in tqdm(audio_files, desc = "Génération des descriptions"):
        path = os.path.join(AUDIO_DIR, file)
        try:
            # Charger et préparer le son
            waveform, sr = torchaudio.load(path)
            if waveform.shape[0] > 1:
                waveform = torch.mean(waveform, dim = 0, keepdim = True)
            if sr != TARGET_SR:
                resampler = torchaudio.transforms.Resample(orig_freq = sr, new_freq = TARGET_SR)
                waveform = resampler(waveform)
                sr = TARGET_SR

            waveform = waveform.to(device)

            # Génération de la description
            with torch.no_grad():
                outputs = model(waveform, sr = sr)
                description = outputs["cands"][0]

        except Exception as e:
            description = f"Erreur: {str(e)}"

        writer.writerow([file, description])

print(f"\nTerminé ! Les descriptions sont dans '{OUTPUT_CSV}'.")