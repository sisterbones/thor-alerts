
# This file contains mappings from met.no weather icons to various other icon systems, as well as a label

import io
import json
import os
import sys

import wx
from PIL import Image

base_path = os.path.dirname(str(sys.modules['__main__'].__file__))

with open(os.path.join(base_path, 'icons.json'), "r") as f:
    icons = json.load(f)

def get_by_yr(icon=None):
    return next((item for item in icons if item["yr"] == icon), icon)

def get_by_thoricon(icon=None):
    return next((item for item in icons if item["thoricon"] == icon), icon)

def get_by_freedesktop(icon=None):
    return next((item for item in icons if item["freedesktop"] == icon), icon)

def get_by_fafree(icon=None):
    return next((item for item in icons if item["fa-free"] == icon), icon)

def get_thoricon(icon="sun-cloud-rain-thunder", size=(32, 32)):
    try:
        img = Image.open(os.path.join(base_path, 'assets', 'icons', f'{str(icon)}.png'))
    except:
        print("Image not found")
        return None

    if size != (32, 32):
        img = img.resize((size[0], size[1]), Image.Resampling.NEAREST)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes

def get_thoricon_bitmap(icon="sun-cloud-rain-thunder", size=(32, 32)):
    # thoricon = get_thoricon(icon, size)
    return wx.Bitmap(wx.Image(os.path.join(base_path, 'assets', 'icons', f'{str(icon)}.png')))

class ThorIconArtProvider(wx.ArtProvider):
    def __init__(self):
        wx.ArtProvider.__init__(self)

    def CreateBitmap(self, id, client, size):
        # Adapted from https://github.com/wxWidgets/wxPython-Classic/blob/19571e1ae65f1ac445f5491474121998c97a1bf0/demo/ArtProvider.py#L76

        bmp = wx.NullBitmap

        if os.path.exists(os.path.join(base_path, 'assets', 'icons', f'{str(id)}.png')):
            print("Icon exists")
            bmp = get_thoricon_bitmap(id, (32, 32))

        return bmp
