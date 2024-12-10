
import json
import os

from PIL import Image

# Load icons
with open("../thor_alerts/icons.json", "r") as f:
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

    timestwo = new_icon.resize((64, 64), Image.Resampling.NEAREST)
    timesthree = new_icon.resize((96, 96), Image.Resampling.NEAREST)
    timesfour = new_icon.resize((128, 128), Image.Resampling.NEAREST)

    new_icon.save('../thor_alerts/assets/icons/' + icon + '.png', 'PNG')
    timestwo.save('../thor_alerts/assets/icons/' + icon + '@2x.png', 'PNG')
    timesthree.save('../thor_alerts/assets/icons/' + icon + '@3x.png', 'PNG')
    timesfour.save('../thor_alerts/assets/icons/' + icon + '@4x.png', 'PNG')
