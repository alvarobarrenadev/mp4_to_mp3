# pip install ffmpeg-python

import os
import ffmpeg

def convertir_videos_a_mp3(carpeta_entrada, carpeta_salida, bitrate="192k"):
    print("Iniciando el proceso de conversión de videos a MP3...\n")

    # Verificar si la carpeta de entrada existe
    if not os.path.exists(carpeta_entrada):
        print(f"Error: La carpeta de entrada '{carpeta_entrada}' no existe.")
        return

    # Crear la carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        print(f"Se ha creado la carpeta de salida: {carpeta_salida}")

    # Extensiones de video admitidas
    extensiones_validas = (".mp4", ".mov")
    archivos = [f for f in os.listdir(carpeta_entrada) if f.lower().endswith(extensiones_validas)]

    if not archivos:
        print("No se encontraron archivos MP4 o MOV en la carpeta de entrada.")
        return

    print(f"Archivos encontrados en '{carpeta_entrada}': {archivos}\n")

    for archivo in archivos:
        video_path = os.path.join(carpeta_entrada, archivo)
        mp3_filename = os.path.splitext(archivo)[0] + ".mp3"
        audio_path = os.path.join(carpeta_salida, mp3_filename)

        print(f"Procesando: {archivo} -> {mp3_filename}")

        # Convertir video a MP3 usando ffmpeg-python
        try:
            ffmpeg.input(video_path).output(audio_path, audio_bitrate=bitrate).run(overwrite_output=True)
            print(f"✅ Conversión completada: {audio_path}")
        except ffmpeg.Error as e:
            print(f"❌ Error al convertir {video_path}: {e}")
        except Exception as e:
            print(f"⚠️ Error inesperado con {video_path}: {e}")

    print("\nProceso de conversión finalizado.")

if __name__ == "__main__":
    carpeta_entrada = "videos"  # Ruta relativa de la carpeta de entrada
    carpeta_salida = "audios"   # Ruta relativa de la carpeta de salida
    convertir_videos_a_mp3(carpeta_entrada, carpeta_salida)