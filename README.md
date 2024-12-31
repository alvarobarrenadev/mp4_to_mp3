# MP4 to MP3 Converter
---

This project provides a Python script to convert MP4 video files to MP3 audio files using `ffmpeg-python`.

## Requirements

Make sure you have the following dependencies installed:

- **Python 3.x**  
- **ffmpeg**: Required for performing the conversion.  
- **ffmpeg-python**: Python library that provides an interface for working with `ffmpeg`.

### Installation

#### Windows (using `winget`)

1. **Install `winget`**:  
   `winget` is a command-line package manager for Windows. If you don't have it installed, follow these steps:
   - Download and install `winget` from [here](https://github.com/microsoft/winget-cli).
   - Go to the **Releases** section and download the `.msixbundle` file.
   - Once downloaded, install the `.msixbundle` file by double-clicking it.

2. **Install `ffmpeg` using `winget`**:  
   After installing `winget`, open a command prompt and run the following command to install `ffmpeg`:

   ```bash
   winget install "FFmpeg (Essentials Build)"
   ```

3. **Install Python dependencies**:  
   In the project directory, run the following command to install the required Python libraries:

   ```bash
   pip install ffmpeg-python
   ```

#### macOS

1. **Install `ffmpeg` using Homebrew**:  
   If you are using macOS, you can easily install `ffmpeg` with Homebrew:

   ```bash
   brew install ffmpeg
   ```

2. **Install Python dependencies**:  
   In the project directory, install `ffmpeg-python`:

   ```bash
   pip install ffmpeg-python
   ```

#### Linux (Ubuntu/Debian)

1. **Install `ffmpeg` using `apt`**:  
   On Debian-based distributions (e.g., Ubuntu), you can install `ffmpeg` using `apt`:

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

2. **Install Python dependencies**:  
   In the project directory, install `ffmpeg-python`:

   ```bash
   pip install ffmpeg-python
   ```

## Usage

### Folder Structure

To use the script, you need two folders:

- **videos**: The folder that contains the MP4 files you want to convert.
- **audios**: The folder where the converted MP3 files will be saved.

### Running the Script

1. Ensure that the **videos** and **audios** folders are in the same directory as the `script.py` file.
2. Run the script from the terminal or command line:
   ```bash
   python script.py
   ```

The script will go through all `.mp4` files in the **videos** folder and convert them to `.mp3` files in the **audios** folder.

### Customization

- **Input Folder**: The path to the folder containing the MP4 files is defined in the `carpeta_entrada` variable. By default, it is `"videos"`.
- **Output Folder**: The path where the converted MP3 files will be saved is defined in the `carpeta_salida` variable. By default, it is `"audios"`.

If you prefer to use custom paths, simply edit these variables in the code.

## Example

If you have an MP4 file named `video1.mp4` in the **videos** folder, running the script will convert it to `video1.mp3` and save it in the **audios** folder.

## Contributing

Contributions are welcome. If you want to improve this project, feel free to fork it and create a pull request.