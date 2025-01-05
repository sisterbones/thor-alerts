import os

import wx

from MyFrame3 import MyFrame3

from thor_alerts.icons import ThorIconArtProvider

wx.ArtProvider.Push(ThorIconArtProvider())

app = wx.App()
frm = MyFrame3(None)
frm.Show()
app.MainLoop()
