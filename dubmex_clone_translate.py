from TTS.api import TTS
import os
from legend_clean import parse_subtitle
from adjust_time import adjust_and_save_audio as adjust_time
from merge_audio import concatenate_audio_files as merge_audio
from file_list import file_list
from pydub import AudioSegment
from rename import rename
from Coqui_functions import XTTS_speak_text, speak_text
import requests
import json


# Paths
input_voice_path ="voices_origin/Whinderson_Nunes/Whinderson.mp3"
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
00:00:00,000 --> 00:00:01,600
The place where I live is very high, you know?

2
00:00:01,600 --> 00:00:03,100
Here is the...

3
00:00:03,900 --> 00:00:04,900
The roof.

4
00:00:04,900 --> 00:00:05,500
The building.

5
00:00:05,500 --> 00:00:08,000
The building is something that also makes me very thoughtful.

6
00:00:08,000 --> 00:00:10,300
I keep thinking, how did the guys decide, right?

7
00:00:10,300 --> 00:00:11,700
I was going, going, going, and the guys said like this,

8
00:00:11,700 --> 00:00:12,700
Guys, it's full!

9
00:00:13,000 --> 00:00:13,700
Let's go upstairs!

10
00:00:13,700 --> 00:00:15,100
The first person who gave this idea, right?

11
00:00:15,100 --> 00:00:17,100
Let's do it on top of your house!

12
00:00:17,100 --> 00:00:17,700
Are you crazy, bro?

13
00:00:17,700 --> 00:00:19,100
No, bro, think with me.

14
00:00:19,100 --> 00:00:22,500
I do a business where I go up and live on top.

15
00:00:22,500 --> 00:00:24,400
João Nelson, stop being a dreamer.

16
00:00:24,400 --> 00:00:30,400
Here I live on top of the idea of ​​João Nelson.
""")

def creat_audios(input_legend):
    voice_id="3852ceca-2db9-49f7-9f8f-0d77e15eab56"
    # text="Isso é apenas um teste"
    name="Whinderson"

    # Running a multi-speaker and multi-lingual model

    # List available 🐸TTS models and choose the first one
    #model_name = TTS.list_models()[0]
    # Init TTS
    #tts = TTS(model_name,  progress_bar=True, gpu=False)

    # audio = {"id":"1e236c6b-4459-4a99-a76f-01854fd85e51","name":"André MotoGarage","created_at":"2023-07-14T19:19:32.416788Z","text":"Isso é apenas um teste","audio_url":"https://coqui-prod-creator-app-synthesized-samples.s3.amazonaws.com/xtts_samples/1e236c6b-4459-4a99-a76f-01854fd85e51.wav"}

    # Voice cloning with YourTTS in English
    for text in input_legend:
        time_text = f"{int(text['time'].split('-')[0])}-{(int(text['time'].split('-')[1]))}"                  
        input_text = text['text']
        # tts.tts_to_file(input_text, speaker_wav=input_voice_path, language="en", file_path=output_voice_path1+"/"+time_text+".wav")
        audio = speak_text(voice_id, text=input_text, name=name)
        
        audio_link = json.loads(audio)['audio_url']

        # Faz o download do arquivo de áudio
        response = requests.get(audio_link)

        # Verifica se o download foi bem-sucedido
        if response.status_code == 200 or response.status_code == 201:
            # Abre o arquivo de saída em modo de gravação
            output_path = f"{output_voice_path1}/{time_text}.wav"
            with open(output_path, "wb") as output_file:
                # Escreve o conteúdo baixado no arquivo de saída
                output_file.write(response.content)
            print(f"Arquivo {time_text}.wav salvo com sucesso em:", output_path)
        else:
            print("Erro ao baixar o arquivo de áudio:", response.status_code)

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
        merge_audio(output_voice_path2, os.path.join(output_voice_path3, output_folder_name+"_output.wav"))
    
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




