
import asyncio
import platform

import wx.adv

from desktop_notifier import DesktopNotifier, Icon

async def async_notify(title, message, taskbaricon:wx.adv.TaskBarIcon=None):
    notifier = DesktopNotifier(
        "Thor"
    )

    if taskbaricon:
        if taskbaricon.ShowBalloon(title, message) and platform.release() not in ["10", "11"]:
            return
    await notifier.send(title=title, message=message)

def notify(title, message, taskbaricon:wx.adv.TaskBarIcon=None):
    asyncio.run(async_notify(title, message, taskbaricon))
