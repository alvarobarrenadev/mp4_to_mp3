# pip install ffmpeg-python

import os
import ffmpeg
from concurrent.futures import ThreadPoolExecutor

def convertir_archivo(video_path, audio_path):
    try:
        ffmpeg.input(video_path).output(audio_path).run()
        print(f"Convertido: {video_path} -> {audio_path}")
    except ffmpeg.Error as e:
        print(f"Error al convertir {video_path}: {str(e)}")
    except Exception as e:
        print(f"Error inesperado con {video_path}: {str(e)}")

def convertir_videos_a_mp3(carpeta_entrada, carpeta_salida, num_hilos=4):
    print("Iniciando el proceso de conversión...")

    if not os.path.exists(carpeta_entrada):
        print(f"La carpeta de entrada {carpeta_entrada} no existe.")
        return

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener todos los archivos en la carpeta de entrada
    archivos = os.listdir(carpeta_entrada)
    print(f"Archivos en la carpeta de entrada: {archivos}")

    # Filtrar archivos de video compatibles
    formatos_video = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']
    archivos_videos = [
        archivo for archivo in archivos 
        if any(archivo.lower().endswith(ext) for ext in formatos_video)
    ]
    print(f"Archivos de video detectados: {archivos_videos}")

    if not archivos_videos:
        print("No se encontraron archivos de video en la carpeta de entrada.")
        return

    # Usar un ThreadPoolExecutor para procesar varios archivos a la vez
    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        for archivo in archivos_videos:
            video_path = os.path.join(carpeta_entrada, archivo)
            mp3_filename = os.path.splitext(archivo)[0] + ".mp3"  # Cambiar extensión a .mp3
            audio_path = os.path.join(carpeta_salida, mp3_filename)
            executor.submit(convertir_archivo, video_path, audio_path)

if __name__ == "__main__":
    carpeta_entrada = "videos"  # Ruta relativa o absoluta de la carpeta de entrada
    carpeta_salida = "audios"  # Ruta relativa o absoluta de la carpeta de salida
    convertir_videos_a_mp3(carpeta_entrada, carpeta_salida, num_hilos=9)
