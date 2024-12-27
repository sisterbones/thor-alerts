
import asyncio
import os
import pathlib
import platform
import sys

import wx.adv

from desktop_notifier import DesktopNotifier, Icon

base_path = os.path.dirname(str(sys.modules['__main__'].__file__))

notifier = DesktopNotifier(
    "Thor"
)

async def async_notify(title, message, taskbaricon:wx.adv.TaskBarIcon=None, notification_icon=None):
    if taskbaricon:
        if platform.release() not in ["8.1", "10", "11"]:
            taskbaricon.ShowBalloon(title, message)

    icon = Icon(path=pathlib.Path(os.path.join(base_path, "assets", "icons", f"{notification_icon}@4x.png")))

    await notifier.send(title=title, message=message, icon=icon)

def notify(title, message, taskbaricon:wx.adv.TaskBarIcon=None, notification_icon="alert"):
    asyncio.run(async_notify(title, message, taskbaricon, notification_icon))
