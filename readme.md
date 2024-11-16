# Handbrake Batch processing

- Python script to batch process videos using [HandbrakeCLI](https://handbrake.fr/docs/en/latest/cli/cli-options.html). Used for optimizing and standardizing static assets for web. Ensures consistent output format and quality across assets.
- Usage examples in `process_files.example.sh`.
- Supports presets. Tune your preset using the Handbrake GUI. Then pass the preset file path to this script.
- Tested in macOS.
- To-do:
  - Multiple threads

## Install HandbrakeCLI

```bash
brew install handbrake
```

## Path to Handbrake user presets

```bash
cd ~/Library/Containers/fr.handbrake.HandBrake/Data/Library/Application\ Support/HandBrake/UserPresets.json
```
