from TTS.api import TTS
import os
from legend_clean import parse_subtitle
from adjust_time import adjust_and_save_audio as adjust_time
from merge_audio import concatenate_audio_files as merge_audio
from file_list import file_list
from pydub import AudioSegment
from rename import rename
import requests
import json


# Paths
input_voice_path ="voices_origin/Augusto/AUGUSTO - INTRODU O SOBRE BRITADOR DE MAND BULAS.mp3"
output_folder_name = input_voice_path.split("/")[-2]

file_list_path = f"legend_process1/{output_folder_name}"
output_voice_path1 = f"legend_process1/{output_folder_name}"
output_voice_path2 = f"legend_process2/{output_folder_name}"
output_voice_path3 = f"legend_process3/{output_folder_name}"

# Cria as pastas se não existirem
if not os.path.exists(output_voice_path1):
    os.makedirs(output_voice_path1)

if not os.path.exists(output_voice_path2):
    os.makedirs(output_voice_path2)

if not os.path.exists(output_voice_path3):
    os.makedirs(output_voice_path3)

# Input texts
input_legend = parse_subtitle("""
1
00:00:00,000 --> 00:00:04,000
Il y a une phrase qui dit que le connaissement génére le mieux les jeux

2
00:00:04,000 --> 00:00:10,000
Pensant à cela, nous avons créé une plateforme, avec plusieurs cours inclus, où vous pouvez se qualifier de différentes manières

3
00:00:10,000 --> 00:00:13,000
Où nous avons le cours de réducteurs et d'engrenage

4
00:00:13,000 --> 00:00:17,000
Le cours de transporteur de courriers et de ses components

5
00:00:17,000 --> 00:00:21,000
Le cours de bombes centrifugales, inspection et maintenance

6
00:00:21,000 --> 00:00:24,000
Le cours d'accompagnement, montage et inspection

7
00:00:24,000 --> 00:00:27,000
Le cours d'éléments de vedation

8
00:00:27,000 --> 00:00:30,000
Et nous avons aussi le cours de mancailles et de roulements

9
00:00:30,000 --> 00:00:33,000
Pour chaque cours, nous émettons un certificat exclusif

10
00:00:33,000 --> 00:00:36,000
Cliquez sur le bouton en bas pour vous enregistrer

""")

language="en"

def creat_audios(input_legend):
    # Running a multi-speaker and multi-lingual model

    # List available 🐸TTS models and choose the first one
    model_name = TTS.list_models()[0]
    # Init TTS
    tts = TTS(model_name,  progress_bar=True, gpu=False)
    
    # Voice cloning with YourTTS in English
    for text in input_legend:
        time_text = f"{int(text['time'].split('-')[0])}-{(int(text['time'].split('-')[1]))}"                  
        input_text = text['text']
        tts.tts_to_file(input_text, speaker_wav=input_voice_path, language=language, file_path=output_voice_path1+"/"+time_text+".wav")
        
if __name__ == "__main__":
    creat_audios(input_legend)    
    audio = AudioSegment.from_file(input_voice_path, format="mp3")
    legend_time = int(input_legend[-1]['time'].split('-')[1])
    if len(audio) > legend_time:
        print("################################")
        print(f'O tempo do áudio será reajustado')
        print(f'Tempo do áudio: {len(audio)}ms')
        print(f'Tempo da legenda: {legend_time}ms')
        print("################################")

        legend_time = len(audio)
                
        adjust_time(file_list_path, output_voice_path1, output_voice_path2, input_voice_path, legend_time)
        merge_audio(output_voice_path2, os.path.join(output_voice_path3, output_folder_name+"-"+language+"_output.wav"))
    
    elif len(audio) < legend_time:
        print("################################")
        print(f'O tempo do áudio será reajustado')
        print(f'Tempo do áudio: {len(audio)}ms')
        print(f'Tempo da legenda: {legend_time}ms')
        print("################################")

        # adjust_time(file_list_path, output_voice_path1, output_voice_path2, input_voice_path, legend_time)
        merge_audio(output_voice_path1, os.path.join(output_voice_path3, output_folder_name+"_output.wav"))
    else:
        print("################################")
        print('Não é necessário ajustar tempo')
        print("################################")
        merge_audio(output_voice_path1, os.path.join(output_voice_path3, output_folder_name+"_output.wav"))




