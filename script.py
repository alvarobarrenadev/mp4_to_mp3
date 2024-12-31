# pip install ffmpeg-python

import os
import ffmpeg

def convertir_mp4_a_mp3(carpeta_entrada, carpeta_salida):
    print("Iniciando el proceso de conversión...")

    # Verificar si la carpeta de entrada existe
    if not os.path.exists(carpeta_entrada):
        print(f"La carpeta de entrada {carpeta_entrada} no existe.")
        return

    # Crear la carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener todos los archivos .mp4 en la carpeta de entrada
    archivos = os.listdir(carpeta_entrada)
    if not archivos:
        print("No se encontraron archivos en la carpeta de entrada.")
    else:
        print(f"Archivos encontrados en {carpeta_entrada}: {archivos}")

    for archivo in archivos:
        if archivo.endswith(".mp4"):
            video_path = os.path.join(carpeta_entrada, archivo)
            mp3_filename = archivo.replace(".mp4", ".mp3")
            audio_path = os.path.join(carpeta_salida, mp3_filename)

            # Convertir MP4 a MP3 usando ffmpeg-python
            try:
                ffmpeg.input(video_path).output(audio_path).run()
                print(f"Convertido: {video_path} -> {audio_path}")
            except ffmpeg.Error as e:
                print(f"Error al convertir {video_path}: {str(e)}")
            except Exception as e:
                print(f"Error inesperado con {video_path}: {str(e)}")

if __name__ == "__main__":
    carpeta_entrada = "videos"  # Ruta relativa de la carpeta de entrada
    carpeta_salida = "audios"  # Ruta relativa de la carpeta de salida
    convertir_mp4_a_mp3(carpeta_entrada, carpeta_salida)
