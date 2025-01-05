
# This file contains mappings from met.no weather icons to various other icon systems, as well as a label

import io
import json
import os
import sys

import wx
# from PIL import Image

base_path = (os.environ.get("BASE_PATH") or os.path.dirname(str(sys.modules[__name__].__file__)))

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

def get_thoricon(icon="sun-cloud-rain-thunder"):
    try:
        img = Image.open(os.path.join(base_path, 'assets', 'icons', f'{str(icon)}.png'))
    except:
        print("Image not found")
        return None

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes

def get_thoricon_bitmap(icon="sun-cloud-rain-thunder", scale=1):
    # thoricon = get_thoricon(icon, size)
    filename = f'{str(icon)}.png'
    if 2 >= scale >= 4:
        filename = f'{str(icon)}@{scale}x.png'
    return wx.Bitmap(wx.Image(os.path.join(base_path, 'assets', 'icons', filename)))

class ThorIconArtProvider(wx.ArtProvider):
    def __init__(self):
        wx.ArtProvider.__init__(self)

    def CreateBitmap(self, id, client, size):
        # Adapted from https://github.com/wxWidgets/wxPython-Classic/blob/19571e1ae65f1ac445f5491474121998c97a1bf0/demo/ArtProvider.py#L76

        bmp = wx.NullBitmap

        scale = size.width // 32

        if client == wx.ART_CMN_DIALOG: scale = 3
        if client == wx.ART_MENU: scale = 2
        if client == wx.ART_OTHER: scale = 4

        filename = f'{str(id)}.png'
        if 2 >= scale >= 4:
            filename = f'{str(id)}@{scale}x.png'

        if os.path.exists(os.path.join(base_path, 'assets', 'icons', filename)):
            bmp = get_thoricon_bitmap(id, scale)

        return bmp
