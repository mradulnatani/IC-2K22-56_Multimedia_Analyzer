# Multimedia Analyzer

A comprehensive Python-based multimedia analysis and enhancement toolkit for images, audio, and video files. This project includes metadata extraction, image enhancement, and voice cloning using ElevenLabs' API.

## Features

### Image Analysis
- File information: filename, size, and format
- Image properties: width, height, resolution (DPI), and color mode
- EXIF metadata extraction: camera make/model, capture date, orientation, and software info

### Image Enhancement
- Brightness adjustment
- Contrast enhancement
- Color adjustment
- Sharpening
- Median-filter based denoising

### Audio Analysis
- File information: filename and size
- Audio properties: channels, sample rate, and bitrate
- Duration calculation
- Metadata extraction using ID3 and other supported tags

### Voice Cloning
- Reference voice sample upload for consent-based voice cloning
- Generation of a unique voice ID from ElevenLabs
- Text-to-speech generation using the generated voice ID

### Video Analysis
- File information: filename and size
- Container metadata: format and duration
- Video stream analysis: resolution, frame rate, bitrate, and codec
- Audio stream analysis: codec, channels, sample rate, and bitrate

## Requirements

- Python 3.10+
- Pillow
- mutagen
- ffmpeg and ffprobe
- elevenlabs

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mradulnatani/IC-2K22-56_Multimedia_Analyzer.git
cd IC-2K22-56_Multimedia_Analyzer
```

2. Install the required Python dependencies:
```bash
pip install Pillow mutagen elevenlabs
```

3. Install FFmpeg:
- Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```

- macOS (Homebrew):
```bash
brew install ffmpeg
```

- Windows:
```bash
choco install ffmpeg
```

4. Set your ElevenLabs API key:
```bash
export ELEVENLABS_API_KEY="your-api-key-here"
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

# Enhance an image
python main.py --enhance samples/photo.jpg

# Analyze an audio file
python main.py samples/song.mp3

# Clone a voice and generate speech
python main.py --voice-clone samples/reference_voice.mp3 --text "Hello, this is my cloned voice"

# Analyze a video
python main.py samples/video.mp4
```

## Output

Analysis reports are generated in the `reports/` directory. Each report may include:
- File type identification
- Detailed metadata and properties
- Enhancement results
- Voice cloning status and generated voice ID
- Errors encountered during processing

## Project Structure

```text
IC-2K22-56_Multimedia_Analyzer/
├── main.py                 # Main entry point
├── image_analyzer.py       # Image analysis module
├── image_enhancer.py       # Image enhancement module
├── audio_analyzer.py       # Audio analysis module
├── video_analyzer.py       # Video analysis module
├── voice_cloner.py         # Voice cloning module using ElevenLabs API
├── file_utils.py           # File utilities and type detection
├── report_generator.py     # Report generation module
├── reports/                # Generated analysis reports
├── samples/                # Sample multimedia files
├── README.md               # Project documentation
└── requirements.txt        # Dependency list
```

## Supported File Formats

### Images
- JPEG, PNG, GIF, BMP, TIFF, WebP, and other formats supported by Pillow

### Audio
- MP3, FLAC, OGG, WAV, M4A, and other formats supported by Mutagen

### Video
- MP4, MKV, AVI, MOV, WebM, and other formats supported by FFmpeg

## Technical Details

### Image Analyzer
- Built using Pillow
- EXIF data extraction via PIL's ExifTags support
- Captures core image metadata and dimensions

### Image Enhancer
- Implements classical image-processing operations
- Supports brightness, contrast, color tuning, sharpening, and denoising
- Uses median filtering for noise reduction

### Audio Analyzer
- Uses Mutagen for metadata extraction
- Detects audio format automatically
- Retrieves bitrate, duration, and ID3-related metadata

### Voice Cloner
- Integrates ElevenLabs voice-cloning API
- Sends a consented reference voice sample
- Generates a voice ID
- Uses that voice ID for text-to-speech synthesis

### Video Analyzer
- Uses FFprobe to extract metadata
- Analyzes both video and audio streams separately

## Error Handling

The tool is designed to handle:
- Missing or inaccessible files
- Unsupported file types
- Corrupted or incomplete metadata
- Missing external dependencies
- API connectivity or rate-limit issues during voice cloning

## Author

Created for the IC-2K22-56 Multimedia project.

## License

[Add your license information here]

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.
