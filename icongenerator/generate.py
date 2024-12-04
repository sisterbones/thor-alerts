
import json
import os

from rich import print
from PIL import Image

# Load icons
with open("../thor-alerts/icons.json", "r") as f:
    icons = json.load(f)

needed_icons = []
for icon in icons:
    if icon.get('thoricon'):
        needed_icons.append(icon['thoricon'])

image_parts = {}

for icon in needed_icons:
    new_icon = Image.new("RGBA", (32, 32))

    # Split icon names into their different parts and load the images
    parts = icon.split("-")
    # Set variations of parts
    if 'rain' in parts:
        if {'rain', 'lightning'}.intersection(set(parts)):
            parts[parts.index('cloud')] = 'cloud_grey'
    if len(parts) <= 1:
        if 'sun' in parts:
            parts = ['sun_large']
        if 'moon' in parts:
            parts = ['moon_large']

    # Try load the icons
    for part in parts:
        if part not in image_parts:
            try:
                image_parts[part] = Image.open(os.path.join('img', f"{part}.png"))
            except FileNotFoundError:
                image_parts[part] = Image.new("RGBA", (32, 32))

        # Overlay the part onto the image
        new_icon.paste(image_parts[part], mask=image_parts[part])

    new_icon.save('../thor-alerts/assets/icons/' + icon + '.png', 'PNG')

