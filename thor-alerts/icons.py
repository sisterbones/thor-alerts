
# This file contains mappings from met.no weather icons to various other icon systems, as well as a label

import json

import wx

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

class IconArtProvider(wx.ArtProvider):
    pass
