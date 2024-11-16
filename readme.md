# Handbrake Batch processing

Used for batch processing videos with Handbrake. Used for optimizing static assets.

Example usage:

```bash
chmod +x process_files.sh
```

```bash
python handbrake_batch.py /path/to/input/videos /path/to/output/directory --preset /path/to/your/preset.json
```

## Install Handbrake

```bash
brew install handbrake
```

## Locate Handbrake presets

```bash
cd ~/Library/Containers/fr.handbrake.HandBrake/Data/Library/Application\ Support/HandBrake/UserPresets.json
```
