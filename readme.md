# Handbrake Batch processing

- Used for optimizing static assets for web.
- Supports presets. Tune your preset using the Handbrake GUI. Then pass the path to the preset file to this script.
- Check the example script `process_files.example.sh` for usage.
- To-do: Multiple threads.

## Install Handbrake

```bash
brew install handbrake
```

## Locate Handbrake presets

```bash
cd ~/Library/Containers/fr.handbrake.HandBrake/Data/Library/Application\ Support/HandBrake/UserPresets.json
```
