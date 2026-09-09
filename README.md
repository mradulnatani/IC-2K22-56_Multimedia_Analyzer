# Multimedia Analyzer

A comprehensive Python-based tool for analyzing and extracting detailed information from multimedia files including images, audio, and videos.

## Features

### Image Analysis
- **File Information**: Extracts filename, file size, and format
- **Image Properties**: Captures width, height, resolution (DPI), and color mode
- **EXIF Metadata**: Extracts camera details (make, model), capture date, orientation, and software information

### Audio Analysis
- **File Information**: Filename and file size
- **Audio Properties**: Number of channels, sampling rate, and bit rate
- **Duration**: Total playback length in seconds
- **Metadata**: Extracts ID3 tags and other audio metadata

### Video Analysis
- **File Information**: Filename and file size
- **Container Information**: Video format and total duration
- **Video Stream Details**: Resolution, frame rate, bit rate, and codec
- **Audio Stream Details**: Codec, channels, sampling rate, and bit rate
- **Metadata**: Extracts container-level metadata tags

## Requirements

- Python 3.10+
- `Pillow` - Image processing
- `mutagen` - Audio metadata extraction
- `ffmpeg` and `ffprobe` - Video processing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mradulnatani/IC-2K22-56_Multimedia_Analyzer.git
cd IC-2K22-56_Multimedia_Analyzer
```

2. Install Python dependencies:
```bash
pip install Pillow mutagen
```

3. Install FFmpeg (required for video analysis):

**On Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**On macOS (with Homebrew):**
```bash
brew install ffmpeg
```

**On Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use:
```bash
choco install ffmpeg
```

## Usage

Run the analyzer with a multimedia file path:

```bash
python main.py <path_to_media_file>
```

### Examples

```bash
# Analyze an image
python main.py samples/photo.jpg

# Analyze an audio file
python main.py samples/song.mp3

# Analyze a video
python main.py samples/video.mp4
```

## Output

Analysis reports are generated as text files in the `reports/` directory. Each report contains:
- File type identification
- Detailed metadata and properties specific to the file type
- Any errors encountered during analysis

## Project Structure

```
IC-2K22-56_Multimedia_Analyzer/
├── main.py                 # Main entry point
├── image_analyzer.py       # Image analysis module
├── audio_analyzer.py       # Audio analysis module
├── video_analyzer.py       # Video analysis module
├── file_utils.py           # File utilities (existence check, type detection)
├── report_generator.py     # Report generation module
├── reports/                # Output directory for analysis reports
└── samples/                # Sample multimedia files for testing
```

## Supported File Formats

### Images
- JPEG, PNG, GIF, BMP, TIFF, WebP, and other PIL-supported formats

### Audio
- MP3, FLAC, OGG, WAV, M4A, and other Mutagen-supported formats

### Video
- MP4, MKV, AVI, MOV, WebM, and other FFmpeg-supported formats

## Technical Details

### Image Analyzer
- Uses `PIL (Pillow)` for image processing
- Extracts EXIF data using PIL's ExifTags module
- Provides comprehensive metadata about image properties

### Audio Analyzer
- Uses `Mutagen` library for universal audio metadata support
- Handles multiple audio formats with automatic format detection
- Extracts technical information and ID3/Vorbis tags

### Video Analyzer
- Uses `FFprobe` (part of FFmpeg) to extract detailed metadata
- Analyzes both video and audio streams independently
- Provides container and codec information

## Error Handling

The tool gracefully handles:
- Missing or inaccessible files
- Unsupported file formats
- Files with missing or corrupted metadata
- Missing external dependencies (FFmpeg/FFprobe)

## Author

Created for IC-2K22-56 project

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.
