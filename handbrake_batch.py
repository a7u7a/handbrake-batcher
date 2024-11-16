import os
from pathlib import Path
import subprocess
import argparse

def process_video(input_file, output_dir, preset, preset_name=None, output_name=None, index=None):
    """Process a single video file using HandBrakeCLI."""
    input_path = Path(input_file)
    
    if output_name and index is not None:
        output_filename = f"{output_name}_{index}{input_path.suffix}"
    else:
        output_filename = f"{input_path.stem.replace(' ', '_')}_handbrake_optimized{input_path.suffix}"
    
    output_path = Path(output_dir) / output_filename
    
    print(f"Input path: {input_path}")
    print(f"Output path: {output_path}")
    command = [
        "HandBrakeCLI",
        "-i", str(input_path),
        "-o", str(output_path),
        "--preset-import-file", preset,
        "-Z", preset_name
    ]
    
    print(f"Processing: {input_path.name}")
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully processed: {input_path.name}")
        else:
            print(f"Error processing {input_path.name}: {result.stderr}")
    except Exception as e:
        print(f"Exception while processing {input_path.name}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Batch process videos using HandBrakeCLI")
    parser.add_argument("input_dir", help="Directory containing input videos")
    parser.add_argument("output_dir", help="Directory for processed videos")
    parser.add_argument("--preset-name", help="Name of the preset to use")
    parser.add_argument("--preset", help="Path to HandBrake preset file", required=True)
    parser.add_argument("--output-name", help="Optional prefix for output filenames")
    parser.add_argument("--threads", type=int, default=os.cpu_count(), 
                        help="Number of concurrent processes")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    
    video_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.m4v')
    input_files = [
        f for f in Path(args.input_dir).glob("**/*")
        if f.suffix.lower() in video_extensions
    ]

    for i, input_file in enumerate(input_files, 1):
        print(f"\nProcessing file {i} of {len(input_files)}")
        process_video(
            str(input_file), 
            args.output_dir, 
            args.preset,
            args.preset_name,
            args.output_name,
            i if args.output_name else None
        )

    print(f"Found {len(input_files)} video files to process")


if __name__ == "__main__":
    main()