import argparse
import os
import subprocess


def generate_speech(
    ref_audio,
    ref_text,
    gen_text,
    model="F5TTS_v1_Base",
):
    """
    Generate speech using F5-TTS voice cloning.

    Args:
        ref_audio: Reference voice recording.
        ref_text: Exact transcription of reference recording.
        gen_text: Text that the cloned voice should speak.
        model: F5-TTS model name.
    """

    if not os.path.isfile(ref_audio):
        raise FileNotFoundError(
            f"Reference audio not found: {ref_audio}"
        )

    if not ref_text.strip():
        raise ValueError(
            "Reference text cannot be empty."
        )

    if not gen_text.strip():
        raise ValueError(
            "Generated text cannot be empty."
        )

    command = [
        "f5-tts_infer-cli",
        "--model",
        model,
        "--ref_audio",
        ref_audio,
        "--ref_text",
        ref_text,
        "--gen_text",
        gen_text,
    ]

    print("=" * 60)
    print("        F5-TTS VOICE CLONING")
    print("=" * 60)

    print(f"\nReference audio : {ref_audio}")
    print(f"Reference text  : {ref_text}")
    print(f"Generated text  : {gen_text}")
    print("\nStarting F5-TTS...\n")

    try:
        subprocess.run(
            command,
            check=True,
        )

    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            f"F5-TTS inference failed with exit code "
            f"{error.returncode}"
        )

    print("\n" + "=" * 60)
    print("F5-TTS GENERATION COMPLETED")
    print("=" * 60)


def main():

    parser = argparse.ArgumentParser(
        description="F5-TTS Voice Cloning"
    )

    parser.add_argument(
        "audio",
        help="Reference audio file"
    )

    parser.add_argument(
        "ref_text",
        help="Transcript of the reference audio"
    )

    parser.add_argument(
        "gen_text",
        help="Text to generate using the reference voice"
    )

    parser.add_argument(
        "--model",
        default="F5TTS_v1_Base",
        help="F5-TTS model"
    )

    args = parser.parse_args()

    generate_speech(
        ref_audio=args.audio,
        ref_text=args.ref_text,
        gen_text=args.gen_text,
        model=args.model,
    )


if __name__ == "__main__":
    main()
