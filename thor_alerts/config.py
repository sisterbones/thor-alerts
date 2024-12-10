
import json
import os

import wx
import platformdirs

config_dir = platformdirs.PlatformDirs("thor-alerts").user_config_path

print(config_dir)

conf = {}

weather_img = None
current_status = ""
current_weather = {}
status_last_update = 0

default_icon = "cloud-rain_heavy-lightning"
default_icon_tooltip = "THOR"

def setup_config():
    global conf
    # Check the config dir exists
    os.makedirs(config_dir, exist_ok=True)

    # Check that the config file exists
    if not os.path.exists(os.path.join(config_dir, "config.json")):
        with open(os.path.join(config_dir, "config.json"), "x"):
            print("Created config.json.")
        with open(os.path.join(config_dir, "config.json"), "w") as ff: ff.write("{}")
    with open(os.path.join(config_dir, "config.json"), "r") as ff: conf = json.load(ff)

def set(key, value):
    global conf
    conf[key] = value
    with open(os.path.join(config_dir, "config.json"), "w") as ff:
        json.dump(conf, ff)
    return conf

def get(key, fallback=None):
    return conf.get(key, fallback)
