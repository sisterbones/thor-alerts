
import asyncio
import os
import threading
import time

import socketio
import wx
import wx.adv
import wx.svg

import config
from ThorAlertsMainFrame import ThorAlertsMainFrame as MainFrame
from notify import notify
import icons

config.setup_config()

sio = socketio.Client()

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame: MainFrame):
        wx.adv.TaskBarIcon.__init__(self)

        self.frame = frame

        if config.get("show_tray_icon"):
            self.SetIcon(wx.Icon('testicon.png', wx.BITMAP_TYPE_ANY), config.default_icon_tooltip)

        # self.Bind(wx.adv.EVT_TASKBAR_LEFT_UP, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarShowPreferences, id=2)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=3)

    #-----------------------------------------------------------------------

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, 'Show')
        menu.Append(2, 'Preferences')
        menu.Append(3, 'Quit')
        return menu

    def OnTaskBarActivate(self, event):
        if self.frame.IsShown():
            self.frame.Raise()
        else:
            self.frame.Show()

    def OnTaskBarShowPreferences(self, event):
        self.frame.show_preferences(event)

    def OnTaskBarClose(self, event):
        self.Destroy()
        self.frame.Destroy()

class ThorApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        frame.Show(True)
        self.frame=frame
        self.tskic = MyTaskBarIcon(frame)
        frame.tskic = self.tskic
        self.SetTopWindow(frame)

        # self.Bind(wx.wxEVT_DESTROY, self.onFrameDestroy, frame)

        return True

    # def onFrameDestroy(self, event):
    #     self.tskic.Destroy()

def receive_alert(data):
    print(data)

app = ThorApp()
tskic = app.tskic
frame = app.frame

@sio.on('weather')
def receive_weather(data):
    config.current_weather = data
    config.status_last_update = time.time()

@sio.on('connect')
def connected():
    notify("Thor", "Successfully connected to Thor.", tskic)
    sio.emit('ask', 'weather')

def init_socketio():
    while not sio.connected:
        try:
            sio.connect(config.get("hub_url", "http://localhost:8467"))
        except socketio.exceptions.ConnectionError:
            config.current_status = "Failed to connect to {}. Is it running?".format(config.get("hub_url", "http://localhost:8467"))

def main():
    global tskic, frame
    sio_thread = threading.Thread(target=init_socketio, daemon=True)
    sio_thread.start()
    app.MainLoop()

if __name__ == "__main__": main()
