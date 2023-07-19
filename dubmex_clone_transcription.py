from TTS.api import TTS
import os
from legend_clean import parse_subtitle
from adjust_time import adjust_and_save_audio as adjust_time
from merge_audio import concatenate_audio_files as merge_audio
from file_list import file_list
from pydub import AudioSegment
from rename import rename

# Paths
input_voice_path ="voices_origin/Augusto/Augusto_original.wav"
output_voice_path = input_voice_path.split("/")[-2]

file_list_path = f"legend_process1/{output_voice_path}"
output_voice_path1 = f"legend_process1/{output_voice_path}"
output_voice_path2 = f"legend_process2/{output_voice_path}"
output_voice_path3 = f"legend_process3/{output_voice_path}"

# Cria as pastas se não existirem
if not os.path.exists(output_voice_path1):
    os.makedirs(output_voice_path1)

if not os.path.exists(output_voice_path2):
    os.makedirs(output_voice_path2)

if not os.path.exists(output_voice_path3):
    os.makedirs(output_voice_path3)

# Input texts
input_legend = """
The place where I live is very high, you know? Here is the... 
The roof. 
The building. 
The building is something that also makes me very thoughtful. 
I keep thinking, how did the guys decide, right? 
I was going, going, going, and the guys said like this, Guys, it's full!
Let's go upstairs! 
The first person who gave this idea, right?
Let's do it on top of your house!
Are you crazy, bro? 
No, bro, think with me. 
I do a business where I go up and live on top. 
João Nelson, stop being a dreamer. 
Here I live on top of the idea of ​​João Nelson.
"""

def creat_audio(input_legend):
    # Running a multi-speaker and multi-lingual model

    # List available 🐸TTS models and choose the first one
    model_name = TTS.list_models()[0]

    # Init TTS
    tts = TTS(model_name,  progress_bar=True, gpu=False)

    # Example voice cloning with YourTTS in English, French and Portuguese
    tts.tts_to_file(input_legend, speaker_wav=input_voice_path, language="en", file_path=output_voice_path1+f"/{output_voice_path}_transcription.wav")

if __name__ == "__main__":
    creat_audio(input_legend)




