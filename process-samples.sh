#!/bin/bash

. /venv/bin/activate

selected_palettes="ascii-few:hue ascii-few:brightness ascii-several:hue ascii-several:brightness unicode-shade:brightness unicode-colored-dots:hue"

rm samples/output/*

python app/nerdascii.py samples/curtain.jpg 'samples/output/curtain-{palette}-{method}.txt' $selected_palettes
python app/nerdascii.py samples/stylised.jpg 'samples/output/stylised-{palette}-{method}.txt' $selected_palettes
python app/nerdascii.py samples/device.png 'samples/output/device-{palette}-{method}.txt' $selected_palettes
