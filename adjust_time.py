from pydub import AudioSegment
from legend_clean import parse_subtitle
import os
from rename import rename
from file_list import file_list as f_list

# Caminho da pasta
folder_path = 'legend_process1'

# Lista para armazenar os nomes dos arquivos
audio_list = []

def adjust_and_save_audio(audio_list_path, folder_path, folder_path2, input_voice_path=None, legend_time=None):
    # Cria um áudio em branco para ser usado como silêncio
    silent_segment = AudioSegment.silent(duration=1000)  # 1 segundo de silêncio

    audio_origin = AudioSegment.from_file(input_voice_path, format="mp3")

    # Lista para armazenar os nomes dos arquivos
    audio_list = f_list(audio_list_path)

    if len(audio_origin) < legend_time:
        rename(f"{folder_path}", f"{f_list(folder_path)[-1]}", f"{f_list(folder_path)[-1].split('-')[0]}-{len(audio_origin)}")  
        audio_list = []
        audio_list = f_list(audio_list_path) 

    # Percorre a lista de áudios e ajusta-os individualmente
    for audio_file in audio_list:
        # Extrai os tempos inicial e final da legenda do nome do arquivo
        start_time, end_time = audio_file.split("-")
        start_time = float(start_time)
        end_time = float(end_time[:-4])  # Remove a extensão .mp3

        start_time = int(start_time)
        end_time = int(end_time)  # Converte em milisegundos

        # Lê o áudio do arquivo
        audio = AudioSegment.from_file(folder_path+"/"+audio_file, format="mp3")
            
        if len(audio) < end_time:
            # rename(f"{folder_path}", f"{audio_file.split('-')[0]}-{len(audio)/1000}")
            # audio_file = f"{audio_file.split('-')[0]}-{len(audio)/1000}"
            adjusted_audio = audio[:len(audio)]
            audio_file = f"{audio_file.split('-')[0]}-{len(audio)}.wav"
        elif len(audio) > end_time:
            # Ajusta a duração do áudio para corresponder ao tempo estabelecido
            target_duration = int(len(audio) - end_time)  # Converte para milissegundos
            audio_file = f"{audio_file.split('-')[0]}-{len(audio)}.wav"
            adjusted_audio = audio + AudioSegment.silent(duration=target_duration)
        else:
            adjusted_audio = end_time

        # # Calcula a duração do áudio ajustado
        # adjusted_duration = len(adjusted_audio)

        # # Verifica se é necessário adicionar silêncio após o áudio
        # if adjusted_duration < target_duration:
        #     # Calcula a quantidade de silêncio necessário
        #     silence_duration = target_duration - adjusted_duration

        #     # Calcula quantas vezes o segmento de silêncio precisa ser repetido
        #     num_silence_segments = int(silence_duration / 1)

        #     # Adiciona o segmento de silêncio repetido ao áudio ajustado
        #     adjusted_audio += silent_segment * num_silence_segments

        # Salva o áudio ajustado em um arquivo separado
        adjusted_audio.export(folder_path2 + "/" + audio_file, format="wav")

if __name__ == "__main__":
    # Ajusta e salva os arquivos de áudio individualmente
    adjust_and_save_audio(audio_list, folder_path)



