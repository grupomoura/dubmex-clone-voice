import soundfile as sf
import os
import numpy as np

def concatenate_audio_files(folder_path, output_path):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]
    
    # Ordena os arquivos para garantir a ordem correta
    audio_files.sort()
    
    # Cria uma lista para armazenar os segmentos de áudio a serem concatenados
    segments = []
    
    for file in audio_files:
        try:
            audio, sample_rate = sf.read(os.path.join(folder_path, file))
        except:
            pass
        
        # Adiciona o segmento de áudio à lista
        segments.append(audio)
    
    # Concatena todos os segmentos de áudio
    concatenated_audio = np.concatenate(segments)
    
    # Grava o áudio concatenado em um arquivo WAV
    sf.write(output_path, concatenated_audio, sample_rate)

# Caminho da pasta de entrada
input_folder_path = 'legend_process2'

# Caminho da pasta de saída
output_folder_path = 'legend_process3'

if __name__ == "__main__":
    # Chama a função para concatenar os arquivos de áudio
    concatenate_audio_files(input_folder_path, os.path.join(output_folder_path, "output.wav"))
