# Final Project - Multimedia Analyzer

Accepts any media file (Image, Audio, Video), auto-detects the type, routes it to the correct analyzer module, and produces a structured JSON report.

## Project Structure
```
multimedia_analyzer/
├── main.py
├── file_utils.py
├── image_analyzer.py
├── audio_analyzer.py
├── video_analyzer.py
├── report_generator.py
├── samples/
│   ├── sample.jpg
│   ├── sample.mp3
│   └── sample.mp4
└── reports/
    └── report.json
```

## Usage
```bash
python main.py samples/sample.jpg
python main.py samples/sample.mp3
python main.py samples/sample.mp4
```

## Requirements
```
pip install Pillow mutagen
# Also: FFmpeg installed on system
```
