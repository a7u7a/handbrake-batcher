#!/bin/bash
python handbrake_batch.py \
    --preset "~/Library/Containers/fr.handbrake.HandBrake/Data/Library/Application Support/HandBrake/UserPresets.json" \
    --output-name "optimized" \
    "your/input/directory" \
    "your/output/directory"

# Test HandBrakeCLI command
# HandBrakeCLI -i "your/input/file.mp4" \
#              -o "your/output/file.mp4" \
#              --preset-import-file ~/Library/Containers/fr.handbrake.HandBrake/Data/Library/Application\ Support/HandBrake/UserPresets.json \
#              -Z esrs-2024-portfolio