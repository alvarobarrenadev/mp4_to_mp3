import os
import ffmpeg
from concurrent.futures import ThreadPoolExecutor

def convertir_archivo(video_path, audio_path):
    try:
        # Crear la carpeta de destino si no existe
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
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

    formatos_video = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']
    tareas = []

    # Recorrer recursivamente todas las carpetas
    for raiz, dirs, archivos in os.walk(carpeta_entrada):
        for archivo in archivos:
            if any(archivo.lower().endswith(ext) for ext in formatos_video):
                # Obtener la ruta completa del archivo de video
                video_path = os.path.join(raiz, archivo)
                
                # Crear la ruta relativa para mantener la estructura de carpetas
                ruta_relativa = os.path.relpath(raiz, carpeta_entrada)
                
                # Crear la ruta de salida manteniendo la estructura de carpetas
                mp3_filename = os.path.splitext(archivo)[0] + ".mp3"
                audio_path = os.path.join(carpeta_salida, ruta_relativa, mp3_filename)
                
                tareas.append((video_path, audio_path))

    if not tareas:
        print("No se encontraron archivos de video.")
        return

    print(f"Se encontraron {len(tareas)} archivos para convertir.")

    # Usar un ThreadPoolExecutor para procesar varios archivos a la vez
    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        for video_path, audio_path in tareas:
            executor.submit(convertir_archivo, video_path, audio_path)

if __name__ == "__main__":
    carpeta_entrada = "videos"  # Ruta relativa o absoluta de la carpeta de entrada
    carpeta_salida = "audios"  # Ruta relativa o absoluta de la carpeta de salida
    convertir_videos_a_mp3(carpeta_entrada, carpeta_salida, num_hilos=9)