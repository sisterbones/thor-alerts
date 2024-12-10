
# This file contains mappings from met.no weather icons to various other icon systems, as well as a label

import io
import json

import wx
from PIL import Image

with open("icons.json", "r") as f:
    icons = json.load(f)

def get_by_yr(icon=None):
    return next((item for item in icons if item["yr"] == icon), icon)

def get_by_thoricon(icon=None):
    return next((item for item in icons if item["thoricon"] == icon), icon)

def get_by_freedesktop(icon=None):
    return next((item for item in icons if item["freedesktop"] == icon), icon)

def get_by_fafree(icon=None):
    return next((item for item in icons if item["fa-free"] == icon), icon)

def get_thoricon(icon="sun-cloud-rain-thunder", size=wx.Size(32, 32)):
    try:
        img = Image.open(f'assets/icons/{icon}.png')
    except:
        return None
    if size is not wx.Size(32, 32):
        img = img.resize((size.width, size.height), Image.Resampling.NEAREST)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes

def get_thoricon_bitmap(icon="sun-cloud-rain-thunder", size=wx.Size(32, 32)):
    thoricon = get_thoricon(icon, size)

    if thoricon:
        return wx.BitmapFromImage(wx.ImageFromStream(thoricon))
    else:
        return wx.NullBitmap

class ThorIconArtProvider(wx.ArtProvider):
    def __init__(self):
        wx.ArtProvider.__init__(self)

    def CreateBitmap(self, id, client, size):
        # Adapted from https://github.com/wxWidgets/wxPython-Classic/blob/19571e1ae65f1ac445f5491474121998c97a1bf0/demo/ArtProvider.py#L76

        return get_thoricon_bitmap(id.decode(), size)
