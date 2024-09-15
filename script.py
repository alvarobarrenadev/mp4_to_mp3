import os
from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(input_folder, output_folder):
    # Verificar si la carpeta de entrada existe
    if not os.path.exists(input_folder):
        print(f"La carpeta de entrada {input_folder} no existe.")
        return

    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtener todos los archivos .mp4 en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_folder, filename)
            mp3_filename = filename.replace(".mp4", ".mp3")
            audio_path = os.path.join(output_folder, mp3_filename)

            # Convertir video a audio
            try:
                with VideoFileClip(video_path) as video:
                    video.audio.write_audiofile(audio_path)
                print(f"Convertido: {video_path} -> {audio_path}")
            except Exception as e:
                print(f"Error al convertir {video_path}: {e}")


if __name__ == "__main__":
    # Ruta de la carpeta que contiene los videos .mp4
    carpeta_videos = "videos"
    # Ruta de la carpeta donde se guardarán los archivos .mp3
    carpeta_salida = "audios"
    convert_mp4_to_mp3(carpeta_videos, carpeta_salida)
